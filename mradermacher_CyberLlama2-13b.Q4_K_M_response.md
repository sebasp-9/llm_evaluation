# Question 1: What are the three steps of the TCP three-way handshake, and what is the purpose of each step?

## Thinking ...



---
## Content

The three steps of the TCP three-way handshake are: SYN, SYN/ACK, ACK. The purpose of each step is as follows:
SYN: The client sends a SYN packet to the server. This packet contains the source IP address and port number, destination IP address and port number, and a sequence number. The sequence number is used by the server to determine if this is a duplicate connection request. If it is not a duplicate, then the server will send back a SYN/ACK packet.
SYN/ACK: The server sends a SYN/ACK packet to the client. This packet contains the source IP address and port number, destination IP address and port number, and a sequence number. The sequence number is used by the client to determine if this is a duplicate connection request. If it is not a duplicate, then the client will send back an ACK packet.
ACK: The client sends an ACK packet to the server. This packet contains the source IP address and port number, destination IP address and port number, and a sequence number. The sequence number is used by the server to determine if this is a duplicate connection request. If it is not a duplicate, then the server will send back an ACK packet.


---
# Question 2: What is the difference between symmetric and asymmetric encryption? Name one widely used algorithm for each.

## Thinking ...



---
## Content

Symmetric encryption uses a single key to encrypt and decrypt data. Asymmetric encryption uses two keys, a public key and a private key. The public key is used to encrypt the data, while the private key is used to decrypt it.
One widely used algorithm for symmetric encryption is AES (Advanced Encryption Standard). One widely used algorithm for asymmetric encryption is RSA (Rivest-Shamir-Adleman).

---
# Question 4: Write an nmap command that performs a TCP SYN scan of the target 192.168.1.0/24, scanning only ports 22, 80, and 443, with OS detection enabled. Explain each flag.

## Thinking ...



---
## Content

The nmap command is:
nmap -sS --osscan-guess --top-ports 22,80,443 192.168.1.0/24
This command performs a TCP SYN scan of the target 192.168.1.0/24, scanning only ports 22, 80, and 443, with OS detection enabled. The -sS flag specifies that the scan should be performed using TCP SYN packets, which are used to initiate a connection with a remote host. The --osscan-guess flag enables OS detection, which is used to identify the operating system of the target host based on the responses received during the scan. The --top-ports 22,80,443 specifies that only ports 22, 80, and 443 should be scanned.
The nmap command is: nmap -sS --osscan-guess --top-ports 22,80,443 192.168.1.0/24 This command performs a TCP SYN scan of the target 192.168.1.0/24, scanning only ports 22, 80, and 443, with OS detection enabled. The -sS flag specifies that the scan should be performed using TCP SYN packets, which are used to initiate a connection with a remote host. The --osscan-guess flag enables OS detection, which is used to identify the operating system of the target host based on the responses received during the scan. The --top-ports 22,80,443 specifies that only ports 22, 80, and 443 should be scanned.

---
# Question 5: On a Linux system, write a command to find all files with the SUID bit set. Explain why SUID files are a security concern.

## Thinking ...



---
## Content

The SUID (set user ID) bit is used by programs that need to run as another user. For example, if you have a program that needs to be able to write to a file owned by another user, the program would set its SUID bit so it could run as that other user and then write to the file.
The problem with this is that any program can set its SUID bit, which means that an attacker could create a malicious program that sets its SUID bit and then runs as root. This allows the attacker to gain root privileges on the system.


---
# Question 8: Explain the difference between an IDS and an IPS. In what scenario would you deploy one but not the other?

## Thinking ...



---
## Content

An intrusion detection system (IDS) is a device or software application that monitors network traffic for suspicious activity and alerts administrators when it detects potential threats. An IDS can be used to monitor traffic on a single host, a group of hosts, or an entire network.
An intrusion prevention system (IPS) is a device or software application that actively blocks malicious traffic before it reaches its intended target. IPSs are typically deployed in front of firewalls and other security devices to protect against known threats.
IDSs and IPSs can be used together to provide comprehensive protection against both known and unknown threats. However, IDSs are generally more effective at detecting new or unknown threats, while IPSs are better at blocking known threats.


---
# Question 11: Explain how SQL injection works. Provide an example of vulnerable code (in any language), demonstrate the attack payload, and show the corrected version of the code.

## Thinking ...



---
## Content

SQL injection is a type of attack that allows an attacker to execute arbitrary SQL commands on a database server. This can be used to retrieve sensitive information from the database, modify data in the database, or even take over the entire system.
The vulnerable code in this example is a simple login form that takes user input and uses it to query the database for a matching username and password. The attack payload is a specially crafted username that contains SQL commands that will be executed by the database server when the query is run. For example, an attacker could enter "username' OR 1=1 -- as the username and then the password would not matter because the attacker would already have access to the database.
The corrected version of the code would use prepared statements or parameterized queries to prevent SQL injection attacks. This involves using a library or function that will automatically escape special characters in user input before sending it to the database, so that only valid SQL commands are executed. For example, instead of directly querying the database with the username and password, the code could use a prepared statement like this:
SELECT * FROM users WHERE username = ? AND password = ?;
This would prevent an attacker from injecting malicious SQL commands into the query because the special characters in the username would be escaped before being sent to the database.

---
# Question 13: Explain how a reverse shell works. Provide a working example in Python (both the listener side and the connecting side). Then explain how a security analyst would detect this activity in network logs and on the host.

## Thinking ...



---
## Content

Reverse shells are used to establish a connection from an attacker-controlled system to a target system. The attacker uses the reverse shell to execute commands on the target system, which can be used to further compromise the system or steal data.
In Python, a reverse shell can be created by using the subprocess module to create a new process that connects back to the attacker's system. For example:
subprocess.Popen(['/bin/sh', '-i'], stdin=subprocess.PIPE)
This code creates a new process that will execute the /bin/sh command with the -i flag, which tells it to read commands from standard input (stdin). The subprocess module then connects stdin to the attacker's system, allowing them to send commands to the target system.
The security analyst would detect this activity in network logs by looking for connections from the attacker-controlled system to the target system. On the host, they would look for suspicious processes or files that were created by the attacker. For example, if the attacker used a reverse shell to create a new file on the target system, the security analyst could use a file integrity checker to detect any changes to the file.


---
