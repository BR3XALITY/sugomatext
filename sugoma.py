#!/usr/bin/env python3
import tkinter
from tkinter import filedialog
import tkinter.font as tkfont

def main():
    global screen, menu_bar, textbox, font, tab_size
    screen = tkinter.Tk()
    screen.title("sugomatext")
    screen.geometry("1080x720")
    menu_bar = tkinter.Menu(screen, bg="#444444", fg="#FFFFFF")
    screen.config(menu=menu_bar)
    file_menu = tkinter.Menu(menu_bar, tearoff=False, bg="#444444", fg="#FFFFFF")
   config_menu = tkinter.Menu(menu_bar, tearoff=False, bg="#444444", fg="#FFFFFF")
   textbox = tkinter.Text(screen, insertbackground="grey", height=80, width=620)
    textbox.configure(bg="#232323", fg="#FFFFFF")
    font = tkfont.Font(font=textbox['font'])
    tab_size = font.measure("    ")
    textbox.pack()
    textbox.config(tabs=tab_size)
    screen.mainloop()

if __name__ == "__main__":
    main()


