# Remote-Backup-using-Socket-Programming
Remote Backup System using Socket Programming in Python

![image](https://github.com/Darsh1907/Remote-Backup-using-Socket-Programming/assets/118650412/35a8b223-8d96-47f5-9c34-1fb1a5c84710)


## Overview

Remote Backup is a simple Python-based system designed to facilitate the automated backup of files from a client machine to a remote server. This project aims to provide users with a straightforward solution for ensuring data safety by automating the backup process.

## Features

- **User Interface**: A simple web interface for uploading files to be backed up, using Streamlit.
- **Multi-device support**

## Getting Started

### Prerequisites

- Python 3.x
- Streamlit (for the client interface)

### Installation

1. Clone the repository:
`git clone https://github.com/Darsh1907/Remote-Backup-using-Socket-Programming.git`

2. Navigate to the project directory:
`cd Remote-Backup-using-Socket-Programming`

3. Install Streamlit (if not already installed):
`pip install streamlit`


### Running the Server

1. Navigate to the server directory in the server machine:
`cd server`

2. Run the server script:
`python server.py`


### Running the Client

1. Navigate to the client directory in client machine:
`cd client`

2. Set the IP address in client code to the IP address of the server machine. **Make sure the Client and Server are connected on the same network**.

```
IP = '192.168.43.79' # change it to the IP of the server
PORT = 6000
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
```

**Note**: If your client machine and server machine is intended to run on the same machine, then you can set the IP in the following way:

```
IP = socket.gethostbyname(socket.gethostname())
PORT = 6000
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
```

3. Run the Streamlit app:
`streamlit run client.py`

4. Open the streamlit webpage on the Network URL as shown in the image.
![image](https://github.com/Darsh1907/Remote-Backup-using-Socket-Programming/assets/118650412/43b4fcf0-d817-4f7a-a3ee-40892b1b4717)

**Tip:** If the streamlit app is not able to work on the network URL or if it fails to upload the file, try disabling the Firewall of both the server machine and client machine. 

## Usage

1. Open the client interface in your web browser.
2. Upload the file you wish to back up.
3. Optionally, choose to delete the file from your system after it has been backed up.

## Contributing

Contributions are welcome!

## Acknowledgments

- Python's socket programming capabilities for enabling communication between the client and server.
- Streamlit for providing a simple web interface for file uploads.

