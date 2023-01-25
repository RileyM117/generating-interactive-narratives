from narrative import action
from creation import CreateCharacter, CreateEffect, CreateItem, CreatePlace

# atttributes in the format: name, body type, hairstyle, outfit, hair color, eye color, skin color.
protag = CreateCharacter('Protag','B','Spiky','LightArmour','red','blue',5).get() 
smithy = CreateCharacter('Smithy','F', 'Short_Full', 'Peasant','black','brown',3).get()
louis = CreateCharacter('Louis', 'D', 'Long', 'Merchant', 'black', 'green', 1).get()
clark = CreateCharacter('Clark', 'H', 'Musketeer', 'Bandit', 'black', 'brown',1).get()
cassandra = CreateCharacter('Cassandra', 'A', 'Long', 'Noble', 'blonde', 'blue', 5).get()
witch = CreateCharacter('Witch', 'G', 'Short', 'Witch', 'black', 'green', 3).get()

blacksmith = CreatePlace('Blacksmith','Blacksmith').get()
camp = CreatePlace('Camp','Camp').get()
forest_path = CreatePlace('ForestPath','ForestPath').get()
ruins = CreatePlace('Ruins','Ruins')

sword = CreateItem('Sword','Sword').get()
hammer = CreateItem('hammer', 'Hammer').get()
gem = CreateItem('gem','JewelKey').get()

char_list = [protag,smithy,louis,clark,cassandra,witch]
place_list = [blacksmith,camp,forest_path,ruins]
item_list = [sword,hammer,gem]

def create_set_character():
  for i in char_list:
    action('CreateCharacter({},{})'.format(i[0],i[1]))
    action('SetHairstyle({},{})'.format(i[0],i[2]))
    action('SetClothing({},{})'.format(i[0],i[3]))
    action('SetHairColor({},{})'.format(i[0],i[4]))
    action('SetEyeColor({},{})'.format(i[0],i[5]))
    action('SetSkinColor({},{})'.format(i[0],i[6]))

def create_place():
  for i in place_list:
    action('CreatePlace({},{})'.format(i[0],i[1]))

def create_item():
  for i in item_list:
    action('CreateItem({},{})'.format(i[0],i[1]))
