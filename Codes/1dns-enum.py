import dns.resolver # type: ignore
import dns.exception # type: ignore
dominio = "dominio.com"
registros = ["A", "AAAA", "MX", "NS"] #1

for registro in registros:
    resposta = dns.resolver.query(dominio, registro, raise_on_no_answer=False) #2
    if resposta.rrset is not None:
        print (resposta.rrset)

        try:
            resposta = dns.resolver.query(dominio, registro)
            for rdata in resposta:
                print(f"{registro}: {rdata}")
        except dns.resolver.NoAnswer:
            pass
        except dns.resolver.NXDOMAIN:
            print(f"Domínio inexistente: {dominio}")
        except dns.exception.Timeout:
            print("Timeout na consulta DNS")
        except dns.resolver.NoNameservers:
            print("Nenhum servidor DNS disponível")