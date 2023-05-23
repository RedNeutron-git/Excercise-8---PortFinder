import socket
from concurrent.futures import ThreadPoolExecutor

print("--------------------------")
print("PortFinder V0.0.1")
print("Author: RedNeutron")
print("--------------------------")
print("")

target_host_input = input('Input Target Host (IP/Domain): ')
start_port = 1
end_port = 65535
thread = input('Set The Thread (1-1000): ')
thread = int(thread)
max_errors = 3

if thread <= 0:
    print("Thread must large than 0")
    exit()
if thread > 1000:
    print("Thread must lower than 1000")
    exit()

def port_scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)        
        result = sock.connect_ex((target_host_input, port))
        if result == 0:
            print(f"Port {port} is Open")
        sock.close()
    except socket.error:
        print(f"Status Host {target_host_input} is Unreachable!")
        raise Exception("Connection failed")
with ThreadPoolExecutor(max_workers=thread) as executor:
    executor.map(port_scan, range(start_port, end_port+1))
