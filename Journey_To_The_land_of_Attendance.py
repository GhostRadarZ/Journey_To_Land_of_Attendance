# Author: Aaron Castellino and Lucas Grala
# Date: 5/8/2018
# File Name: Functions.py
# Description: This Program is a supplementary program containing Functions

import random # imports random library
import copy #imports the copy function

title_pic1 =' ╦┌─┐┬ ┬┬─┐┌┐┌┌─┐┬ ┬  ┌┬┐┌─┐  ┌┬┐┬ ┬┌─┐  ┬  ┌─┐┌┐┌┌┬┐  ┌─┐┌─┐  ╔═╗┌┬┐┌┬┐┌─┐┌┐┌┌┬┐┌─┐┌┐┌┌─┐┌─┐'#stores 1 line of the title
title_pic2 =' ║│ ││ │├┬┘│││├┤ └┬┘   │ │ │   │ ├─┤├┤   │  ├─┤│││ ││  │ │├┤   ╠═╣ │  │ ├┤ │││ ││├─┤││││  ├┤ '#stores 1 line of the title
title_pic3 ='╚╝└─┘└─┘┴└─┘└┘└─┘ ┴    ┴ └─┘   ┴ ┴ ┴└─┘  ┴─┘┴ ┴┘└┘─┴┘  └─┘└    ╩ ╩ ┴  ┴ └─┘┘└┘─┴┘┴ ┴┘└┘└─┘└─┘'#stores 1 line of the title

title_pic = [title_pic1,title_pic2,title_pic3] # stores all title graphics

creeper_pic_p1 ='██████████'# stores 1 line of the creeper
creeper_pic_p2 ='█░░░░░░░░█'# stores 1 line of the creeper
creeper_pic_p3 ='█░██░░██░█'# stores 1 line of the creeper
creeper_pic_p4 ='█░░░██░░░█'# stores 1 line of the creeper
creeper_pic_p5 ='█░░████░░█'# stores 1 line of the creeper
creeper_pic_p6 ='█░░█░░█░░█'# stores 1 line of the creeper
creeper_pic_p7 ='█░░░░░░░░█'# stores 1 line of the creeper
creeper_pic_p8 ='██████████'# stores 1 line of the creeper
creeper_pic_p9 ='  █░░░░█'# stores 1 line of the creeper
creeper_pic_p10 ='  █░░░░█'# stores 1 line of the creeper
creeper_pic_p11 ='  █░░░░█'# stores 1 line of the creeper
creeper_pic_p12 ='  █░░░░█'# stores 1 line of the creeper
creeper_pic_p13 ='██████████'# stores 1 line of the creeper
creeper_pic_p14 ='█░░░██░░░█'# stores 1 line of the creeper
creeper_pic_p15 ='█░░░██░░░█'# stores 1 line of the creeper
creeper_pic_p16 ='█▄█▄██▄█▄█'# stores 1 line of the creeper

creeper_pic = [creeper_pic_p1,creeper_pic_p2,creeper_pic_p3,creeper_pic_p4,creeper_pic_p5,creeper_pic_p6,creeper_pic_p7,creeper_pic_p8,creeper_pic_p9,creeper_pic_p10,creeper_pic_p11,creeper_pic_p12,creeper_pic_p13,creeper_pic_p14,creeper_pic_p15,creeper_pic_p16]# puts all pieces of the creeper together

grim_reaper_pic1 ="                 ,____"# stores 1 line of the grim reaper
grim_reaper_pic2 ="                 |---.\ "# stores 1 line of the grim reaper
grim_reaper_pic3 ="         ___     |    `"# stores 1 line of the grim reaper
grim_reaper_pic4 ="        / .-\  ./=)"# stores 1 line of the grim reaper
grim_reaper_pic5 ='       |  |"|_/\/|'# stores 1 line of the grim reaper
grim_reaper_pic6 ="       ;  |-;| /_|"# stores 1 line of the grim reaper
grim_reaper_pic7 ="      / \_| |/ \ |"# stores 1 line of the grim reaper
grim_reaper_pic8 ="     /      \/\( |"# stores 1 line of the grim reaper
grim_reaper_pic9 ="     |   /  |` ) |"# stores 1 line of the grim reaper
grim_reaper_pic10 ="     /   \ _/    |"# stores 1 line of the grim reaper
grim_reaper_pic11 ="    /--._/  \    |"# stores 1 line of the grim reaper
grim_reaper_pic12 ="    `/|)    |    /"# stores 1 line of the grim reaper
grim_reaper_pic13 ="      /     |   |"# stores 1 line of the grim reaper
grim_reaper_pic14 ="    .'      |   |"# stores 1 line of the grim reaper
grim_reaper_pic15 ="   /         \  |"# stores 1 line of the grim reaper
grim_reaper_pic16 ="  (_.-.__.__./  /"# stores 1 line of the grim reaper

grim_reaper_pic = [grim_reaper_pic1,grim_reaper_pic2,grim_reaper_pic3,grim_reaper_pic4,grim_reaper_pic5,grim_reaper_pic6,grim_reaper_pic7,grim_reaper_pic8,grim_reaper_pic9,grim_reaper_pic10,grim_reaper_pic11,grim_reaper_pic12,grim_reaper_pic13,grim_reaper_pic14,grim_reaper_pic15,grim_reaper_pic16]# puts all pieces of the grim reaper together


dragon_pic1 ="<>=======() "
dragon_pic2 ="(/====/|\          ()==========\)"
dragon_pic3 ="      / | \        //|\   / )"
dragon_pic4 ="        |  \      // | _/"
dragon_pic5 ="          |/|   //  //"
dragon_pic6 ="           (oo)\ //  /"
dragon_pic7 ="          //// /  |"
dragon_pic8 ="         @@/  |=\  \  |"
dragon_pic9 ="              =_ \ |"
dragon_pic10 ="                ==\ | snd"
dragon_pic11 ="             (===(  )\ "
dragon_pic12 ="            (((~) (/   |"
dragon_pic13 ="                 (((~) \  /"
dragon_pic14 ="                 / /"
dragon_pic15 ="                 '------'"
 
dragon_pic = [dragon_pic1,dragon_pic2,dragon_pic3,dragon_pic4,dragon_pic5,dragon_pic6,dragon_pic7,dragon_pic8,dragon_pic9,dragon_pic10,dragon_pic11,dragon_pic12,dragon_pic13,dragon_pic14,dragon_pic15]


sonic_pic1 ='          .,'# stores 1 line of the sanic
sonic_pic2 =".      _,'f----.._"# stores 1 line of the sanic
sonic_pic3 ="|\ ,-''/  |     ,'"# stores 1 line of the sanic
sonic_pic4 ='|,_  ,--.      / '# stores 1 line of the sanic
sonic_pic5 ="/,-. ,'`.     (_"# stores 1 line of the sanic
sonic_pic6 ='|  o|  o|__     "`-.'# stores 1 line of the sanic
sonic_pic7 =",-._.,--'_ `.   _.,-`"# stores 1 line of the sanic
sonic_pic8 ="`'' ___.,'` j,-'"# stores 1 line of the sanic
sonic_pic9 ="  `-.__.,--'"# stores 1 line of the sanic

mega_man_pic1 ='        ▄▄█▀▀▄'# stores 1 line of the megaman
mega_man_pic2 ='      ▄█████▄▄█▄'# stores 1 line of the megaman
mega_man_pic3 ='     ▄▀██████▄▄██'# stores 1 line of the megaman
mega_man_pic4 ='     █░█▀░░▄▄▀█░█'# stores 1 line of the megaman
mega_man_pic5 ='     ▄██░░░▀▀░▀░█'# stores 1 line of the megaman
mega_man_pic6 ='  ▄█▀░░▀█░▀▀▀▀▄▀▀█▄'# stores 1 line of the megaman
mega_man_pic7 =' ▄███░▄░░▀▀▀▀▀▄░███▄'# stores 1 line of the megaman
mega_man_pic8 =' ██████░░░░░░░██████'# stores 1 line of the megaman
mega_man_pic9 =' ▀███▀█████████▀███▀'# stores 1 line of the megaman
mega_man_pic10 ='    ▄█▄░▀▀█▀░░░█▄'# stores 1 line of the megaman
mega_man_pic11 =' ▄▄█████▄▀ ▀▄█████▄▄'# stores 1 line of the megaman
mega_man_pic12 ='█████████    █████████'# stores 1 line of the megaman

super_mario_pic1 ='         ▄▄▄▄'# stores 1 line of the super mario
super_mario_pic2 ='      ▄▀▀░░░░█'# stores 1 line of the super mario
super_mario_pic3 ='    ▄▀░░▄▄██████▄'# stores 1 line of the super mario
super_mario_pic4 ='   ▄█▄▄█▀░░▄░█▀▀'# stores 1 line of the super mario
super_mario_pic5 ='   █░░██▄░░▀░▀▀▀▄'# stores 1 line of the super mario
super_mario_pic6 ='   ▀▄░░▀░▄█▄░░░▄▀'# stores 1 line of the super mario
super_mario_pic7 ='    ▄██▄░░░▀▀█▀'# stores 1 line of the super mario
super_mario_pic8 ='   ▄▀░░▀██▀▀▀▄'# stores 1 line of the super mario
super_mario_pic9 ='   █░░░░█░░░░░█'# stores 1 line of the super mario
super_mario_pic10 ='   ██▄░░░█▄▄▄█▀█'# stores 1 line of the super mario
super_mario_pic11 ='    ██████▄▄██▄█'# stores 1 line of the super mario
super_mario_pic12 ='    ███████████'# stores 1 line of the super mario
super_mario_pic13 ='     █▀▀▀▀▀█▀▀'# stores 1 line of the super mario
super_mario_pic14 ='     █▄▄▄▄▄▄█'# stores 1 line of the super mario

link_pic1 ='           ░░░░░░░░░░░' # stores 1 line of links code
link_pic2 ='        ░░░░░░░░░░░░░░░░' # stores 1 line of links code
link_pic3 ='    ▒▒  ░░▓▓▓▓▓▓▓▓▓▓▓░░░  ▒▒' # stores 1 line of links code
link_pic4 ='    ▒▒  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▒▒' # stores 1 line of links code
link_pic5 ='    ▒▒▒▒▓▒▒▒░░▒▒▒▒░░▒▒▒▓▒▒▒▒' # stores 1 line of links code
link_pic6 ='    ▒▒▒▒▓▒▒▒██▒▒▒▒██▒▒▒▓▒▒▒▒' # stores 1 line of links code
link_pic7 ='      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓' # stores 1 line of links code
link_pic8 ='      ░░░▒▒▒▒▒▓▓▓▓▒▒▒▒░░▓▓▓▓' # stores 1 line of links code
link_pic9 ='  ▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░▒▒' # stores 1 line of links code
link_pic10 ='▓▓▓▓▒▒▓▓▓▓▓▓▓▓░░░░░░░░░░░░▒▒' # stores 1 line of links code
link_pic11 ='▓▓▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓░░░░▓▓' # stores 1 line of links code
link_pic12 ='▓▓▓▓▒▒▓▓▓▓▓▓▒▒░░▓▓▓▓▓▓░░' # stores 1 line of links code
link_pic13 ='▓▓▓▓▒▒▓▓▓▓▓▓▒▒▓▓▓▓░░░░░░' # stores 1 line of links code
link_pic14 ='▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░██' # stores 1 line of links code
link_pic15 ='  ▒▒▒▒▒▒▒▒▒▒    ██████' # stores 1 line of links code
link_pic16 ='                ██████' # stores 1 line of links code

link_pic = [link_pic1,link_pic2,link_pic3,link_pic4,link_pic5,link_pic6,link_pic7,link_pic8,link_pic9,link_pic10,link_pic11,link_pic12,link_pic13,link_pic14,link_pic15,link_pic16] #stores all link graphics 
mega_man_pic = [mega_man_pic1,mega_man_pic2,mega_man_pic3,mega_man_pic4,mega_man_pic5,mega_man_pic6,mega_man_pic7,mega_man_pic8,mega_man_pic9,mega_man_pic10,mega_man_pic11,mega_man_pic12]#stores all mega man graphics
sonic_pic = [sonic_pic1,sonic_pic2,sonic_pic3,sonic_pic4,sonic_pic5,sonic_pic6,sonic_pic7,sonic_pic8,sonic_pic9]#stores sonic graphics
super_mario_pic = [super_mario_pic1,super_mario_pic2,super_mario_pic3,super_mario_pic4,super_mario_pic5,super_mario_pic6,super_mario_pic7,super_mario_pic8,super_mario_pic9,super_mario_pic10,super_mario_pic11,super_mario_pic12,super_mario_pic13,super_mario_pic14]#stores all super mario pictures

#weapons = (name,descotption,atk stat)
#Starting Weapons
rubber_mallet = ['Rubber Mallet', 'Sad excuse of a hammer. Atk - 5', 5]#rubber mallet stats
mega_buster = ['Pea Shooter', 'Petty and underwhelming. Atk - 5', 5] #mega buster stats
training_sward = ['Training Sward', 'Has dull edges for the untrained hands. Atk - 5', 5] #training sward stats
spin_dash = ['Spin Dash', 'Your too slow! Atk - 5', 5] #spin dash stats

#World 1 Weapons
poke_ball = ['Poké Ball', 'Will cause brusing if thrown hard enough. Atk - 7', 7]
key_blade = ['Key Blade', 'Cannot actually open doors. Atk - 9', 9]
shrink_ray = ['Shrink Ray', 'Capture the moon in one easy step. Atk - 11', 11]
buster_sword = ['Buster Sward', 'Extremely heavy and impractical, but you look really cool holding it. Atk - 13', 13]

#World 1 Special Weapon

magic_wand = ['Magic Wand', 'Bippity boppity boo! Atk - 15', 15]

#World 2 Weapons
donut_launcher = ['Donut Launcher', 'Weaponized delights. Atk - 18', 18]
zapotron = ['Zapotron', '10 000 volts of pain and suffering. Atk - 20', 20]
lawnmower_5000 = ['Lawnmower 5000', 'You can really see the bits and pieces fly with this thing! Atk - 22', 22]
master_sword = ['Master Sward', 'The great sward of the chosen hero. Atk - 26', 26]

#World 2 Special Weapon

magic_staff = ['Staff of Butterflies and Rainbows', 'It was a struggle to forcfully stuff all the different kinds of butterflies into this staff. Atk - 30', 30]

#World 3 Weapon

death_sicle = ['Death Sicle', 'A weapons torn from the hands of the Pumpkin King. Atk - 42', 42]


###########################################################################################################################################################
#                           Following list appears after start aswell make sure to make changes there aswell                                              #
###########################################################################################################################################################
find_weapons1 = [poke_ball,key_blade,shrink_ray,buster_sword]
find_weapons2 = [master_sword,donut_launcher,zapotron,lawnmower_5000] # creates a weapons list
find_weapons3 = [death_sicle]
random.shuffle(find_weapons1)# randomizes the weapon order
random.shuffle(find_weapons2)# randomizes the weapon order
#Cheats

ban_hammer = ['Ban Hammer 5000', 'How did you get this weapon? Atk - unknown', 9999999999999999999999]

#Consumables

#Slightly increases your (4th)
#Moderately increases your (3rd)
#Greatly increases your (2nd)
#Tremendously increases your (1st)

#Attack buffs
atk_item_one = ['Protein Powder', 'Scoop not included. Slightly increases your Attack temporarily.', 1.25, 'Attack']
atk_item_two = ['Plane', 'Substitute for "jet". Moderately increases your Attack temporarily.', 1.50,'Attack']
atk_item_three = ['Super Shroom', 'Increases your strength on a physical and spiritual level. Greatly increases your attack temporarily.', 1.75, 'Attack']
atk_item_four = ['Scroll of Unlimited Power', 'As "unlimiting" as a single use item can be. Tremendously increases your attack temporarily.', 2, 'Attack']

#Speed buffs
spd_item_one = ['Broken Speedometer', 'Grants the illusion of swiftness. Slightly increases your Speed temporarily.', 1.25, 'Speed']
spd_item_two = ['Slippery Footwear', 'Utterly discusting but allows you to move around faster. Moderately increases your Speed temporarily.', 1.50, 'Speed']
spd_item_three = ['Mountable Jaguar', 'Feed regularly before you become his next meal. Greatly increases your Speed temporarily.', 1.75, 'Speed']
spd_item_four = ['Focus Powder', 'You will be able to see sounds with this stuff. Tremendously increases your Speed temporarily.', 2, 'Speed']

#Luck buffs 
lck_item_one = ['Seven Leaf Clover', 'Made in China. Slightly increases your Luck temporarily.', 1.25, 'Luck']
lck_item_two = ['Daily Horoscope', 'Too bad you can\'t read Mandarin Chinese. Moderately increases your Luck temporarily.', 1.50, 'Luck']
lck_item_three = ['Gold Plated Horseshoe', 'Useless, unnecessary and expensive. Greatly increases your Luck temporarily.', 1.75, 'Luck']
lck_item_four = ['Loaded Dice', 'Gambling ruings lives, take chance out of the equation by cheating instead. Tremendously increases your Luck temporarily.', 2, 'Luck']

#Healing items
heal_item_one = ['Fruit Salad', 'Yummy yummy. Restores 50 HP.', 50, 'Health']
heal_item_two = ['Half-Eaten Sandwitch', 'Where is the other half? Restores 70 HP.', 70, 'Health']
heal_item_three = ['Fresh Avocado', 'Tasty in a taco. Restores 90 HP.', 90, 'Health']
heal_item_four = ['Freeze Dried Water', 'Refreshingly paradoxical! Restores 120 HP.', 120, 'Health']

#Shields
#sld_item_one = ['Pot Lid', 'Resourceful at best. Blocks one attack.', 1, 'Shield']
#sld_item_two = ['Extra Thick Leather Belt', 'Doubles as disiplinary enforcing tool. Blocks one attack.', 1, 'Shield']
#sld_item_three = ['Barrier Elixer', 'Protects you from the next attacks. Blocks two attacks.', 2, 'Shield']
#sld_item_four = ['Paladium Shield', 'Shield with incomparable protecting abilities. Blocks two attacks.', 2, 'Shield']

###########################################################################################################################################################
#                           Following list appears after start aswell make sure to make changes there aswell                                              #
###########################################################################################################################################################
find_item1 = [heal_item_one, heal_item_two, atk_item_one, atk_item_two, spd_item_one, spd_item_two, lck_item_one, lck_item_two, ] #items in world one
find_item2 = [heal_item_three, heal_item_four, atk_item_three, atk_item_four, spd_item_three, spd_item_four, lck_item_three, lck_item_four, ] #items in world two
find_item3 = [heal_item_three, heal_item_four, atk_item_three, atk_item_four, spd_item_three, spd_item_four, lck_item_three, lck_item_four,  ] #items in world three
random.shuffle(find_item1)# randomizes the weapon order
random.shuffle(find_item2)# randomizes the weapon order

#store in World 1
store1_item1 = ['Half-Eaten Sandwitch    ', 'Where is the other half? Restores 70 HP.', 70, 'Health']
store1_item2 = ['Plane                   ', 'Substitute for "jet". Moderately increases your Attack temporarily.', 1.50,'Attack']
store1_item3 = ['Slippery Footwear       ', 'Utterly discusting but allows you to move around faster. Moderately increases your Speed temporarily.', 1.50, 'Speed']
store1_item4 = ['Daily Horoscope         ', 'Too bad you can\'t read Mandarin Chinese. Moderately increases your Luck temporarily.', 1.50, 'Luck']
store1_item5 = ['Fresh Avocado           ', 'Tasty in a taco. Restores 90 HP.', 90, 'Health']
store1_item6 = ['Ray Gun                 ', 'Please res me bro. Atk - 18', 18]

store1_items = [store1_item1,store1_item2,store1_item3,store1_item4,store1_item5,store1_item6]
store1_item_price = [100,100,50,50,80,1000]
store1_item_quantity = [3,2,2,2,2,1]

#store in World 2 
store2_item1 = ['Fresh Avocado        ', 'Tasty in a taco. Restores 90 HP.', 90, 'Health']
store2_item2 = ['Super Shroom         ', 'Increases your strength on a physical and spiritual level. Greatly increases your attack temporarily.', 1.75, 'Attack']
store2_item3 = ['Mountable Jaguar     ', 'Feed regularly before you become his next meal. Greatly increases your Speed temporarily.', 1.75, 'Speed']
store2_item4 = ['Gold Plated Horseshoe', 'Useless, unnecessary and expensive. Greatly increases your Luck temporarily.', 1.75, 'Luck']
store2_item5 = ['Fruit Salad          ', 'Yummy yummy. Restores 50 HP.', 50, 'Health']
store2_item6 = ['Ray Gun mk2          ', 'New and improved. Atk - 30',30]

store2_items = [store2_item1,store2_item2,store2_item3,store2_item4,store2_item5,store2_item6]
store2_item_price = [200,250,100,100,350,2000]
store2_item_quantity = [3,2,2,2,2,1]

#store in World 3
store3_item1 = ['Freeze Dried Water       ', 'Refreshingly paradoxical! Restores 120 HP.', 120, 'Health']
store3_item2 = ['Scroll of Unlimited Power', 'As "unlimiting" as a single use item can be. Tremendously increases your attack temporarily.', 2, 'Attack']
store3_item3 = ['Focus Powder             ', 'You will be able to see sounds with this stuff. Tremendously increases your Speed temporarily.', 2, 'Speed']
store3_item4 = ['Loaded Dice              ', 'Gambling ruings lives, take chance out of the equation by cheating instead.', 2, 'Luck']
store3_item5 = ['Fresh Avocado', 'Tasty in a taco. Restores 90 HP.', 90, 'Health']
store3_item6 = ['Ray Gun mk3              ', 'The ultimate version. Atk - 50',50]

store3_items = [store3_item1,store3_item2,store3_item3,store3_item4,store3_item5,store3_item6]
store3_item_price = [250,400,200,200,400,3000]
store3_item_quantity = [3,2,2,2,2,1]

#Basic enemies:

#variable name = (persons name, descrption, attack, health, speed, exp, gold)

