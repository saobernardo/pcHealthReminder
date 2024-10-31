import tkinter as tk
from tkinter import ttk
from plyer import notification
from tkinter import *
import apsw
import apsw.bestpractice

def threadslist_screen(main):
    apsw.bestpractice.apply(apsw.bestpractice.recommended)

    db = apsw.Connection('db.sqlite', flags=apsw.SQLITE_OPEN_READWRITE)
    cursor = db.cursor()

    for row in cursor.execute('''SELECT background_color, font_color, screen_size FROM tbltheme_configuration WHERE active = 1'''):
        backgroundColor = '#%s' % row[0]
        font_color = '#%s' % row[1]
        screen_size = row[2]

    threadlistScreen = tk.Toplevel(main)
    threadlistScreen.iconbitmap("src/icons/signofhealth_medical_10742.ico")
    threadlistScreen.geometry(screen_size)
    threadlistScreen.title('Lista de Tarefas - PC Health Reminder')
    threadlistScreen.configure(background=backgroundColor)