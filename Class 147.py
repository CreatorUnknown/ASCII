from tkinter import *
root = Tk()
root.title("ASCII Converter")
root.geometry("400x400")
root.configure(bg = "snow")

word = Entry(root)
word.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label = Label(root,text = "Name in ASCII ", bg = "light yellow", fg = "black")
label1 = Label(root,text = "Encrypted name ", bg = "light yellow", fg = "black")

def asciiConverter():
    input_word = word.get()
    for letter in input_word:
        label["text"] += str(ord(letter)) + " "
        label1["text"] += str(chr(ord(letter)- 1))
    
button = Button(root, text = "Show name in ASCII", command = asciiConverter, bg = "gold", fg="black")

button.place(relx = 0.5, rely = 0.5, anchor = CENTER)
label.place(relx = 0.5, rely = 0.6, anchor = CENTER)
label1.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()