#World 1 enemies
goomba = ('Goon baa', 'Was bullied for most of his childhood, displays an extreame case of social anxiety.', 0, 10, 200, 5, 0, ' does not want to fight. Desperatly pleads for mercy.') # array which contains all stats relating to goomba
tweety_bird = ('Teeny Bird', 'A bird of the age between 13-19.', 15, 25, 100, 15, 100, ' viciously pecks you.') # array which contains all stats relating to tweety bird
waddle_dee = ('Waddle Dee', 'Enjoys long walks on the beach and bathing in the blood of his enemies.', 15, 15, 100, 15, 120, ' hugs you tightly.') # array which contains all stats relating to nyan cat
slimes = ('Slime', 'Icky slimy and overall gross.', 15, 35, 80, 20, 120, ' slowly moves towards you.') # array which contains all stats relating to slime
daffy_duck = ("Daffy Dunk", 'Had been through a lot.', 20, 40, 100, 20, 140, ' literally shoots you with a gun.') # array which contains all stats relating to daffy duck
tasmanian_devil = ('Austalian Devil', 'Got bored from Tasmania and moved down under.', 30, 25, 120, 20, 140, ' thows high velocity boomerang. Crikey.') # array which contains all stats relating to tasmanian devil
murloc = ('Murloc', 'Not aesthetically pleasing.', 25, 50, 110, 25, 160, ' spits venom on your foot.') # array which contains all stats relating to murloc
boo = ('Queen Boo', 'Spooks children in her free time.', 20, 50, 100, 25, 160,' produces spooky "woooooo" noises.') # array which contains all stats relating to boo
billy_bob = ('Billy Bob', 'A fallen hero of tremendous potential.', 30, 60, 120, 30, 180, ' fist bumps you with an irregulary strong force.')#BILLY BOB IS THE REEPER OF SOULS

find_enemy1 = [tweety_bird, tasmanian_devil, daffy_duck, goomba, billy_bob, murloc, boo, waddle_dee, slimes]

#                                                      attack, health, speed, exp, gold

#World 2 enemies
charizard = ('Flying Lizard with a flame on its tail','Oddly nostalgic.', 30, 70, 100, 25, 120, ' scourches you with fire breath.') # array which contains all stats relating to nyan cat
Big_Daddy = ('Paternal Protector', 'Searching for his little sister.', 30, 70, 100, 25, 125, ' skewers you with his arm.') # array which contains all stats relating to nyan cat
zombie = ('Undead humman', 'Technically just a normal person.', 35, 80, 70, 30, 125,' nibbles on your brain.') # array which contains all stats relating to nyan cat
cyborg = ('Roboman', '50% human 50% robot', 40, 90, 80, 30, 130, ' fires his arm cannons.') # array which contains all stats relating to nyan cat
Blastoise = ('Blue Turle with Water Canons', 'At least he\'s not a grass starter.', 40, 90, 60, 30, 140, ' uses your body as a surfboard.') # array which contains all stats relating to nyan cat
enderman = ('Slave of the Ender Dragon', 'Has an affection for picking up blocks', 30, 100, 120, 35, 150, ' makes you dizzy by teleporting around you at high speeds.') # array which contains all stats relating to nyan cat
red_koopa = ('Slave of the Turtle King','Dislikes being stomped on.', 40, 60, 100, 30, 150, ' slowly walks into you with exceptional force.') # array which contains all stats relating to nyan cat
mutant_ninja_turtle = ('Radical Reptile','Mutant turtle named after an italian artist.', 50, 70, 100, 40, 155, ' attacks with the full force of a 7 year long karate training program.') # array which contains all stats relating to nyan cat
nyancat = ('Rainbow Kitty','Her body looks like a poptart.', 50, 80, 120, 40, 160, ' projectile vomits rainbows in your eyes.') # array which contains all stats relating to nyan cat

find_enemy2 = [charizard, Big_Daddy, zombie, cyborg, Blastoise, enderman, red_koopa, mutant_ninja_turtle, nyancat]

# World 2 mini boss

familiar_shadow = ('Familiar Shadow','A Shadow with a famiar feel to it.', 50, 80, 120, 40, 160, ' slowly sucks the life force out of your body.') # array which contains all stats relating to nyan cat
#World 3 enemies
bank_robber = ('A Bank Robber', 'We know you don\'t want to grind for items before the final fight so have some gold.', 0, 50, 200, 100, 9999999999999, ' tries to escape but runs into a wall.') # array which contains all stats relating to nyan cat

find_enemy3 = [bank_robber]

#Bosses:

#Boss attacks and abilities
#variable name = (attack descriction, attack damage, heal amount, sheild avoid, debuff, debuff value, ability charge)

agressive_hiss = ['Stalker hisses at you with desturbing malice.', 30, 0, False, 'Speed', 0.25, 0]
ram = ['Stalker charges its\' body at you.', 45, 0, False, 'None', 0, 0]
charging_fuse = ['Stalker charges it\'s fuse.', 0, 0, True, 'None', 0, 1]
explosion = ['Stalker explodes with an extremely devistating force!', 1000, 0, True, 'None', 0, 0]
stalker_attacks = [agressive_hiss, charging_fuse, ram]

sythe_slash = ['Grub Reaper slashes you with it\'s sythe.', 80, 0, True, 'None', 0, 1]
soul_feast = ['Grub Reaper munches on your soul.', 60, 30, False, 'None', 0, 1]
shadow_cast = ['Grub Reaper casts a depressing shadow over the battlefield.', 20, 0, True, 'Attack', 0.25, 1]
snacking = ['Grub Reaper begins munching on a "sad meal".', 0, 100, True, 'None', 0, 0]
grub_reaper_attacks = [sythe_slash, soul_feast, shadow_cast]

antimatter_breath = ['Mecha Dragon 4000 breathes a deadly antimatter .', 65, 0, True, 'None', 0, 1]
mecha_chomp = ['Mecha Dragon 4000 chomps your body with incredible power.', 80, 0, False, 'None', 0, 1]
confident_glance = ['Mecha Dragon 4000 glares at your soul with shocking confidence.', 0, 0, True, 'All', 0.5, 1]
spacial_pressure = ['Mecha Dragon 4000 distorts the gravity around you causing immense pressure.', 100, 0, True, 'All', 0.5, 0]
dragon_attacks = [antimatter_breath, mecha_chomp, confident_glance]


#variable name = (boss_name, boss_picture, description, health stat, max health, speed stat, exp, gold, attacks, ability, current ability charge, ability charge)
               
stalker = ['Stalker', creeper_pic, 'Embodies the rage and agony of seeing your home explode. Warning! Will explode if fuse charges for three turns!', 150, 150, 110, 40, 200, stalker_attacks, explosion, 0, 3] # array which contains all stats relating to stalker
            
grub_reaper = ['Grub Reaper', grim_reaper_pic, 'Abandoned his old occupation of a life of luxury and gluttony.', 300, 300, 150, 65, 400, grub_reaper_attacks, snacking, 0, 5] # array which contains all stats relating to grub reaper 

dragon = ['Mecha Dragon 4000', dragon_pic, 'Great defender of the diploma. Your final challenge.', 500, 500, 175, 0, 0, dragon_attacks, spacial_pressure, 0, 5]


#Characters = [name, pic, start weapon, life check, speed, luck, attack, max hp, current hp, level, xp, gold, shield]
super_mario = ['Supra Mayro',super_mario_pic,rubber_mallet, True, 100, 12, 120, 100, 100, 1, 0, 0, 0]#array containing all stats for Hero Super Mario
mega_man = ['Mini Man',mega_man_pic,mega_buster, True, 120, 12, 100, 120, 120, 1, 0, 0, 0] #array containing all stats for Hero Mega Man
link = ['Lunk',link_pic,training_sward, True, 100, 10, 120, 120, 120, 1, 0, 0, 0] #array containing all stats for Hero Link
sonic = ['Sanic',sonic_pic,spin_dash, True, 200, 15, 80, 80, 80, 1, 0, 0, 0] #array containing all stats for Hero Sonic


characters = [super_mario,link,sonic,mega_man] # stores all basic characters
consumables = [] #creates the consumables array
keyitems = [['My Blueprint','Shows you the surrounding area to help you navigate, open my blue print on the action screen']] #creates the consumables array
weapons = [] #creates the consumables array
y_n = ('Yes','No') # creates a yes no array
turn_options = ['Move','Check Profile','Open Bag','View My Blueprint','Return to Main Menu'] # turn options


#### When in Combat ####

def space(spaces): #function creates a dialogue space however long necessary
    for counter in range(0, spaces): 
        print(' ') #prints the space as many times as counter permits
        
def getNumber(question,lowest,highest): # defines function which can get a number within a range
    num_true = False # sets num true to False
    while num_true == False: # runs while num true to False
        numbersz = input(question)# gets the number input from user
        if numbersz.isdigit() == True: # checks if input was a number
            numbersz = int(numbersz) #converts numbersz to an integer
            if numbersz > highest or numbersz < lowest: # checks if numbersz is within the range
                print('please input a number between ' + str(lowest) + ' and ' + str(highest)) #shows to user the highest and lowest value
            else: #runs if number is accpetable
                num_true = True # ends the loop by changing variable
        else: # runs if user did not input a number
            print('please input a number') # tells user to input a number
    return numbersz #returns value of numbers

def getOption(question,array_of_options,name):
    print(question)
    length_list = len(array_of_options) + 1 # gets the length of list and adds 1
    for list_number in range (1,length_list): # runs for length of array but every number the counter is increased by 1
        array_number = list_number - 1 # decrease list number by 1
        if name == True:
            print(str(list_number) + ' - ' + array_of_options[array_number][0]) # prints the number with a corresponding number readable to user
        else:
            print(str(list_number) + ' - ' + array_of_options[array_number]) # prints the number with a corresponding number readable to user
    array_number = length_list - 1 # decreases length list by 1 and stores it
    item_use = getNumber('Enter: ',1,array_number) # gets the number that the user wants
    array_position = item_use - 1 # decreases items use by 1 and stores it in array position
    item_use = array_of_options[array_position] # gets appropriate items and stores it
    return item_use
            
def getOptionExit(question,array_of_options):
    print(question)
    length_list = len(array_of_options) + 1 # gets the length of list and adds 1
    for list_number in range (1,length_list): # runs for length of array but every number te counter is increased by 1
        array_number = list_number - 1 # decrease list number by 1
        print(str(list_number) + ' - ' + array_of_options[array_number]) # prints the number with a corresponding number readable to user
    print(str(length_list) + ' - Exit') # prints out the button for the user to press exit
    item_use = getNumber('Enter: ',1,length_list) # gets the number that the user wants
    if item_use != length_list: #runs if user did not input exit
        array_position = item_use - 1 # decreases items use by 1 and stores it in array position
        item_use = array_of_options[array_position] # gets appropriate items and stores it

def percentChance(): #function creates a random number between 1 to 100
    chance = random.randint(0,100) #variable holds a random number from 1 to 100
    return chance #returns the random number

def combatMenu(): #fuction displayes the combat menu and asks player for input on what to do during turn
    space(1)
    combat_choice = getOption('what would you like to do',['Attack', 'Check Enemy', 'Check Profile', 'Inventory', 'Flee'],False) #makes sure player enters a value between 1 and 4
    if combat_choice == 'Attack':
        space(1)
        print('Begin attack!')  #begin attack sequence
    elif combat_choice == 'Check Enemy':    
        space(1)
        print('Observing Enemy')#begin check sequence
    elif combat_choice == 'Check Profile':    #begin flee sequence
        space(1)
        #begin check player sequence        
    elif combat_choice == 'Inventory':
        space(1)
        print('Opening Bag') #open inventory
    elif combat_choice == 'Flee':    #begin flee sequence
        space(1)
        print('You start running') #begin flee sequence

        
    return combat_choice #returns player's choice

def whatSpeedDo(player_speed, speed_buff, attack_type): #function determines the player's total speed
    if attack_type == 'Light attack':
        player_speed = player_speed + (player_speed / 5)
    elif attack_type == 'Heavy attack':
        player_speed = player_speed - (player_speed / 5)
    speed_mltiplyer = player_speed * speed_buff #stat multiplyer
    new_speed = float(speed_mltiplyer) #cast speed value as float
    #print('Your speed ' + str(new_speed))
    return new_speed #return the player's total speed

def whatSpeedDoFlee(player_speed, speed_buff): #function determines the player's total speed
    speed_mltiplyer = player_speed * speed_buff #stat multiplyer
    new_speed = float(speed_mltiplyer) #cast speed value as float        
    return new_speed #return the player's total speed
    
def accuracy(attack_hit, new_speed, speed_chance): #function determines if the player hits the enemy
    if new_speed >= speed_chance: 
        #print('attack hit')
        attack_hit = True #player lands hit if the player's speed value is greater than the random value out of 100
    elif new_speed <= speed_chance:
        #space(1)
        input('Attack missed ~>')
        #space(1)
        attack_hit = False #player misses hit if the player's speed value is less than the random value out of 100
    elif new_speed >= 100:
        #print('attack hit')
        attack_hit = True #player always lands hit if the player's speed value is higher than 100
    else:
        print('Speed ERROR') #Speed ERROR statement
    return attack_hit #return if the player hits or misses attack
    
def whatLuckDo(player_luck, luck_buff): #function determines the player's total luck and if their hit is a critical which does double damage
    luck_chance = percentChance() #random value out of 100 is created
    #print('luck chance = ' + str(luck_chance))
    luck_mltiplyer = player_luck * luck_buff 
    new_luck = float(luck_mltiplyer) #total luck is player's luck plus any added buff
    #print('luck = ' + str(new_luck))
    if new_luck >= luck_chance:
        #print('Critcal attack')
        crit = True #player's attack is a crit if player's luck is greater or equal to percent chance
    elif new_luck < luck_chance:
        #print('Regular')
        crit = False #player's attack is regular if player's luck is less than percent chance
    else:
        print('Luck ERROR') #Luck ERROR statement
    return crit #return if attack was a crit or not

def totalDamage(player_attack, weapon_attack, crit, attack_buff, attack_type): #determines the player's total damage done to the enemy during turn
    strength = round(player_attack / 5) #stength is half of the user's attack stat
    #print('Strength ' + str(strength))
    
    if attack_type == 'Light attack' :
        player_damage = (strength + weapon_attack) * attack_buff
        player_damage = player_damage - (player_damage / 4) #player's damage is the player's attack plus the weapon's attack minus 30% for being a light attack
    elif attack_type == 'Heavy attack':
        player_damage = (strength + weapon_attack) * attack_buff
        player_damage = player_damage + (player_damage / 2) #player's damage is the player's attack plus the weapon's attack plus 30% for being a heavy attack
    else:
        print('Something wrong with the attack choice.') #ERROR attack choice
    
    if crit == True:
        space(1)
        print('Critical Hit')
        space(1)
        player_damage = player_damage * 2 #player's damage is multiplied by 2 for a crit
    elif crit == False:
        player_damage = player_damage #player's damage doesn't change
    else:
        print('Crit Error') #ERROR Crit problem

    player_damage = round(player_damage)
    return player_damage #return player's attack damage on enemy

def whoGoesFirst(new_speed, enemy_speed, enemy_name, attack_hit, enemy_hit): #function determines if player attacks first or last
    if attack_hit == True and enemy_hit == False:
        input(enemy_name + ' attacks first ~>')
        attack_priority = False #player automatically attacks first if enemy's attack missed
    elif attack_hit == False and enemy_hit == True:
        input(enemy_name + ' attacks first ~>')
        attack_priority = False #enemy automatically attacks first if player's attack missed
    elif new_speed >= enemy_speed:
        input('You attack first ~>')
        attack_priority = True #player attacks first if player's speed is greater than enemy's speed
    elif new_speed <= enemy_speed:
        input(enemy_name + ' attacks first ~>')
        attack_priority = False #enemy attacks first if player's speed is less than enemy's speed
    else:
        print('Priority ERROR') #Priority ERROR
    return attack_priority #return if the player or enemy attacks first

def hurtEnemy(current_enemy_hp, player_damage, enemy_name): #determines the enemy's health after player attacks
    #print(current_enemy_hp)
    #print(player_damage)
    current_enemy_hp = current_enemy_hp - player_damage #enemy's health is it's current health subtracted by the player's damage
    if current_enemy_hp > 0:
        print(enemy_name + ' has ' + str(current_enemy_hp) + ' HP remaining.') #display how much health the enemy has left if not yet defeated
    elif current_enemy_hp <= 0:
        print('') #print nothing if enemy's health is 0 or less
    return current_enemy_hp #return the enemy's health

def enemyAccuracy(enemy_speed, enemy_name): #determines if the enemy lands a hit on the player
    number = percentChance() #creates random value out of 100
    if (enemy_speed / 2) > number:
        hit = True #if enemy's speed is greater than chance out of 100, enemy's attack hits 
    elif (enemy_speed / 2) <= number:
        hit = True #if enemy's speed is less than chance out of 100, enemy's attack misses
    return hit #return if the enemy lands a hit or not

def enemyAttack(current_hp, enemy_attack): #determines the amount of damage the enemy does to the player
    hurt_player = current_hp - enemy_attack #player's health is deducted by the enemy's attack damage
    return hurt_player #return player's current health

def runChance(enemy_speed, player_speed): #determines the needed speed to flee from combat
    chance = percentChance() #random number out of 100
    player_speed = player_speed / 3
    #print(player_speed)
    enemy_speed = enemy_speed /5
    chance = chance + enemy_speed
    #print(chance)
    if player_speed >= chance:
        escape = True
    elif player_speed < chance:
        escape = False
    return escape
    
def runningLoss(gold): #function gets the amount of gold the player will lose from trying to run
    lost_gold = gold / 10
    lost_gold = round(lost_gold)
    return lost_gold #return the amount of gold lost

def attackChoice():
    question = 'How would you like to attack?'
    choice_one = 'Light attack'
    choice_two = 'Heavy attack'
    choice = (choice_one, choice_two)
    attack_choice = getOption(question, choice, False)
    return attack_choice

def randomizeEnemyStats(stat):
    #print('Stat changes')
    #print(stat)
    delta_stat_positive = round(stat / 10)
    #print(delta_stat_positive)
    delta_stat_negative = round(stat / -10)
    #print(delta_stat_negative)
    random_stat = random.randint(delta_stat_negative, delta_stat_positive)
    #print(random_stat)
    new_stat = stat + random_stat
    #print(new_stat)
    return new_stat

