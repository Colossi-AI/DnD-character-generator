class Data():
    def __init__(self):
        self.races = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Halfling',
         'Half-Orc', 'Human', 'Tiefling', 'Aaracockra', 'Genasi', 'Goliath', 'Aasimar', 'Bugbear', 
         'Firbolg', 'Goblin', 'Hobgoblin', 'Kenku', 'Kobold', 'Lizardfolk', 'Orc', 'Tabaxi', 'Triton', 
         'Yuan-ti Pureblood', 'Feral Tiefling', 'Tortle', 'Changeling', 'Kalashtar', 'Orc of Eberron', 
         'Shifter', 'Gith', 'Centaur', 'Loxodon', 'Minotaur', 'Simic Hybrid', 'Vedalken', 'Verdan']
         
        self.appearence = ['Flashy jewelry: earrings, necklace, bracelet, bracelets', 'Piercings', 'Fancy or foreign clothes', 'Formal and clean clothes', 'Torn and dirty clothes', 
        'Notorious scar', 'Missing tooth', 'Missing fingers', 'Unusual eye color (or two different colors)', 'Tattoos', 'Birthmark', 'Unusual skin color', 'Bald', 'Braided beard or hair', 'Unusual hair color', 
        'Nervous eyes movement', 'Distinctive nose', 'Different posture (crooked or rigid)', 'Exceptionally beautiful', 'Exceptionally ugly', 'A long, glorious beard. Each braid represents another person that has asked him what the\n braids mean.',
        'The npc has a cleft cut into their nose.', 'The npc has many tiny tattoos across their face starting from the corner of their mouth to the\n edge of their eye.',
        'The npc has an extra hand coming out of their right arm the hand is as small as a child’s and is\n blackened and seems to be of no use.', 'The NPC is missing a tooth.',
        'One of the NPC’s arms is a different tone, length, and has a different shape of hand\n than the other.', 'The NPC has been cursed to have a part of their body, (arm, leg, hand, maybe even a tail…)\n that is of a different race. (ex. A human with the hand of a tabaxi…)',
        'The NPC has many scars and callouses along their forearms, perhaps being formed over many\n brutal sparring sessions.', 'The NPC has long, slender fingers, perhaps from living an easy life in the high class or perhaps\n from living a life scrounging in the streets.'
        'The NPC has well-toned leg muscles. Clearly, they are used to running.', 'The NPC has bags under their eyes, perpetually unable to sleep a full night.', 
        'The NPC has meticulously groomed hair (beard and mustache as well, if applicable) and is\n almost never seen with an out-of-place hair.',
        'The NPC wears an array of gaudy and flamboyant jewellery, supporting itself on a cane\n embedded with a poorly cut ruby too big to be real. It’s ears sport a multitude of filigree ear\n rings, as if to distract from it crooked and yellow teeth.',
        'The npc’s eyes change color with their mood.', 'The npc is abnormally tall/short for their race.', 'The NPC’s left hand has steel claws that appear to be artificially attached.',
        'The NPC has a very faint tattoo on their forehead that requires a DC 15 Investigation check to\n make out clearly. The tattoo is enchanted to cast suggestion on someone who successfully\n investigates the tattoo. The suggestion is “Stop looking at my forehead.',
        'NPC has no hair.', 'NPC has a mohawk.', 'NPC has a beard with beads in it.', 'NPC has half of their hair blonde, and has one blonde eye on the same side.', 'NPC is carrying a large sack. On the sack are the letters TBD.',
        'NPC doesn’t have eyebrows, but instead has tattooed eyebrows slightly too high, which gives a look\n of permanent surprise.', 'PC is covered in tattoos of the cities they have been to. Each one best representing that city.',
        'NPC has a mouth on their back that says mean stuff about them. This  would usually sadden\n people but this just pushes them to complete their goals more.', 
        'NPC has a horn coming out of their forehead that they are very self conscious about.\n They constantly shave it off if they have time.', 'NPC has scales on his legs. (If they are a species that usually has scales then their legs\n are human.)',
        'NPC has no natural teeth left. Luckily for him his enemies had some of theres. His jaw is full\n of random teeth that are surgically placed in. They may not be fabulous but they sure is scary!', 'NPC has a magical tattoo that can answer riddles.',
        'NPC is missing his left eye. He constantly forgets which eye is actually gone.', 'NPC has acid burn scars on both of his hands.', 'NPC is fascinated by jewelry so much so that they are wearing so much jewelry that it weighs\n them down.', 
        'NPC has a scar around their neck.', 'NPC has orange eyes that glow when near heroic people.', 'NPC has white eyes that glow when near neutral good to lawful good holy symbols.', 'NPC has red eyes that glow when near blood.', 
        'NPC has green eyes that glow when near poison.', 'NPC is extremely muscular but lazy in actions.', 'NPC has bright yellow hair that glows in the dark.', 'NPC has the tail of a rat.', 'NPC is blinded in daylight but can see perfectly in the dark.',
        'NPC was given a curse by a witch when he was a child and now has a finger on his right\n arm that points in the direction of the closest person that wants to kill him.', 
        'NPC has a extremely chapped li ps.', 'NPC has a tattoo of a map leading to an X. Doesn’t remember when it got there or\n why it’s there.', 'NPC has a mechanical limb that they cannot fully control. It does the motion for whatever he\n is thinking even if it’s socially wrong.',
        'NPC has a horrid burn mark running down from their left elbow to their hand.', 'The NPC is missing his/her left arm, and doesn’t seem quite used to functioning without it.', 'The NPC has a jewel implanted in the place of a lost eye.',
        'The NPC has a distracting mole.', 'The NPC has one long fingernail, presumably left unfiled for strumming an instrument.', 'The NPC has a violet bruise on the bone of their cheek.', 'The NPC has acne scars pockmarked across their face.', 
        'The NPC has a snaggletooth long enough to be a fang.', 'The NPC has one leg severely deformed; they carry themselves around on double crutches.', 'The NPC has a pair of thick spectacles that don’t fit.',
        'The NPC has thick, greasy dreadlocks from years of improper washing.', 'The NPC has one eye swollen over from a recent fight.', 'The NPC’s mouth is permanently crooked, giving them a cocky smirk even in serious moments',
        'The NPC has not cut or groomed his/her hair since he/she was defeated by his/her rival 8 years ago.', 'Scars… Everywhere.', 'The NPC has a beard that is visibly fake.', 'The NPC has an eye on the palm of his/her right hand that he/she tries to hide\n with a fingerless glove.',
        'NPC has one blue eye and one brown.', 'NPC’s face has splotches the color of red wine.', 'NPC has a sparse beard, like underarm hair.', 'NPC has bushy eyebrows that waggle when they talk.', 'The NPC has no nose. He has one big hole where the nose was supposed to be.',
        'NPC walks with a significant limp requiring a cane to help them walk.', 'NPC has a very muscular upper body, but their legs look very underdeveloped.', 'Male NPC talks with a define lisp and tends be be flamboyant with arm gestures.', 'NPC has 6 fingers.',
        'NPC has a Hunchback and disfigured face with extra growths.', 'NPC has whats left of a hand still attached. It looks like it was crushed and\n was never amputated.', 'NPC has abnormally large forearms and/or calves.', 'The NPC is wearing an obvious wig.',
        'The NPCs left eye has three pupils.', 'The NPC constantly smells of rosemary and brimstone.', 'The NPC has a long pointy nose that curls and wiggles according the NPC’s emotions.', 'A holy symbol is branded onto the NPC’s right hand.',
        'The NPC’s teeth are made out of various rare metals.', 'Exotic runes are carved on the NPC’s forearm.', 'NPC’s hands are stained multiple colors.', 'NPC has a forked tongue', 'NPC has piercings all over their body. Bars and rings cover them.',
        'NPC is blind/deaf.', 'NPC has ashen skin and no hair.', 'NPC has sharpened teeth and loves to smile.', 'NPC is unusually hairy, having thick hair on almost all visible skin apart from around\n eyes and palms.', 'NPC always wears bright, vibrant clothing.',
        'NPC constantly twitches. They can’t stay still.', 'The skin on the NPC’s left forearm is transparent.', 'There are small mushrooms on the back of the NPC’s neck.', 'The NPC has small woodland critters in their hair.', 'The NPC uses overly-exagerated movements for everything.'
        'The NPC is slowly rotting away.', 'The NPC has incredibly beautiful features. One of the most beautiful people you’ve ever seen!']

        self.talents = ['Plays a music instrument', 'Speaks several languages fluently', 'Unbelievably luck', 'Perfect memory', 'Great with animals', 'Great with children',
        'Great at solving puzzles', 'Great at one game', ' Great at impersonations', 'Draws Beutifully', 'Paints beautifully', 'Sings beautifully', 
        'Drinks everyone under the table', 'Expert carpenter', 'Expert cook', 'Expert dart thrower and rock skipper', 'Expert juggler', 
        'Skilled actor and master of disguise', 'Skilled dancer', '''Know thieves' cant''' ]

        self.manneirisms = ['Prone to singing, whistling, or humming quietly', 'pulls on ear', 'taps chin', 'wrings hands', 'flexes arms', 'puffs out chest', 'clenches fist(s)', 'clenches jaw', 'looks at the speakers forehead', 'taps nose', 'licks lips', 'chews nails',
        'chews straw/tobacco/gum', 'clicks tounge', 'acts bored', 'swallows a lot', 'pulls/twists clothing', 'covers mouth when speaking', 'sniffs often', 'bites lips', 'teeth chatter or grind', 'coughing (genuine)', 'constantly clears throat (think umbridge)',
        'adjusts glasses/spectacles', 'caresses a coin', 'strokes chin/beard', 'invades personal space', 'flips a coin', 'rests hand on hilt of sword/dagger', 'shamelessly hits on all male PCs (winks, waggle-brows, touching, etc)',
        'shamelessly hits on all female PCs  (winks, waggle-brows, touching, etc)', 'Rarely blinks', 'Excessive blinking', '[Pops lips](https://www.youtube.com/watch?v=MqBKJqzeeEk)', 'Flexes muscles', 'Taps foot', 'Never looks at the person talking',
        'Eyes constantly shifting around', 'Gets lost in a daze', 'Easily distracted', 'Cracks knuckles', 'Drums fingers', 'Waggles eyebrows', 'Picks nose', 'Holds head high', '[Delayed reactions](https://www.youtube.com/watch?v=IL2_MreyKMY)',
        'Slumps shoulders', 'Shuffles feet', 'Jogs in place', 'Writes down every word said', 'Only looks at the speaker’s chin']

        self.interaction_trait = ['Argumentative', 'Arrogant', 'Blustering', 'Rude', 'Curious', 'Friendly', 'Honest', 'Hot tempered', 'Irritable', 'Ponderous', 'Quiet', 'Suspicious']

        self.ideals = [['Good - Beauty', 'Good - Charity', 'Good - Greater good', 'Good - Life', 'Good - Respect', 'Good - Self-sacrifice'], ['Neutral - Balance', 'Neutral - Knowledge', 'Neutral - Live and let live', 'Neutral - Moderation', 'Neutral - Neutrality', 'Neutral - People'],
        ['Evil - Domination', 'Evil - Greed', 'Evil - Might', 'Evil - Pain', 'Evil - Retribution', 'Evil - Slaughter'], ['Lawful - Community', 'Lawful - Fairness', 'Lawful - Honor', 'Lawful - Logic', 'Lawful - Responsability', 'Lawful - Tradition'], 
        ['Chaotic - Change', 'Chaotic - Creativity', 'Chaotic - Freedom', 'Chaotic - Independence', 'Chaotic - No limits', 'Chaotic - Whimsy'], ['Other - Aspiration', 'Other - Discovery', 'Other - Glory', 'Other - Nation', 'Other - Redemption', 'Other - Self-knowledge']]

        self.bonds = ['Dedicated to fulfilling a personal life goal', 'Protective of close family members', 'Protective of colleagues or compatriots', 'Loyal to a benefactor, patron, or employer',
        'Captivated by a romantic interest', 'Drawn to a special place', 'Protective of a sentimental keepsake', 'Protective of a valuable possession', 'Out of revenge']

        self.flaws = ['Forbidden love or susceptibility to romance', 'Enjoys decadent pleasures', 'Arrogance', 'Envies another creatures possessions or station', 'Overpowering greed', 'Prone to rage', 'Has a powerful enemy', 'Specific phobia', 'Shameful or scandalous history', 
        'Secret crime or misdeed', 'Possession or forbidden lore', 'Foolhardy bravery']

        self.vocal_textures = ['Gruff', 'Smooth', 'Strained', 'Relaxed', 'Breathy', 'From the back of the throat (wolfy)', 'Scratchy', 'Nasal']

        self.vocal_patterns = ['Speaks in rhyme or some other peculiar way', 'Incoherent except for a few key words', 'Stutters', 'lots of um', 'lots of like', 'lots of swearing', '''uses thee's and thou's''', 'never stops to breathe', 'Short, clipped sentences', 'talks in third person',
        '''doesn't conjugate well ("me make good soup")''', 'all S-sounds become Z-sounds', 'all w-sounds become v-sounds', '''R's arrrrrre always rrrrrrrolled''', 'Whiny', 'stuffy nose', 'tongue stuck to back of teeth',
        'opens mouth too wide', 'clenched teeth', 'barely opens lips', 'repeats the last few words of a sentence/thought ("nice to meet you, meet you.")', 'uses full titles or descriptions of how he knows you ("ellen-farmers-daughter is pretty")',
        'strings together adj/adv for more impact ("wow, your dress is pretty-pretty!" "I am short-short-short.")', 'All non-proper nouns end with "en"/"sen" ("may I have some applesen?" "I saw a big moosen!")', 'L-sounds become w-sounds', 
        'repeats the last word you say before responding', 'sings everything', 'does the wrong em*phas*is on the wrong syl*lab*les', 'pauses often', 'staccato speech', 'Monotonous', 'whistles on S-sounds', 
        'spits on Th-sounds and S-sounds (think Sylvester the cat from Looney toons)', 'light lisp', 'r-sounds become w-sounds', 'severe underbite', 'severe overbite', 'speaks out of the corner of his mouth',
        'always pouting', '"ar/er" sounds become "aye" sounds (fart will sound like fight, water will sound like watay)', 'soft letters are elongated ("ssssso, hhhhhhow are you?")', 'slurrs words', 'mouth is always full when talking',
        'Sighs after each sentence', 'Never uses am/is/are/was/were (“I big.” “She pretty.”)', 'Responds in the form of questions', 'Always over-exaggerates', 'Never tells the complete truth', 'mutters to self']