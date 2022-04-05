import random
nom1 = str (input ('Digite o nome:'))
nom2 = str (input ('Digite o segundo nome:'))
nom3 = str (input ('Digite o terceiro nome:'))
nom4 = str (input ('Digite o quarto nome:'))
print ('O nome sorteado foi: {}'.format (random.choice ([nom1, nom2, nom3, nom4])))