def activeCombatTutorial(names, character_stats, weapon_stash, item_stash):

    #variable name = (persons name, descrption, health stat, attack stat, speed stat, exp, gold)
    
    life = character_stats[3]                 #####################     Stats     #####################
    player_speed = character_stats[4]
    player_luck = character_stats[5]
    player_attack = character_stats[6]
    max_hp = character_stats[7]
    current_hp = character_stats[8]
    exp = character_stats[10]
    level = character_stats[9]
    gold = character_stats[11]
    #print(weapon_stash)
    weapon_attack = weapon_stash[0][2]
    #print(weapon_attack)
    enemy_name = 'Dummy'
    enemy_description = 'Tutorial fight.'
    current_enemy_hp = 30
    enemy_attack = 10
    enemy_speed = 50
    enemy_exp = 0
    enemy_gold = 0
    enemy_attack_name = ' disturbes you with it\'s ominous silence.'
    weapons = weapon_stash
    consumables = item_stash
    gained_gold = 0
    lost_gold = 0
    attack_buff = 1
    speed_buff = 1
    luck_buff = 1
    health_buff = 0
    shield_buff = character_stats[12]
    stats = ['', '', 0, '']

    input('A wild ' + enemy_name + ' has appeared ~>') #DOO DOO ROO DOO, DOO DOO ROO DOO, DOO DOO DOO DOO DOO DOO DOO DOO DOOOOOOOOOOOOOOOOOOOOOO (opening battle theme pokemon) 
    space(1)
    
    print('Dummy')
    print('Tutorial fight.')
    space(1)
    print('Has ' + str(current_enemy_hp) + ' HP remaining.')
    print('Has an attack of ' + str(enemy_attack))
    print('Has a speed of ' + str(enemy_speed))
    input('Continue ~>')
    space(1)
    input('Basic Combat ~>')
    space(1)
    print('When in combat you have the choice of either: ')
    input('attacking, checking the enemy\'s stats, checking your player\'s current stats, browsing your inventory or fleeing from combat ~>')
    space(1)
    input('When Attacking: ~>')
    space(1)
    print('You have the choice either a light attack or a heavy attack.')
    print('Light attack - a more reliable  and faster meathod of attack which hasa high chance of hitting the enemy while doing less damage to the enemy.')
    print('Heavy attack - a less reliable and slower meathod of attack which has a lower chance of hitting the enemy while doing much more damage to the enemy.')
    space(1)
    print('The enemy will then either attack you first or second depending on whether your speed is greater than that of the enemy\'s speed.')
    input('You will be rewarded with exp and gold after defeating the enemy. ~>')
    space(1)
    print('When attacking your attack has a chance of missing the enemy.')
    print('This chance is either amplified or reduced based on your speed compared to the enemy\'s speed.')
    input('The higher your speed the higher chance you have to land your attack ~>')
    space(1)
    print('Your luck also plays a role in combat as the higher luck value your player has the more common it is to have a critical hit.')
    input('A critical hit doubles the total damage of the attack. ~>')
    space(1)
    input('When Checking the Enemy\'s Stats: ~>')
    space(1)
    input('You will be told the enemy\'s name, discription, attack, speed, and remaining HP. ~>')
    space(1)
    input('When Checking Character Profile: ~>')
    space(1)
    print('You will be told all of your current stats as well as any buffs you have activated at the time.')
    space(1)
    input('When in Inventory: ~>')
    space(1)
    print('You can change your primary weapon for another weapon in your weapon stash, or use a consumable item to buff one of your stats.')
    print('Note that when you use a consumable it is gone forever.')
    input('Any attack, speed, or luck buff will only last for the duration of the battle and will go away after. ~>')
    space(1)
    input('When Fleeing: ~>')
    space(1)
    print('Your chance to escape combat is determined by your current speed.')
    print('The higher your speed the easier it will be to escape combat.')
    space(1)
    print('When you escape or attempt to escape and fail, you will lose 10% of your total current gold.')
    print('You can attampt to escape combat as many times as you wish with your gold as the cost to do so.')
    input('Note that you can never attempt to flee during any boss combat. ~>')
    space(2)
    input('Remember that choosing to do any combat option except attack will not result in the enemy\'s turn to attack you. ~>')
    
    combat_flag = True
    while combat_flag == True:

        current_choice = combatMenu() #display combat menu
        if current_choice == 'Attack':
            
            life = True
            attack_hit = True
            enemy_hit = True
            crit = True
            weapon_attack = weapon_stash[0][2]
            weapon_name = weapon_stash[0][0]
            
            attack_type = attackChoice() #ask user if they want to use a light or heavy attack
            
            space(1)

            shield_buff = shield_buff

            if attack_type == 'Light attack':
                print(attack_type)
                
            elif attack_type == 'Heavy attack':
                print(attack_type)

            weapon_attack = weapon_stash[0][2] #equip the first weapon in the weapon list

            speed_chance = percentChance() #determine the amount of speed the player needs to hit the enemy
            
            new_speed = whatSpeedDo(player_speed, speed_buff, attack_type) #determine the speed of the player after any buffs 
            
            attack_hit = accuracy(attack_hit, new_speed, speed_chance) #determine if the player acctually hits the enemy
            
            crit = whatLuckDo(player_luck, luck_buff) #determine if your attack was a critical hit or not

            player_damage = totalDamage(player_attack, weapon_attack, crit, attack_buff, attack_type) #determines the total damage to the enemy during this turn
            
            enemy_hit = enemyAccuracy(enemy_speed, enemy_name) #determine if the enemy's attack hits the player

            attack_priority = whoGoesFirst(new_speed, enemy_speed, enemy_name, attack_hit, enemy_hit) #determine if the player or the enemy attacks first
            
            if attack_hit == True: #follow path if the player hits the enemy

                if attack_priority == True:

                    space(1)
                    
                    input('You dealt ' + str(player_damage) + ' DMG with the ' + weapon_name + ' ~>') #display the player's damage done towards the enemy
                    
                    current_enemy_hp = hurtEnemy(current_enemy_hp, player_damage, enemy_name) #take away the enemy's hitpoints corresponding to your attack damage
                    
                    if current_enemy_hp <= 0: #if enemy is defeated
                        combat_flag = False #ends combat
                        print('You Won!')
                        space(1)
                        print(enemy_name + ' was defeated.')
                        input('You earned 0 gold and 0 exp ~>')
                    
                    elif current_enemy_hp > 0 and shield_buff == 0: #if enemy is alive and you have no shields
                        space(1)
                        if enemy_hit == True: #if enemy lands it's attack
                            print(enemy_name + enemy_attack_name)
                            current_hp = enemyAttack(current_hp, enemy_attack) #enemy deals it's attack to player's health
                            input(enemy_name + ' deals ' + str(enemy_attack) + ' damage ~>') #displayes how muck damage the enemy has delt towards the player
                            
                            if current_hp <= 0: #if player falls in combat
                                life = False #players life is gone
                                combat_flag = False #combat protocall finishes
                                #Player has died in combat
                                
                            elif current_hp > 0: #if player is alive and kicking
                                print('You have ' + str(current_hp) + ' HP left.') #display player's current health
                                space(1)
                                input('Next turn ~>')
                                
                    elif current_enemy_hp > 0 and shield_buff >= 1: #you still have shield
                        space(1)
                        input('You are protected from injury. ~>')
                        shield_buff = shield_buff - 1

                        if enemy_hit == False: #if enemy missed it's attack
                            space(1)
                            print(enemy_name + '\'s attack missed!')
                            input('Hallelujah! ~>')

                elif attack_priority == False: #if enemy attacks first
                    
                    if shield_buff >= 1:
                        space(1)
                        print(enemy_name + enemy_attack_name)
                        input('You are protected from injury. ~>') #enemy does no damage
                        shield_buff = shield_buff - 1 #sheild counter subtracts one

                        space(1)
                        
                        #crit = whatLuckDo(player_luck, luck_buff) #determine if your attack was a critical hit or not

                        player_damage = totalDamage(player_attack, weapon_attack, crit, attack_buff, attack_type) #determines the total damage to the enemy during this turn
                    
                        input('You dealt ' + str(player_damage) + ' DMG with the ' + weapon_name + ' ~>') #display the player's damage done towards the enemy
                    
                        current_enemy_hp = hurtEnemy(current_enemy_hp, player_damage, enemy_name) #take away the enemy's hitpoints corresponding to your attack damage
                    
                        if current_enemy_hp <= 0: #if enemy is defeated
                            combat_flag = False #ends combat
                            print('You Won!')
                            space(1)
                            print(enemy_name + ' was defeated.')
                            input('You earned 0 gold and 0 exp ~>')
                            
                        else: #if enemy is alive
                            space(1)
                            input('Next turn ~>')
                        
                    elif enemy_hit == True: #if enemy lands it's attack
                        space(1)
                        print(enemy_name + enemy_attack_name)
                        current_hp = enemyAttack(current_hp, enemy_attack) #enemy deals it's attack to player's health
                        input(enemy_name + ' deals ' + str(enemy_attack) + ' damage ~>') #displayes how much damage the enemy has delt toward the player
                            
                        if current_hp <= 0: #if player falls in combat
                            life = False #players life is gone
                            combat_flag = False #combat protocall finishes
                            #Player has died in combat
                                
                        elif current_hp > 0: #if player is alive and kicking
                            print('You have ' + str(current_hp) + ' HP left.') #display player's current health
                            space(1)
                            crit = whatLuckDo(player_luck, luck_buff) #determine if your attack was a critical hit or not

                            player_damage = totalDamage(player_attack, weapon_attack, crit, attack_buff, attack_type) #determines the total damage to the enemy during this turn
                    
                            input('You dealt ' + str(player_damage) + ' DMG with the ' + weapon_name + ' ~>') #display the player's damage done towards the enemy
                    
                            current_enemy_hp = hurtEnemy(current_enemy_hp, player_damage, enemy_name) #take away the enemy's hitpoints corresponding to your attack damage
                    
                            if current_enemy_hp <= 0: #if enemy is defeated
                                combat_flag = False #ends combat
                                print('You Won!')
                                space(1)
                                print(enemy_name + ' was defeated.')
                                input('You earned ' + str(enemy_gold) + ' gold and ' + str(enemy_exp) + ' exp ~>')
                        
                            else: #if enemy is alive
                                space(1)
                                input('Next turn ~>')
                                
                    elif enemy_hit == False: #if enemy missed it's attack
                        space(1)
                        print(enemy_name + '\'s attack missed!')
                        input('Hallelujah! ~>')

                        print('You have ' + str(current_hp) + ' HP left.') #display player's current health
                            
                        space(1)
                        crit = whatLuckDo(player_luck, luck_buff) #determine if your attack was a critical hit or not

                        player_damage = totalDamage(player_attack, weapon_attack, crit, attack_buff, attack_type) #determines the total damage to the enemy during this turn
                    
                        input('You dealt ' + str(player_damage) + ' DMG with the ' + weapon_name + ' ~>') #display the player's damage done towards the enemy
                    
                        current_enemy_hp = hurtEnemy(current_enemy_hp, player_damage, enemy_name) #take away the enemy's hitpoints corresponding to your attack damage
                    
                        if current_enemy_hp <= 0: #if enemy is defeated
                            combat_flag = False #ends combat
                            print('You Won!')
                            space(1)
                            print(enemy_name + ' was defeated.')
                            input('You earned 0 gold and 0 exp ~>')
                        
                        else: #if enemy is alive
                            space(1)
                            input('Next turn ~>')

            elif attack_hit == False: #if player's attack missed
                if enemy_hit == True: #if enemy lands it's attack
                    space(1)
                    input(enemy_name + enemy_attack_name)
                    current_hp = enemyAttack(current_hp, enemy_attack) #player's health is deducted by enemy's attack 
                    print(enemy_name + ' deals ' + str(enemy_attack) + ' damage ~>') #display how much damage was done by the enemy
                    
                    if current_hp <= 0: #Player has died in combat
                        life = False
                        combat_flag = False #ends combat
                        
                        
                    elif current_hp > 0: #Player is still alive
                        print('You have ' + str(current_hp) + ' HP left.') #display player's current health
                        space(1)
                        input('Next turn')
                        
                elif enemy_hit == False: #if enemy missed it's attack
                    space(1)
                    print(enemy_name + '\'s attack missed!')
                    input('Hallelujah! ~>')
                    
            else:
                print('') #ERROR 2
                
        elif current_choice == 'Check Enemy':
            space(1)
            print('Dummy')
            print('Tutorial Battle')
            space(1)
            print('Has ' + str(current_enemy_hp) + ' HP remaining.')
            print('Has an attack of ' + str(enemy_attack))
            print('Has a speed of ' + str(enemy_speed))
            input('Continue ~>')
            space(1)
            
        elif current_choice == 'Inventory':
            inventory_loop = True # sets the inventory loop to ture
            while inventory_loop == True: # runs while the inventory loop is true
                space(1)
                print('What would you like to access?') # aks user if they would like to acsses their inventory
                printInventory() # m shows the user their inventory     
                inventory_menu = input('Enter: ')# gets input from user   
                if inventory_menu == '1': # checks if user chose key items
                    items_loop = True #loops inventory
                    while items_loop == True: #runs until items loop is false
                        return_array = getOptionExitWeapon('Choose a Key Item',keyitems,True)
                        key_items = return_array[0]
                        if key_items == 'Exit':
                            space(1)
                            items_loop = False
                        else:
                            print(key_items[1])
                            space(1)
                elif inventory_menu == '2': # checks if user chose weapons
                    #workingInventory (weapons,'Weapons') #uses working Inventory function for weapons OLD SYSTEM DO NOT USE
                    items_loop = True #loops inventory
                    while items_loop == True: #runs until items loop is false
                        print('Your primary weapon is currently ' + weapons[0][0])
                        return_array = getOptionExitWeapon('Choose a Weapon',weapons,True)
                        weapon = return_array[0]
                        positions = return_array[1]
                        if weapon == 'Exit':
                            items_loop = False
                            space(1)
                        else:
                            print(weapon[1])
                            equip_option = getOption('Do you want to equip ' + weapon[0]  +' as your primary weapon',['Yes','No'],False)
                            if equip_option == 'Yes':                                    
                                current_weapon = weapons[0]
                                new_weapon = weapons [positions]
                                if current_weapon == new_weapon:
                                    print(weapon[0] + ' was aldready selected as your Primary Weapon')
                                    items_loop = False
                                    space(1)
                                else:
                                    print(weapon[0] + ' is  Your Primary Weapon')
                                    items_loop = False
                                    space(1)
                                weapons[0] = new_weapon
                                weapons [positions] = current_weapon
                            else:
                                weapons = weapons
                                
 
                elif inventory_menu == '3': # checks if user chose consumables
                    stats = ['', '', 0, '']
                    items_loop = True #loops inventory
                    while items_loop == True: #runs until items loop is false
                        return_array = getOptionExitWeapon('Choose a Consumable',consumables,True)
                        consumable = return_array[0]
                        positions = return_array[1]
                        if consumable == 'Exit':
                            items_loop = False
                        else:
                            print(consumable[1])
                            equip_option = getOption('Do you want to use ' + consumable[0] ,['Yes','No'],False)
                            if equip_option == 'Yes':
                                space(1)
                                print('You used ' + consumable[0])
                                stats = consumables.pop(positions)
                                #print(stats)
                                #print(stats[3])
                                if stats[3] == 'Health':
                                    if current_hp == max_hp:
                                        print("you cannot use a Health item at full HP")
                                    else:
                                        health_buff = stats[2]
                                        current_hp = current_hp + health_buff #restores health equivilant to the items value
                                        if current_hp > max_hp:
                                            current_hp = max_hp
                                        print('You restored ' + str(health_buff) +' HP ~>')
                                        input('You\'re Health is ' + str(current_hp) + '/' + str(max_hp) + ' ~>')
                                        health_buff = 0
                                        space(1)
                                elif stats[3] == 'Attack':
                                    attack_buff = attack_buff + stats[2]
                                elif stats[3] == 'Speed':
                                    speed_buff = speed_buff + stats[2]
                                elif stats[3] == 'Shield':
                                    shield_buff = shield_buff + stats[2]

                    
                elif inventory_menu == '4':# checks if user chose to quit
                    inventory_loop = False #sets inventory loop to False
                    print('You have stopped looking through your Inventory') # tells user they have stopped looking through their bag            

        elif current_choice == 'Flee':
            space(1)
            
            new_speed = whatSpeedDoFlee(player_speed, speed_buff) #determine player's speed after buffs
            
            run = runChance(enemy_speed, new_speed) #determine the speed needed to escape combat

            lost_gold = runningLoss(gold) #determine the amount of gold that is lossed

            gold = (gold - lost_gold) #deduct the gold lost from fleeing from the player's gold
            #print(gold)
            
            if run == True: #player escapes combat
                space(1)
                print(str(names) + ' has successfully escaped combat')
                input('but lost ' + str(lost_gold) + ' gold ~>')
                combat_flag = False #ends combat
                space(1)
                
            elif run == False: #player fails to escape
                space(1)
                print(str(names) + ' has failed to escape combat')
                input('and lost ' + str(lost_gold) + ' gold ~>')
                space(1)

        elif current_choice == 'Check Profile': #display player's character
            max_exp = getEXPMax(character[9])
            print('Name: ' + name) #display name
            print('Character: ' + character_stats[0] ) #display character
            printGraphics(character_stats[1]) #display portrait
            print('Health: ' + str(current_hp) + '/' + str(max_hp)) #display health
            print('Gold: ' + str(character_stats[11])) #display gold
            print('Lv: ' + str(character_stats[9])) #display level
            print('Exp:' + str(character_stats[10]) + '/' + str(max_exp)) #display exp
            if attack_buff == 1:
                print('Attack: ' + str(character_stats[6])) #display player's attack
            elif attack_buff > 1:
                print('Attack: ' + str(character_stats[6]) + ' * ' + str(attack_buff))
            if speed_buff == 1:
                print('Speed: ' + str(character_stats[4])) #display player's speed
            elif speed_buff > 1:
                print('Speed: ' + str(character_stats[4]) + ' * ' + str(speed_buff))
            if luck_buff == 1:
                print('Luck: ' + str(character_stats[5])) #display player's luck
            elif luck_buff > 1:
                print('Luck: ' + str(character_stats[5]) + ' * ' + str(luck_buff))
            print('Current shield: ' + str(shield_buff)) #display player's shielding
            space(1)
            input('Continue ~>')
                
        else:
            print('UMMMM') #ERROR

    space(1)
    
    if life == True: #if the player sucessfully defeats enemy
        print('Good Job!') #diaplay victory text
        input('You have completed the tutorial (what an accomplishment) ~>')
        space(1)

    if life == False:
        print('???') #diaplay victory text
        input('How could you possibly lose in the tutorial? ~>')
        space(1)

    life = life
    player_speed = character_stats[4]
    player_luck = character_stats[5]
    player_attack = character_stats[6]
    max_hp = character_stats[7]
    current_hp =  current_hp
    exp = character_stats[10] + enemy_exp
    level = character_stats[9]
    if current_enemy_hp <= 0:
        gold = character_stats[11] + enemy_gold
    elif current_enemy_hp > 0:
        gold = character_stats[11] - lost_gold
    else:
        print('Gold ERROR')
    new_character_stats = [character_stats[0], character_stats[1], character_stats[2], life, player_speed, player_luck, player_attack, max_hp, current_hp, level, exp,  gold, shield_buff]
    after_combat = [new_character_stats, weapons, consumables]
    
    return after_combat #returns the character's new stats, changed weapons and current items

    # End of Tutorial

