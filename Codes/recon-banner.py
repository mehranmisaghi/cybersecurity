import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)

try:
    sock.connect(("localhost", 22))
    data = sock.recv(2048)
    print(data.decode(errors="ignore"))
except Exception as e:
    print("Erro:", e)
finally:
    sock.close()
