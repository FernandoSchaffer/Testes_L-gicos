#Faça um Programa que crie uma lista com as 
#médias de cada aluno, imprima as médias de cada aluno e 
#a quantidade de alunos com média maior que 7.


alunos = ["José", "Joana", "Maria", "Carla", "Mauricio", "Andre", "Tiago", "Enzo", "Amanda", "Alessandra"]
notas = [
    [10, 9, 8, 8],
    [9, 7, 6, 4],
    [10, 10, 10, 10],
    [5, 3, 10, 9],
    [7, 6, 6, 6],
    [7, 7, 8, 7],
    [7, 7, 7, 9],
    [8, 5, 6, 7],
    [10, 9, 7, 4],
    [10, 1, 3, 3],
]

medias = []
for i in range(len(notas)):
    media = sum(notas[i])/len(notas[i])
    medias.append(media)
    print(alunos[i], f"média: {media}")

contador = 0
for media in medias:
    if media >= 7:
        contador += 1
        
print(f'{contador} alunos tiveram nota maior ou igual a 7')