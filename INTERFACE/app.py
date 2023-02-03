from tkinter import *
import webbrowser


def open_graven_channel():
    webbrowser.open_new("http://youtube.com")


# creer une premier fenetre
window = Tk()

# personnaliser cette fenetre
window.title("My Application")
# ttaille fixe
window.geometry("720x480")
window.minsize(480, 480)
# logo de fenetre
window.iconbitmap("aa.ico")
window.config(background='#41B77F')

# creer la frame
# frame = Frame(window, bg='#41B77F', bd=1, relief=SUNKEN)
frame = Frame(window, bg='#41B77F')
# aajouter un premier texte
label_title = Label(frame, text="Bienvenue sur l'application", font=("Courrier", 30), bg='#41B77F', fg='white')
label_title.pack()

# ajouter un second texte
label_subtitle = Label(frame, text="Hey salut à tous c'est Azza", font=("Courrier", 20), bg='#41B77F', fg='white')
label_subtitle.pack()
# ajouter un premier boutton
yt_button = Button(frame, text="Ouvrir Youtube", font=("Courrier", 20), bg='white', fg='#41B77F', command=open_graven_channel)
yt_button.pack(pady=25, fill=X)
frame.pack(expand=YES)
# afficher
window.mainloop()
