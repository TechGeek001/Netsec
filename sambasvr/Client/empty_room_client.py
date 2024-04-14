import socket
import time

def send_credentials(host, port, directory, username, password, interval):
    while True:
        try:
            # Create a new socket for each connection attempt
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((host, port))
                
                # Wait for the server to send the "Directory: " prompt
                print(sock.recv(1024).decode(), end='')

                # Send the directory followed by a newline
                sock.sendall(directory.encode() + b'\n')

                # Wait for the server to send the "Username: " prompt
                print(sock.recv(1024).decode(), end='')

                # Send the username followed by a newline
                sock.sendall(username.encode() + b'\n')

                # Wait for the server to send the "Password: " prompt
                print(sock.recv(1024).decode(), end='')

                # Send the password followed by a newline
                sock.sendall(password.encode() + b'\n')

                # Wait to receive the "Access denied." message from the server
                print(sock.recv(1024).decode())

        except Exception as e:
            print(f"Connection failed: {e}")
        
        time.sleep(interval)

def main():
    host = 'samba.netsec-docker.isi.jhu.edu'
    port = 45
    directory = '/Public'
    username = 'empire'
    password = 'NOrebelsPLEASE'
    interval = 10

    send_credentials(host, port, directory, username, password, interval)

if __name__ == "__main__":
    main()
