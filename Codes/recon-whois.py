import whois 

dominio = "dominio.com"

try:
    consultaWhois = whois.whois(dominio)

    print("Email (atributo):", consultaWhois.email)
    print("Email (chave):", consultaWhois.get("email"))
    print("Texto completo:\n", consultaWhois.text)

except Exception as e:
    print("Erro ao consultar WHOIS:", e)
