import random
import pickle
from tkinter import *
from randomization_data import Data
from character_class import character

def update_character_list():
        character_menu.children["menu"].delete(0, "end")
        for c in ch.character_list:
            character_menu.children.add_command(label=c, command=lambda char=c: ch.selected_character.set(char))
        ch.selected_character.set(ch.character_list[0])      

def save_character_used():
    ch.save_character()
    update_character_list()

#interface configuration
interface_theme = 'standard'
if interface_theme == 'golden':
    buttons_background_color = 'gold'
    buttons_text_color = 'black'
    active_button_background_color = 'gold2'

    subtitles_text_color = 'red2'
    subtitles_font = 'Times 16 bold'

    characteristics_category_text_color = 'black'
    characteristics_category_font ='Times 13 bold'
    characteristics_text_color = 'black'
    characteristics_font = 'Times 13 bold'

    background_color = 'white'
elif interface_theme == 'dark':
    buttons_background_color = 'gray'
    buttons_text_color = 'black'
    active_button_background_color = 'gold2'

    subtitles_text_color = 'red2'
    subtitles_font = 'Times 16 bold'

    characteristics_category_text_color = 'black'
    characteristics_category_font ='Times 13 bold'
    characteristics_text_color = 'black'
    characteristics_font = 'Times 13 bold'

    background_color = 'midnight blue'
else:
    buttons_background_color = 'red2'
    buttons_text_color = 'white'
    active_button_background_color = 'red4'

    subtitles_text_color = 'gold'
    subtitles_font = 'Times 16 bold'

    characteristics_category_text_color = 'white'
    characteristics_category_font ='Times 13 bold'
    characteristics_text_color = 'white'
    characteristics_font = 'Times 13 bold'

    background_color = 'black'

characteristics_category_x = 670
characteristics_x = 800
subtitles_x = 720
character_name_entry = 800
button_x = 670
text_buttons_x = 800
character_menu_x = 300

x_value = -70
y_value = 200


#Window configuration
window = Tk()
window.state('zoomed')
window.title("D&D Character Generator")
window.configure(background = background_color)
window.resizable(0,0)
window.grid_rowconfigure([3, 10, 14, 21], minsize = 80)

#Creating characters
ch = character()

#Title and logo
dnd_logo = PhotoImage(file = 'dnd_logo_reduced.png')
Label(window, bg = background_color, image = dnd_logo, width = 250, height = 125).place(x=580, y = 10)

Label(window, anchor = 'nw', text = 'Character Generator', bg = background_color, fg = 'white', font = 'Times 34 bold').place(x=840, y=45)

#OUTPUTS
#Stats
Label(window, text = 'Stats:', bg = background_color, fg =subtitles_text_color, font=subtitles_font ).place(x = x_value + subtitles_x, y =y_value + 6)

Label(window, text = 'Strength:', bg = background_color, fg =characteristics_category_text_color, font=characteristics_category_font).place(x= x_value + characteristics_category_x, y=y_value + 50)
Label(window, textvariable = ch.variable_strength, bg = background_color, fg =characteristics_text_color, font=characteristics_font).place(x = x_value + characteristics_x, y=y_value + 50)

Label(window, text = 'Dexterity:', bg = background_color, fg =characteristics_category_text_color, font=characteristics_category_font).place(x=x_value + characteristics_category_x, y=y_value + 70)
Label(window, textvariable = ch.variable_dexterity, bg =background_color, fg =characteristics_text_color, font=characteristics_font).place(x =x_value + characteristics_x, y=y_value + 70)

Label(window, text = 'Constitution:', bg = background_color, fg =characteristics_category_text_color, font=characteristics_category_font).place(x=x_value + characteristics_category_x, y=y_value + 90)
Label(window, textvariable = ch.variable_constitution, bg = background_color, fg =characteristics_text_color, font=characteristics_font).place(x =x_value + characteristics_x, y=y_value + 90)

Label(window, text = 'Intelligence:', bg = background_color, fg =characteristics_category_text_color, font=characteristics_category_font).place(x=x_value + characteristics_category_x, y=y_value + 110)
Label(window, textvariable = ch.variable_intelligence, bg = background_color, fg =characteristics_text_color, font=characteristics_font).place(x =x_value + characteristics_x, y=y_value + 110)

