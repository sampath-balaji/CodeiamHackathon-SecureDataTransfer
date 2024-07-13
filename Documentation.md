# Secure and Efficient Data Transfer Between Isolated and Internet-Connected Systems
## Overview

This project facilitates secure data transfer between two computers:

1. **Client (Computer 1)**: Sends the data.
2. **Server (Computer 2)**: Receives the data.

## Prerequisites

### General Requirements

1. Ensure Python 3.x is installed on both Computer 1 and Computer 2.

### OpenSSL Installation (For Client)

1. Install the OpenSSL command prompt by downloading "Win64 OpenSSL v3.3.1 Light" from [this website](https://slproweb.com/products/Win32OpenSSL.html).
2. Generate the certificates `cert.pem` and `key.pem` by running the following command in your terminal:
    ```sh
    openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
    ```
    - During this process, you will be prompted to answer a few questions.
    - The certificates will be generated in the directory from which you run the command.

### File Placement

1. **Server (Computer 2)**: Place `data_receive.py`, `cert.pem`, and `key.pem` in the same directory.
2. **Client (Computer 1)**: Place `data_transfer.py`, `data_extraction.py`, `cert.pem`, `key.pem`, and `DBSql_Script.sql` in the same directory.
3. The files in this repository are already organised as descibed above here.
   
### Library Installation

#### For Computer 2 (Server)

No additional libraries are required.

#### For Computer 1 (Client)

1. **Database Setup**:
    - Create a MySQL database and table by running the `DBSql_Script.sql` script located in the client folder of this repository.
    - Update the database root password in the `data_extraction.py` script accordingly.
2. **Install MySQL Connector**:
    - Open Python IDLE or a Python environment on Computer 1.
    - Install the `mysql-connector-python` library using the following command:
    ```python
    import subprocess
    subprocess.check_call(["python", "-m", "pip", "install", "mysql-connector-python"])
    ```


## File Descriptions

1. **data_receive.py**: Sets up the server to listen for incoming data connections and securely receives the data sent from the client.
2. **data_transfer.py**: Initiates the connection to the server from the client and sends the extracted data.
3. **data_extraction.py**: Extracts data from the MySQL database and saves it in a `.csv` format.
4. **DBSql_Script.sql**: Contains the SQL script to set up the database and table required for data extraction.
5. **cert.pem**: SSL certificate file used for securing the data transfer.
6. **key.pem**: Private key file used for securing the data transfer.


## Important Configuration Step

- **Update IP Addresses**: Ensure to update the IP address of the server (Computer 2) in both the `data_transfer.py` and `data_receive.py` scripts:
    - In `data_transfer.py`, update the server hostname and IP address in the following lines:
        ```python
        with context.wrap_socket(sock, server_hostname='169.254.207.58') as ssock:
            ssock.connect(('169.254.207.58', 12345))
        ```
    - In `data_receive.py`, update the IP address in the following line:
        ```python
        sock.bind(('169.254.207.58', 12345))
        ```
        
## Running the Scripts

### Step 1: Data Extraction on Client (Computer 1)

1. Ensure your MySQL database is active.
2. Run the `data_extraction.py` script to extract data from the database table into a `.csv` file:
    ```sh
    python data_extraction.py
    ```

### Step 2: Data Transfer

#### On Server (Computer 2)

1. Run the `data_receive.py` script to set up the server to listen for incoming connections:
    ```sh
    python data_receive.py
    ```
    - This script sets up an SSL-enabled server that listens for incoming connections on a specified port.
    - Always run the server script first.

#### On Client (Computer 1)

1. Once the server script is running and listening for connections, run the `data_transfer.py` script to initiate the connection and begin sending the data:
    ```sh
    python data_transfer.py
    ```
    - This script connects to the server and sends the extracted data in chunks of 1024 bytes.
    - Always run the client script after running the server script.

### Example Configurations and Outputs

**Server Output Example:**
```sh
2024-07-13 15:14:09,379 - INFO - Starting server...
2024-07-13 15:14:09,383 - INFO - Listening for connections...
2024-07-13 15:14:09,383 - INFO - Server is ready and waiting for a connection...
2024-07-13 15:14:18,110 - INFO - Connection established with ('169.254.18.112', 63625)
2024-07-13 15:14:18,110 - INFO - Receiving data...
2024-07-13 15:14:18,111 - DEBUG - Received 1024 bytes
2024-07-13 15:14:18,113 - DEBUG - Received 443 bytes
2024-07-13 15:14:19,116 - DEBUG - No more data received.
2024-07-13 15:14:19,117 - INFO - File received successfully. Total bytes received: 1467
```

**Client Output Example:**
```sh
2024-07-13 15:14:16,060 - INFO - Creating socket...
2024-07-13 15:14:16,067 - INFO - Connecting to the server...
2024-07-13 15:14:18,134 - INFO - Cipher suite in use: ('TLS_AES_256_GCM_SHA384', 'TLSv1.3', 256)
2024-07-13 15:14:18,134 - INFO - Sending data...
2024-07-13 15:14:18,134 - DEBUG - Sent 1024 bytes
2024-07-13 15:14:18,134 - DEBUG - Sent 443 bytes
2024-07-13 15:14:18,134 - INFO - File sent successfully. Total bytes sent: 1467
```

## Data Transfer Details

- The data is transferred in chunks of 1024 bytes to ensure efficient and reliable transmission.
- A confirmation message is displayed on both the client and server upon successful data transfer, indicating that the process has completed without errors.

### Secure Data Transfer Use Cases

Please note that this method for securely transferring data between Computer 1 and Computer 2 is effective in the following scenarios:

1. **Computer 1 is completely isolated from the internet and Computer 2 is connected to the internet.**
2. **Computer 1 is connected to the internet and Computer 2 is isolated from the internet.**
3. **Both Computer 1 and Computer 2 are connected to the internet.**
4. **Both Computer 1 and Computer 2 are completely isolated from the internet.**

This method ensures secure data transfer regardless of whether the computers are connected to the internet or not, as long as they are on the same LAN or wireless network.

## Troubleshooting Tips

1. **Connection Issues**: Ensure that the server is running and listening on the correct port before starting the client script.
2. **SSL Certificate Errors**: Verify that `cert.pem` and `key.pem` are correctly generated and placed in the appropriate directories.
3. **Database Connection Errors**: Check that the MySQL database credentials in `data_extraction.py` are correct and that the database is running.

## Security Considerations

1. **Certificate Security**: Keep `cert.pem` and `key.pem` files secure and do not share them publicly. Use the certificate provided in this repository for testing purposes only.
2. **Data Encryption**: The use of SSL ensures that the data transferred between the client and server is encrypted, providing an additional layer of security.
   The SSL encryption used in this project employs the TLSv1.3 (Transport Layer Security version 1.3) protocol with the (Advanced Encryption Standard GCM (Galois/Counter Mode)) AES 256 GCM cipher suite,
   ensuring robust security and data integrity during transfer. The chosen cipher suite provides 256-bit encryption, which is currently widely used in networking related applications and is considered highly secure.

---

By following these detailed instructions, you will be able to securely transfer data from the client computer to the server computer using the provided scripts and configurations.
