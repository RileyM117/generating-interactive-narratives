# Protagonist house (camp) scene
# In this scene, the smithy arrives to tell Cassandra about his missing gem
# This scene provides further setup for the narrative and some characterization.

def Protag_house_setup():
  action('Enter(Smithy,Camp.Exit)')
  action('Face(Smithy,Protag)')
  action('WalkTo(Smithy,Cassandra)') # Smithy walks up to Cassandra
  action('WalkTo(Cassandra,Camp.RightLog)')
  action('WalkTo(Louis,Camp.LeftLog)')
  action('WalkTo(Protag,Camp.Log)') # Makes protag stand up
  action('Face(Cassandra,Smithy)')
  action('Face(Protag,Smithy)')
  action('Face(Louis,Smithy)')
  action('Face(Clark,Smithy)')
  action('SetNarration("Smithy: Cassandra! my gem has been stolen! Please help me!")') # Defines the narrative of the scene.
  action('SetNarration("Protag: Calm down! When was it stolen?")')
  action('SetNarration("Smithy: It was in my chest in the shop just last night.")')
 
  action('SetNarration("Cassandra: Were there any signs of a break in last night?")')
  action('SetNarration("Smithy: No, none at all!")')
  action('SetNarration("Cassandra: Who came into your shop today?")')
  action('SetExpression(Smithy,sad)')
  action('SetNarration("Smithy: I didnt have any customers today.")')
  action('SetNarration("Cassandra: Well, its almost dark out. We will start investigating in the morning.")')
  action('SetNarration("Smithy: Thank you Cassandra. I owe you.")')
  action('Exit(Smithy,Camp.Exit)')
  action('Enter(Smithy,Blacksmith.Door)')
  action('SetNarration("Cassandra: You three! Get off your asses and get ready to set out tomorrow!")')
  action('SetNarration("Clark: Cant we let the castle guards handle this? This sounds like so much effort for one little rock.")')  # Clark is apathetic but not the thief
  action('SetNarration("Louis: Dont be difficult Clark. The man needs help and the castle guards are useless.")') #Louis is good but thief
  action('SetNarration("Clark: Fine.")')
  
  action('WalkTo(Cassandra,Camp.Exit)')
  action('Face(Cassandra,Clark)')
  action('SetNarration("Cassandra: I am heading to town to check for clues at the Blacksmiths shop. You three get up and start looking for that gem. Now.")')
  action('SetNarration("Clark: Sending us to do the hard work?")')
  action('SetNarration("Louis: Just do what she says Clark, we will find the gem Cassandra.")')
  action('Exit(Cassandra,Camp.Exit)')
  action('Enter(Cassandra,Blacksmith.Door)')
  action('EnableInput()') # Enables user input
  action('EnableIcon(Pick up, Pickup, Scroll, Pickup, true)') # Enables Icon that says "Pickup" when hovering over the scroll (Not interactive yet)
  action('Pickup(Protag,Scroll,Camp.Barrel)') 
  action('SetNarration("Protag: Hey guys! What is this scroll doing here. There is a picture of a gem on it, I assume its the Blacksmiths.")')
  action('DisableInput()') # Disables user input
  action('SetNarration("Louis: Oh yeah, he gave me a drawing of the gem before he left last night.")')
  action('SetNarration(Protag: I dont remember that, when did that happen?")')
  action('Pocket(Protag,Scroll)') # Protag puts the scroll away.
  action('SetNarration(Clark: Who cares, at least we have something to go on now.")')
  action('SetNarration("Louis: Come on, lets get moving.")')
  action('Exit(Louis,Camp.Exit)')
  action('Exit(Clark,Camp.Exit)')
  action('Exit(Protag,Camp.Exit)')
  action('Enter(Louis,Camp.Exit)')
  action('Enter(Clark,Camp.Exit)')
  action('Enter(Protag,Camp.Exit)')

