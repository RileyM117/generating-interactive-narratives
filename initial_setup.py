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

# Louis (Antagonist)
  action('CreateCharacter(Louis,D)')
  action('SetHairStyle(Louis, Long)')
  action('SetEyeColor(Louis,green)')
  action('SetClothing(Louis,Merchant)')
  action('SetHairColor(Louis,black)')
  action('SetSkinColor(Louis,1)')
  action('SetExpression(Louis,neutral)')
  action('SetPosition(Louis,Camp.LeftLog)')
  action('Sit(Louis,Camp.LeftLog)')

#Clark (Extra)
  action('CreateCharacter(Clark,H)')
  action('SetHairStyle(Clark, Musketeer)')
  action('SetEyeColor(Clark,brown)')
  action('SetClothing(Clark,Bandit)')
  action('SetHairColor(Clark,black)')
  action('SetSkinColor(Clark,1)')
  action('SetExpression(Clark,neutral)')
  action('SetPosition(Clark,Camp.Barrel)')


# Cassandra (Leader)
  action('CreateCharacter(Cassadnra,A)')
  action('SetHairStyle(Cassandra, Long)')
  action('SetEyeColor(Cassandra,blue)')
  action('SetClothing(Cassandra,Noble)')
  action('SetHairColor(Cassandra,blonde)')
  action('SetSkinColor(Cassandra,5)')
  action('SetExpression(Cassandra,neutral)')
  action('SetPosition(Cassandra,Camp.RightLog)')
  action('Sit(Cassandra,Camp.RightLog)')  

# Items

# Smithy Sword
  action('CreateItem(Sword,Sword)')
  action('SetPosition(Sword,Blacksmith.Anvil)')

# Smithy Hammer
  action('CreateItem(hammer,Hammer)')
  action('SetPosition(hammer,Smithy)')
