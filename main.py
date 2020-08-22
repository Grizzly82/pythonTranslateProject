from translate import Translator

translator = Translator(to_lang="es")

try:
    with open('translateText.txt', mode='r+') as my_file:
       # print(my_file.readlines())
        myFile = my_file.read()
        #newText = " ".join(myFile)
        translation = translator.translate(myFile)
        print(translation)
except FileNotFoundError as err:
    print("This file was not found or does not exist")
