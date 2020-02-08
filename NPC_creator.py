import random
from tkinter import *
from randomization_data import Data
from character_class import character


ch = character()

#window configuration
window = Tk()
window.title("D&D Character Generator")
window.configure(background = 'gold2')
window.resizable(0,0)

#Title and logo
dnd_logo = PhotoImage(file = 'dnd_logo_reduced.png')
Label(window, bg = 'gold2', image = dnd_logo, width = 250, height = 125).grid(row = 0, column = 0)

Label(window, anchor = 'nw', text = 'Character Generator', bg = 'gold2', fg = 'white', font = 'Times 34 bold'). grid(row = 0, column = 1)

#Outputs
Label(window, text = 'Strength:', bg = 'gold2', fg ='black', font='Times 15 bold').grid(row = 4, column = 0)
Label(window, text = ch.strength, bg = 'gold2', fg ='black', font='Times 15 bold').grid(row = 4, column = 1)

Label(window, text = 'Dexterity:', bg = 'gold2', fg ='black', font='Times 15 bold').grid(row = 5, column = 0)
Label(window, text = ch.dexterity, bg = 'gold2', fg ='black', font='Times 15 bold').grid(row = 5, column = 1)

Label(window, text = 'Constitution:', bg = 'gold2', fg ='black', font='Times 15 bold').grid(row = 6, column = 0)
Label(window, text = ch.constitution, bg = 'gold2', fg ='black', font='Times 15 bold').grid(row = 6, column = 1)

Label(window, text = 'Intelligence:', bg = 'gold2', fg ='black', font='Times 15 bold').grid(row = 7, column = 0)
Label(window, text = ch.intelligence, bg = 'gold2', fg ='black', font='Times 15 bold').grid(row = 7, column = 1)

Label(window, text = 'Wisdom:', bg = 'gold2', fg ='black', font='Times 15 bold').grid(row = 8, column = 0)
Label(window, text = ch.wisdom, bg = 'gold2', fg ='black', font='Times 15 bold').grid(row = 8, column = 1)

Label(window, text = 'Charisma:', bg = 'gold2', fg ='black', font='Times 15 bold').grid(row = 9, column = 0)
Label(window, text = ch.charisma, bg = 'gold2', fg ='black', font='Times 15 bold').grid(row = 9, column = 1)

#Entry

#Buttons
Button(window, activebackground = 'red4', activeforeground = 'black',
bg = 'red2', fg = 'black', height = 1, width = 12, text = 'Re-roll all', command = ch.randomize_strength).grid(row=30, column=40)


window.mainloop()

