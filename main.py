import tkinter.messagebox
import PIL
from PIL import ImageTk, Image
from tkinter import *
from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key=key)
password = ""
window = Tk()
window.title("Secret notes!")
window.minsize(300, 600)
window.config(bg="light blue", pady=30)

img = PIL.Image.open("secret.gif")
resizeImg = ImageTk.PhotoImage(img.resize((50, 50)))

imageLabel = Label(image=resizeImg, pady=1000, bg="black")
imageLabel.pack()

titleLabel = Label(text="Enter your title", bg="light blue", pady=10, font=("Arial", 12, "normal"))
titleLabel.pack()

titleEntry = Entry(width=30)
titleEntry.pack()

secretLabel = Label(text="Enter your secret", bg="light blue", pady=10, font=("Arial", 12, "normal"))
secretLabel.pack()

secretText = Text(width=20, height=10)
secretText.pack()

keyLabel = Label(text="Enter master key", bg="light blue", pady=10, font=("Arial", 12, "normal"))
keyLabel.pack()

keyEntry = Entry(width=30)
keyEntry.pack()


def saveBtnClicked():
    global password
    text = secretText.get(0.1, END)
    if text != "" and titleEntry.get() != "" and keyEntry.get() != "":
        encrypt = fernet.encrypt(text.encode()).decode()
        with open("myFile.txt", mode="a") as myFile:
            myFile.write(f"{titleEntry.get()}\n{encrypt}\n\n")
            secretText.delete(0.1, END)
            titleEntry.delete(0, END)
            password = keyEntry.get()
    else:
        tkinter.messagebox.showerror(title="Error", message="please make sure of encrypted info.")


def decrytpBtnClicked():
    global password
    text = secretText.get(0.1, END)
    if text != "" and keyEntry.get() != "":
        print(password)
        if keyEntry.get() == password:
            byteText = bytes(text, "utf-8")
            decrypto = fernet.decrypt(byteText).decode()
            secretText.delete(0.1, END)
            secretText.insert("1.0", decrypto)
        else:
            tkinter.messagebox.showerror(title="Error", message="wrong password!")


saveBtn = Button(text="save & encrypt", bg="white", height=1, command=saveBtnClicked)
decryptBtn = Button(text="Decrypt", bg="white", command=decrytpBtnClicked)

saveBtn.pack()
decryptBtn.pack()

mainloop()
