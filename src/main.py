from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os

class Window:
    def __init__(self):
        self.window = Tk()
        self.window.title("Search String")
        self.window.resizable(0,0)
        self.window.geometry("240x130")
        self.window.iconbitmap("icon.ico")
        self.widgets()
        self.window.mainloop()

    def widgets(self):
        self.frame = ttk.LabelFrame(self.window, text="Details")
        self.frame.grid(column = 0, row = 0, padx = 5, pady = 5)
        self.label = {}
        self.entry = {}
        self.bttns = {}
        w = 20
        self.label["file"] = ttk.Label(self.frame, text = "File")
        self.label["file"].grid(column = 0, row = 0, padx = 5, pady = 5)
        self.label["strg"] = ttk.Label(self.frame, text = "String")
        self.label["strg"].grid(column = 0, row = 1, padx = 5, pady = 5)
    
        self.bttns["file"] = ttk.Button(self.frame, width = w, text = "Choose File", command = self.ChooseFile)
        self.bttns["file"].grid(column = 1, row = 0, padx = 5, pady = 5)
        self.entry["strg"] = ttk.Entry(self.frame)
        self.entry["strg"].grid(row = 1, column = 1, padx = 5, pady = 5)

        self.bttns["srch"] = ttk.Button(self.frame, text = "Search", command = self.SearchString)
        self.bttns["srch"].grid(column = 0, row = 2, padx = 5, pady = 5)

        self.bttns["cler"] = ttk.Button(self.frame, text = "Reset", command = self.Reset)
        self.bttns["cler"].grid(column = 1, row = 2, padx = 5, pady = 5)
        
    def ChooseFile(self):
        self.file = filedialog.askopenfile(mode = 'r', filetypes =[('Text Files', '*.txt')])
        self.bttns["file"]["text"] = "File Selected"

    def SearchString(self):
        self.string = self.entry["strg"].get()
        if(self.string == ""):
            self.error()
        else:
            if self.file is not None:
                self.content = self.file.read()
                if self.string in self.content:
                    self.message()
                else:
                    self.error()
            else:
                self.error()


    def message(self):
        messagebox.showinfo("Message", " Success! String found.")
  
    def error(self):
        messagebox.showerror("Message", "Failure! String not found.")

            
    def Reset(self):
        self.bttns["file"]["text"] = "Choose File"
        self.file = ""
        self.entry["strg"].delete(0,END)
        
if __name__ == "__main__":
    Window()
