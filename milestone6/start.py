import random
#from Character import char_list
from Character import char_list
def action(command):
    print('start ' + command)
    while(True):
        i = input()
        if(i == 'succeeded ' + command):
            return True
        elif(i == 'failed ' + command):
            return False
        elif(i.startswith('error')):
            return False
action("ShowMenu()")
#possible_locations = ['Bridge','CastleBedroom','Cottage','CastleCrossroads', 'Hallway',
#            'DiningRoom','Farm','Port',
#             'Storage']
definite_locations = ['AlchemyShop','Blacksmith','Camp','GreatHall','City','Courtyard','Dungeon','Tavern','ForestPath','SpookyPath','Ruins','Library']

#rand_locations = []
#num = random.randint(1, len(possible_locations))

#for i in range(num):
#    rand_str = random.choice(possible_locations)
#    rand_locations.append(rand_str)

all_locations = definite_locations #rand_locations + definite_locations

locations = set(all_locations)

for i in locations:
  action("CreatePlace({},{})".format(i,i))

for i in char_list:
  action("CreateCharacter({},{})".format(i.name,i.body))
  action("SetEyeColor({},{})".format(i.name,i.eye_color))
  action("SetHairColor({},{})".format(i.name,i.hair_color))
  action("SetHairStyle({},{})".format(i.name,i.hairstyle))
  action("SetSkinColor({},{})".format(i.name,i.skin_color))
  action("SetClothing({},{})".format(i.name,i.outfit))

for i in char_list:
  #if i.location in locations:
    action("SetPosition({},{})".format(i.name,i.location))
  
while(True):
  i = input()
  if(i == 'input Selected Start'):
   
   action("Sit({},City.Bench)".format(char_list[6].name))
   action("Face({},City.Fountain)".format(char_list[5].name))
   action('SetCameraFocus({})'.format(char_list[0].name))
   action('HideMenu()')
   action('EnableInput()')
   action('EnableInput()')

  if(i == 'input arrived ' + char_list[0].name + ' position Camp.Exit'):
     action("SetPosition({},ForestPath)".format(char_list[0].name))
  if(i == 'input arrived ' + char_list[0].name + ' position ForestPath.EastEnd'):
     action("SetPosition({},City.EastEnd)".format(char_list[0].name))
  if(i == 'input arrived ' + char_list[0].name +' position City.NorthEnd'):
     action("SetPosition({},SpookyPath.WestEnd)".format(char_list[0].name))
      
