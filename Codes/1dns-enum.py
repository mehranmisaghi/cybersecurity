import dns.resolver

dominio = "dominio.com"
registros = ["A", "AAAA", "MX", "NS"] #1

for registro in registros:
    resposta = dns.resolver.query(dominio, registro, raise_on_no_answer=False) #2
    if resposta.rrset is not None:
        print (resposta.rrset)