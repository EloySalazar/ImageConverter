import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green") 

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Converter")
        self.geometry("400x300")
        self.resizable(0,0)
        
        self.initialize_gui()


    def converter_image(self):

        self.im = Image.open(self.entry_converter.get()).convert("RGB")

        files = os.path.split(self.entry_converter.get())[1]
        file = files[:files.find(".")]
        exten = files[files.find("."):]
       

        if exten == ".jpg":
            self.im.save(file + ".png", quality=95)
            messagebox.showinfo("Succes","The image was successfully converted.")
        elif exten == ".png":
            self.im.save(file + ".jpg", quality=95)
            messagebox.showinfo("Succes","The image was successfully converted.")
        elif exten == ".webp":
            self.im.save(file + ".png",quality = 95)    
            messagebox.showinfo("Succes","The image was successfully converted.")
        else:
            messagebox.showerror("Error","This is not a valid extension")

  
        self.entry_converter.delete(0,tk.END)

    def find(self):
        file = filedialog.askopenfile(defaultextension= ".txt",filetypes= [("All files","*.*"),("Text Documents", "*.txt"),("Python","*.py")])
        file = file.name
        
        self.entry_converter.insert(tk.END,file)

    def initialize_gui(self):
 
        self.entry_converter = ctk.CTkEntry(self,width=300,font = ("Arial",22),placeholder_text= "Enter the file to convert")
        self.entry_converter.place(x = 0,y = 0)

        self.boton_find = ctk.CTkButton(self,width = 20,font = ("Arial",22),text = "...",command= self.find)
        self.boton_find.place(x = 300,y = 0)

        self.boton_converter = ctk.CTkButton(self,text = "Converter",font = ("Arial",25),command= self.converter_image)
        self.boton_converter.place(x = 0,y = 200)



app = App()
app.mainloop()