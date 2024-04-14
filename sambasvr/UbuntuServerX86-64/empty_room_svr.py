import socket

def handle_client(client_socket):
    try:
        client_socket.sendall(b"Username: ")
        username = client_socket.recv(1024).strip()
        if not username:
            return  # Terminate if no username is provided

        client_socket.sendall(b"Password: ")
        password = client_socket.recv(1024).strip()
        if not password:
            return  # Terminate if no password is provided

        # Just echo back received username and password for the sake of this mock server
        client_socket.sendall(b"Access denied.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def main():
    host = '0.0.0.0'  # Listen on all available IPs
    port = 45         # The port the server will listen on

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Listening on {host}:{port}")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")
            handle_client(client_socket)
    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()