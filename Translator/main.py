from googletrans import Translator
quit = False
while quit == False:
    translator = Translator()

    message = str(input("Message: "))
    language = str(input('Language: '))
    out = translator.translate(message, dest=language)
    print(out.text)

    cont = str(input("Would you like to continue? "))
    if cont.lower() in ["n", "no"]:
        quit = True
