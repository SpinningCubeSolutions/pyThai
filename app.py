import pyperclip as pc
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry, Button
from thai import trans_thai

class MainWindow(Frame):

    def __init__(self):
        super().__init__()

        self.startUI()

    def startUI(self):
        self.master.title("Thai Transliterator")
        self.pack(fill=BOTH, expand=True)

        def transliterate():
            text = text_thai.get("1.0","end")
            transliteration = trans_thai(text)
            text_transliteration["state"] = "normal"
            text_transliteration.delete("1.0","end")
            text_transliteration.insert("1.0", transliteration)
            text_transliteration["state"] = "disabled"
            
        def copy():
            pc.copy(text_transliteration.get("1.0","end"))

        def paste():
            text_thai.delete("1.0","end")
            text_thai.insert("1.0", pc.paste())

        
        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl_thai = Label(frame1, text="Thai Text:", width=10)
        lbl_thai.pack(side=LEFT,padx=5, pady=5)

        btn_paste = Button(frame1, text="Paste", command=paste)
        btn_paste.pack(side=LEFT, padx=5,pady=5)

        text_thai = Text(frame1, height=10)
        text_thai.pack(fill=X, expand = True )

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Romanized", width=10)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        btn_copy = Button(frame2, text="Copy!", command=copy)
        btn_copy.pack(side=LEFT, padx=5,pady=5)

        text_transliteration = Text(frame2, height=10)
        text_transliteration["state"] = "disabled"
        text_transliteration.pack(fill=X, expand = True, pady=15)

        frame3 = Frame(self)
        frame3.pack(fill=X)

        btn_submit = Button(frame3, text="Transliterate!", command=transliterate)
        btn_submit.pack(side=LEFT, padx=5,pady=5)

        

def main():

    root = Tk()
    app = MainWindow()
    root.mainloop()

if __name__ == "__main__":
    main()



