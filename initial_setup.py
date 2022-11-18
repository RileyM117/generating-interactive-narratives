# Create Characters,items,locations, and set initial positions.
def inital_setup():

#Locations
 # Creates the Blacksmith's shop, the Protagonist's home (Camp) and a path to investigate.
  action('CreatePlace(Blacksmith,Blacksmith)')
  action('CreatePlace(Camp,Camp)')
  action('CreatePlace(ForestPath,ForestPath)')

# Characters
 # This defines the characteristics of the characters.
  
# Protag
  action('CreateCharacter(Protag,B)') # Creates character with name "Protag" with body type B
  action('SetHairStyle(Protag, Spiky)') # Gives Protag the Spiky Hairstyle
  action('SetEyeColor(Protag,blue)') # Gives Protag blue eyes
  action('SetClothing(Protag,LightArmour)') #Gives Protag Light Armor for clothing
  action('SetHairColor(Protag,red)') # Gives Protag red hair
  action('SetSkinColor(Protag,5)') # Gives Protag fair skin (Skin color is defined on a scale from 0-10 with 0 being very pale and 10 being very dark).
  action('SetExpression(Protag,neutral)') # Sets Protag's facial expression to neutral
  action('SetPosition(Protag,Camp.Log)') # Sets Protag's initial position to the default log in the Camp location
  action('Sit(Protag,Camp.Log)') # Makes Protag sit on the default log in the Camp

# Blacksmith
  action('CreateCharacter(Smithy,F)')
  action('SetHairStyle(Smithy, Short_Full)')
  action('SetEyeColor(Smithy,brown)')
  action('SetClothing(Smithy,Peasant)')
  action('SetHairColor(Smithy,black)')
  action('SetSkinColor(Smithy,3)')
  action('SetExpression(Smithy,happy)')
  action('SetPosition(Smithy,Blacksmith.Anvil)')
  action('Face(Smithy,Blacksmith.Anvil)') # Makes Smithy look at the anvil in the Blacksmith's shop

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
  action('CreateCharacter(Cassandra,A)')
  action('SetHairStyle(Cassandra, Long)')
  action('SetEyeColor(Cassandra,blue)')
  action('SetClothing(Cassandra,Noble)')
  action('SetHairColor(Cassandra,blonde)')
  action('SetSkinColor(Cassandra,5)')
  action('SetExpression(Cassandra,neutral)')
  action('SetPosition(Cassandra,Camp.RightLog)')
  action('Sit(Cassandra,Camp.RightLog)')  

# Items
 # Create Items and set their intial positions
# Smithy Sword
  action('CreateItem(Sword,Sword)') # Creates a Sword
  action('SetPosition(Sword,Blacksmith.Anvil)') # Places the Sword on the anvil in Blacksmith's shop

# Smithy Hammer
  action('CreateItem(hammer,Hammer)') # Creates a hammer
  action('SetPosition(hammer,Smithy)') # Sets hammer in Blacksmith's left hand
  
  # Scroll with drawing of Smithy's gem
  action('CreateItem(Scroll,Scroll)')
  action('SetPosition(Scroll,Camp.Barrel)') # Sets scroll on the barrel at the Camp.
