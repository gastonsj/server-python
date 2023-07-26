import socket

def respond_to_client(client_socket):
    # Read the contents of the HTML file
    with open('index.html', 'r') as file:
        html_content = file.read()

    # Send the HTTP response with the HTML content
    http_response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{html_content}"
    client_socket.send(http_response.encode())

def main():
    host = 'localhost'
    port = 4233

    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((host, port))

    # Start listening for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        try:
            # Accept incoming connection
            client_socket, client_address = server_socket.accept()
            print(f"Connection established with {client_address}")

            # Respond to the client with the web page
            respond_to_client(client_socket)

            # Close the connection
            client_socket.close()
            print(f"Connection closed with {client_address}")
        except KeyboardInterrupt:
            print("Server stopped by the user.")
            break

    # Close the server socket
    server_socket.close()

if __name__ == "__main__":
    main()
