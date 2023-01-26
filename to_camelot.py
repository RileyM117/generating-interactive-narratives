from action import action
import narrative_elements

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
