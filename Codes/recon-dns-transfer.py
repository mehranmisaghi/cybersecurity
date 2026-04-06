import dns.query
import dns.zone
import dns.resolver

dominio = "google.com"

# Consulta os servidores NS do domínio
registrosNS = dns.resolver.resolve(dominio, "NS")

lista = []

for registro in registrosNS:
    lista.append(str(registro).rstrip("."))

for registro in lista:
    try:
        print(f"Tentando transferência de zona em {registro}...")

        transferenciaZona = dns.zone.from_xfr(
            dns.query.xfr(registro, dominio)
        )

    except Exception as e:
        print(f"Erro na transferência de zona: {e}")

    else:
        registroDNS = sorted(transferenciaZona.nodes.keys())

        for n in registroDNS:
            print(transferenciaZona[n].to_text(n))