def activeCombat(names, character_stats, enemy_stats, weapon_stash, item_stash): #function activates the combat protocall if a user encounters any enemy

    #variable name = (persons name, descrption, health stat, attack stat, speed stat, exp, gold)
    
    life = character_stats[3]                 #####################     Stats     #####################
    player_speed = character_stats[4]
    player_luck = character_stats[5]
    player_attack = character_stats[6]
    max_hp = character_stats[7]
    current_hp = character_stats[8]
    exp = character_stats[10]
    level = character_stats[9]
    gold = character_stats[11]
    
    #print(weapon_stash)
    weapon_attack = weapon_stash[0][2]
    #print(weapon_attack)
    
    enemy_name = enemy_stats[0]            #Enemy Stats
    enemy_description = enemy_stats[1]
    current_enemy_hp = enemy_stats[3]
    enemy_attack = enemy_stats[2]
    enemy_speed = enemy_stats[4]
    enemy_exp = enemy_stats[5]
    enemy_gold = enemy_stats[6]
    enemy_attack_name = enemy_stats[7]
    
    #randomize stats
    current_enemy_hp = randomizeEnemyStats(current_enemy_hp)
    enemy_attack = randomizeEnemyStats(enemy_attack)
    enemy_speed = randomizeEnemyStats(enemy_speed)
    enemy_exp = randomizeEnemyStats(enemy_exp)
    enemy_gold = randomizeEnemyStats(enemy_gold)

    weapons = weapon_stash              #Item, weapon and buff stats
    consumables = item_stash
    gained_gold = 0
    lost_gold = 0
    attack_buff = 1
    speed_buff = 1
    luck_buff = 1
    health_buff = 0
    shield_buff = character_stats[12]
    stats = ['', '', 0, '']
    
    input('A wild ' + enemy_name + ' has appeared ~>') #DOO DOO ROO DOO, DOO DOO ROO DOO, DOO DOO DOO DOO DOO DOO DOO DOO DOOOOOOOOOOOOOOOOOOOOOO (opening battle theme pokemon) 
    space(1)
    
    print(enemy_stats[0])
    print(enemy_stats[1])
    space(1)
    print('Has ' + str(current_enemy_hp) + ' HP remaining.')
    print('Has an attack of ' + str(enemy_attack))
    print('Has a speed of ' + str(enemy_speed))
    space(1)
    print('You have ' + str(current_hp) + '/' + str(max_hp) + ' HP') #display health
    input('Continue ~>')
    space(1)
    combat_flag = True
    while combat_flag == True:
        
        current_choice = combatMenu() #display combat menu
        if current_choice == 'Attack':
            
            life = True
            attack_hit = True
            enemy_hit = True
            crit = True
            weapon_attack = weapon_stash[0][2]
            weapon_name = weapon_stash[0][0]
            
            attack_type = attackChoice() #ask user if they want to use a light or heavy attack
            
            space(1)

            shield_buff = shield_buff

            if attack_type == 'Light attack':
                print(attack_type)
                
            elif attack_type == 'Heavy attack':
                print(attack_type)

            weapon_attack = weapon_stash[0][2] #equip the first weapon in the weapon list

            speed_chance = percentChance() #determine the amount of speed the player needs to hit the enemy
            
            new_speed = whatSpeedDo(player_speed, speed_buff, attack_type) #determine the speed of the player after any buffs 
            
            attack_hit = accuracy(attack_hit, new_speed, speed_chance) #determine if the player acctually hits the enemy
            
            crit = whatLuckDo(player_luck, luck_buff) #determine if your attack was a critical hit or not

            player_damage = totalDamage(player_attack, weapon_attack, crit, attack_buff, attack_type) #determines the total damage to the enemy during this turn
            
            enemy_hit = enemyAccuracy(enemy_speed, enemy_name) #determine if the enemy's attack hits the player

            attack_priority = whoGoesFirst(new_speed, enemy_speed, enemy_name, attack_hit, enemy_hit) #determine if the player or the enemy attacks first
            
            if attack_hit == True: #follow path if the player hits the enemy

                if attack_priority == True:

                    space(1)
                    
                    input('You dealt ' + str(player_damage) + ' DMG with the ' + weapon_name + ' ~>') #display the player's damage done towards the enemy
                    
                    current_enemy_hp = hurtEnemy(current_enemy_hp, player_damage, enemy_name) #take away the enemy's hitpoints corresponding to your attack damage
                    
                    if current_enemy_hp <= 0: #if enemy is defeated
                        combat_flag = False #ends combat
                        gained_gold = enemy_stats[5]
                        print('You Won!')
                        space(1)
                        print(enemy_name + ' was defeated.')
                        input('You earned ' + str(enemy_gold) + ' gold and ' + str(enemy_exp) + ' exp ~>')
                    
                    elif current_enemy_hp > 0 and shield_buff == 0: #if enemy is alive and you have no shields
                        space(1)
                        if enemy_hit == True: #if enemy lands it's attack
                            print(enemy_name + enemy_attack_name)
                            current_hp = enemyAttack(current_hp, enemy_attack) #enemy deals it's attack to player's health
                            input(enemy_name + ' deals ' + str(enemy_attack) + ' damage ~>') #displayes how muck damage the enemy has delt towards the player
                            
                            if current_hp <= 0: #if player falls in combat
                                life = False #players life is gone
                                combat_flag = False #combat protocall finishes
                                #Player has died in combat
                                
                            elif current_hp > 0: #if player is alive and kicking
                                print('You have ' + str(current_hp) + ' HP left.') #display player's current health
                                space(1)
                                input('Next turn ~>')
                        if enemy_hit == False: #if enemy missed it's attack
                            space(1)
                            print(enemy_name + '\'s attack missed!')
                            print('Hallelujah!')
                            input('Next turn ~>')
                                
                    elif current_enemy_hp > 0 and shield_buff >= 1: #you still have shield
                        space(1)
                        input('You are protected from injury. ~>')
                        shield_buff = shield_buff - 1

                        

                elif attack_priority == False: #if enemy attacks first
                    
                    if shield_buff >= 1:
                        space(1)
                        print(enemy_name + enemy_attack_name)
                        input('You are protected from injury. ~>') #enemy does no damage
                        shield_buff = shield_buff - 1 #sheild counter subtracts one

                        space(1)
                        
                        crit = whatLuckDo(player_luck, luck_buff) #determine if your attack was a critical hit or not

                        player_damage = totalDamage(player_attack, weapon_attack, crit, attack_buff, attack_type) #determines the total damage to the enemy during this turn
                    
                        input('You dealt ' + str(player_damage) + ' DMG with the ' + weapon_name + ' ~>') #display the player's damage done towards the enemy
                    
                        current_enemy_hp = hurtEnemy(current_enemy_hp, player_damage, enemy_name) #take away the enemy's hitpoints corresponding to your attack damage
                    
                        if current_enemy_hp <= 0: #if enemy is defeated
                            combat_flag = False #ends combat
                            gained_gold = enemy_stats[5]
                            print('You Won!')
                            space(1)
                            print(enemy_name + ' was defeated.')
                            input('You earned ' + str(enemy_gold) + ' gold and ' + str(enemy_exp) + ' exp ~>')
                            
                        else: #if enemy is alive
                            space(1)
                            input('Next turn ~>')
                        
                    elif enemy_hit == True: #if enemy lands it's attack
                        space(1)
                        print(enemy_name + enemy_attack_name)
                        current_hp = enemyAttack(current_hp, enemy_attack) #enemy deals it's attack to player's health
                        input(enemy_name + ' deals ' + str(enemy_attack) + ' damage ~>') #displayes how much damage the enemy has delt toward the player
                            
                        if current_hp <= 0: #if player falls in combat
                            life = False #players life is gone
                            combat_flag = False #combat protocall finishes
                            #Player has died in combat
                                
                        elif current_hp > 0: #if player is alive and kicking
                            print('You have ' + str(current_hp) + ' HP left.') #display player's current health
                            space(1)
                            crit = whatLuckDo(player_luck, luck_buff) #determine if your attack was a critical hit or not

                            player_damage = totalDamage(player_attack, weapon_attack, crit, attack_buff, attack_type) #determines the total damage to the enemy during this turn
                    
                            input('You dealt ' + str(player_damage) + ' DMG with the ' + weapon_name + ' ~>') #display the player's damage done towards the enemy
                    
                            current_enemy_hp = hurtEnemy(current_enemy_hp, player_damage, enemy_name) #take away the enemy's hitpoints corresponding to your attack damage
                    
                            if current_enemy_hp <= 0: #if enemy is defeated
                                combat_flag = False #ends combat
                                gained_gold = enemy_stats[5]
                                print('You Won!')
                                space(1)
                                print(enemy_name + ' was defeated.')
                                input('You earned ' + str(enemy_gold) + ' gold and ' + str(enemy_exp) + ' exp ~>')
                        
                            else: #if enemy is alive
                                space(1)
                                input('Next turn ~>')
                                
                    elif enemy_hit == False: #if enemy missed it's attack
                        space(1)
                        print(enemy_name + '\'s attack missed!')
                        input('Hallelujah! ~>')

                        print('You have ' + str(current_hp) + ' HP left.') #display player's current health
                            
                        space(1)
                        crit = whatLuckDo(player_luck, luck_buff) #determine if your attack was a critical hit or not

                        player_damage = totalDamage(player_attack, weapon_attack, crit, attack_buff, attack_type) #determines the total damage to the enemy during this turn
                    
                        input('You dealt ' + str(player_damage) + ' DMG with the ' + weapon_name + ' ~>') #display the player's damage done towards the enemy
                    
                        current_enemy_hp = hurtEnemy(current_enemy_hp, player_damage, enemy_name) #take away the enemy's hitpoints corresponding to your attack damage
                    
                        if current_enemy_hp <= 0: #if enemy is defeated
                            combat_flag = False #ends combat
                            gained_gold = enemy_stats[5]
                            print('You Won!')
                            space(1)
                            print(enemy_name + ' was defeated.')
                            input('You earned ' + str(enemy_gold) + ' gold and ' + str(enemy_exp) + ' exp ~>')
                        
                        else: #if enemy is alive
                            space(1)
                            input('Next turn ~>')

            elif attack_hit == False: #if player's attack missed
                
                if enemy_hit == True: #if enemy lands it's attack
                    space(1)
                    print(enemy_name + enemy_attack_name)
                    current_hp = enemyAttack(current_hp, enemy_attack) #player's health is deducted by enemy's attack 
                    input(enemy_name + ' deals ' + str(enemy_attack) + ' damage ~>') #display how much damage was done by the enemy
                    
                    if current_hp <= 0: #Player has died in combat
                        life = False
                        combat_flag = False #ends combat
                        
                        
                    elif current_hp > 0: #Player is still alive
                        print('You have ' + str(current_hp) + ' HP left.') #display player's current health
                        space(1)
                        input('Next turn ~>')
                        
                elif enemy_hit == False: #if enemy missed it's attack
                    space(1)
                    print(enemy_name + '\'s attack missed!')
                    input('Hallelujah! ~>')
                    
            else:
                print('') #ERROR 2
                
        elif current_choice == 'Check Enemy':
            space(1)
            print(enemy_stats[0])
            print(enemy_stats[1])
            space(1)
            print('Has ' + str(current_enemy_hp) + ' HP remaining.')
            print('Has an attack of ' + str(enemy_attack))
            print('Has a speed of ' + str(enemy_speed))
            input('Continue ~>')
            space(1)
            
        elif current_choice == 'Inventory':
            inventory_loop = True # sets the inventory loop to ture
            while inventory_loop == True: # runs while the inventory loop is true
                space(1)
                print('What would you like to access?') # aks user if they would like to acsses their inventory
                printInventory() # m shows the user their inventory     
                inventory_menu = input('Enter: ')# gets input from user
                space(1)
                if inventory_menu == '1': # checks if user chose key items
                    items_loop = True #loops inventory
                    while items_loop == True: #runs until items loop is false
                        return_array = getOptionExitWeapon('Choose a Key Item',keyitems,True)
                        key_items = return_array[0]
                        if key_items == 'Exit':
                            space(1)
                            items_loop = False
                        else:
                            print(key_items[1])
                            space(1)
                elif inventory_menu == '2': # checks if user chose weapons
                    #workingInventory (weapons,'Weapons') #uses working Inventory function for weapons OLD SYSTEM DO NOT USE
                    items_loop = True #loops inventory
                    while items_loop == True: #runs until items loop is false
                        print('Your primary weapon is currently ' + weapons[0][0])
                        return_array = getOptionExitWeapon('Choose a Weapon',weapons,True)
                        weapon = return_array[0]
                        positions = return_array[1]
                        if weapon == 'Exit':
                            items_loop = False
                            space(1)
                        else:
                            print(weapon[1])
                            equip_option = getOption('Do you want to equip ' + weapon[0]  +' as your primary weapon',['Yes','No'],False)
                            if equip_option == 'Yes':                                    
                                current_weapon = weapons[0]
                                new_weapon = weapons [positions]
                                if current_weapon == new_weapon:
                                    print(weapon[0] + ' was aldready selected as your Primary Weapon')
                                    items_loop = False
                                    space(1)
                                else:
                                    print(weapon[0] + ' is  Your Primary Weapon')
                                    items_loop = False
                                    space(1)
                                weapons[0] = new_weapon
                                weapons [positions] = current_weapon
                            else:
                                weapons = weapons
                                
 
                elif inventory_menu == '3': # checks if user chose consumables
                    stats = ['', '', 0, '']
                    items_loop = True #loops inventory
                    while items_loop == True: #runs until items loop is false
                        return_array = getOptionExitWeapon('Choose a Consumable',consumables,True)
                        consumable = return_array[0]
                        positions = return_array[1]
                        if consumable == 'Exit':
                            space(1)
                            items_loop = False
                        else:
                            print(consumable[1])
                            equip_option = getOption('Do you want to use ' + consumable[0] ,['Yes','No'],False)
                            if equip_option == 'Yes':
                                space(1)
                                print('You used ' + consumable[0])
                                stats = consumables.pop(positions)
                                #print(stats)
                                #print(stats[3])
                                if stats[3] == 'Health':
                                    if current_hp == max_hp:
                                        print("you cannot use a Health item at full HP")
                                    else:
                                        health_buff = stats[2]
                                        current_hp = current_hp + health_buff #restores health equivilant to the items value
                                        if current_hp > max_hp:
                                            current_hp = max_hp
                                        input('You restored ' + str(health_buff) +' HP ~>')
                                        input('You\'re Health is ' + str(current_hp) + '/' + str(max_hp) + ' ~>')
                                        health_buff = 0
                                        space(1)
                                elif stats[3] == 'Attack':
                                    attack_buff = attack_buff + stats[2]
                                elif stats[3] == 'Speed':
                                    speed_buff = speed_buff + stats[2]
                                elif stats[3] == 'Shield':
                                    shield_buff = shield_buff + stats[2]

                    
                elif inventory_menu == '4':# checks if user chose to quit
                    inventory_loop = False #sets inventory loop to False
                    print('you have stopped looking through your Inventory') # tells user they have stopped looking through their bag
            
        elif current_choice == 'Flee':
            space(1)
            
            new_speed = whatSpeedDoFlee(player_speed, speed_buff) #determine player's speed after buffs
            
            run = runChance(enemy_speed, new_speed) #determine the speed needed to escape combat

            lost_gold = runningLoss(gold) #determine the amount of gold that is lossed

            gold = round(gold - lost_gold) #deduct the gold lost from fleeing from the player's gold
            #print(gold)
            
            if run == True: #player escapes combat
                space(1)
                print(str(names) + ' has successfully escaped combat')
                input('but lost ' + str(lost_gold) + ' gold ~>')
                combat_flag = False #ends combat
                space(1)
                
            elif run == False: #player fails to escape
                space(1)
                print(str(names) + ' has failed to escape combat')
                input('and lost ' + str(lost_gold) + ' gold ~>')
                space(1)

        elif current_choice == 'Check Profile':
            max_exp = getEXPMax(character[9])
            print('Name: ' + name)
            print('Character: ' + character_stats[0] )
            printGraphics(character_stats[1])
            print('Health: ' + str(current_hp) + '/' + str(max_hp))
            print('Gold: ' + str(character_stats[11]))
            print('Lv: ' + str(character_stats[9]))
            print('Exp:' + str(character_stats[10]) + '/' + str(max_exp))
            if attack_buff == 1:
                print('Attack: ' + str(character_stats[6]))
            elif attack_buff > 1:
                print('Attack: ' + str(character_stats[6]) + ' * ' + str(attack_buff))
            if speed_buff == 1:
                print('Speed: ' + str(character_stats[4]))
            elif speed_buff > 1:
                print('Speed: ' + str(character_stats[4]) + ' * ' + str(speed_buff))
            if luck_buff == 1:
                print('Luck: ' + str(character_stats[5]))
            elif luck_buff > 1:
                print('Luck: ' + str(character_stats[5]) + ' * ' + str(luck_buff))
            print('Current shield: ' + str(shield_buff))
            space(1)
            input('Continue ~>')
                
        else:
            print('UMMMM') #ERROR
            
    space(1)
    
    if life == True: #if the player sucessfully defeats enemy
        input('Good Job! ~>') #diaplay victory text
        #expGain(player_exp, player_level) #player gains exp points and may level up
        space(1)
        
    elif life == False: #if the player falls in combat
        print('You feel cold and your skin looks pale.')
        print('You drop dead where you once stood.')
        space(1)
        input('GAME OVER ~>') #display game over text
        space(1)

    #[name, pic, start weapon, life check, speed, luck, attak, max hp, current hp, level,xp, gold, shield]
    
    life = life
    player_speed = character_stats[4]
    player_luck = character_stats[5]
    player_attack = character_stats[6]
    max_hp = character_stats[7]
    current_hp =  current_hp
    exp = character_stats[10] + enemy_exp
    level = character_stats[9]
    if current_enemy_hp <= 0:
        gold = character_stats[11] + enemy_gold
    elif current_enemy_hp > 0:
        gold = character_stats[11] - lost_gold
    else:
        print('Gold ERROR')
    #print(weapon_stash)
    new_character_stats = [character_stats[0], character_stats[1], character_stats[2], life, player_speed, player_luck, player_attack, max_hp, current_hp, level, exp,  gold, shield_buff]
    after_combat = [new_character_stats, weapons, consumables]
    
    return after_combat #returns the character's new stats, changed weapons and current items

