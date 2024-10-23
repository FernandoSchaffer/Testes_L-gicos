#Achar a soma para dar 9
nums = [11, 15, 2, 5, 7]
alvo = 9
lista = []

for i in range(len(nums)):
    for j in range( i + 1, len(nums)):
        if nums[j] + nums[i] == 9:
            resultado = nums[j] + nums[i]
            print(resultado)





    




    