Label(window, text = 'Wisdom:', bg = background_color, fg =characteristics_category_text_color, font=characteristics_category_font).place(x=x_value + characteristics_category_x, y=y_value + 130)
Label(window, textvariable = ch.variable_wisdom, bg = background_color, fg =characteristics_text_color, font=characteristics_font).place(x =x_value + characteristics_x, y=y_value + 130)

Label(window, text = 'Charisma:', bg = background_color, fg =characteristics_category_text_color, font=characteristics_category_font).place(x=x_value + characteristics_category_x, y=y_value + 150)
Label(window, textvariable = ch.variable_charisma, bg = background_color, fg =characteristics_text_color, font=characteristics_font).place(x =x_value + characteristics_x, y=y_value + 150)

#Physical traits
Label(window, text = 'Physical traits:', bg = background_color, fg =subtitles_text_color, font=subtitles_font ).place(x = x_value + subtitles_x, y =y_value + 190)

Label(window, text = 'Gender:', bg = background_color, fg =characteristics_category_text_color, font=characteristics_category_font).place(x=x_value + characteristics_category_x, y=y_value + 230)
Label(window, textvariable = ch.variable_gender, bg = background_color, fg =characteristics_text_color, font=characteristics_font).place(x =x_value + characteristics_x, y=y_value + 230)

Label(window, text = 'Race:', bg = background_color, fg =characteristics_category_text_color, font=characteristics_category_font).place(x=x_value + characteristics_category_x, y=y_value + 250)
Label(window, textvariable = ch.variable_race, bg = background_color, fg =characteristics_text_color, font=characteristics_font).place(x =x_value + characteristics_x, y=y_value + 250)

Label(window, text = 'Appearence:', bg = background_color, fg =characteristics_category_text_color, font=characteristics_category_font).place(x=x_value + characteristics_category_x, y=y_value + 270)
Label(window, textvariable = ch.variable_appearence, bg = background_color, fg =characteristics_text_color, font=characteristics_font).place(x =x_value + characteristics_x, y=y_value + 270)

#Personality traits
Label(window, text = 'Personality traits:', bg = background_color, fg =subtitles_text_color, font=subtitles_font ).place(x = x_value + subtitles_x, y =y_value + 320)

Label(window, text = 'Talents:', bg = background_color, fg=characteristics_category_text_color, font=characteristics_category_font).place(x=x_value + characteristics_category_x, y=y_value + 360)
Label(window, textvariable = ch.variable_talents, bg = background_color, fg =characteristics_text_color, font=characteristics_font).place(x =x_value + characteristics_x, y=y_value + 360)

Label(window, text = 'Manneirisms:', bg = background_color, fg=characteristics_category_text_color, font=characteristics_category_font).place(x=x_value + characteristics_category_x, y=y_value + 380)
Label(window, textvariable = ch.variable_manneirisms, bg = background_color, fg =characteristics_text_color, font=characteristics_font).place(x =x_value + characteristics_x, y=y_value + 380)

Label(window, text = 'Interaction trait:', bg = background_color, fg=characteristics_category_text_color, font=characteristics_category_font).place(x=x_value + characteristics_category_x, y=y_value + 400)
Label(window, textvariable = ch.variable_interaction_trait, bg = background_color, fg =characteristics_text_color, font=characteristics_font).place(x =x_value + characteristics_x, y=y_value + 400)

Label(window, text = 'Ideals:', bg = background_color, fg=characteristics_category_text_color, font=characteristics_category_font).place(x=x_value + characteristics_category_x, y=y_value + 420)
Label(window, textvariable = ch.variable_ideals, bg = background_color, fg =characteristics_text_color, font=characteristics_font).place(x =x_value + characteristics_x, y=y_value + 420)

Label(window, text = 'Bonds:', bg = background_color, fg=characteristics_category_text_color, font=characteristics_category_font).place(x=x_value + characteristics_category_x, y=y_value + 440)
Label(window, textvariable = ch.variable_bonds, bg = background_color, fg =characteristics_text_color, font=characteristics_font).place(x =x_value + characteristics_x, y=y_value + 440)

