# Calculadora de partidas rankeadas

vitorias = int(input('Informe o número de vitórias do seu herói: '))
derrotas = int(input('Informe o número de derrotas do seu herói: '))
nivel = ''


def avaliarRankeadas (vitorias, derrotas):
    saldoDeVitorias = vitorias - derrotas
    return saldoDeVitorias


rankFinal = avaliarRankeadas(vitorias, derrotas)

if rankFinal <= 10:
    nivel = 'ferro'
    print(f"O herói tem saldo de {rankFinal} e está no nível de {nivel}")
elif rankFinal <= 20:
    nivel = 'bronze'
    print(f"O herói tem saldo de {rankFinal} e está no nível de {nivel}")
elif rankFinal <= 50:
    nivel = 'prata'
    print(f"O herói tem saldo de {rankFinal} e está no nível de {nivel}")
elif rankFinal <= 80:
    nivel = 'ouro'
    print(f"O herói tem saldo de {rankFinal} e está no nível de {nivel}")
elif rankFinal <= 90:
    nivel = 'diamante'
    print(f"O herói tem saldo de {rankFinal} e está no nível de {nivel}")
elif rankFinal <= 100:
    nivel = 'lendário'
    print(f"O herói tem saldo de {rankFinal} e está no nível de {nivel}")
else:
    nivel = 'imortal'
    print(f"O herói tem saldo de {rankFinal} e está no nível de {nivel}")