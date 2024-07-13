import socket
import ssl
import logging
import time

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def send_file():
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

    # Add a fixed delay to ensure the server is ready
    time.sleep(5)  # 5 seconds delay

    retries = 5
    delay = 2  # seconds

    while retries > 0:
        try:
            logging.info('Creating socket...')
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                with context.wrap_socket(sock, server_hostname='169.254.207.58') as ssock:
                    logging.info('Connecting to the server...')
                    ssock.connect(('169.254.207.58', 12345))
                    logging.info(f"Cipher suite in use: {ssock.cipher()}")

                    with open('data.csv', 'rb') as file:
                        logging.info('Sending data...')
                        total_bytes_sent = 0
                        while True:
                            data = file.read(1024)
                            if not data:
                                break
                            ssock.sendall(data)
                            total_bytes_sent += len(data)
                            logging.debug(f'Sent {len(data)} bytes')
                        logging.info(f'File sent successfully. Total bytes sent: {total_bytes_sent}')
                    
                    # Wait a bit to ensure all data is sent
                    time.sleep(1)
                    ssock.shutdown(socket.SHUT_WR)
                    ssock.close()
                    return  # exit after successful send
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            retries -= 1
            logging.info(f"Retrying in {delay} seconds... ({retries} retries left)")
            time.sleep(delay)

    logging.error("Failed to connect to the server after several retries.")

if __name__ == "__main__":
    send_file()
