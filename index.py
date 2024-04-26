from tkinter import *

from tkinter import messagebox  # Ajout pour la boîte de dialogue d'erreur
import calendar


# Fonction de lancement
def showCalendar():
    year_str = year_field.get()
    if year_str:
        year = int(year_str)
        gui = Tk()
        gui.config(background='green')
        gui.title("Calendrier pour l'année")
        gui.geometry("550x600")
        gui_content = calendar.calendar(year)
        calYear = Label(gui, text=gui_content, font="Consolas 10 bold")
        calYear.grid(row=5, column=1, padx=20)
        gui.mainloop()
    else:
        messagebox.showerror("Error", "Veuillez entrer une année valide.")

# Fonction de fermeture
def quitApp():
    root.destroy()

if __name__ == '__main__':
    root = Tk()
    root.config(background='yellow')
    root.title("Master Lipakumu Calendrier GUI")
    root.geometry("250x200")

    cal = Label(root, text="Voir Calendrier", bg='grey', font=("times", 28, "bold"))
    year = Label(root, text="Entrée l'année", bg='dark grey')
    year_field = Entry(root)
    button = Button(root, text='Cliquer ici pour voir', fg='black', bg='Blue', command=showCalendar)
    quit_button = Button(root, text='Quitter', fg='Black', bg='Red', command=quitApp)

    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    quit_button.grid(row=5, column=1)

    root.mainloop()
#MonaTechnology