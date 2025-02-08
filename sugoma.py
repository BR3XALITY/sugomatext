#!/usr/bin/env python3
import tkinter
from tkinter import filedialog
import tkinter.font as tkfont

# Adjust size 
root.geometry( "200x200" ) 
  
# Change the label text 
def show(): 
    label.config( text = clicked.get() ) 
  
# Dropdown menu options 
options = [ 
    "Hawk", 
    "Tuah", 
    "Spit", 
    "On", 
    "Dat", 
    "LOOW", 
    "TAPEERR FADEE"
] 
  
# datatype of menu text 
clicked = StringVar() 
  
# initial menu text 
clicked.set( "Monday" ) 
  
# Create Dropdown menu 
drop = OptionMenu( root , clicked , *options ) 
drop.pack() 
  
# Create button, it will change label text 
button = Button( root , text = "click Me" , command = show ).pack() 
  
# Create Label 
label = Label( root , text = " " ) 
label.pack() 

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

def get_tab_size():
    global tab_size
    tab_size = entry.get()
    top.destroy()
    tabsize_l = []
    for i in range(int(tab_size)):
        tabsize_l.append(" ")
    textbox.config(tabs=font.measure("".join(tabsize_l)))

def changetabsize():
    global top, entry
    top = tkinter.Toplevel(screen, bg="#232323")
    top.geometry("250x100")
    top.title("Config")
    label = tkinter.Label(top, text="Number of spaces in tab?", bg="#232323", fg="#FFFFFF")
    label.pack()
    entry = tkinter.Entry(top, bg="#232323", fg="#FFFFFF", insertbackground="gray")
    entry.pack()
    entry.focus_set()
    button = tkinter.Button(top, text="Submit", command=get_tab_size, bg="#444444", fg="#FFFFFF")
    button.pack()

def main():
    global screen, menu_bar, textbox, font, tab_size
    screen = tkinter.Tk()
    screen.title("sugomatext")
    screen.geometry("1080x720")
    screen.bind("<Control-o>", open_dialog_open)
    screen.bind("<Control-s>", save_file)
    screen.bind("<Control-q>", close)
    menu_bar = tkinter.Menu(screen, bg="#444444", fg="#FFFFFF")
    screen.config(menu=menu_bar)
    file_menu = tkinter.Menu(menu_bar, tearoff=False, bg="#444444", fg="#FFFFFF")
    file_menu.add_command(label="Open... (CTRL-O)", command=open_file)
    file_menu.add_command(label="Save as... (CTRL-S)", command=savefile)
    file_menu.add_command(label="Quit (CTRL-Q)", command=closequit)
    config_menu = tkinter.Menu(menu_bar, tearoff=False, bg="#444444", fg="#FFFFFF")
    config_menu.add_command(label="Tab size", command=changetabsize)
    menu_bar.add_cascade(label="File", menu=file_menu)
    menu_bar.add_cascade(label="Config", menu=config_menu)
    textbox = tkinter.Text(screen, insertbackground="grey", height=80, width=620)
    textbox.configure(bg="#232323", fg="#FFFFFF")
    font = tkfont.Font(font=textbox['font'])
    tab_size = font.measure("    ")
    textbox.pack()
    textbox.config(tabs=tab_size)
    screen.mainloop()

if __name__ == "__main__":
    main()

