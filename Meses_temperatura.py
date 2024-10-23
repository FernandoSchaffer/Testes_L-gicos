#Em quais meses a média de temperatura foi maior do que a média nacional?

meses = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
]

temperaturas = [30, 29, 28, 28, 25, 26, 20, 21, 19, 25, 27, 32]

for i in range(len(temperaturas)):
    media = sum(temperaturas) / len(temperaturas)
    if temperaturas[i] > media:
        print(f"Mês de {meses[i]} foi maior que a média nacional")

    

print(media)
