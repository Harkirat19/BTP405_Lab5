import socket
import threading

def handle_connection(conn, addr):

    with conn:
        print(f'Connected by {addr}')

        while True:

            # Receive Data From Client
            data = conn.recv(1024)
            message = data.decode()
            print(f'Received from client: {message}')

            if not data:
                break
            if message == 'quit':
                break

            # Send Response To Client
            conn.sendall(data)

        print(f'Client disconnected')


def start_server(host='127.0.0.1', port=8080):

    # Create Socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        print(f'Server started, listening on {host}:{port}')
        s.listen()

        while True:
            # Accept Connection
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_connection, args=(conn, addr))
            thread.start()
            thread.join()
        s.close()

if __name__ == "__main__":
    start_server()
