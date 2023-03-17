!pip install --upgrade pip
!pip install openai
!pip install fantasynames
import os
import openai
import random
import fantasynames as names
import re

def action(command):
    
      print('start ' + command)
      # Get responses until success or failure response is received from Camelot
      while(True):  
        # Get response from Camelot    
        i = input()
         # Return True if succeeds and False if fails.
        if(i == 'succeeded ' + command):
          return True
        elif(i == 'failed ' + command):
          return False
        elif(i.startswith('error')):
          return False
        else:
          return False

male_body_types = ['B','D','F','H']
female_body_types = ['A','C','E','G']
eye_colors = ['white', 'black', 'blue', 'red', 'brown', 'green']
hair_colors = ['gray', 'black', 'brown', 'red', 'blonde']
skin_colors = [0,1,2,3,4,5,6,7,8,9,10]
hairstyles = ['Long','Spiky','Short','Short_Beard','Short_Full','bald']
hairstyles_female = ['Ponytail','Straight']
hairstyles_male = ['Mage','Mage_Beard','Mage_Full','Musketeer','Musketeer_Beard','Musketeer_Full']
outfits = ['Bandit','Beggar','HeavyArmour','LightArmour','Merchant','Noble','Peasant','Priest']
outfits_female = ['Queen','Witch']
outfits_male = ['King','Warlock']

possible_locations = ['Bridge','CastleBedroom','Cottage','CastleCrossroads', 'Hallway'
             'DiningRoom','Farm','Port',
             'Storage']
definite_locations = ['AlchemyShop','Blacksmith','Camp','GreatHall','City','Courtyard','Dungeon','Tavern','ForestPath','SpookyPath','Ruins','Library']

rand_locations = []

num = random.randint(1, len(possible_locations))


for i in range(num):
    rand_str = random.choice(possible_locations)
    rand_locations.append(rand_str)


all_locations = rand_locations + definite_locations

locations = set(all_locations)

for i in locations:
  action("CreatePlace({},{})".format(i,i))

class Character(object):
  def __init__(self,name,body,eye_color,hair_color,hairstyle,skin_color,outfit,location):
    self.name = name
    self.body = body
    self.eye_color = eye_color
    self.hair_color = hair_color
    self.hairstyle = hairstyle
    self.skin_color = skin_color
    self.outfit = outfit
    self.location = location
  def get_char(self):
    return [self.name,self.body,self.eye_color,self.hair_color,self.hairstyle,self.skin_color,self.outfit]
  def set_loc(self):
    return self.location
  def change_loc(self,new_loc):
    self.location = new_loc
    return new_loc
    
main_char = Character(names.human('female'),random.choice(female_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_female),random.choice(skin_colors),random.choice(outfits),'Camp')
# blacksmith's
blacksmith = Character(names.human('male'),'F','brown','black','Short_Beard',3,'Peasant','Blacksmith')
#alchemyshop
alchemist  = Character(names.human('female'),'C','blue','blonde','Short',4,'Merchant','AlchemyShop')
#bridge
bridge_rando1 = Character(names.human('male'),random.choice(male_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_male),random.choice(skin_colors),random.choice(outfits),'Bridge')
bridge_rando2 = Character(names.human('female'),random.choice(male_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_female),random.choice(skin_colors),random.choice(outfits),'Bridge')
# castlebedroom
king = Character(names.human('male'),'H','blue','blonde','Musketeer_Beard',3,'King','GreatHall')
queen = Character(names.human('female'),'H','blue','red','Straight',3,'Queen','GreatHall')
#castlecrossroads
guard = Character(names.human('female'),'E','brown','brown','Ponytail',8,'HeavyArmour','CastleCrossroads')
#city 
city_rando1 = Character(names.human('male'),random.choice(male_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_male),random.choice(skin_colors),random.choice(outfits),'City')
city_rando2 = Character(names.human('female'),random.choice(female_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_female),random.choice(skin_colors),random.choice(outfits),'City')
city_rando3 = Character(names.human('male'),random.choice(male_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_male),random.choice(skin_colors),random.choice(outfits),'City')
beggar = Character(names.human('female'),random.choice(female_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_female),random.choice(skin_colors),'Beggar','City')
#cottage
cottage_rando1 = Character(names.human('female'),random.choice(female_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_female),random.choice(skin_colors),random.choice(outfits),'Cottage')
#courtyard
noble1 = Character(names.human('male'),random.choice(male_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_male),random.choice(skin_colors),'Noble','Courtyard')
noble2 = Character(names.human('male'),random.choice(male_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_male),random.choice(skin_colors),'Noble','Courtyard')
noble3 = Character(names.human('female'),random.choice(female_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_female),random.choice(skin_colors),'Noble','Courtyard')
merchant = Character(names.human('male'),random.choice(male_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_male),random.choice(skin_colors),'Merchant','Courtyard')
#dungeon
dungeon_guard = Character(names.human('male'),'B','brown','brown','Short',6,'HeavyArmour','Dungeon')
prisoner = Character(names.human('male'),'D','black','red','Long',8,'Naked','Dungeon')
# farm
farmer = Character(names.human('male'),'D','black','black','Short',9,'Peasant','Farm')
#forestpath
bandit = Character(names.human('male'),'H','red','red','Spiky',2,'Bandit','ForestPath')
#Library
librarian = Character(names.human('female'),'A','black','blonde','Short',7,'Peasant','Library')
student = Character(names.human('female'),'A','green','black','Long',4,'Noble','Library')
#ruins
witch = Character(names.human('female'),'G','white','gray','Spiky',1,'Witch','Ruins')
#spookypath
bandit2 = bandit = Character(names.human('female'),'A','red','red','Spiky',2,'Bandit','SpookyPath')
#tavern
barkeep = Character(names.human('male'),'B','green','blonde','Short',8,'Merchant','Tavern')
drunk1 = Character(names.human('female'),random.choice(female_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_female),random.choice(skin_colors),'Peasant','Tavern')
drunk2 = Character(names.human('male'),random.choice(female_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_female),random.choice(skin_colors),'Beggar','Tavern')

char_list = [main_char,blacksmith,alchemist,bridge_rando1,bridge_rando2,king,queen,guard,city_rando1,city_rando2,
             city_rando3,beggar,cottage_rando1,noble1,noble2,noble3,merchant,dungeon_guard,prisoner,
             farmer,bandit,librarian,student,witch,bandit2,barkeep,drunk1,drunk2]

for i in char_list:
  i.get_char()
  i.set_loc()

for i in char_list:
  action("CreateCharacter({},{})".format(i.name,i.body))
  action("SetEyeColor({},{})".format(i.name,i.eye_color))
  action("SetHairColor({},{})".format(i.name,i.hair_color))
  action("SetHairstyle({},{})".format(i.name,i.hairstyle))
  action("SetSkinColor({},{})".format(i.name,i.skin_color))
  action("SetOutfit({},{})".format(i.name,i.outfit))

for i in char_list:
  if i.location in locations:
    action("SetPosition({},{})".format(i.name,i.location))
