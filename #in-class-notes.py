import socket

##
# DGRAM vs. STREAM
# Basically SOCK_DGRAM is used for UDP packets, SOCK_STREAM for TCP.
# As far as reliability issues, it's UDP vs. TCP issues - no guarantee for UDP, guaranteed delivery for TCP.
##
#ms_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
ms_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)

ms_socket.connect(('134.170.188.221', 80))
ms_socket.connect(('23.200.143.77', 80))
ms_socket.connect(('www.microsoft.com', 80))

msg = "GET / HTTP/1.1\r\n"
msg += "Host:www.microsoft.com\r\n\r\n"

ms_socket.sendall(msg)

# loop this in order to read page
response = ms_socket.recv(4096)
response

ms_socket.close()
