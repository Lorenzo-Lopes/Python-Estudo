"""contando letras de uma string e mostrando qual mais se repete."""


frase = "O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido von Rossum."
frase_lower = frase.lower()
frase_lower_nowhitespaces= frase_lower.replace(' ','')

repetiu_mais= 0
letra_mais_repetiu =''
i = 0 
letras_verificadas = []
while i < len(frase_lower_nowhitespaces):
    if frase_lower_nowhitespaces[i] not in letras_verificadas:
        repete = frase_lower_nowhitespaces.count(frase_lower_nowhitespaces[i])
        letras_verificadas.append(frase_lower_nowhitespaces[i])
    if repetiu_mais < repete:
        repetiu_mais = repete
        letra_mais_repetiu=frase_lower_nowhitespaces[i]
    i+=1
print (f"a letra que mais repetiu foi: {letra_mais_repetiu} , ela repete um total de {repetiu_mais}x")