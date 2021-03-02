# tcp_server.py

import socket
from sh_protocol import SHProtocol
from sh_server import SHServer
    
if __name__ == "__main__":
    # Create the server socket
    # Defaults family=AF_INET, type=SOCK_STREAM, proto=0, filno=None
    serversoc = socket.socket()
    
    # Bind to local host:50000
    serversoc.bind(("localhost",50000))
                   
    # Make passive with backlog=5
    serversoc.listen(5)
    
    # Wait for incoming connections
    while True:
        print("Listening on ", 50000)
        
        # Accept the connection
        commsoc, raddr = serversoc.accept()
        
        # Run the application protocol
        shp = SHProtocol(commsoc)
        shs = SHServer(shp)
        shs.run()
        
        # Close the comm socket
        commsoc.close()
    
    # Close the server socket
    serversoc.close()
    
