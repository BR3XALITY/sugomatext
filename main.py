#!/usr/bin/env python3
import tkinter
from tkinter import filedialog

def open_dialog_open(event):
    if event.keysym == "o" and event.state & 0x4:
        file_path = filedialog.askopenfilename()
        with open(file_path, "r") as file:
            textbox.delete(1.0, tkinter.END)
            textbox.insert(tkinter.END, file.read())
            file.close()
            
def open_file():
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

def savefile():
    file_path = filedialog.asksaveasfilename()
    with open(file_path, "w") as file:
        file.write(textbox.get("1.0", "end-1c"))
        file.close()

def close(event):
    if event.keysym == "q" and event.state & 0x4:
        result = tkinter.messagebox.askyesno("Quitting", "Quit?")
        if result:
            exit()

def closequit():
    result = tkinter.messagebox.askyesno("Quitting", "Quit?")
    if result:
        exit()    

def main():
    theme = False
    global screen
    screen = tkinter.Tk()
    screen.title("vvipertext")
    screen.geometry("1080x720")
    file_path = ""
    screen.bind("<Control-o>", open_dialog_open)
    screen.bind("<Control-s>", save_file)
    screen.bind("<Control-q>", close)
    global menu_bar
    menu_bar = tkinter.Menu(screen, bg="#444444", fg="#FFFFFF")
    screen.config(menu=menu_bar)
    file_menu = tkinter.Menu(menu_bar, tearoff=False, bg="#444444", fg="#FFFFFF")
    file_menu.add_command(label="Open... (CTRL-O)", command=open_file)
    file_menu.add_command(label="Save as... (CTRL-S)", command=savefile)
    file_menu.add_command(label="Quit (CTRL-Q)", command=closequit)
    menu_bar.add_cascade(label="File", menu=file_menu)
    global textbox
    textbox = tkinter.Text(screen, insertbackground="grey", height=52, width=620)
    textbox.configure(bg="#232323", fg="#FFFFFF")
    textbox.pack()
    screen.mainloop()

if __name__ == "__main__":
    main()

