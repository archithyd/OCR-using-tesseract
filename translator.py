import googletrans as gs
from googletrans import Translator
list_of_languages = gs.LANGUAGES

def translator1(str):
    trans=Translator()
    val = trans.detect(str)
    print(list_of_languages[val.lang])
    if val.lang=='en':
        return str
    else:
        return trans.translate(str).text



