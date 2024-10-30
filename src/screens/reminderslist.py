import tkinter as tk
from tkinter import ttk
from plyer import notification
from tkinter import *
import apsw
import apsw.bestpractice

def reminderlist_screen(main):
    apsw.bestpractice.apply(apsw.bestpractice.recommended)

    db = apsw.Connection('db.sqlite', flags=apsw.SQLITE_OPEN_READWRITE)
    cursor = db.cursor()

    for row in cursor.execute('''SELECT background_color, font_color, screen_size FROM tbltheme_configuration WHERE active = 1'''):
        backgroundColor = '#%s' % row[0]
        font_color = '#%s' % row[1]
        screen_size = row[2]

    reminderScreen = tk.Toplevel(main)
    reminderScreen.geometry(screen_size)
    reminderScreen.title('Lista de lembretes - PC Health Reminder')
    reminderScreen.configure(background=backgroundColor)

    table = ttk.Treeview(reminderScreen, columns=('Editar', 'id', 'tarefa', 'Horário periódico', 'Horário Fixo', 'Dias da semana', 'Excluir?'))
    table.pack()