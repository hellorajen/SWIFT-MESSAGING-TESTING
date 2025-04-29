import socket

def create_swift_message():
    """Generate properly formatted SWIFT MT202"""
    return """{1:F01BANKDEFFAXXX5432109876}\r
{2:202BANKGB2LAXXX1234567890}\r
3:\r
4:20:TRANSREF2024\r
21:RELATEDREF123\r
32A:240531EUR50000,\r
52A:BANKFRPP\r
53A:BANKUS33\r
58A:BANKDEFF\r
72:/BNF/INV 5678
-
}"""

def send_swift_message(host='localhost', port=5000):
    swift_msg = create_swift_message()
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(swift_msg.encode('utf-8'))
        print(f"Raw bytes sent: {swift_msg.encode('utf-8')}")
        # Should show b'{1:F01...}\\r\\n{2:202...}\\r\\n...'
        response = sock.recv(1024)
        print(f"Server response: {response.decode('utf-8')}")
        print(f"Sent SWIFT:\n{swift_msg}")

if __name__ == "__main__":
    send_swift_message()