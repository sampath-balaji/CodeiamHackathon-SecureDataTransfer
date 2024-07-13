import socket
import ssl
import logging

# Corrected logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def receive_file():
    logging.info('Starting server...')
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(('169.254.207.58', 12345))  # Replace with the actual IP address of Computer 2
        sock.listen(5)
        logging.info('Listening for connections...')
        with context.wrap_socket(sock, server_side=True) as ssock:
            logging.info('Server is ready and waiting for a connection...')
            conn, addr = ssock.accept()
            logging.info(f'Connection established with {addr}')
            with conn:
                with open('received_data.csv', 'wb') as file:
                    logging.info('Receiving data...')
                    total_bytes_received = 0
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            logging.debug('No more data received.')
                            break
                        file.write(data)
                        total_bytes_received += len(data)
                        logging.debug(f'Received {len(data)} bytes')
                    logging.info(f'File received successfully. Total bytes received: {total_bytes_received}')
                    conn.shutdown(socket.SHUT_RD)
                    conn.close()

if __name__ == "__main__":
    receive_file()
