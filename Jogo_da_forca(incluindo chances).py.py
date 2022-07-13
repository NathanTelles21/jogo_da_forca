#!/usr/bin/env python
# coding: utf-8

# In[13]:


secreto = 'perfume'
digitados = []
chances = 5

while True:
    if chances < 1:
        print("Você perdeu!!")
        break
        
    letra = input('Digite uma letra: ')
    
    if len(letra) > 1:
        print('Isso não vale')
        continue
        
    digitados.append(letra)
    
    if letra in secreto:
        print(f'A letra "{letra}" existe na palavra secreta')
    else:
        print(f'A letra "{letra}" NÃO EXISTE na palavra secreta')
        digitados.pop()
        
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitados:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
            
    if secreto_temporario == secreto:
        print(f'You WIN !! A palavra secreta era "{secreto_temporario}"')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')
        
    if letra not in secreto:
        chances -= 1
        
    print(f'Você ainda tem {chances} chances')


# 

# In[ ]:





# In[ ]:




