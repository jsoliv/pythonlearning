import random


escolha=int(input("Choose 1 if you want had or two if you have tail: "))

random_integer = random.randint(1, 2)

if escolha == 1:
    escolha_ht = "heads"
else:
    escolha_ht = "tail"
    
    
print(f"You choose {escolha_ht}")


if random_integer == 1:
    resultado = "heads"
else:
    resultado = "tail"

    
if escolha == random_integer:
        print(f"The results is {resultado}, you win")
else:
        print(f"The results is {resultado}, you loose")

    
