from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator


def change(text="type", sc="English", dest="Hindi"):
    text1 = text
    sc1 = sc
    dest1 = dest
    trans = GoogleTranslator(source=sc1, target=dest1)  # Fixed the argument names
    trans1 = trans.translate(text)  # Translate the text
    return trans1


def data():
    s = com_sor.get()
    d = com_dest.get()
    masg = Sor_txt.get(1.0, END)
    textget = change(text=masg, sc=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)


root = Tk()
root.title("Translator")
root.geometry("500x800")
root.config(bg="light blue")


lab_txt = Label(root, text="Translator", font=("Times New Roman", 40, "bold"))
lab_txt.place(x=100, y=40, height=50, width=300)


frame = Frame(root).pack(side=BOTTOM)


lab_txt = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), fg="black", bg="light blue")
lab_txt.place(x=100, y=100, height=20, width=300)

Sor_txt = Text(frame, font=("Times New Roman", 20, "bold"), wrap=WORD)
Sor_txt.place(x=10, y=130, height=150, width=480)


list_text = [
    "afrikaans", "albanian", "amharic", "arabic", "armenian", "assamese", "aymara", "azerbaijani", 
    "bambara", "basque", "belarusian", "bengali", "bhojpuri", "bosnian", "bulgarian", "catalan", 
    "cebuano", "chichewa", "chinese (simplified)", "chinese (traditional)", "corsican", "croatian", 
    "czech", "danish", "dhivehi", "dogri", "dutch", "english", "esperanto", "estonian", "ewe", 
    "filipino", "finnish", "french", "frisian", "galician", "georgian", "german", "greek", 
    "guarani", "gujarati", "haitian creole", "hausa", "hawaiian", "hebrew", "hindi", "hmong", 
    "hungarian", "icelandic", "igbo", "ilocano", "indonesian", "irish", "italian", "japanese", 
    "javanese", "kannada", "kazakh", "khmer", "kinyarwanda", "konkani", "korean", "krio", 
    "kurdish (kurmanji)", "kurdish (sorani)", "kyrgyz", "lao", "latin", "latvian", "lingala", 
    "lithuanian", "luganda", "luxembourgish", "macedonian", "maithili", "malagasy", "malay", 
    "malayalam", "maltese", "maori", "marathi", "meiteilon (manipuri)", "mizo", "mongolian", 
    "myanmar", "nepali", "norwegian", "odia (oriya)", "oromo", "pashto", "persian", "polish", 
    "portuguese", "punjabi", "quechua", "romanian", "russian", "samoan", "sanskrit", "scots gaelic", 
    "sepedi", "serbian", "sesotho", "shona", "sindhi", "sinhala", "slovak", "slovenian", "somali", 
    "spanish", "sundanese", "swahili", "swedish", "tajik", "tamil", "tatar", "telugu", "thai", 
    "tigrinya", "tsonga", "turkish", "turkmen", "twi", "ukrainian", "urdu", "uyghur", "uzbek", 
    "vietnamese", "welsh", "xhosa", "yiddish", "yoruba", "zulu"
]
# Sample languages

com_sor = ttk.Combobox(frame, value=list_text)
com_sor.place(x=10, y=300, height=40, width=150)
com_sor.set("english")

button_change = Button(frame, text="Translate", relief=RAISED, command=data)

button_change.place(x=170, y=300, height=40, width=150)

com_dest = ttk.Combobox(frame, value=list_text)
com_dest.place(x=330, y=300, height=40, width=150)
com_dest.set("english")


lab_txt = Label(root, text="Dest Text", font=("Times New Roman", 20, "bold"), fg="black", bg="light blue")
lab_txt.place(x=100, y=360, height=20, width=300)

dest_txt = Text(frame, font=("Times New Roman", 25, "bold"), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)


root.mainloop()
