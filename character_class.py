import random
import pickle
from randomization_data import Data
from tkinter import *

data = Data()

class character:
    'D&D character'
    
    def __init__(self, strength = 10, dexterity = 10, constitution = 10, intelligence = 10, wisdom = 10, charisma = 10,
    gender = None, race = None, appearence = None, talents = None, manneirisms = None, interaction_trait = None, 
    ideals = None, bonds = None, flaws = None, voice_speed = None, voice_pitch = None, vocal_texture = None, vocal_patterns = None):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.gender = gender
        self.race = race
        self.appearence = appearence
        self.talents = talents
        self.manneirisms = manneirisms
        self.interaction_trait = interaction_trait
        self.ideals = ideals
        self.bonds = bonds
        self.flaws = flaws
        self.voice_speed = voice_speed
        self.voice_pitch = voice_pitch
        self.vocal_texture = vocal_texture
        self.vocal_patterns = vocal_patterns
        
        #TKINTER VARIABLES:
        #Stats
        self.variable_strength = IntVar()
        self.variable_strength.set(self.strength)

        self.variable_dexterity = IntVar()
        self.variable_dexterity.set(self.dexterity)

        self.variable_constitution = IntVar()
        self.variable_constitution.set(self.constitution)

        self.variable_intelligence = IntVar()
        self.variable_intelligence.set(self.intelligence)

        self.variable_wisdom = IntVar()
        self.variable_wisdom.set(self.wisdom)

        self.variable_charisma = IntVar()
        self.variable_charisma.set(self.charisma)

        #Physical traits
        self.variable_gender = StringVar()
        self.variable_gender.set(self.gender)

        self.variable_race = StringVar()
        self.variable_race.set(self.race)

        self.variable_appearence = StringVar()
        self.variable_appearence.set(self.appearence)

        #Personality traits
        self.variable_talents = StringVar()
        self.variable_talents.set(self.talents)

        self.variable_manneirisms = StringVar()
        self.variable_manneirisms.set(self.manneirisms)

        self.variable_interaction_trait = StringVar()
        self.variable_interaction_trait.set(self.interaction_trait)

        self.variable_ideals = StringVar()
        self.variable_ideals.set(self.ideals)

        self.variable_bonds = StringVar()
        self.variable_bonds.set(self.bonds)

        self.variable_flaws = StringVar()
        self.variable_flaws.set(self.flaws)

        #Vocal traits
        self.variable_voice_speed = StringVar()
        self.variable_voice_speed.set(self.voice_speed)

        self.variable_voice_pitch = StringVar()
        self.variable_voice_pitch.set(self.voice_pitch)

        self.variable_vocal_texture = StringVar()
        self.variable_vocal_texture.set(self.variable_vocal_texture)

        self.variable_vocal_patterns = StringVar()
        self.variable_vocal_patterns.set(self.vocal_patterns)

        #Data
        self.variable_character_name = StringVar()
        self.character_list = ["None"]
        self.selected_character = StringVar()
        self.selected_character.set(self.character_list[0])
        
        #Inicialization
        self.randomize_all()

    def generate_stat(self):
        rolls = []
        rolls.append(random.randint(1, 6))
        rolls.append(random.randint(1, 6))
        rolls.append(random.randint(1, 6))
        rolls.append(random.randint(1, 6))
        rolls.sort()
        del rolls[0]
        return sum(rolls)

    def randomize_strength(self):
        self.strength = self.generate_stat()
        self.variable_strength.set(self.strength)
    
    def randomize_dexterity(self):
        self.dexterity = self.generate_stat()
        self.variable_dexterity.set(self.dexterity)
    
    def randomize_constitution(self):
        self.constitution = self.generate_stat()
        self.variable_constitution.set(self.constitution)

    def randomize_intelligence(self):
        self.intelligence = self.generate_stat()
        self.variable_intelligence.set(self.intelligence)

    def randomize_wisdom(self):
        self.wisdom = self.generate_stat()
        self.variable_wisdom.set(self.wisdom)

    def randomize_charisma(self):
        self.charisma = self.generate_stat()
        self.variable_charisma.set(self.charisma)

    def randomize_gender(self):
        self.gender = random.choice(('Male', 'Female'))
        self.variable_gender.set(self.gender)

    def randomize_race(self):
        self.race = random.choices(population = data.races,
          weights = [0.01, 0.04, 0.07, 0.03, 0.08, 0.1, 0.05, 0.13, 0.01, 0.01, 0.01, 0.02, 0.01, 0.03, 
          0.1, 0.5, 0.3, 0.1, 0.2, 0.1, 0.5, 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3, 0.2, 0.1, 0.1, 0.1, 0.1, 0.2])
        self.variable_race.set(self.race)
    
    def randomize_appearence(self):
        self.appearence = random.choice(data.appearence)
        self.variable_appearence.set(self.appearence)
    
    def randomize_talents(self):
        self.talents = random.choice(data.talents)
        self.variable_talents.set(self.talents)
    
    def randomize_manneirisms(self):
        self.manneirisms = random.choice(data.manneirisms)
        self.variable_manneirisms.set(self.manneirisms)
    
    def randomize_interaction_trait(self):
        self.interaction_trait = random.choice(data.interaction_trait)
        self.variable_interaction_trait.set(self.interaction_trait)
    
    def randomize_ideals(self):
        ideals_list = random.choice(data.ideals)
        self.ideals = random.choice(ideals_list)
        
        if 'Good' in self.ideals or 'Evil' in self.ideals:
            ideals_list = random.choices(population = data.ideals, weights = [0, 0.25, 0, 0.25, 0.25, 0.25 ])
            ideals_list = random.choice(ideals_list)
            selected_ideal = random.choice(ideals_list)
            self.ideals += ' | ' + selected_ideal
        
        elif 'Lawful' in self.ideals or 'Chaotic' in self.ideals:
            ideals_list = random.choices(population = data.ideals, weights = (0.25, 0.25, 0.25, 0, 0, 0.25))
            ideals_list = random.choice(ideals_list)
            selected_ideal = random.choice(ideals_list)
            self.ideals += ' | ' + selected_ideal
        
        elif 'Other' in self.ideals:
            ideals_list = random.choices(population = data.ideals, weights = (0.2, 0.2, 0.2, 0.2, 0.2, 0))
            ideals_list = random.choice(ideals_list)
            selected_ideal = random.choice(ideals_list)
            self.ideals += ' | ' + selected_ideal
       
        else:
            selected_ideal = self.ideals
            while self.ideals == selected_ideal:
                ideals_list = random.choice(data.ideals)
                selected_ideal = random.choice(ideals_list)
            self.ideals += ' | ' + selected_ideal
        
        self.variable_ideals.set(self.ideals)
    
    def randomize_bonds(self):
        self.bonds = random.choice(data.bonds)
        self.variable_bonds.set(self.bonds)

    def randomize_flaws(self):
        self.flaws = random.choice(data.flaws)
        self.variable_flaws.set(self.flaws)
    
    def randomize_voice_speed(self):
        self.voice_speed = random.choice(['Slow', 'Medium', 'Fast'])
        self.variable_voice_speed.set(self.voice_speed)

    def randomize_voice_pitch(self):
        self.voice_pitch = random.choice(['Low', 'Medium', 'High'])
        self.variable_voice_pitch.set(self.voice_pitch)

    def randomize_vocal_texture(self):
        self.vocal_texture = random.choice(data.vocal_textures)
        self.variable_vocal_texture.set(self.vocal_texture)

    def randomize_vocal_patterns(self):
        self.vocal_patterns = random.choice(data.vocal_patterns)
        self.variable_vocal_patterns.set(self.vocal_patterns)

    def randomize_stats(self):
        self.randomize_strength()
        self.randomize_dexterity()
        self.randomize_constitution()
        self.randomize_intelligence()
        self.randomize_wisdom()
        self.randomize_charisma()
    
    def randomize_physical_traits(self):
        self.randomize_appearence()
        self.randomize_gender()
        self.randomize_race()
    
    def randomize_personality_trait(self):
        self.randomize_talents()
        self.randomize_manneirisms()
        self.randomize_interaction_trait()
        self.randomize_ideals()
        self.randomize_bonds()
        self.randomize_flaws()
    
    def randomize_voice_traits(self):
        self.randomize_voice_speed()
        self.randomize_voice_pitch()
        self.randomize_vocal_texture()
        self.randomize_vocal_patterns()
    
    def update_data(self):
        self.variable_strength.set(self.strength)
        self.variable_dexterity.set(self.dexterity)
        self.variable_constitution.set(self.constitution)
        self.variable_intelligence.set(self.intelligence)
        self.variable_wisdom.set(self.wisdom)
        self.variable_charisma.set(self.charisma)
        self.variable_gender.set(self.gender)
        self.variable_race.set(self.race)
        self.variable_appearence.set(self.appearence)
        self.variable_talents.set(self.talents)
        self.variable_manneirisms.set(self.manneirisms)
        self.variable_interaction_trait.set(self.interaction_trait)
        self.variable_ideals.set(self.ideals)
        self.variable_bonds.set(self.bonds)
        self.variable_flaws.set(self.flaws)
        self.variable_voice_speed.set(self.voice_speed)
        self.variable_voice_pitch.set(self.voice_pitch)
        self.variable_vocal_texture.set(self.vocal_texture)
        self.variable_vocal_patterns.set(self.vocal_patterns)
        
    def randomize_all(self):
        self.randomize_stats()
        self.randomize_physical_traits()
        self.randomize_personality_trait()
        self.randomize_voice_traits()

    def save_character(self):
        self.data = [self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma,
        self.gender, self.race, self.appearence, self.talents, self.manneirisms, self.interaction_trait, self.ideals,
        self.bonds, self.flaws, self.voice_speed, self.voice_pitch, self.vocal_texture, self.vocal_patterns]
        self.character_name = self.variable_character_name.get()

        f = open(r'C:\Users\Pcyes\Desktop\programação\python\projetos\saved_characters\\' + self.character_name + '.dnd', mode = 'wb')
        pickle.dump(self.data, f)
        
        self.character_list.append(self.character_name)
    
    def load_character(self):
        self.character_name = self.variable_character_name.get()
        f = open(r'C:\Users\Pcyes\Desktop\programação\python\projetos\saved_characters\\' + self.character_name + '.dnd', mode = 'rb')
        self.loaded_data = pickle.load(f)
        self.strength = self.loaded_data[0]
        self.dexterity = self.loaded_data[1]
        self.constitution = self.loaded_data[2]
        self.intelligence = self.loaded_data[3]
        self.wisdom = self.loaded_data[4]
        self.charisma = self.loaded_data[5]
        self.gender = self.loaded_data[6]
        self.race = self.loaded_data[7]
        self.appearence = self.loaded_data[8]
        self.talents = self.loaded_data[9]
        self.manneirisms = self.loaded_data[10]
        self.interaction_trait = self.loaded_data[11]
        self.ideals = self.loaded_data[12]
        self.bonds = self.loaded_data[13]
        self.flaws = self.loaded_data[14]
        self.voice_speed = self.loaded_data[15]
        self.voice_pitch = self.loaded_data[16]
        self.vocal_texture = self.loaded_data[17]
        self.vocal_patterns = self.loaded_data[18]
        self.update_data()
        