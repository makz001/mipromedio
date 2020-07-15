from tkinter import Tk, Label, Entry, Button

class Mipromedio():
    def __init__(self, v):
        self.v = v
        self.v.title('Mi Promedio')
        self.v.geometry('400x500')

        # interfaz

        Label(text='nota 1', padx=20, pady=10).grid(row=0, column=0)
        self.nota1 = Entry().grid(row=0, column=1)
        Label(text='nota 2', padx=20, pady=10).grid(row=1, column=0)
        self.nota2 = Entry().grid(row=1, column=1)
        Label(text='nota 3', padx=20, pady=10).grid(row=2, column=0)
        self.nota3 = Entry().grid(row=2, column=1)
        Label(text='nota 4', padx=20, pady=10).grid(row=3, column=0)
        self.nota4 = Entry().grid(row=3, column=1)
        Label(text='nota 5', padx=20, pady=10).grid(row=4, column=0)
        self.nota5 = Entry().grid(row=4, column=1)
        Label(text='nota 6', padx=20, pady=10).grid(row=5, column=0)
        self.nota6 = Entry().grid(row=5, column=1)
        Label(text='nota 7', padx=20, pady=10).grid(row=6, column=0)
        self.nota7 = Entry().grid(row=6, column=1)
        Label(text='nota 8', padx=20, pady=10).grid(row=7, column=0)
        self.nota8 = Entry().grid(row=7, column=1)
        Label(text='nota 9', padx=20, pady=10).grid(row=8, column=0)
        self.nota9 = Entry().grid(row=8, column=1)
        Label(text='nota 10', padx=20, pady=10).grid(row=9, column=0)
      
        self.nota10 = Entry().grid(row=9, column=1)

        Button (text='+').grid(row=10, columnspan=2)

if __name__ == '__main__' :
    v = Tk()
    x = Mipromedio(v)
    v.mainloop()
