# Blacksmith shop scene
# In this scene, The blacksmith goes to put a Sword in the chest in his shop
# He then notices that his Gem is missing and goes to tell the others.

def blacksmith_scene():
  action('Putdown(Smithy,hammer)')
  action('Pickup(Smithy,Sword)') 
  action('WalkTo(Smithy,Blacksmith.Chest)') 
  action('LookAt(Smithy,Blacksmith.Chest)') 
  action('Open(Smithy,Blacksmith.Chest)')
  action('Put(Smithy,Sword,Blacksmith.Chest)')
  action('SetExpression(Smithy,surprised)')
  action('SetNarration("Smithy: Oh no! My precious gem is gone!")')
  action('SetNarration("Smithy: I have to tell Protag about this!")')
  action('SetExpression(Smithy,angry)')
  action('Exit(Smithy,Blacksmith.Door)')
