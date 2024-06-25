meme_dict = {'XD': 'se usa cuando algo es gracioso',
             'POSSER': 'fan por moda',
             'CHAMBA': 'trabajar',
             'FANBOY': 'es un fan ciego',
             'MOMOS': 'es lo mismo que memes
            }
            
for i in range(5):
    word = input("Que palabra quieres entender?").upper()
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Aun falta agregar elementos al diccionario")
