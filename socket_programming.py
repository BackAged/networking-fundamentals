import argparse, socket

MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram

def client(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = '127.0.0.1'
    while True:
        s.connect((host, port))
        message = input('Input message to send to server:' )
        data = message.encode('ascii')
        s.send(data)
        data = s.recv(MAX_SIZE_BYTES) 
        text = data.decode('ascii')
        print('The server replied with {!r}'.format(text))


def server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = '127.0.0.1'
    s.bind((hostname, port))
    print('Listening at {}'.format(s.getsockname()))
    while True:
        data, clientAddress = s.recvfrom(MAX_SIZE_BYTES)
        message = data.decode('ascii')
        print('The client at {} says {!r}'.format(clientAddress, message))
        msg_to_send = input('Input message to send to client:' )
        data = msg_to_send.encode('ascii')
        s.sendto(data, clientAddress)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('role', default="s", help='TCP port (default 1060)')
    parser.add_argument('port', default=3000, help='TCP port (default 1060)')
    args = parser.parse_args()
    if (args.role == "s"):
        server(int(args.port))
    else:
        client(int(args.port))