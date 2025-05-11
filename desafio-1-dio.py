heroi = {
    'Capitão América': 8500,
    'Homem de Ferro': 6000,
    'Homem Aranha': 2500,
    'Pantera Negra': 8000,
    'Capitã Marvel': 9600,
    'Homem Formiga': 1500,
    'Thor': 11000,
    'Doutor Estranho': 6200,
    'Viúva Negra': 2500,
    'Feiticeira Escarlate': 9400
}
nome = input('Digite o nome do herói: ')

if nome in heroi:
    xp = heroi[nome]

    if xp < 1000:
        nivel = 'Ferro'
    elif 1001 <= xp <= 2000:
        nivel = 'Bronze'
    elif 2001 <= xp <= 5000:
        nivel = 'Prata'
    elif 5001 <= xp <= 7000:
        nivel = 'Ouro'
    elif 7001 <= xp <= 8000:
        nivel = 'Platina'
    elif 8001 <= xp <= 9000:
        nivel = 'Ascendente'
    elif 9001 <= xp <= 10000:
        nivel = 'Imortal'
    else:
        nivel = 'Radiante'

    print('O herói de nome {} está no nível {}.')
else:
    print("Herói não encontrado.")
