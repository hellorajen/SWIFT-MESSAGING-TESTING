import socket
from datetime import datetime

class SwiftServer:
    def __init__(self, host='0.0.0.0', port=5000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(1)
        
    def log_message(self, msg):
        with open("swift_messages.log", "a") as f:
            f.write(f"{datetime.now()} | {msg}\n")
    
    def validate_swift(self, msg):
        print("\nServer received raw message:")
        print(repr(msg))  # Shows hidden characters
        
        if not msg.startswith("{1:"):
            print("NAK: Missing Basic Header Block")
            return False
        if not "\n{2:" in msg:
            print("NAK: Missing Application Header Block")
            return False
        if not msg.endswith("-\n}"):
            print(f"NAK: Bad termination (ends with {msg[-5:]!r})")
            return False
        
        print("ACK: Valid SWIFT Message")
        return True

    def start(self):
        print("SWIFT Server listening on port 5000...")
        conn, addr = self.sock.accept()
        
        with conn:
            print(f"Connected to {addr}")
            while True:
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break
                
                if self.validate_swift(data):
                    print(f"Valid SWIFT: {data}")
                    self.log_message(data)
                    conn.sendall(b"ACK")  # Basic acknowledgment
                else:
                    conn.sendall(b"NAK")  # Negative acknowledgment

if __name__ == "__main__":
    server = SwiftServer()
    server.start()