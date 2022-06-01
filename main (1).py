#Programa usado para verificar se a string é um palíndromo: 

sentença = input("Digite uma string: ")

inverso = sentença[::-1]

if (sentença == inverso):
  print("Sucesso, você digitou um palíndromo")
else:
  print("Ops, você não digitou um palíndromo")


#Programa usado para verificar se a string é um palíndromo, contudo, apresentando agora condições específicas:

def VerificarPalíndromo(sentença):
    l, h = 0, len(sentença) - 1
   
    # Definindo a string como minúscula
    sentença = sentença.lower()
   
    # Comparando os caracteres até eles se tornarem iguais
    while (l <= h):
   
        if (not(sentença[l] >= 'a' and sentença[l] <= 'z')):
            l += 1
   
        elif (not(sentença[h] >= 'a' and sentença[h] <= 'z')):
            h -= 1
   
        # Caso os caracteres sejam iguais
        elif (sentença[l] == sentença[h]):
            l += 1
            h -= 1
         
        #Se os caracteres não são iguais esse sentença não será um palíndromo
        else:
            return False
    # Retorna verdadeiro caso seja palíndromo
    return True
   
# Testando se o programa é um palíndromo
if (VerificarPalíndromo(sentença)):
    print ("Sucesso, a string digitada é um palíndromo.")
else:
    print ("Opa, a string digitada não é um palíndromo.")
 