def activeBossCombat(names, character_stats, enemy_stats, weapon_stash, item_stash):

    #variable name = (persons name, descrption, health stat, attack stat, speed stat, exp, gold)
    
    life = character_stats[3]                 #####################     Stats     #####################
    player_speed = character_stats[4]
    player_luck = character_stats[5]
    player_attack = character_stats[6]
    max_hp = character_stats[7]
    current_hp = character_stats[8]
    exp = character_stats[10]
    level = character_stats[9]
    gold = character_stats[11]
    
    #print(weapon_stash)
    weapon_attack = weapon_stash[0][2]
    #print(weapon_attack)
    
    enemy_name = enemy_stats[0]            #Enemy Stats
    enemy_picture = enemy_stats[1]
    enemy_description = enemy_stats[2]
    current_enemy_hp = enemy_stats[3]
    enemy_hp = enemy_stats[4]
    enemy_speed = enemy_stats[5]
    enemy_exp = enemy_stats[6]
    enemy_gold = enemy_stats[7]
    enemy_attack_one = enemy_stats[8][0]
    enemy_attack_two = enemy_stats[8][1]
    enemy_attack_three = enemy_stats[8][2]
    enemy_ability = enemy_stats[9]
    current_enemy_ability_charge = enemy_stats[10]
    enemy_ability_charge = enemy_stats[11]
    
    
    weapons = weapon_stash              #Item, weapon and buff stats
    consumables = item_stash
    gained_gold = 0
    lost_gold = 0
    attack_buff = 1
    speed_buff = 1
    luck_buff = 1
    health_buff = 0
    shield_buff = character_stats[12]
    stats = ['', '', 0, '']

    input('A wild ' + enemy_name + ' has appeared ~>') #DOO DOO ROO DOO, DOO DOO ROO DOO, DOO DOO DOO DOO DOO DOO DOO DOO DOOOOOOOOOOOOOOOOOOOOOO (opening battle theme pokemon) 
    space(1)
    
    print(enemy_stats[0])
    print(enemy_stats[2])
    space(1)
    printGraphics(enemy_stats[1])
    #print(enemy_stats[1])    Boss picture
    space(1)
    print('Has ' + str(current_enemy_hp) + ' HP.')
    print('Has a speed of ' + str(enemy_speed))
    print('Has an ability charge of ' + str(current_enemy_ability_charge) + '/' + str(enemy_ability_charge))
    space(1)
    print('You have ' + str(current_hp) + '/' + str(max_hp) + ' HP') #display health
    input('Continue ~>')
    space(1)
    
    combat_flag = True
    while combat_flag == True:

        current_choice = combatMenu() #display combat menu
        if current_choice == 'Attack':
                
            life = True
            attack_hit = True
            enemy_hit = True
            crit = True
            weapon_attack = weapon_stash[0][2]
            weapon_name = weapon_stash[0][0]

            attack_type = attackChoice() #ask user if they want to use a light or heavy attack
            enemy_attack_type = 0
            debuff = 'None'
            debuff_value = 0
            
            space(1)

            shield_buff = shield_buff

            if attack_type == 'Light attack':
                print(attack_type)
                    
            elif attack_type == 'Heavy attack':
                print(attack_type)

            weapon_attack = weapon_stash[0][2] #equip the first weapon in the weapon list

            speed_chance = percentChance() #determine the amount of speed the player needs to hit the enemy
                
            new_speed = whatSpeedDo(player_speed, speed_buff, attack_type) #determine the speed of the player after any buffs 
                
            attack_hit = accuracy(attack_hit, new_speed, speed_chance) #determine if the player acctually hits the enemy
                
            crit = whatLuckDo(player_luck, luck_buff) #determine if your attack was a critical hit or not

            player_damage = totalDamage(player_attack, weapon_attack, crit, attack_buff, attack_type) #determines the total damage to the enemy during this turn
                
            enemy_hit = enemyAccuracy(enemy_speed, enemy_name) #determine if the enemy's attack hits the player

            attack_priority = whoGoesFirst(new_speed, enemy_speed, enemy_name, attack_hit, enemy_hit) #determine if the player or the enemy attacks first
            
            enemy_attack_type = random.randint(1,3)
            
            if enemy_name == 'Stalker' and current_enemy_ability_charge ==  enemy_ability_charge or enemy_name == 'Grub Reaper' and current_enemy_ability_charge ==  enemy_ability_charge or enemy_name == 'Mecha Dragon 5000' and current_enemy_ability_charge ==  enemy_ability_charge: #check if boss ability charge is ready or not
                current_enemy_attack = enemy_ability #boss attack becomes it's ability
                #print(enemy_attack_type)
                current_enemy_ability_charge = 0 #ability charge is reset
                
            else:
                #print(enemy_attack_type)
                if enemy_attack_type == 1:
                    current_enemy_attack = enemy_attack_one
                    debuff = enemy_attack_one[4]
                    debuff_value = enemy_attack_one[5]
                    #print(current_enemy_attack)
                elif enemy_attack_type == 2:
                    current_enemy_attack = enemy_attack_two
                    debuff = enemy_attack_two[4]
                    debuff_value = enemy_attack_one[5]
                    #print(current_enemy_attack)
                elif enemy_attack_type == 3:
                    current_enemy_attack = enemy_attack_three
                    debuff = enemy_attack_three[4]
                    debuff_value = enemy_attack_three[5]
                    #print(current_enemy_attack)
                else:
                    print('problem determining enemy attack')


            if attack_hit == True: #follow path if the player hits the enemy

                if attack_priority == True: #player attacks first

                    space(1)
                    
                    input('You dealt ' + str(player_damage) + ' DMG with the ' + weapon_name + ' ~>') #display the player's damage done towards the enemy
                    
                    current_enemy_hp = hurtEnemy(current_enemy_hp, player_damage, enemy_name) #take away the enemy's hitpoints corresponding to your attack damage
                    
                    if current_enemy_hp <= 0: #if enemy is defeated
                        combat_flag = False #ends combat
                        gained_gold = enemy_stats[5]
                        print('You Won!')
                        space(1)
                        print(enemy_name + ' was defeated.')
                        input('You earned ' + str(enemy_gold) + ' gold and ' + str(enemy_exp) + ' exp ~>')
                    
                    elif current_enemy_hp > 0 and shield_buff == 0 or current_enemy_hp > 0 and current_enemy_attack[4] == True: #if enemy is alive and you have no shields
                        space(1)
                        if enemy_hit == True: #if enemy lands it's attack
                            print(current_enemy_attack[0])
                            current_hp = enemyAttack(current_hp, current_enemy_attack[1]) #enemy deals it's attack to player's health
                            input(enemy_name + ' deals ' + str(current_enemy_attack[1]) + ' damage ~>') #displayes how muck damage the enemy has delt towards the player
                            if current_enemy_attack[2] > 0: #enemy heals an amount
                                current_enemy_hp = current_enemy_hp + current_enemy_attack[2]
                                print(enemy_name + ' restores ' + str(current_enemy_attack[2]) + ' HP')
                                if current_enemy_hp > enemy_hp:
                                    current_enemy_hp = enemy_hp    
                            if current_enemy_attack[6] > 0:
                                current_enemy_ability_charge = current_enemy_ability_charge + 1
                                input(enemy_name + '\'s ability charge went up by 1 ' + str(current_enemy_ability_charge) + '/' + str(enemy_ability_charge) + (' ~>'))
                        if debuff == 'Attack':
                            space(1)
                            input('Your Attack went down. ~>')
                            print(attack_buff)
                            attack_buff = attack_buff - debuff_value #adds an attack debuff to the player
                            print(attack_buff)
                        elif debuff == 'Speed':
                            space(1)
                            input('Your Speed went down. ~>')
                            speed_buff = speed_buff - debuff_value #adds an speed debuff to the player
                        elif debuff == 'Luck':
                            space(1)
                            input('Your Luck went down. ~>')
                            luck_buff = luck_buff - debuff_value #adds an luck debuff to the player
                        elif debuff == 'All':
                            space(1)
                            input('All of your stats went down. ~>')
                            attack_buff = attack_buff - debuff_value
                            speed_buff = speed_buff - debuff_value
                            luck_buff = luck_buff - debuff_value      #adds a debuff to all stats
                            
                            if current_hp <= 0: #if player falls in combat
                                life = False #players life is gone
                                combat_flag = False #combat protocall finishes
                                #Player has died in combat
                                
                            elif current_hp > 0: #if player is alive and kicking
                                print('You have ' + str(current_hp) + ' HP left.') #display player's current health
                                space(1)
                                input('Next turn ~>')

                        elif enemy_hit == False: #if enemy missed it's attack
                            space(1)
                            print(enemy_name + '\'s attack missed!')
                            print('Hallelujah!')
                            space(1)
                            input('Next turn ~>')
                                
                    elif current_enemy_hp > 0 and shield_buff >= 1 or shield_buff >= 1 and current_enemy_hp > 0 and current_enemy_attack[4] == False: #you still have shield
                        space(1)
                        input('You are protected from injury. ~>')
                        shield_buff = shield_buff - 1
                        space(1)
                        input('Next turn ~>')

                elif attack_priority == False: #if enemy attacks first
                    
                    if shield_buff >= 1 and current_enemy_attack[4] == False:
                        space(1)
                        print(enemy_name + enemy_attack_name)
                        input('You are protected from injury. ~>') #enemy does no damage
                        shield_buff = shield_buff - 1 #sheild counter subtracts one

                        space(1)
                        
                        crit = whatLuckDo(player_luck, luck_buff) #determine if your attack was a critical hit or not

                        player_damage = totalDamage(player_attack, weapon_attack, crit, attack_buff, attack_type) #determines the total damage to the enemy during this turn
                    
                        input('You dealt ' + str(player_damage) + ' DMG with the ' + weapon_name + ' ~>') #display the player's damage done towards the enemy
                    
                        current_enemy_hp = hurtEnemy(current_enemy_hp, player_damage, enemy_name) #take away the enemy's hitpoints corresponding to your attack damage
                    
                        if current_enemy_hp <= 0: #if enemy is defeated
                            combat_flag = False #ends combat
                            print('You Won!')
                            space(1)
                            print(enemy_name + ' was defeated.')
                            input('You earned 0 gold and 0 exp ~>')
                            
                        else: #if enemy is alive
                            space(1)
                            input('Next turn ~>')
                        
                    elif enemy_hit == True: #if enemy lands it's attack
                        space(1)
                        print(current_enemy_attack[0])
                        current_hp = enemyAttack(current_hp, current_enemy_attack[1]) #enemy deals it's attack to player's health

                        if current_hp <= 0: #if player falls in combat
                            life = False #players life is gone
                            combat_flag = False #combat protocall finishes
                            #Player has died in combat
                        
                        input(enemy_name + ' deals ' + str(current_enemy_attack[1]) + ' damage ~>') #displayes how muck damage the enemy has delt towards the player
                        if current_enemy_attack[2] > 0: #enemy heals an amount
                            current_enemy_hp = current_enemy_hp + current_enemy_attack[2]
                            print(enemy_name + ' restores ' + str(current_enemy_attack[2]) + ' HP')
                            if current_enemy_hp > enemy_hp:
                                current_enemy_hp = enemy_hp
                        if current_enemy_attack[6] > 0:
                            current_enemy_ability_charge = current_enemy_ability_charge + 1
                            input(enemy_name + '\'s ability charge went up by 1 ' + str(current_enemy_ability_charge) + '/' + str(enemy_ability_charge) + ' ~>')
                        if debuff == 'Attack':
                            space(1)
                            input('Your Attack went down. ~>')
                            attack_buff = attack_buff - debuff_value #adds an attack debuff to the player
                        elif debuff == 'Speed':
                            space(1)
                            input('Your Speed went down. ~>')
                            speed_buff = speed_buff - debuff_value #adds an speed debuff to the player
                        elif debuff == 'Luck':
                            space(1)
                            input('Your Luck went down. ~>')
                            luck_buff = luck_buff - debuff_value #adds an luck debuff to the player
                        elif debuff == 'All':
                            space(1)
                            input('All of your stats went down. ~>')
                            attack_buff = attack_buff - debuff_value
                            speed_buff = speed_buff - debuff_value
                            luck_buff = luck_buff - debuff_value      #adds a debuff to all stats
                              
                                
                        elif current_hp > 0: #if player is alive and kicking
                            print('You have ' + str(current_hp) + ' HP left.') #display player's current health
                            
                            space(1)
                            
                            crit = whatLuckDo(player_luck, luck_buff) #determine if your attack was a critical hit or not

                            player_damage = totalDamage(player_attack, weapon_attack, crit, attack_buff, attack_type) #determines the total damage to the enemy during this turn
                    
                            input('You dealt ' + str(player_damage) + ' DMG with the ' + weapon_name + ' ~>') #display the player's damage done towards the enemy
                    
                            current_enemy_hp = hurtEnemy(current_enemy_hp, player_damage, enemy_name) #take away the enemy's hitpoints corresponding to your attack damage
                    
                            if current_enemy_hp <= 0: #if enemy is defeated
                                combat_flag = False #ends combat
                                print('You Won!')
                                space(1)
                                print(enemy_name + ' was defeated.')
                                input('You earned ' + str(enemy_gold) + ' gold and ' + str(enemy_exp) + ' exp ~>')
                        
                            else: #if enemy is alive
                                space(1)
                                input('Next turn ~>')
                                
                    elif enemy_hit == False: #if enemy missed it's attack
                        space(1)
                        print(enemy_name + '\'s attack missed!')
                        input('Hallelujah!')

                        print('You have ' + str(current_hp) + ' HP left.') #display player's current health
                            
                        space(1)
                        crit = whatLuckDo(player_luck, luck_buff) #determine if your attack was a critical hit or not

                        player_damage = totalDamage(player_attack, weapon_attack, crit, attack_buff, attack_type) #determines the total damage to the enemy during this turn
                    
                        input('You dealt ' + str(player_damage) + ' DMG with the ' + weapon_name + ' ~>') #display the player's damage done towards the enemy
                    
                        current_enemy_hp = hurtEnemy(current_enemy_hp, player_damage, enemy_name) #take away the enemy's hitpoints corresponding to your attack damage
                    
                        if current_enemy_hp <= 0: #if enemy is defeated
                            combat_flag = False #ends combat
                            print('You Won!')
                            space(1)
                            print(enemy_name + ' was defeated.')
                            input('You earned 0 gold and 0 exp ~>')
                        
                        else: #if enemy is alive
                            space(1)
                            input('Next turn')

            elif attack_hit == False: #if player's attack missed
                #space(1)
                #input('Your attack missed ~>')
                if enemy_hit == True: #if enemy lands it's attack
                    space(1)
                    print(current_enemy_attack[0])
                    current_hp = enemyAttack(current_hp, current_enemy_attack[1]) #enemy deals it's attack to player's health
                    input(enemy_name + ' deals ' + str(current_enemy_attack[1]) + ' damage ~>') #displayes how muck damage the enemy has delt towards the player
                    if current_enemy_attack[2] > 0: #enemy heals an amount
                        current_enemy_hp = current_enemy_hp + current_enemy_attack[2]
                        print(enemy_name + ' restores ' + str(current_enemy_attack[2]) + ' HP')
                        if current_enemy_hp > enemy_hp:
                            current_enemy_hp = enemy_hp
                    if current_enemy_attack[6] > 0:
                        current_enemy_ability_charge = current_enemy_ability_charge + 1 #enemy's ability charge increases by one
                        input(enemy_name + '\'s ability charge went up by 1 ' + str(current_enemy_ability_charge) + '/' + str(enemy_ability_charge) + (' ~>'))
                    if debuff == 'Attack':
                        space(1)
                        input('Your Attack went down. ~>')
                        attack_buff = attack_buff - debuff_value #adds an attack debuff to the player
                    elif debuff == 'Speed':
                        space(1)
                        input('Your Speed went down. ~>')
                        speed_buff = speed_buff - debuff_value #adds an speed debuff to the player
                    elif debuff == 'Luck':
                        space(1)
                        input('Your Luck went down. ~>')
                        luck_buff = luck_buff - debuff_value #adds an luck debuff to the player
                    elif debuff == 'All':
                        space(1)
                        input('All of your stats went down. ~>')
                        attack_buff = attack_buff - debuff_value
                        speed_buff = speed_buff - debuff_value
                        luck_buff = luck_buff - debuff_value      #adds a debuff to all stats
                              
                    if current_hp <= 0: #if player falls in combat
                        life = False #players life is gone
                        combat_flag = False #combat protocall finishes
                        #Player has died in combat
                           
                    elif current_hp > 0: #Player is still alive
                        print('You have ' + str(current_hp) + ' HP left.') #display player's current health
                        space(1)
                        input('Next turn ~>')
                        
                elif enemy_hit == False: #if enemy missed it's attack
                    space(1)
                    print(enemy_name + '\'s attack missed!')
                    input('Hallelujah!')
                    
            else:
                print('') #ERROR 2 boss

        elif current_choice == 'Check Enemy':
            space(1)
            print(enemy_stats[0]) #display enemy name
            print(enemy_stats[2]) #display enemy description
            space(1)
            printGraphics(enemy_stats[1]) #display enemy picture
            space(1)
            print('Has ' + str(current_enemy_hp) + ' HP remaining.') #display enemy health
            print('Has a speed of ' + str(enemy_speed)) #display enemy speed
            print('Has an ability charge of ' + str(current_enemy_ability_charge) + '/' + str(enemy_ability_charge)) #display enemy ability charge
            input('Continue ~>')
            space(1)

        elif current_choice == 'Inventory':
            inventory_loop = True # sets the inventory loop to ture
            while inventory_loop == True: # runs while the inventory loop is true
                space(1)
                print('What would you like to access?') # aks user if they would like to acsses their inventory
                printInventory() # m shows the user their inventory     
                inventory_menu = input('Enter: ')# gets input from user   
                if inventory_menu == '1': # checks if user chose key items
                    items_loop = True #loops inventory
                    while items_loop == True: #runs until items loop is false
                        return_array = getOptionExitWeapon('Choose a Key Item',keyitems,True)
                        key_items = return_array[0]
                        if key_items == 'Exit':
                            items_loop = False
                        else:
                            print(key_items[1])
                            space(1)
                            
                elif inventory_menu == '2': # checks if user chose weapons
                    #workingInventory (weapons,'Weapons') #uses working Inventory function for weapons OLD SYSTEM DO NOT USE
                    items_loop = True #loops inventory
                    while items_loop == True: #runs until items loop is false
                        print('Your primary weapon is currently ' + weapons[0][0])
                        return_array = getOptionExitWeapon('Choose a Weapon',weapons,True)
                        weapon = return_array[0]
                        positions = return_array[1]
                        if weapon == 'Exit':
                            items_loop = False
                            space(1)
                        else:
                            print(weapon[1])
                            equip_option = getOption('Do you want to equip ' + weapon[0]  +' as your primary weapon',['Yes','No'],False)
                            if equip_option == 'Yes':                                    
                                current_weapon = weapons[0]
                                new_weapon = weapons [positions]
                                if current_weapon == new_weapon:
                                    print(weapon[0] + ' was aldready selected as your Primary Weapon')
                                    items_loop = False
                                    space(1)
                                else:
                                    print(weapon[0] + ' is  Your Primary Weapon')
                                    items_loop = False
                                    space(1)
                                weapons[0] = new_weapon
                                weapons [positions] = current_weapon
                            else:
                                weapons = weapons
                                
 
                elif inventory_menu == '3': # checks if user chose consumables
                    stats = ['', '', 0, '']
                    items_loop = True #loops inventory
                    while items_loop == True: #runs until items loop is false
                        return_array = getOptionExitWeapon('Choose a Consumable',consumables,True)
                        consumable = return_array[0]
                        positions = return_array[1]
                        if consumable == 'Exit':
                            items_loop = False
                        else:
                            print(consumable[1])
                            equip_option = getOption('Do you want to use ' + consumable[0] ,['Yes','No'],False)
                            if equip_option == 'Yes':
                                space(1)
                                print('You used ' + consumable[0])
                                stats = consumables.pop(positions)
                                #print(stats)
                                #print(stats[3])
                                if stats[3] == 'Health':
                                    if current_hp == max_hp:
                                        print("you cannot use a Health item at full HP")
                                    else:
                                        health_buff = stats[2]
                                        current_hp = current_hp + health_buff #restores health equivilant to the items value
                                        if current_hp > max_hp:
                                            current_hp = max_hp
                                        input('You restored ' + str(health_buff) +' HP ~>')
                                        input('You\'re Health is ' + str(current_hp) + '/' + str(max_hp) + ' ~>')
                                        health_buff = 0
                                        space(1)
                                elif stats[3] == 'Attack':
                                    attack_buff = attack_buff + stats[2] #increase player's attack
                                elif stats[3] == 'Speed':
                                    speed_buff = speed_buff + stats[2] #increase player's speed
                                elif stats[3] == 'Shield':
                                    shield_buff = shield_buff + stats[2] #increase player's shield

                    
                elif inventory_menu == '4':# checks if user chose to quit
                    inventory_loop = False #sets inventory loop to False
                    print('you have stopped looking through your Inventory') # tells user they have stopped looking through their bag


        elif current_choice == 'Flee':
            space(1)
            input('You cannot escape from boss combat. ~>')

        elif current_choice == 'Check Profile':
            max_exp = getEXPMax(character_stats[9]) 
            print('Name: ' + name) #display player's name
            print('Character: ' + character_stats[0] ) #display player's character
            printGraphics(character_stats[1]) #display player's picture
            print('Health: ' + str(current_hp) + '/' + str(max_hp)) #display player's health
            print('Gold: ' + str(character_stats[11])) #display player's gold
            print('Lv: ' + str(character_stats[9])) #display player's level
            print('Exp:' + str(character_stats[10]) + '/' + str(max_exp)) #display player's exp
            if attack_buff == 1:
                print('Attack: ' + str(character_stats[6])) #display player's attack
            elif attack_buff != 1:
                print('Attack: ' + str(character_stats[6]) + ' * ' + str(attack_buff)) 
            if speed_buff == 1:
                print('Speed: ' + str(character_stats[4])) #display player's speed
            elif speed_buff != 1:
                print('Speed: ' + str(character_stats[4]) + ' * ' + str(speed_buff))
            if luck_buff == 1:
                print('Luck: ' + str(character_stats[5])) #display player's luck
            elif luck_buff != 1:
                print('Luck: ' + str(character_stats[5]) + ' * ' + str(luck_buff))
            print('Current shield: ' + str(shield_buff)) #display player's shield
            space(1)
            input('Continue ~>')

        else:
            print('UMMMM') #ERROR

    space(1)

    if life == True: #if the player sucessfully defeats enemy
        print('Good Job!') #diaplay victory text
        input('What a great triumph that is! ~>')
        space(1)
        
    elif life == False: #if the player falls in combat
        print('You feel cold and your skin looks pale.')
        print('You drop dead where you once stood.')
        space(1)
        input('GAME OVER ~>') #display game over text
        space(1)

    #[name, pic, start weapon, life check, speed, luck, attak, max hp, current hp, level,xp, gold, shield]
    
    life = life
    player_speed = character_stats[4]
    player_luck = character_stats[5]
    player_attack = character_stats[6]
    max_hp = character_stats[7]
    current_hp =  current_hp
    exp = character_stats[10] + enemy_exp
    level = character_stats[9]
    if current_enemy_hp <= 0:
        gold = character_stats[11] + enemy_gold
    elif current_enemy_hp > 0:
        gold = character_stats[11] - lost_gold
    else:
        print('Gold ERROR')
    #print(weapon_stash)
    new_character_stats = [character_stats[0], character_stats[1], character_stats[2], life, player_speed, player_luck, player_attack, max_hp, current_hp, level, exp,  gold, shield_buff]
    after_combat = [new_character_stats, weapons, consumables]
    
    return after_combat #returns the character's new stats, changed weapons and current items

    #### End of combat sequence ####

def randomizeStats(stat):# defines function which alters certain stats
    if stat < 2:#if value is lower than 2
        stat = stat #keeps stat the same
    elif stat < 10: #if value is lower than 10
        stat += random.randint(-3,3) # increase or decreases stat by 3
    elif stat < 20: #if value is lower than 20
        stat += random.randint(-5,5) # increase or decreases stat by 5
    elif stat < 29: #if value is lower than 29
        stat += random.randint(-7,7) # increase or decreases stat by 7
    else: #if value is higher than 29
        stat += random.randint(-10,10) # increase or decreases stat by 10
    return stat # rreturns the value of stat

def getNumber(question,lowest,highest): # defines function which can get a number within a range
    num_true = False # sets num true to False
    while num_true == False: # runs while num true to False
        numbersz = input(question)# gets the number input from user
        if numbersz.isdigit() == True: # checks if input was a number
            numbersz = int(numbersz) #converts numbersz to an integer
            if numbersz > highest or numbersz < lowest: # checks if numbersz is within the range
                print('please input a number between ' + str(lowest) + ' and ' + str(highest)) #shows to user the highest and lowest value
            else: #runs if number is accpetable
                num_true = True # ends the loop by changing variable
        else: # runs if user did not input a number
            print('please input a number') # tells user to input a number
    return numbersz #returns value of numbers 


def printGraphics(maps):# defines function which prints out the map
    map_length = len(maps) #gets the length of the map
    for line in range (0,map_length): # runs for the length of the map
        current_line = maps[line] # gets a row of the map depending on the loop
        line_length = len(current_line)# gets the length of the row
        for symbols in range (0,line_length): # runs for the length of the row
            print(current_line[symbols], end='') # prints out a symbol from the map depending of the length
        print('')#starts a new line of the map
        
def movement(maps,hidden_maps,direction):# defines function which move character right,left,up or down
    if direction == 'D' or direction == 'S': # checks if direction is 1 or 4
        difference = 1 # sets differnece 1
    else: # runs if direction is not 1 or 4
        difference = - 1 # sets differnece to -1
        
    map_length = len(maps) # gets length of the map
    counter = 0 #sets counter to 0
    for line in range (0,map_length): # gets length of the map
        current_line = maps[line] #sets current line to appropriate line
        if ('@' in current_line) == True: # checks if @ symbol is on current line
            counter += 1 #increases counter by 1
            if counter == 1: # checks if counter is equal to 1
                position = current_line.index('@') # gets the position of the @ symbol
                if direction == 'A' or direction == 'D': # runs if direction is left or right
                    next_spot = position + difference # changes the position based on difference
                    maps[line][position] = ' ' # sets the users  current position to a space
                    maps[line][next_spot] = '@' # sets users new position to @ symbol
                    space = hidden_maps[line][next_spot] #gets the symbol from hidden map corresponding to users new location
                else: # runs if direction is up or down
                    next_line = line + difference # changes the line based on difference
                    maps[line][position] = ' ' # sets users old position to a spacep
                    
                    maps[next_line][position] = '@' # sets users new position to @ symbol
                    space = hidden_maps[next_line][position] #gets the symbol from hidden map corresponding to users new location
                    
            else: # checks if counter has been increased
                counter = 2 # sets counter to two
                
    return_array = [maps,space] # puts variable maps and space in an array to return
    return return_array # returns array

def checkRight(maps): # defines function which checks if there is an obstacle to the right of the user
    map_length = len(maps) # gets length of the maps array
    for line in range (0,map_length): #runs for the length of maps array
        current_line = maps[line] # gets appropriate line from maps
        if ('@' in current_line) == True: # checks if @ is in current line
            position = current_line.index('@') #gets the position of @ in array
            next_spot = position + 1 # calculates the next spot
            if maps[line][next_spot] == '█': # checks if there is a block in the next spot
                check = False # sets check to False
            else: #runs if nexxt spot is not a block
                check = True # sets check to True
    return check # returns the value fo check

def checkUp(maps): # defines function which checks if there is an obstacle to the right of the user
    map_length = len(maps) # gets length of the maps array
    for line in range (0,map_length): #runs for the length of maps array
        current_line = maps[line] # gets appropriate line from maps
        if ('@' in current_line) == True: # checks if @ is in current line
            position = current_line.index('@') #gets the position of @ in array
            next_line = line - 1 # calculates the next spot
            if maps[next_line][position] == '█': # checks if there is a block in the next spot
                check = False # sets check to False
            else: #runs if nexxt spot is not a block
                check = True # sets check to True
    return check # returns the value fo check

def checkDown(maps): # defines function which checks if there is an obstacle to the right of the user
    map_length = len(maps) # gets length of the maps array
    for line in range (0,map_length): #runs for the length of maps array
        current_line = maps[line] # gets appropriate line from maps
        if ('@' in current_line) == True: # checks if @ is in current line
            position = current_line.index('@') #gets the position of @ in array
            next_line = line + 1 # calculates the next spot
            if maps[next_line][position] == '█': # checks if there is a block in the next spot
                check = False # sets check to False
            else: #runs if nexxt spot is not a block
                check = True # sets check to True
    return check # returns the value fo check

def checkLeft(maps): # defines function which checks if there is an obstacle to the right of the user
    map_length = len(maps) # gets length of the maps array
    for line in range (0,map_length): #runs for the length of maps array
        current_line = maps[line] # gets appropriate line from maps
        if ('@' in current_line) == True: # checks if @ is in current line
            position = current_line.index('@') #gets the position of @ in array
            next_spot = position - 1 # calculates the next spot
            if maps[line][next_spot] == '█': # checks if there is a block in the next spot
                check = False # sets check to False
            else: #runs if nexxt spot is not a block
                check = True # sets check to True
    return check # returns the value fo check

def getMove(right,left,up,down): #defines functtion which takes the inputs of which moves are acceptable and gets the user to answer
    print('Which direction you would like to move in?') #asks user which direction the would like to move
    
    if up == True: # check if moving up is possible
        print('W - Up') # shows user how to input up
        up_input = 'W'  # sets up input to 3
    else:# runs if moving up is not possible
        up_input = '' #sets up input to a blank
    if left == True: # check if moving left is possible
        
        print('A - Left')# shows user how to input left
        left_input = 'A'  # sets left input to 2
    else:# runs if moving left is not possible
        left_input = '' #setsleft input to a blank
        
    if down == True: # check if moving down is possible
        print('S - Down') # shows user how to input down
        down_input = 'S'  # sets down input to 4
    else:# runs if moving down is not possible
        down_input = '' #sets down input to a blank
        
    if right == True: # check if moving right is possible
        print('D - Right') # shows user how to input right
        right_input = 'D' # sets right input to 1
    else:# runs if moving right is not possible
        right_input = '' #sets right input to a blank
        
    print('1 - Return to Action Menu') # tells user to input 5 for exit
    moves = 6 #3 sets moves to 6
    while moves != right_input and moves != left_input and moves != up_input and moves != down_input and moves != '1' : #runs while none of the value equal to moves
        moves = input('Enter: ') # asks user for input and stores it
        if moves == '': # sets moves to a blank
            moves = 6 # sets moves to 6
        else:
            moves = str.upper(moves)


    #move_options = []
    #if right == True: # check if moving right is possible
    #    move_options.append('Right')
    #if left == True: # check if moving left is possible
    #    move_options.append('Left')
    #if up == True: # check if moving up is possible
    #    move_options.append('Up')
    #if down == True: # check if moving down is possible
    #    move_options.append('Down')
    #move_options.append('Open my Blueprint')
    #moves = getOptionExit('Which direction you would like to move in?',move_options,False)
    return moves # returns the value of moves



def printInventory(): # defines the print Inventory function
    print('1 - Key Items') # tells user the number for Key Items
    print('2 - Weapons') # tells user the number for Weapons
    print('3 - Consumables') # tells user the number for Consumables
    print('4 - Exit') # tells user the number for Exit

def displayItems(arrays,items_class): #defines display Items function which shows items
    print('Select a ' + items_class ) #presents the user with a question
    length_list = len(arrays) + 1 # gets the length of list and adds 1
    for list_number in range (1,length_list): # runs for length of array but every number te counter is increased by 1
        array_number = list_number - 1 # decrease list number by 1
        if items_class == 'Weapons':
            print(str(list_number) + ' - ' + arrays[array_number][0]) # prints the number with a corresponding number readable to user
        else:
            print(str(list_number) + ' - ' + arrays[array_number]) # prints the number with a corresponding number readable to user
    print(str(length_list) + ' - Exit') # prints out the button for the user to press exit
    item_use = getNumber('Enter: ',1,length_list) # gets the number that the user wants
    if item_use != length_list: #runs if user did not input exit
        array_position = item_use - 1 # decreases items use by 1 and stores it in array position
        item_use = arrays[array_position] # gets appropriate items and stores it
    return item_use # returns the value of the item

def workingInventory (array,items_classes): #defines function working Inventory which handles moving around the Inventory
    items_loop = True #loops inventory
    while items_loop == True: #runs until items loop is false
        items_used = displayItems(array,items_classes) # gets user input on which item they want to use
        if items_used == len(array) + 1: #checks if user chose to quit
            items_loop = False # sets item loop to False
            
