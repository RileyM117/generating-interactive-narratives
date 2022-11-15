# Protagonist house (camp) scene

#customize camera and sounds and time of day
def Protag_house_setup():
  action('Enter(Smithy,Camp.Exit)')
  action('Face(Smithy,Protag)')
  action('WalkTo(Smithy,Protag)')
  action('WalkTo(Protag,Camp.Log)') # Makes protag stand up
  action('Face(Protag,Smithy)')
  action('SetNarration("Smithy: Protag! my gem has been stolen! Please help me!")')
  action('SetNarration("Protag: Calm down! When was it stolen?")')
  action('SetNarration("Smithy: It was in my chest in the shop just last night.")')
