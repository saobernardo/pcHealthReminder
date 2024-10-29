import tkinter as tk
from plyer import notification
import apsw
import apsw.bestpractice

apsw.bestpractice.apply(apsw.bestpractice.recommended)

db = apsw.Connection('db.sqlite', flags=apsw.SQLITE_OPEN_READWRITE)
cursor = db.cursor()

for row in cursor.execute('''
SELECT background_color, font_color, screen_size FROM tblsoftware_configuration WHERE active = 1
'''):
  backgroundColor = '#%s' % row[0]
  font_color = '#%s' % row[1]
  screen_size = row[2]

mainScreen = tk.Tk()
mainScreen.geometry(screen_size)
mainScreen.title('PC Health Reminder')
mainScreen.configure(background=backgroundColor)

mainScreen.mainloop()