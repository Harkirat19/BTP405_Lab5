import socket

def start_client(host='127.0.0.1', port=8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # Connect To Server
        s.connect((host, port))

        while True:
            message = input('Enter message: ')
            s.send(message.encode())
            if message == 'quit':
                break

            # Message Received By Server
            data = s.recv(1024)
            print(f'Message sent to server: {data.decode()}')

        # Closing Connection
        s.close()


if __name__ == "__main__":
    start_client()
