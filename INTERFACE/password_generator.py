from tkinter import *

# creer la fenetre
window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.iconbitmap("aa.ico")
window.config(background='#4065A4')

# creation d'image
width = 300
height = 300

image =PhotoImage(file="ss.jpg")
canvas = Canvas(window, width=width, height=height, bg='#4065A4')
canvas.create_image(width / 2, height / 2, image=image)
canvas.pack(expand=YES)

# afficher la fenetre
window.mainloop()
