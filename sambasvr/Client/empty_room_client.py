import socket
import time

def send_credentials(host, port, username, password, interval):
    while True:
        try:
            # Create a new socket for each connection attempt
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((host, port))

                # Wait for the server to send the "Username: " prompt
                print(sock.recv(1024).decode(), end='')

                # Send the username followed by a newline to simulate pressing Enter
                sock.sendall(username.encode() + b'\n')

                # Wait for the server to send the "Password: " prompt
                print(sock.recv(1024).decode(), end='')

                # Send the password followed by a newline
                sock.sendall(password.encode() + b'\n')

                # Wait to receive the "Access denied." message from the server
                print(sock.recv(1024).decode())

        except Exception as e:
            print(f"Connection failed: {e}")
        
        # Sleep for the specified interval before sending the credentials again
        time.sleep(interval)

def main():
    host = 'samba.netsec-docker.isi.jhu.edu'  # Server IP (change if different)
    port = 45           # Port on which server is listening, adjusted to match your server
    username = 'empire'  # Example username
    password = 'NOrebelsPLEASE'  # Example password
    interval = 10        # Time in seconds between each login attempt

    send_credentials(host, port, username, password, interval)

if __name__ == "__main__":
    main()
