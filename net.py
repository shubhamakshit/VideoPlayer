import socket
import subprocess

class NetUtils:
    @staticmethod
    def get_local_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # Connect to an external IP to get the local IP of the host machine
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip

    @staticmethod
    def server(ipv4_address, SERVER_PORT, FOLDER_MAIN="./"):
        # Check if the specified port is already in use
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ipv4_address, SERVER_PORT))
        if result == 0:
            print(f"Port {SERVER_PORT} is already in use. Server cannot be started.")
            return

        # Starting a simple HTTP server on a specified port and directory
        print(['npx', 'http-server', FOLDER_MAIN, '-p', str(SERVER_PORT)])
        subprocess.Popen(['npx', 'http-server', FOLDER_MAIN, '-p', str(SERVER_PORT)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,shell=True)
        print(f'Server started at http://{ipv4_address}:{SERVER_PORT}')


