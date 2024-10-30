import tkinter as tk
from plyer import notification
from tkinter import *
import apsw
import apsw.bestpractice

def reminder_screen(main):
  apsw.bestpractice.apply(apsw.bestpractice.recommended)

  db = apsw.Connection('db.sqlite', flags=apsw.SQLITE_OPEN_READWRITE)
  cursor = db.cursor()

  for row in cursor.execute('''
  SELECT background_color, font_color, screen_size FROM tbltheme_configuration WHERE active = 1
  '''):
    backgroundColor = '#%s' % row[0]
    font_color = '#%s' % row[1]
    screen_size = row[2]

  reminderScreen = tk.Toplevel(main)
  reminderScreen.geometry(screen_size)
  reminderScreen.title('Reminders - PC Health Reminder')
  reminderScreen.configure(background=backgroundColor)

if __name__ == '__main__':
  reminder_screen()