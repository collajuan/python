def censor(text, word):
  if word in text:
    lista_palabras = text.split()
    print (lista_palabras)
    astericos = ''
    for x in word:
      astericos += '*'
    for idx, palabra in enumerate(lista_palabras):
      if word == palabra:
        lista_palabras[idx] = astericos
    return ' '.join(lista_palabras)
  

print (censor("this hack is wack hack", "hack"))