import socket
dominio = "dominio.com"
nomes = ["ns1", "ns2", "www", "ftp", "intranet"]
for nome in nomes:
        DNS = nome + "." + dominio
        try:
            print (DNS + ":" + socket.gethostbyname(DNS))
        except socket.gaierror:
            pass