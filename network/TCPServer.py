import socket
import threading

# This function takes a string key that corresponds to a hand movement
# from the computer vision. It will send the integer value to the Unity client
# where it will 'react' to the mapped control key.
# Parameters:
# 1. controlKey: the string key that corresponds to a Unity control
# 2. cSock: client socket to send data through 
def sendControls(controlKey, cSock):
    if(cSock == None):
        print("No connection established just yet with client")

    cSock.send(controlKey.encode())
    cSock.close()

def clientHandle(cSock):
    clientResponse = cSock.recv(512)
    print(f"DEBUG: response:{clientResponse}")
    if(clientResponse.lower() == "exit"):
        connection.close()
        server.close()

# Initializes the server and binds it to address 127.0.0.1 and port 3005
# It will only listen to one connection which there should be only one.
local_host = "127.0.0.1"
local_port = 3005

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.settimeout(10)
server.bind((local_host, local_port))

server.listen(1)

print(f"DEBUG: host: {local_host}, port: {local_port}")

while True:
    try:
        connection, client_addr = server.accept()
        print(f"DEBUG: Address: {client_addr[0]}, Port: {client_addr[1]}")
        client_wrangler = threading.Thread(target=clientHandle, args=(clientSock,))
    except socket.timeout:
        print("Client timed out. Closing connection")
        connection.close()
        break




    
