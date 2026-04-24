import argparse
import json
import ollama
from datetime import datetime
from typing import Tuple

# default configurations
MODEL_TEMP = 0
MODEL_TOP_P = 0.9
MODEL_NUM_PREDICT = 2048
# partial battery for screening
# remember to OBO (-1) your indexes!
PARTIAL_SCREENING = [0, 1, 3, 4, 7, 10, 12]


def response_chat(llm_model: str, query: str) -> Tuple[str, str]:
    response = ollama.chat(
        model=llm_model,
        messages=[{ 'role': 'user', 'content': query }],
        options={
            'temperature': MODEL_TEMP,
            'top_p': MODEL_TOP_P,
            'num_predict': MODEL_NUM_PREDICT,
        },
    )

    return response['message']['content'], response['message']['thinking']


def stream_chat(llm_model: str, query: str) -> Tuple[str, str]:
    stream = ollama.chat(
        model=llm_model,
        messages=[{'role': 'user', 'content': query}],
        options={
            'temperature': MODEL_TEMP,
            'top_p': MODEL_TOP_P,
            'num_predict': MODEL_NUM_PREDICT,
        },
        stream=True,
    )

    in_thinking = False
    content = ''
    thinking = ''
    for chunk in stream:
        if chunk.message.thinking:
            if not in_thinking:
                in_thinking = True
                print('\n💭 \033[92mThinking:\033[0m\n', end='', flush=True)
            print(chunk.message.thinking, end='', flush=True)
            # accumulate the partial thinking
            thinking += chunk.message.thinking
        elif chunk.message.content:
            if in_thinking:
                in_thinking = False
                print('\n💬 \033[32mAnswer:\033[0m\n', end='', flush=True)
            print(chunk.message.content, end='', flush=True)
            # accumulate the partial content
            content += chunk.message.content

    return content, thinking


def main():
    parser = argparse.ArgumentParser(prog='test', description="test an llm")
    parser.add_argument('-model', '-m', required=True, help="model to query")
    parser.add_argument('-battery', '-b', default='battery.json', help="question battery file to load")
    parser.add_argument('--full', '-f', action='store_true', help="run full question battery, otherwise partial")
    parser.add_argument('--preserve_thinking', '-p', action='store_true', help="preserve thinking in output file")
    parser.add_argument('--stream', '-s', action='store_true', help="stream model response")

    args = parser.parse_args()

    # load battery of questions from file
    battery = None
    with open(args.battery, 'r') as json_file:
        battery = json.load(json_file)

    # set rounds of questioning to either length of battery file for full or predefined list for partial
    rounds = list(range(0, len(battery['questions']))) if args.full else PARTIAL_SCREENING

    # perform battery
    for r in rounds:
        question = battery['questions'][r]['question']
        print(f"\n[{datetime.now()}] ▶️ {args.model} queried: {question}")

        response = stream_chat(args.model, question) if args.stream else response_chat(args.model, question)

        output = f"# Question {r + 1}: {question}\n\n"
        if args.preserve_thinking:
            output += "## Thinking ...\n\n"
            output += response[1]
            output += "\n\n---\n"
            output += "## Content\n\n"
        output += response[0]
        output += "\n\n---\n"

        with open(f'{args.model}_response.md', 'a') as out_file:
            out_file.write(output)


if __name__ == '__main__':
    main()
