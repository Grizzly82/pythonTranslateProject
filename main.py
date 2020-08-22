from translate import Translator

#Link to ISO lang codes : http://www.lingoes.net/en/translator/langcode.htm
# es=Spanish, ja=Japanese, zh=Chinese ...

translator = Translator(to_lang="es")

try:
    with open('translateText.txt', mode='r+') as my_file:
        myFile = my_file.read()
        translation = translator.translate(myFile)
        with open('.test-lang.txt', mode='w') as new_file:
            new_file.write(translation)
            new_file.close()
except FileNotFoundError as err:
    print("This file was not found or does not exist")
