# Create Characters,items,locations, and set initial positions.
def inital_setup():

#Locations
  action('CreatePlace(Blacksmith,Blacksmith)')
  action('CreatePlace(Camp,Camp)')

# Characters

# Protag
  action('CreateCharacter(Protag,B)')
  action('SetHairStyle(Protag, Spiky)')
  action('SetEyeColor(Protag,blue)')
  action('SetClothing(Protag,LightArmour)')
  action('SetHairColor(Protag,red)')
  action('SetSkinColor(Protag,5)')
  action('SetExpression(Protag,neutral)')
  action('SetPosition(Protag,Camp.Log)')
  action('Sit(Protag,Camp.Log)')

# Blacksmith
  action('CreateCharacter(Smithy,F)')
  action('SetHairStyle(Smithy, Short_Full)')
  action('SetEyeColor(Smithy,brown)')
  action('SetClothing(Smithy,Peasant)')
  action('SetHairColor(Smithy,black)')
  action('SetSkinColor(Smithy,3)')
  action('SetExpression(Smithy,happy)')
  action('SetPosition(Smithy,Blacksmith.Anvil)')
  action('Face(Smithy,Blacksmith.Anvil)')

# Items

# Smithy Sword
  action('CreateItem(Sword,Sword)')
  action('SetPosition(Sword,Blacksmith.Anvil)')

# Smithy Hammer
  action('CreateItem(hammer,Hammer)')
  action('SetPosition(hammer,Smithy)')
