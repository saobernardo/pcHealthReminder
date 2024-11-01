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
    reminderScreen.iconbitmap("src/icons/signofhealth_medical_10742.ico")
    reminderScreen.geometry(screen_size)
    reminderScreen.title('Lista de lembretes - PC Health Reminder')
    reminderScreen.configure(background=backgroundColor)
    
    edit_icon = tk.PhotoImage('src/icons/pencil.png')
    remove_icon = tk.PhotoImage('src/icons/trash.png')
    
    editButton = tk.Button(reminderScreen, text='Editar', font=('Montserrat', 12, 'bold'), padx=10, command=edit)

    table = ttk.Treeview(reminderScreen, columns=('id', 'tarefa', 'horario_periodico', 'horario_fixo', 'dias_semana'), show='headings')
    table.heading('id', text='ID')
    table.heading('tarefa', text='Tarefa')
    table.heading('horario_periodico', text='Horário periódico')
    table.heading('horario_fixo', text='Horário fixo')
    table.heading('dias_semana', text='Dias da semana')
    table.pack()
    
    #table.insert(parent = '', index = 0, values = ('Rato', 'Rato2', 'Rato3', 'Rato4', 'rato5', 'Rato6', 'Manocu6x'))
    i = 0
    
    for row in cursor.execute('''SELECT h.id AS id, t.descricao AS tarefa, 
    CASE WHEN h.everyxtimeenable = 1 THEN h.everyxtime ELSE 'Não habilitado' END AS everyxtime, CASE WHEN h.everyxtimeenable = 0 THEN h.defaulttime ELSE 'Não habilitado' END AS defaulttime,
    h.diasemana AS diasemana
    FROM tblhorarios h INNER JOIN tbltarefas t ON t.id = h.id_tarefa'''):
        table.insert(parent = '', index = i, values = (row[0], row[1], row[2], row[3], row[4]))
        i = i+1
        
    table.bind('<<TreeviewSelect>>', lambda event: edit(table))
    table.bind('<Delete>', lambda event: delete_item(table))
    
def edit(table):
    for i in table.selection():
        print(table.item(i))
        
def delete_item(table):
    print('Apagar')