def showMove(movements): #defines function showMove
    if movements == 'D': # checks if the value of movments is to the right
        print('You moved to the right') # tells user they have moved to the right
    elif movements == 'A': # checks if the value of movment is to the left
        print('You moved to the left') # tells user they have moved to the left
    elif movements == 'W': #checks if the value of movments is downwards
        print('You moved up') # tells user to move upwards
    elif movements == 'S': # checks if value of movment is down
        print('You moved down') # tells user they moove down
    else: # runs if an error occurs
        print('error') # tells user an error occured

def getEnemy(): #defines get enemy function
    daffy_duck = ("Daffy Dunk's",'description',10,10,10,10,'Quack Attack')
    return daffy_duck # WIP

def doBattle(): # defines do battle function
    print('WIP do battle') # WIP

def getOption(question,array_of_options,is_double_array): # defines function which gets Option (question to asks user, possible options, True if possible options are a double array)
    print(question) # tells user the question
    length_list = len(array_of_options) + 1 # gets the length of list and adds 1
    for list_number in range (1,length_list): # runs for length of array but every number te counter is increased by 1
        array_number = list_number - 1 # decrease list number by 1
        if is_double_array == True: # checks if name is true
            print(str(list_number) + ' - ' + array_of_options[array_number][0]) # prints the number with a corresponding number readable to user
        else: # runs if name is not true
            print(str(list_number) + ' - ' + array_of_options[array_number]) # prints the number with a corresponding number readable to user
    array_number = length_list - 1 # decreases length list by 1 and stores it
    item_use = getNumber('Enter: ',1,array_number) # gets the number that the user wants
    array_position = item_use - 1 # decreases items use by 1 and stores it in array position
    item_use = array_of_options[array_position] # gets appropriate items and stores it
    return item_use # returns the value of item use
            
def getOptionExit (question,array_of_options,is_double_array):  # defines function with array
    print(question) #shows user the question 
    length_list = len(array_of_options) + 1 # gets the length of list and adds 1
    for list_number in range (1,length_list): # runs for length of array but every number te counter is increased by 1
        array_number = list_number - 1 # decrease list number by 1
        if is_double_array == True: # checks if name is true
            print(str(list_number) + ' - ' + array_of_options[array_number][0]) # prints the number with a corresponding number readable to user
        else: # runs if name is not true
            print(str(list_number) + ' - ' + array_of_options[array_number]) # prints the number with a corresponding number readable to user
    print(str(length_list) + ' - Exit') # prints out the button for the user to press exit
    item_use = getNumber('Enter: ',1,length_list) # gets the number that the user wants
    if item_use != length_list: #runs if user did not input exit
        array_position = item_use - 1 # decreases items use by 1 and stores it in array position
        item_use = array_of_options[array_position] # gets appropriate items and stores it
    else: # tells user the possible
        item_use = 'Exit' #sets item use to Exit
    return item_use # returns the value of the item

def getOptionExitWeapon (question,array_of_options,is_double_array):  # defines function with array
    print(question) #shows user the question 
    length_list = len(array_of_options) + 1 # gets the length of list and adds 1
    for list_number in range (1,length_list): # runs for length of array but every number te counter is increased by 1
        array_number = list_number - 1 # decrease list number by 1
        if is_double_array == True: # checks if name is true
            print(str(list_number) + ' - ' + array_of_options[array_number][0]) # prints the number with a corresponding number readable to user
        else: # runs if name is not true
            print(str(list_number) + ' - ' + array_of_options[array_number]) # prints the number with a corresponding number readable to user
    print(str(length_list) + ' - Exit') # prints out the button for the user to press exit
    item_use = getNumber('Enter: ',1,length_list) # gets the number that the user wants
    if item_use != length_list: #runs if user did not input exit
        array_position = item_use - 1 # decreases items use by 1 and stores it in array position
        item_use = array_of_options[array_position] # gets appropriate items and stores it
        return_array = [item_use,array_position]
    else: # tells user the possible
        item_use = 'Exit' #sets item use to Exit
        return_array = [item_use,0] 
           
    return return_array # returns the value of the item

def getOptionExitShop (question,array_of_options,prices,quantity,is_double_array):  # defines function with array
    print(question) #shows user the question 
    length_list = len(array_of_options) + 1 # gets the length of list and adds 1
    for list_number in range (1,length_list): # runs for length of array but every number te counter is increased by 1
        array_number = list_number - 1 # decrease list number by 1
        if is_double_array == True: # checks if name is true
            print(str(list_number) + ' - ' + array_of_options[array_number][0] + ' -Price: ' + str(prices[array_number]) + '   -Quantity: ' + str(quantity[array_number])) # prints the number with a corresponding number readable to user
        else: # runs if name is not true
            print(str(list_number) + ' - ' + array_of_options[array_number] + ' -Price: ' + str(prices[array_number]) + '   -Quantity: ' + str(quantity[array_number])) # prints the number with a corresponding number readable to user
    print(str(length_list) + ' - Exit') # prints out the button for the user to press exit
    item_use = getNumber('Enter: ',1,length_list) # gets the number that the user wants
    if item_use != length_list: #runs if user did not input exit
        array_position = item_use - 1 # decreases items use by 1 and stores it in array position
        item_use = array_of_options[array_position] # gets appropriate items and stores it
        return_array = [item_use,array_position]
    else: # tells user the possible
        item_use = 'Exit' #sets item use to Exit
        return_array = [item_use,0] 
           
    return return_array # returns the value of the item

def changeName (options,charactersz): # defines change name function
    change_name = getOption('Do you want to change your character\'s name?',options,False)# asks user if they want to change their name
    if change_name == 'Yes': # checks if change name is yes
        print("If you want the character\'s old name don't type a name and hit Enter")
        possible_name = input('Please Enter your character\'s new name: ') # gets the characters name from the user
        if possible_name == '': # checks if user entered a blank
            charactersz = charactersz[0]# sets name to the character
        else:# runs if possible name was not a blank
            charactersz = possible_name# sets name to possible name 
    else: # runs if change name was no
        charactersz = charactersz[0]# sets name to the character
    return charactersz # returns the value of characteresz to the array

def browseStore(): # defines function browse store
    print('WIP')# tells user that this function is a work in progress

def replacePosition(world,hiddenworld):
    map_length = len(world) # gets length of the map
    for line in range (0,map_length): # gets length of the map
        current_line = world[line] #sets current line to appropriate line
        if ('@' in current_line) == True: # checks if @ symbol is on current line
            position = current_line.index('@') # gets the position of the @ symbol
            hiddenworld[line][position] = ' ' # replaces the position with a space
    return hiddenworld # returns the hidden array

def checkLevel(level,experince,character): # defines CheckLevel Fuction
    # gets the characters stats
    speed = character[4]
    luck = character[5]
    attack = character[6]
    max_hp = character[7]
    current_hp = character[8]
    if level == 1: #checks if user is level 1 
        if experince >= 100: # checks if user has enough experince to level up
            experince -= 100 # takes away any xp required too level up
            level += 1 # increasces level
            print('You leveled up to level ' + str(level)) # tells user about increase in level
            print('All of your stats have been increased') # tells user about their stats
            # increases stats
            speed *= 1.1
            luck *= 1.1
            attack *= 1.1
            max_hp *= 1.1
            current_hp = max_hp # heals character
            input('Your health increased to ' + str(round(max_hp)) + ' and you are fully healed ~>') #tells user their new health
        else:
            experince = experince 
    elif level == 2: #checks if user is level 2 
        if experince >= 125:# checks if user has enough experince to level up
            experince -= 125 # takes away any xp required too level up
            level += 1 # increasces level
            print('You leveled up to level ' + str(level)) # tells user about increase in level
            print('All of your stats have been increased') # tells user about their stats
            # increases stats
            speed *= 1.1
            luck *= 1.1
            attack *= 1.1
            max_hp *= 1.1
            current_hp = max_hp  # heals character
            input('Your health increased to ' + str(round(max_hp)) + ' and you fully healed ~>') #tells user their new health
        else:
            experince = experince
    elif level == 3: #checks if user is level 3
        if experince >= 150: # checks if user has enough experince to level up
            experince -= 150 # takes away any xp required too level up
            level += 1 # increasces level
            print('You leveled up to level ' + str(level)) # tells user about increase in level
            print('All of your stats have been increased') # tells user about their stats
            # increases stats
            speed *= 1.1
            luck *= 1.1
            attack *= 1.1
            max_hp *= 1.1
            current_hp = max_hp # heals character
            input('Your health increased to ' + str(round(max_hp)) + ' and you fully healed ~>') #tells user their new health
    elif level == 4: #checks if user is level 4
        if experince >= 200:  # checks if user has enough experince to level up
            experince -= 200  # takes away any xp required too level up
            level += 1 # increasces level
            print('You leveled up to level ' + str(level) + ' This is the maximum level') # tells user about increase in level
            print('All of your stats have been increased') # tells user about their stats
            # increases stats
            speed *= 1.1
            luck *= 1.1
            attack *= 1.1
            max_hp *= 1.1
            current_hp = max_hp # heals character
            input('Your health increased to ' + str(round(max_hp)) + ' and you fully healed ~>') #tells user their new health
        else:
            experince = experince
    else:
        experince = experince
        
    #feeds the new values back into character array
    character[4] = round(speed)
    character[5] = round(luck)
    character[6] = round(attack)
    character[7] = round(max_hp)
    character[8] = round(current_hp)
    character[9] = round(level)
    character[10] = round(experince)
    
    return character # returns character

def getEXPMax(level): # defines ffunction which gets the max xp per level

    if level == 1: #checks level
        experince = 100 #declares Max Xp
    elif level == 2: #checks level
        experince = 125 #declares Max Xp
    elif level == 3: #checks level
        experince = 150  #declares Max Xp
    elif level == 4: #checks level
        experince = 200 #declares Max Xp
    elif level == 5: #checks level
        experince = 'Max XP' #declares Max Xp
    else:
        experince = 700 # sets experince value if error occurs
    return experince #returns the experince

def getArray(number,array1,array2,array3): #defines function which gets corresponding arrray based on number
    if number == 1: # checks if number is 1
        array = array1 #gets correct array
    elif number == 2: # checks if number is 1
        array = array2 #gets correct array
    elif number == 3: # checks if number is 1
        array = array3 #gets correct array
    else:
        print('GET ARRAY ERROR') # prints error
        array = array1 #gets incorrect array
    return array # returns correct aray

def displayOpeningStory(player_name): #Function displays the opening text message
    
    print('Your alarm goes off at 7:00 sharp.')
    input('You get out of bed and get ready for the day. ~>')
    space(1)
    input('It’s your eighteenth birthday and you can’t wait to finally visit Professor Tree’s Lab to get assigned a function in your town. ~>')
    space(1)
    input(player_name + ' enters Professor Tree’s Lab ~>')
    space(1)
    input('Professor Tree: “Oh welcome ' + player_name + ' it seems your eighteenth birthday has finally come around. You must have been waiting ages to be assigned a function.” ~>')
    space(1)
    input('You reminisce on your life before today but oddly enough it feels as though mere seconds have passed before you turned eighteen. ~>')
    space(1)
    input('Professor Tree: “So let me check your resume to see what functions you can perform” ~>')
    space(1)
    print('Professor Tree looks flustered as he checks your resume.')
    input('Professor Tree: “It seems as though you did not obtain a high school diploma. You cannot be assigned any important function without one.” ~>')
    input('Professor Tree: “Do not yet fret for you can still obtain your high school diploma.” ~>')
    space(1)
    input('The worry on your face quickly washes away as you ask where you can obtain a high school diploma. ~>')
    space(1)
    input('Professor Tree: “Now that’s no easy task young man. You must reach the fabled Land of Attendance and defeat the great dragon which guards the diploma.” ~>')
    input('Professor Tree: “To get there you would first have to cross through the Great Uked Forrest, and climb to the summit of Obliteration Mountain, there you will find the Land of Attendance.” ~>')
    space(1)
    print('You look at the professor with great determination and ask for permission to go.')
    input('Professor Tree: “I will not hold you back sunny. Just remember the journey you are embarking on is filled with many trials and enemies, stay determined.”')
    space(1)
    input('Your journey begins! ~>')

def displayEndingOne(player_name): #Function displays the text message if you get the first ending
    
    input('The great Mecha Dragon 5000 falls to the ground with an earth shattering force. ~>')
    space(1)
    print('You gaze upon its body lying still on the floor.')
    input('The dragon slowly begins to move again and looks at you. ~>')
    space(1)
    input('Mecha Dragon 5000: “It seems that you have triumphed over every obstacle on your journey to the great Land of Attendance.” ~>')
    input('Mecha Dragon 5000: “This great feat will not leave you unrewarded young one.” ~>')
    space(1)
    input('The dragon extends it’s claw forward towards you. ~>')
    space(1)
    input('Mecha Dragon 5000: “This diploma certifies the completion of the journey you have embarked on. Take it and return to your home.” ~>')
    space(1)
    input('You received the “High School Diploma” ~>')
    space(1)
    print('The dragon spreads it’s wings and takes lift of.')
    input('Mecha Dragon 5000: “Follow your dreams young one. For you have completed a treacherous trial against all odds. Your destiny is up to you alone, choose what you want to do with it.” ~>')
    space(1)
    print('With that the Mecha Dragon 5000 flies out of sight.')
    input('With your diploma clutched in your hands you begin your trek home. ~>')
    space(1)
    print('Congratulations You Won')
    space(1)
    input('The End')



def displayEndingTwo(player_name): #Function displays the text message if you get the second ending
          
    input('The great Mecha Dragon 5000 falls to the ground with an earth shattering force. ~>')
    space(1)
    print('You gaze upon its body lying still on the floor.')
    input('The dragon slowly begins to move again and looks at you. ~>')
    space(1)
    input('Mecha Dragon 5000: “It seems that you have triumphed over every obstacle on your journey to the great Land of Attendance.” ~>')
    input('Mecha Dragon 5000: “This great feat will not leave you unrewarded young one.” ~>')
    space(1)
    input('The dragon extends it’s claw forward towards you. ~>')
    space(1)
    input('Mecha Dragon 5000: “This diploma certifies the completion of the journey you have embarked on. Take it and return to your home.” ~>')
    space(1)
    input('You received the “High School Diploma” ~>')
    space(1)
    input('The dragon recalls something. ~>')
    space(1)
    print('Mecha Dragon 5000: “I had almost forgot! You were the one who feed me the great delicacies. To think I would have left that great act of kindness would go unnoticed.')
    input('I will grant you a ride to your home.” ~>')
    space(1)
    input('The dragon bends down to let you on his back. ~>')
    space(1)
    input('Mecha Dragon 5000: “Climb in back and we’ll be off.” ~>')
    space(1)
    print('The dragon spreads it’s wings and takes lift of.')
    input('Mecha Dragon 5000: “Follow your dreams young one. For you have completed a treacherous trial against all odds. Your destiny is up to you alone, choose what you want to do with it.” ~>')
    space(1)
    print('With your diploma clutched in your hands you see the great lands you had trek through to complete the journey.')
    input(player_name + ' and the Mecha Dragon 5000 fly off into the sunset. ~>')
    space(1)
    print('Congratulations You Won')
    space(1)
    input('The End')

def displayCredits(): #function displays the credits

    input('Credits:')
    space(1)
    input('Journey to the Land of Attendence ~>')
    space(1)
    print('Chief Technical Officers:')
    input('Aaron Castellino and Lucas Grala ~>')
    space(1)
    print('Technical Directors:')
    input('Aaron Castellino and Lucas Grala ~>')
    space(1)
    print('Program Managers:')
    input('Aaron Castellino and Lucas Grala ~>')
    space(1)
    print('Programmers:')
    input('Aaron Castellino and Lucas Grala ~>')
    space(1)
    print('Creative Directors:')
    input('Aaron Castellino and Lucas Grala ~>')
    space(1)
    print('Directors:')
    input('Aaron Castellino and Lucas Grala ~>')
    space(1)
    print('Designers:')
    input('Aaron Castellino and Lucas Grala ~>')
    space(1)
    print('Presidents:')
    input('Aaron Castellino and Lucas Grala ~>')
    space(1)
    print('Executive Producers:')
    input('Aaron Castellino and Lucas Grala ~>')
    space(1)
    print('Project Directors/Leaders:')
    input('Aaron Castellino and Lucas Grala ~>')
    space(1)
    print('Project Coordinators:')
    input('Aaron Castellino and Lucas Grala ~>')
    space(1)
    print('Producers:')
    input('Aaron Castellino and Lucas Grala ~>')
    space(1)
    print('Graphic Designer:')
    input('Aaron Castellino ~>')
    space(1)
    print('Writer:')
    input('Lucas Grala ~>')
    space(1)
    print('Test Managers/Supervisors:')
    input('Aaron Castellino and Lucas Grala ~>')
    space(1)
    print('Beta Testers:')
    input('Aaron Castellino and Lucas Grala ~>')
    input('Bra██o█ K███ ~>')
    input('M█c██e█ S██a ~>')
    input('J███b B███e█ ~>')
    input('J█h█ P███ ~>')
    input('K█████ G████ ~>')
    input('███████ ███████ ~>')
    
    space(1)
    print('Special Thanks:')
    input('Aaron\'s aunt/cousin who entered our discord call that one time. ~>')
    space(1)
    input('Thanks for Playing')
    space(1)

