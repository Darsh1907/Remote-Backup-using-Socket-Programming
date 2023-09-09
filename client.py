import streamlit as st
import socket
import os

IP = socket.gethostbyname(socket.gethostname())
PORT = 6000
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def send_file_to_server(filename):
    """ Connecting to the server. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(client)

    client.connect(ADDR)

    st.write(f"Sending {filename} to the server.")
    client.send(filename.encode(FORMAT))
    # st.write(f"[SEND] Sending the filename {filename}.")

    """ Waiting for the server to confirm the filename. """
    message = client.recv(SIZE).decode(FORMAT)
    st.write(f"Server says: {message}")

    # Sending the file data to the server.
    with open(filename, "r") as file:
        data = file.read()
        client.send(data.encode(FORMAT))
        st.write(f"Sending the file data.")

    """ Waiting for the server to confirm the file data. """
    message = client.recv(SIZE).decode(FORMAT)
    st.write(f"Server says: {message}")

    # Closing the connection.
    client.close()

def main():
    st.title("Backup - Client")
    st.write(f"Server IP address: {IP}")
    st.write(f"Server port number: {PORT}")

    # Get the file path from the user.
    file_path = st.file_uploader("Upload a file")
    if file_path is not None:
        filename = file_path.name
        with open(filename, "wb") as file:
            file.write(file_path.getbuffer())
            st.write(f"[INFO] File {filename} saved.")
        send_file_to_server(filename)
        if st.button("Delete file from your system"):
            os.remove(filename)
            st.write(f"File {filename} removed from client.")
        if st.button("Dont delete file"):
            st.empty()
            st.write("Didnt delete your file!!")
    else:
        st.write("[INFO] No file uploaded.")

if __name__ == "__main__":
    main()