Label(window, text = 'Flaws:', bg = background_color, fg=characteristics_category_text_color, font=characteristics_category_font).place(x=x_value + characteristics_category_x, y=y_value + 460)
Label(window, textvariable = ch.variable_flaws, bg = background_color, fg =characteristics_text_color, font=characteristics_font).place(x =x_value + characteristics_x, y=y_value + 460)

#Vocal traits
Label(window, text = 'Vocal traits:', bg = background_color, fg =subtitles_text_color, font=subtitles_font ).place(x = x_value + subtitles_x, y =y_value + 500)

Label(window, text = 'Voice speed:', bg = background_color, fg =characteristics_category_text_color, font=characteristics_category_font).place(x=x_value + characteristics_category_x, y=y_value + 540)
Label(window, textvariable = ch.variable_voice_speed, bg = background_color, fg =characteristics_text_color, font=characteristics_font).place(x =x_value + characteristics_x, y=y_value + 540)

Label(window, text = 'Voice pitch:', bg = background_color, fg =characteristics_category_text_color, font=characteristics_category_font).place(x=x_value + characteristics_category_x, y=y_value + 560)
Label(window, textvariable = ch.variable_voice_pitch, bg = background_color, fg =characteristics_text_color, font=characteristics_font).place(x =x_value + characteristics_x, y=y_value + 560)

Label(window, text = 'Vocal texture:', bg = background_color, fg =characteristics_category_text_color, font=characteristics_category_font).place(x=x_value + characteristics_category_x, y=y_value + 580)
Label(window, textvariable = ch.variable_vocal_texture, bg = background_color, fg =characteristics_text_color, font=characteristics_font).place(x =x_value + characteristics_x, y=y_value + 580)

Label(window, text = 'Vocal patterns:', bg = background_color, fg =characteristics_category_text_color, font=characteristics_category_font).place(x=x_value + characteristics_category_x, y=y_value + 600)
Label(window, textvariable = ch.variable_vocal_patterns, bg = background_color, fg =characteristics_text_color, font=characteristics_font).place(x =x_value + characteristics_x, y=y_value + 600)

#Character name entry
Label(window, text = 'Character name:', bg = background_color, fg =characteristics_category_text_color, font=characteristics_category_font).place(x=x_value + characteristics_category_x, y=y_value - 50)
Entry(window, textvariable= ch.variable_character_name).place(x=x_value + character_name_entry, y=y_value - 47)

#Load character menu
character_menu = OptionMenu(window, ch.selected_character, *ch.character_list)
character_menu.place(x = x_value + character_menu_x, y = y_value - 60)

#Buttons
Button(window, activebackground = active_button_background_color, activeforeground = buttons_text_color,
bg = buttons_background_color, fg = buttons_text_color, borderwidth=10, relief='raised', height = 1, width = 12, text = 'Re-roll all', command = ch.randomize_all).place(x = x_value + text_buttons_x, y = y_value + 650)

Button(window, activebackground = active_button_background_color, activeforeground = buttons_text_color,
bg = buttons_background_color, fg = buttons_text_color, borderwidth=10, relief='raised', height = 1, width = 12, text = 'Save character', command = save_character_used).place(x = x_value + text_buttons_x + 160, y = y_value - 60)

Button(window, activebackground = active_button_background_color, activeforeground = buttons_text_color,
bg = buttons_background_color, fg = buttons_text_color, borderwidth=10, relief='raised', height = 1, width = 12, text = 'Load character', command = ch.load_character).place(x = x_value + text_buttons_x + 270, y = y_value - 60)

dice_image_bigger = PhotoImage(file = 'reroll_icon_bigger_reduced.png')

Button(window, bg=background_color, borderwidth=0, image=dice_image_bigger, command = ch.randomize_stats).place(x= x_value + button_x, y=y_value)
Button(window, bg=background_color, borderwidth=0, image=dice_image_bigger, command = ch.randomize_physical_traits).place(x=x_value + button_x, y=y_value + 185)
Button(window, bg=background_color, borderwidth=0, image=dice_image_bigger, command = ch.randomize_personality_trait).place(x=x_value + button_x, y=y_value + 310)
Button(window, bg=background_color, borderwidth=0, image=dice_image_bigger, command = ch.randomize_voice_traits).place(x=x_value + button_x, y=y_value + 493)

window.mainloop()


