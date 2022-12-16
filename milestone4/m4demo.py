import time

# Simple command function probably needs wait param

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


# Create Characters,items,locations, and set initial positions.
#Locations
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


# Protagonist house (camp) scene setup
action('SetCameraFocus(Protag)')
action('Enter(Smithy,Camp.Exit,True)')
action('Face(Smithy,Protag)')
action('WalkTo(Cassandra,Camp.RightLog)')
action('WalkTo(Louis,Camp.LeftLog)')
action('WalkTo(Clark,Louis)')

#Menu
action('SetTitle("Interactive Narrative Demo')
print('start ShowMenu()', flush=True)
action('EnableInput()')

# Protagonist house (camp) scene
while(True):
      i=input()
      if(i == 'input Selected Start'):
            action('HideMenu()')
            action('FadeIn()')
            action('WalkTo(Smithy,Cassandra)')
            action('WalkTo(Protag,Camp.Log)')
            action('Face(Cassandra,Smithy)')
            action('Face(Louis,Smithy)')
            action('Face(Clark,Smithy)')
            action('SetLeft(Smithy)')
            action('SetRight(Protag)')
            action('ShowDialog()')
            action('SetDialog("My gem has been stolen! Please help me!")')
            action('SetDialog("[Stolen?|Stolen?]"')
      if(i == 'input Selected Stolen?'):
            action('SetDialog("It was in my chest in the shop just last night.")')
            time.sleep(2)
            action('ClearDialog')
            action('SetRight(Cassandra)')
            action('SetDialog("Cassandra:Were there any signs of a break in last night?")')
            time.sleep(2)
            action('SetDialog("Smithy: No, none at all!")')
            time.sleep(2)
            action('SetDialog("Cassandra: Who came into your shop today?")')
            time.sleep(2)
            action('SetExpression(Smithy,sad)')
            action('SetDialog("Smithy: I didnt have any customers today.")')
            time.sleep(2)
            action('SetDialog("Cassandra: We will find it for you.")')
            time.sleep(2)
            action('SetDialog("Smithy: Thank you Cassandra. I owe you.")')
            time.sleep(2)
            action('HideDialog')
            action('Exit(Smithy,Camp.Exit)')
            action('SetLeft(Cassandra)')
            action('SetRight(Protag)')
            action('SetDialog("Cassandra: Get ready. Youll be setting out to retrieve it soon.')
            action('SetDialog([Understood.|Understood.]')
            action('ShowDialog()')
      if(i == 'input Selected Understood.'):
            action('HideDialog()')
            action('WalkTo(Louis,Camp.LeftLog)')
            action('Sit(Louis,Camp.LeftLog)')
            action('WalkTo(Clark,Camp.Barrel)')
            action('EnableIcon(Talk, Talk, Louis, Talk to Louis, true)')
            action('EnableIcon(Talk, Talk, Clark, Talk to Clark, true)')
            action('EnableIcon(Talk, Talk, Cassandra, Talk to Cassandra, true)')
      if (i== 'input Talk Clark'):
            action('ClearDialog()')
            action('SetLeft(Clark)')
            action('SetRight(Protag)')
            action('SetDialog("Clark: Hmph. Lets get this over with.")')
            action('SetDialog("[Nice attitude.|Nice attitude.]")')
            action('ShowDialog()')
      if (i== 'input Selected Nice attitude.'):
            action('HideDialog()')
      if (i== 'input Talk Louis'):
            action('ClearDialog()')
            action('SetLeft(Louis)')
            action('SetRight(Protag)')
            action('SetDialog("Louis: This should be easy!")')
            action('SetDialog("[I hope so.|I hope so.]")')
            action('ShowDialog()')
      if (i== 'input Selected I hope so.'):
            action('HideDialog()')
      if (i== 'input Talk Cassandra'):
            action('ClearDialog()')
            action('SetLeft(Cassandra)')
            action('SetRight(Protag)')
            action('SetDialog("Cassandra: The blacksmith is a close friend of mine.")')
            action('SetDialog("Cassandra: I appreciate the help.")')
            action('SetDialog("[Of course.|Of course.]")')
            action('ShowDialog()')
      if (i== 'input Selected Of course.'):
            action('HideDialog()')
time.sleep(20)
            
            
            

'''

action('HideNarration()')
action('Exit(Smithy,Camp.Exit)')
action('Enter(Smithy,Blacksmith.Door)')
action('ShowNarration()')
action('SetNarration("Cassandra: You three! Get off your asses and get ready to set out tomorrow!")')
time.sleep(5)
action('SetNarration("Clark: Cant we let the castle guards handle this? This sounds like so much effort for one little rock.")')  # Clark is apathetic but not the thief
time.sleep(5)
action('SetNarration("Louis: Dont be difficult Clark. The man needs help and the castle guards are useless.")') #Louis is good but thief
time.sleep(5)
action('SetNarration("Clark: Fine.")')
time.sleep(3)
action('HideNarration()')
  # end day, possibly FadeOut()?
action('FadeOut()')
  
  # next day, possibly fadein()
action('WalkTo(Cassandra,Camp.Exit)')
action('FadeIn()')
action('Face(Protag,Cassandra)')
action('Face(Cassandra,Clark)')
action('ShowNarration()')
action('SetNarration("Cassandra: I am heading to town to check for clues at the Blacksmiths shop. You three get up and start looking for that gem. Now.")')
time.sleep(5)
action('SetNarration("Clark: Sending us to do the hard work?")')
time.sleep(5)
action('SetNarration("Louis: Just do what she says Clark, we will find the gem Cassandra.")')
time.sleep(5)
action('HideNarration()')
action('Exit(Cassandra,Camp.Exit)')
action('Enter(Cassandra,Blacksmith.Door)')
action('EnableInput()')
action('EnableIcon(Pick up, Pickup, Scroll, Pickup, true)') # make character grab based on input
action('Pickup(Protag,Scroll,Camp.Barrel)')
action('ShowNarration()')
action('SetNarration("Protag: Hey guys! What is this scroll doing here. There is a picture of a gem on it, I assume its the Blacksmiths.")')
time.sleep(5)
action('DisableInput()')
action('SetNarration("Louis: Oh yeah, he gave me a drawing of the gem before he left last night.")')
time.sleep(5)
action('SetNarration(Protag: I dont remember that, when did that happen?")')
time.sleep(5)
action('HideNarration()')
action('Pocket(Protag,Scroll)')
action('ShowNarration()')
action('SetNarration(Clark: Who cares, at least we have something to go on now.")')
time.sleep(5)
action('SetNarration("Louis: Come on, lets get moving.")')
time.sleep(5)
action('HideNarration()')
action('Exit(Louis,Camp.Exit)')
action('Exit(Clark,Camp.Exit)')
action('Exit(Protag,Camp.Exit,True)')
action('FadeOut()')
time.sleep(5)
'''
