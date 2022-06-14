import socket
HEADER =  64 # bytes

# Set arbritrary port number
## will need to be different if on pi...
## SAME AS IN SERVER>>>
PORT =  12345 

DISCONNECT_MESSAGE = "!Disconnect"

# Different SERVER...
SERVER = '10.248.193.223'

ADDR = (SERVER, PORT)

# SOCKET SET UP! for client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)