main_game = True # sets main game to True
title_counter = 0 # sets title counter to 0
while main_game == True: # runs while the main game is equal to True
    title_counter += 1 # increases the title counter by 1 
    if title_counter == 1: # checks if title counter is equal to 1
        printGraphics(title_pic) # displays the title
        space(1)
    else: # checks if title counter is not 1
        title_counter = 1 # sets title counter to 1
    main_menu = getOptionExit('Please Select an Option',['Start','Help'],False) # asks user for options on the main menu
    space(1)
    if main_menu == 'Help': # checks if user inputted in Help
        help_check = True
        input('Whenever you See ~> at the end of a sentence simply press Enter to proceed ~>')
        while help_check == True:
            help_menu = getOptionExit('Please Select an Option',['General','Move','Check Profile','Open Bag','View My Blueprint'],False)
            if help_menu == 'Exit':
                 help_check = False # leves the help loop
                 space(1)                 
                 title_counter = 0 # sets title counter to 0
            elif help_menu == 'General': #display general help
                space(1)
                input('General Help ~>')
                space(1)
                print('In Journey to the Land of Attendance you as the player will have to explore the land for weapons and consumables to fight through many monsters and bosses.')
                print('If by any chance you fall in combat you will be taken back to the main menu.')
                print('Make sure you chose smart decisions to stay one step ahead of the enemy to reach your destination.')
                print('Have fun!')
                space(1)
                input('Continue ~>')
                space(1)
                
            elif help_menu == 'Move': #display movement help
                space(1)
                input('Move help ~>')
                space(1)
                print('When you chose the option to move you must move your character around the map by inputting')
                input('"W" to move upward, "A" to move left, "S" to move downward or "D" to move right. ~>')
                space(1)
                input('The program will tell you all the movement options you can choose from or you can enter "1" to go back to the main hud. ~>')
                space(1)
                print('An updated map of your area will apear after every move.')
                space(1)
                input('Continue ~>')
                space(1)
                
            elif help_menu == 'Check Profile': #display profile help
                space(1)
                input('Check profile help ~>')
                space(1)
                print('When you choose the "Check Profile" a complete list of your character\'s current stats will be displayed along with the character\'s portrait.')
                space(1)
                input('Continue ~>')
                space(1)
                
            elif help_menu == 'Open Bag': #display inventory help
                space(1)
                input('Open Bag help ~>')
                space(1)
                print('When you access your inventory, you have the option to browse your Key Items, Weapons or Consumables.')
                space(1)
                print('If you choose to access Key Items you have the option to check a key item’s description')
                print('If you choose to access Weapons you have the option to check a weapon’s description and or equip it as your primary weapon you would use in battle.')
                print('If you choose to access Consumables you have the option to check a consumable’s description of which stat it would buff.')
                space(1)
                print('Health buffs restore your lost HP.')
                print('Attack buffs increase your overall attack power for one battle.')
                print('Speed buffs increase your overall speed for one battle.')
                print('Luck buffs increase your overall luck for one battle.')
                #print('Shields increase your shield count which protects you from an enemy’s attack.')
                space(1)
                print('You cannot use any buff outside of combat.')
                space(1)
                input('Continue ~>')
                space(1)
                
            elif help_menu == 'View My Blueprint': #display map help
                space(1)
                input('View My Blueprint Help ~>')
                space(1)
                print('When you access My Blueprint a map of your current area will be displayed.')
                space(1)
                print('Map Legend:')
                print('The @ symbol on the map shows your position')# tells user the rules
                print('The V symbol on the map shows a local vendor selling their goods')# tells user the rules
                print('The + symbol on the map shows a hospital willing to patch you up for a fee')# tells user the rules
                print('The # symbol on the map shows the area to get out of this class room')# tells user the rules
                print('The B symbol on the map shows the Boss of that area')# tells user the rules
                space(1)
                input('Continue ~>')
                space(1)
                
    elif main_menu == 'Exit': # checks if the user inputted Exit
        main_game = False # sets main game equal to False
        
    elif main_menu == 'Start': # sets main game to start
        candy_counter = 0
        consumables = [] # clears the consumables inventory
        switch_counter = 0
        switch_dungeon_1 = False
        dungeon_active = False
        keyitems = [['My Blueprint','Shows you the surrounding area to help you navigate, open my blue print on the action screen']] #creates the consumables array
        weapons = []  # clears the weapons inventory
        title_counter = 0
        boss_battles = 0 #sets your beaten boss status to 0

        super_mario = ['Supra Mayro',super_mario_pic,rubber_mallet, True, 100, 12, 120, 100, 100, 1, 0, 0, 0]#array containing all stats for Hero Super Mario
        mega_man = ['Mini Man',mega_man_pic,mega_buster, True, 120, 20, 100, 120, 120, 1, 0, 0, 0] #array containing all stats for Hero Mega Man
        link = ['Lunk',link_pic,training_sward, True, 100, 10, 120, 120, 120, 1, 0, 0, 0] #array containing all stats for Hero Link
        sonic = ['Sanic',sonic_pic,spin_dash, True, 200, 15, 80, 80, 80, 1, 0, 0, 0] #array containing all stats for Hero Sonic

        characters = [super_mario,link,sonic,mega_man] # stores all basic characters
        monster_candy = ['Monster Candy',' The most delectable candy in all the land, too bad it is highly poisinus']
        w1_lin1 = ['█','█','█','█','█','█','█','█','█','█','█'] #array containg 1 line of visible map world 1
        w1_lin2 = ['█','@',' ',' ',' ',' ',' ',' ','█',' ','█']#array containg 1 line of visible map world 1
        w1_lin3 = ['█','█','█',' ','█','█','█',' ','█',' ','█']#array containg 1 line of visible map world 1
        w1_lin4 = ['█',' ',' ',' ',' ','█',' ',' ',' ',' ','█']#array containg 1 line of visible map world 1
        w1_lin5 = ['█',' ','█','█',' ','█','█','█',' ','█','█']#array containg 1 line of visible map world 1
        w1_lin6 = ['█',' ','█',' ',' ','+',' ',' ',' ',' ','█']#array containg 1 line of visible map world 1
        w1_lin7 = ['█',' ','█','█',' ','█','█','█',' ','█','█']#array containg 1 line of visible map world 1
        w1_lin8 = ['█',' ',' ',' ',' ','█','V',' ',' ','B','#']#array containg 1 line of visible map world 1
        w1_lin9 = ['█','█','█','█','█','█','█','█','█','█','█']#array containg 1 line of visible map world 1


        w1_lin1h = ['█','█','█','█','█','█','█','█','█','█','█']#array containg 1 line of hidden map world 1
        w1_lin2h = ['█',' ','T','M',' ','M','I','S','█','W','█']#array containg 1 line of hidden map world 1
        w1_lin3h = ['█','█','█',' ','█','█','█','M','█','M','█']#array containg 1 line of hidden map world 1
        w1_lin4h = ['█','M',' ','I',' ','█','I',' ','M',' ','█']#array containg 1 line of hidden map world 1
        w1_lin5h = ['█',' ','█','█',' ','█','█','█',' ','█','█']#array containg 1 line of hidden map world 1
        w1_lin6h = ['█','I','█','W','M','+','I','S','M','I','█']#array containg 1 line of hidden map world 1
        w1_lin7h = ['█','M','█','█',' ','█','█','█','M','█','█']#array containg 1 line of hidden map world 1
        w1_lin8h = ['█',' ','M','I','M','█','V',' ',' ','B','#']#array containg 1 line of hidden map world 1
        w1_lin9h = ['█','█','█','█','█','█','█','█','█','█','█']#array containg 1 line of hidden map world 1

        w1d_lin1 =[' ',' ',' ','█','█','█','█','█','█','█','█','█',]
        w1d_lin2 =[' ',' ',' ','█',' ',' ',' ',' ',' ',' ','█','█',]
        w1d_lin3 =['█','█','█','█',' ','█','█','█','█',' ','█','█',]
        w1d_lin4 =['█','@',' ',' ',' ',' ','ʘ',' ','█',' ',' ','#',]
        w1d_lin5 =['█','█','█','█','█','█','█','█','█','█','█','█',]

        w1d_lin1h =[' ',' ',' ','█','█','█','█','█','█','█','█','█',]
        w1d_lin2h =[' ',' ',' ','█',' ','M','M','M',' ','M','█','█',]
        w1d_lin3h =['█','█','█','█',' ','█','█','█','█',' ','█','█',]
        w1d_lin4h =['█',' ',' ','S',' ',' ','ʘ','S',' ','W','I','^',]
        w1d_lin5h =['█','█','█','█','█','█','█','█','█','█','█','█',]

        w2_lin1 = ['█','█','█','█','█','█','█','█','█','█','█','█','█'] #array containg 1 line of visible map world 2
        w2_lin2 = ['█',' ','█',' ',' ','+','█',' ',' ',' ','█','B','#']#array containg 1 line of visible map world 2
        w2_lin3 = ['█',' ','█','█',' ','█','█','█','█',' ','█',' ','█']#array containg 1 line of visible map world 2
        w2_lin4 = ['█',' ','█','V',' ',' ',' ',' ',' ',' ',' ',' ','█']#array containg 1 line of visible map world 2
        w2_lin5 = ['█','@','█','█',' ','█',' ','█','█',' ','█','█','█']#array containg 1 line of visible map world 2
        w2_lin6 = ['█',' ',' ',' ',' ',' ',' ','█',' ',' ','█','●','█']#array containg 1 line of visible map world 2
        w2_lin7 = ['█',' ','█','█',' ','█','█','█','█',' ','█',' ','█']#array containg 1 line of visible map world 2
        w2_lin8 = ['█',' ',' ',' ',' ',' ',' ','█',' ',' ',' ',' ','█']#array containg 1 line of visible map world 2
        w2_lin9 = ['█','█','█','█','█','█','█','█','█','█','█','█','█']#array containg 1 line of visible map world 2

        w2_lin1h = ['█','█','█','█','█','█','█','█','█','█','█','█','█'] #array containg 1 line of visible map world 2
        w2_lin2h = ['█','C','█','M',' ','+','█','I',' ','M','█','B','&']#array containg 1 line of visible map world 2
        w2_lin3h = ['█','M','█','█',' ','█','█','█','█',' ','█',' ','█']#array containg 1 line of visible map world 2
        w2_lin4h = ['█',' ','█','V','M','I',' ','M',' ','M','M','I','█']#array containg 1 line of visible map world 2
        w2_lin5h = ['█',' ','█','█',' ','█','I','█','█',' ','█','█','█']#array containg 1 line of visible map world 2
        w2_lin6h = ['█','M',' ','I',' ',' ','M','█','W','I','█','●','█']#array containg 1 line of visible map world 2
        w2_lin7h = ['█',' ','█','█','I','█','█','█','█','M','█',' ','█']#array containg 1 line of visible map world 2
        w2_lin8h = ['█','M','I',' ','M',' ','W','█','I',' ','M','I','█']#array containg 1 line of visible map world 2
        w2_lin9h = ['█','█','█','█','█','█','█','█','█','█','█','█','█']#array containg 1 line of visible map world 2

        
        w2d_lin1 =[' ','1',' ','2',' ','3',' ']
        w2d_lin2 =['█','#','█','#','█','#','█']
        w2d_lin3 =['█',' ',' ',' ',' ',' ','█']
        w2d_lin4 =['█','█','█',' ','█','█','█']
        w2d_lin5 =[' ',' ','█','@','█',' ',' ']
        w2d_lin6 =[' ',' ','█','█','█',' ',' ']

        w2d_lin1h =[' ',' ',' ',' ',' ',' ',' ']
        w2d_lin2h =['█','1','█','2','█','3','█']
        w2d_lin3h =['█',' ',' ',' ',' ',' ','█']
        w2d_lin4h =['█','█','█',' ','█','█','█']
        w2d_lin5h =[' ',' ','█',' ','█',' ',' ']
        w2d_lin6h =[' ',' ','█','█','█',' ',' ']

        w3_lin1 = ['█','█','█','█','█',' ',' ',' ',' ',' ',' ',' ',' ']
        w3_lin2 = ['█',' ',' ',' ','█',' ',' ',' ',' ',' ',' ',' ',' ']
        w3_lin3 = ['█',' ',' ',' ','█',' ',' ',' ',' ',' ',' ',' ',' ']
        w3_lin4 = ['█',' ',' ',' ','█','█','█','█','█','█','█',' ',' ']
        w3_lin5 = ['█','█',' ','█','█','V','█','+','█','?','█','█','█']
        w3_lin6 = ['█','@',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','B']
        w3_lin7 = ['█','█','█','█','█','█','█','█','█','█','█','█','█']

        w3_lin1h = ['█','█','█','█','█',' ',' ',' ',' ',' ',' ',' ',' ']
        w3_lin2h = ['█','M','M','M','█',' ',' ',' ',' ',' ',' ',' ',' ']
        w3_lin3h = ['█','M','M','M','█',' ',' ',' ',' ',' ',' ',' ',' ']
        w3_lin4h = ['█','M','W','M','█','█','█','█','█','█','█',' ',' ']
        w3_lin5h = ['█','█',' ','█','█','V','█','+','█','?','█','█','█']
        w3_lin6h = ['█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','B']
        w3_lin7h = ['█','█','█','█','█','█','█','█','█','█','█','█','█']



        world1h = [w1_lin1h,w1_lin2h,w1_lin3h,w1_lin4h,w1_lin5h,w1_lin6h,w1_lin7h,w1_lin8h,w1_lin9h] # combines the lines into a hidden map for world 1       
        world1 =[w1_lin1,w1_lin2,w1_lin3,w1_lin4,w1_lin5,w1_lin6,w1_lin7,w1_lin8,w1_lin9] # combines the lines for a visible map for world 1
        world1_dungeon = [w1d_lin1,w1d_lin2,w1d_lin3,w1d_lin4,w1d_lin5] # creates the world 1 dungeon 
        world1h_dungeon = [w1d_lin1h,w1d_lin2h,w1d_lin3h,w1d_lin4h,w1d_lin5h] # creates the world 1 hidden dungeon
        world2 = [w2_lin1,w2_lin2,w2_lin3,w2_lin4,w2_lin5,w2_lin6,w2_lin7,w2_lin8,w2_lin9] # combines the lines into a visible map for world 2
        world2h = [w2_lin1h,w2_lin2h,w2_lin3h,w2_lin4h,w2_lin5h,w2_lin6h,w2_lin7h,w2_lin8h,w2_lin9h] # combines the lines into a hidden map for world 2
        world2_dungeon = [w2d_lin1,w2d_lin2,w2d_lin3,w2d_lin4,w2d_lin5,w2d_lin6] #creates world 2 dungeon
        world2h_dungeon = [w2d_lin1h,w2d_lin2h,w2d_lin3h,w2d_lin4h,w2d_lin5h,w2d_lin6h] # creates the world 2 hidden dungeon
        world3 = [w3_lin1,w3_lin2,w3_lin3,w3_lin4,w3_lin5,w3_lin6,w3_lin7] #creates world 3 to 
        world3h = [w3_lin1h,w3_lin2h,w3_lin3h,w3_lin4h,w3_lin5h,w3_lin6h,w3_lin7h] # creates world 3 hidden

        current_world = copy.deepcopy(world1) # sets the current world to world 1
        current_world_h = copy.deepcopy(world1h) # sets the current hidden world to hidden world 1
        world_track = 1 # sets world track to world 1
        monster_true_count = 0 # sets monster truw count to 0
        monster_false_count = 1 # sets monster false count to 1
        tutorial_count = 0 # sets tutorial count to 0
        player_monty_hall = 0 # sets player monty hall to 0
        monster_candy_deposit = 0 # sets monster candy deposit to 0

        store1_item_quantity = [3,2,2,2,2,1] # reseets store item quantities
        store2_item_quantity = [3,2,2,2,2,1] # reseets store item quantities
        store3_item_quantity = [3,2,2,2,2,1] # reseets store item quantities

        find_weapons2 = [master_sword,donut_launcher,zapotron,lawnmower_5000] # creates a weapons list
        find_weapons1 = [poke_ball,key_blade,shrink_ray,buster_sword]
        find_weapons3 = [death_sicle]
        random.shuffle(find_weapons1)# randomizes the weapon order
        random.shuffle(find_weapons2)# randomizes the weapon order
        
        find_item1 = [heal_item_one, heal_item_two, atk_item_one, atk_item_two, spd_item_one, spd_item_two, lck_item_one, lck_item_two, ] #items in world one
        find_item2 = [heal_item_three, heal_item_four, atk_item_three, atk_item_four, spd_item_three, spd_item_four, lck_item_three, lck_item_four,] #items in world two
        random.shuffle(find_item1)# randomizes the weapon order
        random.shuffle(find_item2)# randomizes the weapon order

        loop = True # sets loop to True
        space(1)
        character_select = False
        while character_select == False:
            character = getOption('Which character would you like to choose?',characters,True) #asks user which caracter they chose
            printGraphics(character[1]) # prints the graphics of chose character
            space(1)
            #prints stats of character
            print('Max Health: ' + str(character[8]))
            print('Attack: ' + str(character[6]))
            print('Speed: ' + str(character[4]))
            print('Luck: ' + str(character[5]))
            character_option = getOption('Are you sure you want ' + character[0]  +' as your character',['Yes','No'],False) # asks users if they want to stay with chosen character
            if character_option == 'No': # checks if user chose no
                character_select = False #sets character select to False
                space(1)
            else:
                character_select = True # sets character select to True
                space(1)
                
            

        print('You chose ' + character[0]) # tells user the character the chose
        name = changeName(y_n,character)# changes the characters name per the users choice
        space(1)
        input('Whenever you See ~> at the end of a sentence simply press Enter to proceed ~>')
        space(1)
        if name == 'Gaster': # gives user ban hammer if there name is saba
            input('The game itself opens before you and bestows upon you the godly Ban Hammer~>')
            space(1)
            weapons.append(ban_hammer)
        #####################################################################
        story_check = getOption('Do you want to listen to the backstory ?' ,['Yes','No'],False )
        if story_check == 'Yes':
            displayOpeningStory(name) # tells user an epic back story
        #####################################################################
        space(1)
        
        print(name +' was given MyBlueprint from Professor Tree') # tells user they found the map
        print(name + ' was given the ' + character[2][0] + ' from Professor Tree')#tells uer they were given a weapon
        space(1)
        input('The '+ character[2][0] +' was added to your Inventory ~>') #tells uer they were given a weapon
        space(1)
        printGraphics(current_world) # prints the current world
        space(1)
        input('Professor Tree\'s words echo in your head: "Open my blue print to help you navigate though the lands." ~>')# tells user the rules
        space(1)
        print('"The @ symbol on the map shows your position"')# tells user the rules
        print('"The V symbol on the map shows a local vendor selling their goods"')# tells user the rules
        print('"The + symbol on the map shows a hospital willing to patch you up for a fee"')# tells user the rules
        print('"The # symbol on the map shows the area to get out of this class room"')# tells user the rules
        print('"The B symbol on the map shows the Boss of that area"')# tells user the rules
        input('"make sure to explore in order to find weapons and items to aid your journey" ~>')# tells user the rules
        space(1)
        input('"Weapons and consumables are a necessity for your journey" ~>')
        input('"You will not able to see regular items and weapons on the map so make sure to check every nook and cranny" ~>')# tells user the rules        
        space(1)
        weapons.append(character[2])######## LUCAS CHANGE THE 2 TO THE POSITION IN THE WEAPON IS STORED IN CHARACTER
        while loop == True: # checks if loop is True
            turn_option = getOption('What would you like to do?',turn_options,False)#gets users optio every turn
            if turn_option == 'View My Blueprint': # checks if user chose my blue print
                printGraphics(current_world)# shows user the world
                space(1)
            elif turn_option == 'Open Bag': # checks turn options
                inventory_loop = True # sets the inventory loop to ture
                while inventory_loop == True: # runs while the inventory loop is true
                    print('Would you like to access in your inventory?') # aks user if they would like to acsses their inventory
                    printInventory() # m shows the user their inventory     
                    inventory_menu = input('Enter: ')# gets input from user
                    space(1)
                    if inventory_menu == '1': # checks if user chose key items
                        items_loop = True #loops inventory
                        while items_loop == True: #runs until items loop is false
                            return_array = getOptionExitWeapon('Choose a Key Item',keyitems,True) # gets key item from user
                            key_item = return_array[0]
                            if key_item == 'Exit': #checks if user chose exit
                                items_loop = False
                                space(1)
                            else:
                                print(key_item[1]) # prints description
                                space(1)
                    elif inventory_menu == '2': # checks if user chose weapons
                        #workingInventory (weapons,'Weapons') #uses working Inventory function for weapons
                        items_loop = True #loops inventory
                        while items_loop == True: #runs until items loop is false
                            print('1 - ' + weapons[0][0] +' is your primary weapon')# prints the primary weapons
                            return_array = getOptionExitWeapon('Choose a Weapon',weapons,True)# tells user to choose a weapon
                            weapon = return_array[0] # gets the weapon array
                            positions = return_array[1] # gets position array
                            if weapon == 'Exit': # checks if user chose exit
                                items_loop = False
                                space(1)
                            else:
                                print(weapon[1]) # prints the Weapons description
                                equip_option = getOption('Do you want to equip ' + weapon[0]  +' as your primary weapon',['Yes','No'],False) # asks user if they want to make this weapon there primaty weapon
                                if equip_option == 'Yes':   # checks if user chose yes                                  
                                    current_weapon = weapons[0] # gets the current weapon
                                    new_weapon = weapons [positions] # get new weapon
                                    if current_weapon == new_weapon: #checks if new weapon is the current weapon 
                                        print(weapon[0] + ' was aldready selected as your Primary Weapon') # tells user the eapon was aldready selected
                                        items_loop = False
                                        space(1)
                                    else:
                                        print(weapon[0] + ' is  Your Primary Weapon')
                                    weapons[0] = new_weapon # sets new weapon to primary weapon
                                    weapons [positions] = current_weapon # ssets primary weapon to space of old weapon
                                    items_loop = False # sets item loop to False
                                else:
                                    weapons = weapons # just something for an else statment
                                
 
                    elif inventory_menu == '3': # checks if user chose consumables
                        items_loop = True #loops inventory
                        while items_loop == True: #runs until items loop is false
                            return_array = getOptionExitWeapon('Choose a Consumable',consumables,True) # tells user to choose a consumable
                            consumable = return_array[0] # sets consumables to return array
                            positions = return_array[1] # sets position to return array
                            if consumable == 'Exit': # checks if consumable is exit
                                items_loop = False
                                space(1)
                            else:
                                print(consumable[1]) #prints the description of consumables
                                equip_option = getOption('Do you want to use ' + consumable[0] ,['Yes','No'],False) #Asks user if they want to uuse consumable
                                if equip_option == 'Yes': # sets equip option to Yes
                                    
                                    stats = consumables[positions] #gets the stats from a consumable
                                    if stats[3] == 'Health': # gets the descrip of consumable and checks if item is health
                                        if character[8] == character[7]: #checks if current health to max health
                                            print("you cannot use a Health item at full HP")
                                            space(1)
                                        else:# checks if user is not at max health
                                            print('You used ' + consumable[0]) # tells user they used th item
                                            stats = consumables.pop(positions)
                                            health_buff = stats[2]
                                            character[8] = character[8] + health_buff #restores health equivilant to the items value
                                            if character[8] > character[7]:
                                                character[8] = character[7]
                                                input('You restored ' + str(health_buff) +' HP ~>') # tells user the health they restored
                                                input("You're Health is " + str(character[7]) + '/' + str(character[8]) + ' ~>') # tells user their current Health
                                                space(1)
                                    else: # if you are trying to use a non-health item
                                        input('You cannot use a ' + stats[3] + ' item outside of battle ~>')
                                        space(1)

                                    
                                    weapons = weapons
                    elif inventory_menu == '4':# checks if user chose to quit
                        inventory_loop = False #sets inventory loop to False
                        print('you have stopped looking through your Inventory') # tells user they have quit the program
                        space(1)
            elif turn_option == 'Return to Main Menu': # returns the turn option to main menu
                quit_option = getOption('Are you sure you want to return you will lose your save?',y_n,False)#asks if the user is sure about their descion
                if quit_option == 'Yes':# checks if quit option is yes    
                    loop = False # sets loop to false
                else:#checks if user did not not choose yes
                    loop = True# sets loop to true
            elif turn_option == 'Check Profile':# check if turn option is equal to Check Profile
                #Characters = [name,pic,start weapon,life check,speed,luck,attak,max hp,current hp,level,xp,gold]
                max_exp = getEXPMax(character[9])
                #shows the characters stats
                print('Name: ' + name)
                print('Character: ' + character [0] )
                printGraphics(character[1])
                print('Health: ' + str(character[8]) + '/' + str(character[7]))
                print('Gold: ' + str(character[11]))
                print('Lv: ' + str(character[9]))
                print('Exp:' + str(character[10]) + '/' + str(max_exp))
                print('Attack: ' + str(character[6]))
                print('Speed: ' + str(character[4]))
                print('Luck: ' + str(character[5]))
                print('Shield: ' + str(character[12]))
                space(1)
                input('Continue ~>')
                space(1)
                
            elif turn_option == 'Move': # checks if user chose
                move_loop = True
                while move_loop == True:
                    if world_track == 1 and dungeon_active == False: # checks if world 1 is active
                        # if space is empty it gets replace with symbol
                        if current_world [7][6] == ' ': 
                            current_world [7][6] = 'V'
                        # if space is empty it gets replace with symbol
                        if current_world [5][5] == ' ':
                            current_world [5][5] = '+'
                    elif world_track == 2 and dungeon_active == False: # checks if world 2 is active
                        # if space is empty it gets replace with symbol
                        if current_world [3][3] == ' ':
                            current_world [3][3] = 'V'
                        # if space is empty it gets replace with symbol
                        if current_world [1][5] == ' ':
                            current_world [1][5] = '+'
                    elif world_track == 3 and dungeon_active == False: # checks if world 3 is active
                        # if space is empty it gets replace with symbol
                        if current_world [4][5] == ' ':
                            current_world [4][5] = 'V'
                        # if space is empty it gets replace with symbol
                        if current_world [4][7] == ' ':
                            current_world [4][7] = '+'
                        # if space is empty it gets replace with symbol
                        if current_world [4][9] == ' ':
                            current_world [4][9] = '?'
                        
                    printGraphics(current_world) # prints the map
                    complete = False # sets complete False
                    right_check = checkRight(current_world) # checks if you can move to right and stores it in right check
                    left_check = checkLeft(current_world)# checks if you can move to left and stores it in  left check
                    up_check = checkUp(current_world)# checks if you can move to up and stores it in  up check
                    down_check = checkDown(current_world)# checks if you can move to down and stores it in down check

                    move = getMove(right_check,left_check,up_check,down_check) # gets users move

                    #Right = 1 Left = 2 Up = 3 Down = 4
                    if move == 'D' or move == 'A' or move  == 'W' or move == 'S': # checks if user chose 1 ,2,3,4 
                        array = movement(current_world,current_world_h,move) # moves icon in direction depandant of users input
                        world1 = array[0] # gets the mapf rom array
                        player_space = array[1]  #gets the players position from array
                        showMove(move)# shows the player moving

                        if player_space == "T": # checks if user is on space to T
                            if tutorial_count == 0: # checks if tutorial to 0
                                tutorial_question = getOption('Would you like to participate in a combat tutorial?',['Yes','No'],False) # asks if user chose 0
                                if tutorial_question == 'Yes': # checks if tutorial is Yes
                                    tutorial_count += 1 # increasces tutorial by 1
                                    #Ask if user wants to participate in the tutorial (yes or no)
                                    #print('Do the Tutorial Fight Lucas')
                                    after_combat = activeCombatTutorial(name, character, weapons, consumables) #fight combat and determine if the player triumphs or falls
                                    character = after_combat[0] #gets the character array
                                    weapons = after_combat[1] #gets the weapons array
                                    consumables = after_combat[2] #gets the consumables array
                                    if character[3] == False: # if life check is False
                                        loop = False #player has fallen and the game ends
                                    elif character[3] == True: # if life check is still True
                                        character = checkLevel(character[9],character[10],character) #player survived and has a chance to level up
                                    else:
                                        print('Are you alive or dead?') # runs if error occurs
                                    move_loop = False # sets move loop to False
                                 
                        if player_space == "B": # checks if the players is on space B
                            if boss_battles == 0:
                                current_boss = 'Stalker' #player fights the first boss
                                after_combat = activeBossCombat(name, character, stalker, weapons, consumables) #fight combat and determine if the player triumphs or falls
                                #print(after_combat)
                                character = after_combat[0]
                                weapons = after_combat[1]
                                consumables = after_combat[2]
                                if character[3] == False:
                                    loop = False #player has fallen and the game ends
                                elif character[3] == True:
                                    current_world_h = replacePosition(current_world,current_world_h)
                                    character = checkLevel(character[9],character[10],character) #player survived and has a chance to level up
                                else:
                                    print('Are you alive or dead?')
                                    
                            elif boss_battles == 1:
                                current_boss = 'Grub Reaper' #player fights the second boss
                                after_combat = activeBossCombat(name, character, grub_reaper, weapons, consumables) #fight combat and determine if the player triumphs or falls
                                #print(after_combat)
                                character = after_combat[0]
                                weapons = after_combat[1]
                                consumables = after_combat[2]
                                if character[3] == False:
                                    loop = False #player has fallen and the game ends
                                elif character[3] == True:
                                    current_world_h = replacePosition(current_world,current_world_h)
                                    character = checkLevel(character[9],character[10],character) #player survived and has a chance to level up
                                else:
                                    print('Are you alive or dead?')
                                    
                            elif boss_battles == 2:
                                current_boss = 'Mecha Dragon' #player fights the final boss
                                after_combat = activeBossCombat(name, character, dragon, weapons, consumables) #fight combat and determine if the player triumphs or falls
                                #print(after_combat)
                                character = after_combat[0]
                                weapons = after_combat[1]
                                consumables = after_combat[2]
                                if character[3] == False:
                                    loop = False #player has fallen and the game ends
                                elif character[3] == True and monster_candy_deposit != 3:
                                    current_world_h = replacePosition(current_world,current_world_h)
                                    space(1)
                                    displayEndingOne(name)
                                    displayCredits()
                                    loop = False
                    ################################## END GAME ####################################
                                elif character[3] == True and monster_candy_deposit == 3: #if the player sacrificed 3 monster candy
                                    current_world_h = replacePosition(current_world,current_world_h) # gets rid of boss fight from map
                                    space(1)
                                    displayEndingTwo(name)
                                    displayCredits()
                                    loop = False
   
                                else:
                                    print('Are you alive or dead?')
                            else:
                                print('Boss battle counter ERROR')
                                
                            boss_battles = boss_battles + 1 #makes sure the player fights the next boss in line


                            
                            move_loop = False

                        if player_space == "M": # checks if player is on space M
                            if monster_true_count >= 2: # check sif monster count has been true twice
                                monster_spawn = 1 # sets monster spawn to 1
                            elif monster_false_count >= 2: # check sif monster count has been false twice
                                monster_spawn = 2 # sets monster spawn to 2
                            else:
                                monster_spawn = random.randint(1,2) # gets a random monster spawn value
                                
                            if monster_spawn == 1: # checks if monster spawn is false
                                monster_true_count = 0 # resets monster spawn is True
                                monster_false_count += 1 # increases monster false counter
                            else:
                                monster_true_count += 1 # increases monster true count value
                                monster_false_count = 0 # set monster false count to 0
                                enemy_array = getArray(world_track,find_enemy1,find_enemy2,find_enemy3)# get Enemy with function
                                current_enemy = random.choice(enemy_array)
                                after_combat = activeCombat(name, character, current_enemy, weapons, consumables) #fight combat and determine if the player triumphs or falls
                                #print(after_combat)
                                character = after_combat[0] # character array is replaced
                                weapons = after_combat[1] # weapons array is replaced
                                consumables = after_combat[2] # consumables array is replaced
                                if character[3] == False: # c
                                    loop = False #player has fallen and the game ends
                                elif character[3] == True:
                                    character = checkLevel(character[9],character[10],character) #player survived and has a chance to level up
                                else:
                                    print('Are you alive or dead?')
                                move_loop = False
                            
                        elif player_space == "W":# checks if user is on a W space
                            if world_track == 1: # checks if world track is 1
                                finding_weapons_flag = True
                                new_weapon = find_weapons1.pop() # takes a weapon from the list
                            elif world_track == 2:  # checks if world track is 2
                                finding_weapons_flag = True
                                new_weapon = find_weapons2.pop() # takes a weapon from the list
                            elif world_track == 3:  # checks if world track is 3
                                finding_weapons_flag = True
                                new_weapon = find_weapons3.pop() # takes a weapon from the list
                            else:
                                finding_weapons_flag = False # sets find weapons flag to false
                            if finding_weapons_flag == True:
                                input(name + ' found the ' + new_weapon[0] + ' and stored it in their inventory ~>')# tells user they found a weapon
                                weapons.append(new_weapon)# adds weapon to inventory
                                current_world_h = replacePosition(current_world,current_world_h) # replaces position so you can't walk over space repeatedly
                            else:
                                print('Find Weapon Error') # displays error
                            
                        elif player_space == "I": # sets player space to I
                            if world_track == 1:
                                finding_item_flag = True
                                new_item = find_item1.pop() # takes a weapon from the list
                            elif world_track == 2:
                                finding_item_flag = True
                                new_item = find_item2.pop() # takes a weapon from the list
                            else:
                                finding_item_flag = False
                            if finding_item_flag == True:
                                input(name + ' found the ' + new_item[0] + ' and stored it in their inventory ~>')# tells user they found a weapon
                                space(1)
                                consumables.append(new_item)# adds weapon to inventory
                                current_world_h = replacePosition(current_world,current_world_h) # replaces position so you can't walk over space repeatedly
                            else:
                                print('Find Weapon Error') # shows error
                                
                        elif player_space == "V":
                            store_check = getOption('You come across a travelling merchant will you browse his wares',y_n,False) # tells user about merchant
                            if store_check == 'Yes': # checks if user browsed store
                                items_loop = True # sets item loop to True
                                while items_loop == True: # runs while item loop is true
                                    print('You have ' + str(character[11]) + ' gold' ) # tells user how much gold they have
                                    space(1)
                                    if world_track == 1: # checks if world 1 and gets appropritae lists
                                        store_items = store1_items # gets coorect store item array
                                        store_item_price = store1_item_price # gets coorect store item array
                                        store_item_quantity = store1_item_quantity
                                    elif world_track == 2: # checks if world 2 and gets appropritae lists
                                        store_items = store2_items # gets coorect store item array
                                        store_item_price = store2_item_price # gets coorect store item array
                                        store_item_quantity = store2_item_quantity # gets coorect store item array
                                    else:
                                        store_items = store3_items # checks if world 3 and gets appropritae lists
                                        store_item_price = store3_item_price # gets coorect store item array
                                        store_item_quantity = store3_item_quantity # gets coorect store item array
                                        
                                    return_array = getOptionExitShop('What would you like to buy ',store_items,store_item_price,store_item_quantity,True) # gets item
                                    space(1)
                                    shop_item = return_array[0] # gets the arrays from function
                                    positions = return_array[1] # gets the arrays from function
                                    if shop_item == 'Exit':# checks if user exited the shop
                                        items_loop = False
                                    else:
                                        if store_item_quantity[positions] == 0: # checks if item is sold out
                                            input('The Item you are trying to buy is sold out ~>') # tells user that the item they're looking for is sold out
                                        else:
                                            print(shop_item[1]) # gets item from store
                                            equip_option = getOption('For '+ str(store_item_price[positions]) + ' gold would you like to buy '+ shop_item[0],['Yes','No'],False) # asks if user want to buy item
                                            if equip_option == 'Yes': # checks if user chose Yes
                                                golds = character[11] # gets gold from user
                                                if golds >= store_item_price[positions]: # check if user has enough gold
                                                    character[11] = golds - store_item_price[positions]
                                                    print('You bought the ' + shop_item[0])
                                                    input('You have ' + str(character[11]) + ' gold remaining ~>' ) # tells usesr how mmuch gold they have remaining
                                                    space(1)
                                                    store_item_quantity[positions] -= 1 # decreasces store item quantity
                                                    item_shop = copy.deepcopy(shop_item) # copies the shop item wwith a deep copy
                                                    item_shop[0] = item_shop[0].rstrip()
                                                    item_shop[0] = item_shop[0].lstrip()
                                                    if len(item_shop) == 4: # checks if item is a consumable
                                                        consumables.append(item_shop) # adds item from shop
                                                    else:
                                                        weapons.append(item_shop)# adds weapon from shop
                                                else:
                                                    print(" You do not have enough gold to purchase this item")
                                            
                                        
                            else:# checks if user did not check store
                                print('You chose not to browse the vendors wares')
                                

                        elif player_space == "S": # Runs code if player goes on switch
                            if world_track == 1 and  dungeon_active == False: # checks if world track is 1 
                                if switch_counter == 0:# sets switch counter to 0                            
                                    switch_question = getOption('You found a hidden switch will you press it?',y_n,False) # tells user the found a hidden switch
                                    if switch_question == 'Yes': # sets switch question to Yes
                                        switch_counter += 1 # increases switch counter by 1
                                        current_world_h = replacePosition(current_world,current_world_h) # replaces current position on grid so Switch dissapears
                                        current_world[7][1] = '●' #creates the hole in world 1
                                        current_world_h[7][1] = '●'  #creates the hole in world 1
                                        input('You hear the sound of a trap door creaking open ~>')
                                        space(1)
                                    else:
                                        switch_counter = switch_counter
                                else:
                                    switch_counter = switch_counter
                            elif world_track == 1 and  dungeon_active == True: # code for switch in sub world world 1 
                                if current_world[3][3] == '@': # checks if user stepped on switch 1
                                    input('You step on a pressure plate altering the walls in the map ~>')
                                    space(1)
                                    if switch_dungeon_1 == False: #checks if switch is False
                                        switch_dungeon_1 = True # sets switch to True
                                        current_world[3][5] = '█' # replaces space with a block
                                    else:
                                        switch_dungeon_1 = False # sets switch to False
                                        current_world[3][5] = ' ' #replaces block with a space
                                elif current_world[3][7] == '@': # checks if user stepped on switch 2
                                    input('You step on a pressure plate altering the walls in the map ~>')
                                    space(1)
                                    current_world[3][8] = ' ' # sets the wall to space
                                    current_world_h = replacePosition(current_world,current_world_h) # takes away the switch
                                        
                        elif player_space == "ʘ": # checks if user steps on magic wand space
                            input(' You found the ' + magic_wand[0] + ' and added it into your inventory ~>') #tells user they found weapon
                            space(1)
                            current_world_h = replacePosition(current_world,current_world_h) # takes away magic wand space
                            weapons.append(magic_wand) # adds magic wepon to inventory
                            
                        elif player_space == "●": # checks if user was on hole space
                            input(name + " goes to investigate the opened hole and falls in ~>")
                            save_main_world = copy.deepcopy(current_world) # copies the world to save it
                            save_main_world_hidden = copy.deepcopy(current_world_h) # copies the world to save it
                            dungeon_active = True #checks if dungeon True
                            if world_track == 1: # checks if it is in world 1
                                input("A magical weapon ʘ is appearing on your map, try to get to the weapon ~>")
                                space(1)
                                current_world = copy.deepcopy(world1_dungeon) # copy the world 1 dungeon
                                current_world_h = copy.deepcopy(world1h_dungeon) # copy the world 1 hidden dungeon
                            else:
                                print("This puzzle is based on the Monty Hall problem if you guess right you will be rewarded or if you guess wrong you will be punished ")
                                print("One door is the correct door and the other 2 doors are not correct")
                                current_world = copy.deepcopy(world2_dungeon) # gets a copy of the world2 dungeon

                                current_world_h = copy.deepcopy(world2h_dungeon) # gets a copy of the world 2 hidden dungeon
                                input("Pick a door  ~>")
                                space(1)
                        
                        elif player_space == '1' or player_space == '2' or player_space == '3': # code for the three doors
                            player_monty_hall += 1 # increases the monty hall counter
                            if player_monty_hall == 1:
                                current_world = copy.deepcopy(world2_dungeon) # copies the world 2 dungeon
                                current_world_h = copy.deepcopy(world2h_dungeon) # copies the world2 hidden dungeon
                                input("You picked door " + player_space + ' ~>')
                                
                                first_door = player_space # gets the location of the first dor
                                get_door = False
                                while get_door == False:
                                    wrong_door = random.choice(['1','2','3']) # picks a random door
                                    if wrong_door == player_space: # checks if user was in the wrong door
                                        get_door = False # sets get door to False
                                    else:
                                        get_door = True # sets get door to True
                                if wrong_door == '1': # checks if wrong door is 1
                                    current_world[1][1] = '█' # blocks of the door
                                elif wrong_door == '2': # checks if wrong door is 2
                                    current_world[1][3] = '█' # blocks of the door
                                elif wrong_door == '3': # checks if wrong door is 3
                                    current_world[1][5] = '█' # blocks of the door
                                else:
                                    print('ERROR')
                                print("Door " + wrong_door + " is not the right door") # tells user the wrong door
                                input("Will you change doors or stay with the same door? ~>") # tells user their options
                                space(1)
                                while get_door == True: # runs while get door is True
                                    right_door = random.choice(['1','2','3']) # randomly gets right door
                                    if right_door == player_space or right_door == wrong_door : # checks if right door is the wrond door or the orignal door
                                        get_door = True # sets get door to True
                                    else: 
                                        get_door = False # sets get door to False
                                
                                if right_door == '1': # check if right door is 1
                                    current_world_h[1][1] = '^' # puts the exit into the correct door
                                elif right_door == '2': # check if right door is 2
                                    current_world_h[1][3] = '^' # puts the exit into the correct door
                                elif right_door == '3': # check if right door is 1
                                    current_world_h[1][5] = '^' # puts the exit into the correct door
                                else:
                                    print('ERROR') # prints out ERROR
                            else:
                                print('You chose the wrong door, door ' + right_door + ' was the right door according to the monty hall problem' )# tells user chose wrong door
                                space(1)
                                after_combat = activeCombat(name, character, familiar_shadow, weapons, consumables) #fight combat and determine if the player triumphs or falls
                                #print(after_combat)
                                # returns the arrays
                                character = after_combat[0] 
                                weapons = after_combat[1]
                                consumables = after_combat[2]
                                if character[3] == False:
                                    loop = False #player has fallen and the game ends
                                elif character[3] == True:
                                    character = checkLevel(character[9],character[10],character) #player survived and has a chance to level up
                                    print(name + " found a step ladder out of the hole and rentered the classroom ")
                                    input('The hole  you came from magically covers itself ~>')
                                    space(1)
                                    current_world = copy.deepcopy(save_main_world) # loads in the previusly saved main world
                                    current_world_h = copy.deepcopy(save_main_world_hidden) # loads in the previusly saved main world
                                    current_world_h[5][11] = ' ' #gets rid of hole in world 2
                                    dungeon_active = False # sets active dungeon to False
                                    move_loop = False
                                else:
                                    print('Are you alive or dead?')
                                                      
                        elif player_space == '^': # checks if user stepped into the warp gate
                            if world_track == 1:
                                print(name + " found a step ladder out of the hole and rentered the classroom ")
                                input('The hole  you came from magically covers itself ~>')
                                current_world = copy.deepcopy(save_main_world) # loads in the previusly saved main world
                                current_world_h = copy.deepcopy(save_main_world_hidden) # loads in the previusly saved main hidden world
                                current_world_h[7][1] = ' ' #gets rid of the hole in world 1
                                dungeon_active = False # sets dungeon to false
                                move_loop = False
                            else:
                                input('You completed the Monty Hall Problem correctly and recieve a prize ~>')
                                input( name + ' found the ' + magic_staff[0] + ' and added it into your inventory ~>')
                                weapons.append(magic_staff) # adds magic staff to inventory
                                print(name + " found a step ladder out of the hole and rentered the classroom ")
                                input('The hole  you came from magically covers itself ~>')
                                current_world = copy.deepcopy(save_main_world) # gets a copy of the world
                                current_world_h = copy.deepcopy(save_main_world_hidden) # gets a copy of the world
                                current_world_h[5][11] = ' ' # changes space to empty
                                dungeon_active = False # sets dungeon to False
                                move_loop = False # sets move loop to False
                                
                        elif player_space == "C": # sets player space to I
                            candy_loop = True
                            while candy_loop == True:
                                if candy_counter < 4: #checks if candy counter is less than 4
                                    candy_question = getOption('Please take one, take a piece of candy?',y_n,False) # asks user if they want candy
                                    if candy_question == 'Yes': # if user chose Yes
                                        candy_counter += 1 # takes candy from user
                                        if candy_counter == 1: # checks if candy counter is 1
                                            input('you take a piece of candy ~>')
                                            space(1)
                                            keyitems.append(monster_candy) # adds monster candy to inventory
                                        elif candy_counter == 2: # checks if candy counter is 2
                                            input('you took another piece of candy, how disgusting ~>')
                                            space(1)
                                            keyitems.append(monster_candy) # adds monster candy to inventory
                                        elif candy_counter == 3: # checks if candy counter is 3
                                            input('You took another piece, you feel like the scum of the earth ~>')
                                            space(1)
                                            keyitems.append(monster_candy) # adds monster candy to inventory
                                        elif candy_counter == 4: # checks if candy counter is 4
                                            input('You took too much too fast, the candy spills onto the ground ~>')
                                            space(1)
                                        else:
                                            print('CANDY ERROR')
                                    else:
                                        candy_loop = False # stops candy loop
                                        move_loop = False # stops move loop
                                else:
                                    input('Look at the candy you spilt on the ground ~>')
                                    candy_loop = False # stops candy loop
                                    move_loop = False
                            
                        elif player_space == "#": # checks if player is on space #
                            print('You made your way through the first world and journey towards the second') # tells users about their journey
                            input('You come across another world. Your MyBlueprint starts glowing and shows you the map of this new world ~>')# tells user story
                            space(1)
                            current_world = copy.deepcopy(world2) # sets the current world to world 1
                            current_world_h = copy.deepcopy(world2h) # sets the current hidden world to hidden world 1
                            printGraphics(current_world) # prints new world
                            world_track = 2  # sets world to 2
                            move_loop = False

                        elif player_space == "+": # checks if player is on space +
                            print('You have ' + str(character[11]) + ' gold') # tells user their gold
                            print('Hp: ' + str(character[8]) + '/' + str(character[7]))
                            store_check = getOption('Would you like to fully heal yourself at the local Hospital for 200 gold',y_n,False) # tells user about merchant
                            space(1)
                            if store_check == 'Yes':
                                golds = character[11]
                                if golds >= 200: # checks if user has enough gold
                                    character[11] = golds - 200
                                    print('You fully healed')
                                    character[8] = character[7] # fully heals characters
                                else:
                                    print("You don't have  enough gold to heal youself")
                                    
                        elif player_space == "&": # checks if player is on space #
                            print(name +  ' journeys onwards and sees the Land of Attendance in the distance')
                            print(' A large Dragon can be seen guarding the Land of Attendance so it would be wise to train before the fight')
                            current_world = copy.deepcopy(world3) # sets the current world to world 1
                            current_world_h = copy.deepcopy(world3h) # sets the current hidden world to hidden world 1
                            world_track = 3
                            move_loop = False

                        elif player_space == "?": # checks if player is on space ?
                            if monster_candy_deposit < 3: # checks if monster candy deposit is less than 3
                                monster_candy_deposit_check = False
                                while monster_candy_deposit_check == False:
                                    sacrifice_check = getOption('Would you like to sacrifice a Monster Candy ' + str(monster_candy_deposit)  + '/3',y_n,False) # tells user about merchant
                                    if sacrifice_check == 'Yes':
                                        position_of_monster_candy = 'A'
                                        consumables_length = len(keyitems) # gets length of the maps array
                                        for item_position in range (0,consumables_length): #runs for the length of maps array
                                            current_line = keyitems[item_position] # gets appropriate line from maps
                                            if ('Monster Candy' in current_line) == True: # checks if @ is in current line
                                                position_of_monster_candy = item_position #gets the position of @ in array
                                        if position_of_monster_candy == 'A':
                                            input('You do not have any monster_candy ~>')
                                            monster_candy_deposit_check = True
                                        else:
                                            del(keyitems[item_position])
                                            monster_candy_deposit += 1
                                            if monster_candy_deposit == 3:
                                                input('The sacrafice is ready ~>') # tells user the sacragice is ready
                                                monster_candy_deposit_check = True
                                            
                                    else:
                                        monster_candy_deposit_check = True
                            else:
                                input(' The sacrafice is ready ~>')

                    elif move == '1': # checks if user inputed 5
                        input('you decided to wait before you move ~>') # tells user they have quit the program
                        space(1)
                        move_loop = False
                    else: # runs if a problem occurs
                        print('ERROR:1')#prints an error message
            else:# check is user inputtted an error
                print('ERROR:2')# prints an error
    else:# checks if error occured
        print('ERROR:3')# prints an error
print('You have quit the program') # tells user they quit
space(1)
