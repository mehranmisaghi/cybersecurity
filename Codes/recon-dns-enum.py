import dns.resolver
import dns.exception

dominio = "dominio.com"
registros = ["A", "AAAA", "MX", "NS"]

for registro in registros:
    try:
        resposta = dns.resolver.resolve(dominio, registro)

        for rdata in resposta:
            print(f"{registro}: {rdata}")

    except dns.resolver.NoAnswer:
        print(f"Sem resposta para o registro {registro}")
    except dns.resolver.NXDOMAIN:
        print(f"Domínio inexistente: {dominio}")
        break
    except dns.exception.Timeout:
        print("Timeout na consulta DNS")
    except dns.resolver.NoNameservers:
        print("Nenhum servidor DNS disponível")
