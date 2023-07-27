from gingerit.gingerit import GingerIt
import pyperclip

text = pyperclip.paste()
text = text.lower()
parser = GingerIt()
a = parser.parse(text)
b = a["result"].capitalize()
pyperclip.copy(b)
