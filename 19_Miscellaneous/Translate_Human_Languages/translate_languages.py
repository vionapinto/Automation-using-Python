from googletrans import Translator

#<python path> -m pip install googletrans==3.1.0a0

translator = Translator()

translation = translator.translate('Wie geht es dir?', dest='en').text

print(translation)