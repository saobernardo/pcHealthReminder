import tkinter as tk
from plyer import notification
from tkinter import *
import apsw
import apsw.bestpractice
import sys
sys.path.insert(0, './src/screens')
from reminderslist import reminderlist_screen
from threadslist import  threadslist_screen

apsw.bestpractice.apply(apsw.bestpractice.recommended)

db = apsw.Connection('db.sqlite', flags=apsw.SQLITE_OPEN_READWRITE)
cursor = db.cursor()

def open_window(main, name = 'lembretes'):
    match name:
        case 'lembretes':
            return reminderlist_screen(main)
        case 'tarefas':
            return threadslist_screen(main)
        case _:
            return 'Não encontrado'

#Main Screen

for row in cursor.execute('SELECT background_color, font_color, screen_size FROM tbltheme_configuration WHERE active = 1'):
    backgroundColor = '#%s' % row[0]
    font_color = '#%s' % row[1]
    screen_size = row[2]

mainScreen = tk.Tk()
mainScreen.iconbitmap("src/icons/signofhealth_medical_10742.ico")
menubar = tk.Menu(mainScreen)

reminders_menu = tk.Menu(menubar, tearoff=0)
reminders_menu.add_command(label='Lembretes', command=lambda: open_window(mainScreen, 'lembretes'))
reminders_menu.add_command(label='Tarefas', command=lambda: open_window(mainScreen, 'tarefas'))
reminders_menu.add_separator()
reminders_menu.add_command(label='Sair', command = mainScreen.quit)
menubar.add_cascade(label='Arquivo', menu=reminders_menu)

configurations_menu = tk.Menu(menubar, tearoff=0, title='Configurações')
configurations_menu.add_command(label='Configuração do sistema', command=lambda: open_window(mainScreen))
configurations_menu.add_separator()
configurations_menu.add_command(label='Sobre o sistema', command=lambda: open_window(mainScreen))
menubar.add_cascade(label='Sistema', menu=configurations_menu)

mainScreen.geometry(screen_size)
mainScreen.title('PC Health Reminder')
mainScreen.configure(background=backgroundColor, menu=menubar)

mainScreen.mainloop()