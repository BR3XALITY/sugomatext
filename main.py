#!/usr/bin/env python3
import tkinter
from tkinter import filedialog
screen = tkinter.Tk()
screen.title("vvipertext")
screen.geometry("1080x720")
file_path = ""
def open_dialog_open(event):
    if event.keysym == "o" and event.state & 0x4:
        file_path = filedialog.askopenfilename()
        with open(file_path, "r") as file:
            textbox.delete(1.0, tkinter.END)
            textbox.insert(tkinter.END, file.read())
            file.close()
def save_file(event):
    if event.keysym == "s" and event.state & 0x4:
        file_path = filedialog.asksaveasfilename()
        with open(file_path, "w") as file:
            file.write(textbox.get("1.0", "end-1c"))
            file.close()
screen.bind("<Control-o>", open_dialog_open)
screen.bind("<Control-s>", save_file)    
textbox = tkinter.Text(screen, height=620, width=520)
textbox.configure(bg="#232323", fg="#FFFFFF")
textbox.pack()
screen.mainloop()
