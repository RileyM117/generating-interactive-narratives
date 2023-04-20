import names as names
import random

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
class character(object):
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
    


main_char = character(names.get_full_name(),random.choice(female_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_female),random.choice(skin_colors),random.choice(outfits),'Camp')
# blacksmith's
blacksmith = character(names.get_full_name(),'F','brown','black','Short_Beard',3,'Peasant','Blacksmith.Anvil')
#alchemyshop
alchemist  = character(names.get_full_name(),'C','blue','blonde','Short',4,'Merchant','AlchemyShop.Bar.Behind')
#bridge
#bridge_rando1 = character(names.get_full_name(),random.choice(male_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_male),random.choice(skin_colors),random.choice(outfits),'Bridge')
#bridge_rando2 = character(names.get_full_name(),random.choice(male_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_female),random.choice(skin_colors),random.choice(outfits),'Bridge')
# castlebedroom
king = character(names.get_full_name(),'H','blue','blonde','Musketeer_Beard',3,'King','GreatHall.LeftThrone')
queen = character(names.get_full_name(),'G','blue','red','Straight',3,'Queen','GreatHall.Throne')
#castlecrossroads
#guard = character(names.get_full_name(),'E','brown','brown','Ponytail',8,'HeavyArmour','CastleCrossroads')
#city 
city_rando1 = character(names.get_full_name(),random.choice(male_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_male),random.choice(skin_colors),random.choice(outfits),'City.Plant')
city_rando2 = character(names.get_full_name(),random.choice(female_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_female),random.choice(skin_colors),random.choice(outfits),'City.Fountain')
city_rando3 = character(names.get_full_name(),random.choice(male_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_male),random.choice(skin_colors),random.choice(outfits),'City.Horse')
beggar = character(names.get_full_name(),random.choice(female_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_female),random.choice(skin_colors),'Beggar','City.Alley')
#cottage
#cottage_rando1 = character(names.get_full_name(),random.choice(female_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_female),random.choice(skin_colors),random.choice(outfits),'Cottage')
#courtyard
noble1 = character(names.get_full_name(),random.choice(male_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_male),random.choice(skin_colors),'Noble','Courtyard')
noble2 = character(names.get_full_name(),random.choice(male_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_male),random.choice(skin_colors),'Noble','Courtyard')
noble3 = character(names.get_full_name(),random.choice(female_body_types),random.choice(eye_colors),random.choice(hair_colors), random.choice(hairstyles_female),random.choice(skin_colors),'Noble','Courtyard.Horse')
merchant = character(names.get_full_name(),random.choice(male_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_male),random.choice(skin_colors),'Merchant','Courtyard.BigStall.Right')
#dungeon
#dungeon_guard = character(names.get_full_name(),'B','brown','brown','Short',6,'HeavyArmour','Dungeon')
#prisoner = character(names.get_full_name(),'D','black','red','Long',8,'Naked','Dungeon')
# farm
#farmer = character(names.get_full_name(),'D','black','black','Short',9,'Peasant','Farm')
#forestpath
#bandit = character(names.get_full_name(),'H','red','red','Spiky',2,'Bandit','ForestPath.Well')
#Library
librarian = character(names.get_full_name(),'A','black','blonde','Short',7,'Peasant','Library.Chair')
student = character(names.get_full_name(),'A','green','black','Long',4,'Noble','Library.SpellBook')
#ruins
witch = character(names.get_full_name(),'G','white','gray','Spiky',1,'Witch','Ruins.Throne')
#spookypath
#bandit2 = character(names.get_full_name(),'A','red','red','Spiky',2,'Bandit','SpookyPath.Well')
#tavern
barkeep = character(names.get_full_name(),'B','green','blonde','Short',8,'Merchant','Tavern.Bar.Behind')
drunk1 = character(names.get_full_name(),random.choice(female_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_female),random.choice(skin_colors),'Peasant','Tavern.FrontLeftStool')
drunk2 = character(names.get_full_name(),random.choice(female_body_types),random.choice(eye_colors),random.choice(hair_colors),random.choice(hairstyles_female),random.choice(skin_colors),'Beggar','Tavern.FrontRightStool')

char_list = [main_char,blacksmith,alchemist,king,queen,city_rando1,city_rando2,
             city_rando3,beggar,noble1,noble2,noble3,merchant,witch,
             librarian,student,barkeep,drunk1,drunk2]
char_names = [main_char.name,blacksmith.name,alchemist.name,king.name,queen.name,city_rando1.name,city_rando2.name,
             city_rando3.name,beggar.name,noble1.name,noble2.name,noble3.name,merchant.name,witch.name,
             librarian.name,student.name,barkeep.name,drunk1.name,drunk2.name]
for i in char_list:
  i.get_char()
  i.set_loc()

