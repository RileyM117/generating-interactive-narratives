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
action('CreatePlace(Blacksmith,Blacksmith)')
action('CreatePlace(Camp,Camp)')
action('CreatePlace(ForestPath,ForestPath)')
action('CreatePlace(Ruins,Ruins)')

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
action('CreateCharacter(Cassandra,A)')
action('SetHairStyle(Cassandra, Long)')
action('SetEyeColor(Cassandra,blue)')
action('SetClothing(Cassandra,Noble)')
action('SetHairColor(Cassandra,blonde)')
action('SetSkinColor(Cassandra,5)')
action('SetExpression(Cassandra,neutral)')
action('SetPosition(Cassandra,Camp.RightLog)')
action('Sit(Cassandra,Camp.RightLog)')

print("start ShowMenu()",flush=True)

  # Witch
action('CreateCharacter(Witch,G)')
action('SetHairStyle(Witch, Short)')
action('SetEyeColor(Witch,green)')
action('SetClothing(Witch,Witch)')
action('SetHairColor(Witch,black)')
action('SetSkinColor(Witch,3)')
action('SetExpression(Witch,neutral)')

# Items

# Smithy Sword
action('CreateItem(Sword,Sword)')
action('SetPosition(Sword,Blacksmith.Anvil)')

# Smithy Hammer
action('CreateItem(hammer,Hammer)')
action('SetPosition(hammer,Smithy)')

#Gem in Ruins
action('CreateItem(gem,JewelKey)')


# Blacksmith shop scene

#customize camera and sounds and time of day
action('SetCameraFocus(Smithy)')
action('HideMenu()')
action('Putdown(Smithy,hammer)')
action('Pickup(Smithy,Sword)')
action('WalkTo(Smithy,Blacksmith.Chest)')
action('LookAt(Smithy,Blacksmith.Chest)')
action('Open(Smithy,Blacksmith.Chest)')
action('Put(Smithy,Sword,Blacksmith.Chest)')
action('SetExpression(Smithy,surprised)')
action('ShowNarration()')
action('SetNarration("Smithy: Oh no! My precious gem is gone!")')
time.sleep(5)
action('SetNarration("Smithy: I have to tell Protag about this!")')
time.sleep(5)
action('HideNarration()')
action('SetExpression(Smithy,angry)')
action('Exit(Smithy,Blacksmith.Door,True)')
action('FadeOut()')
      

# Protagonist house (camp) scene

#customize camera and sounds and time of day
action('SetCameraFocus(Protag)')
action('FadeIn()')
action('Enter(Smithy,Camp.Exit,True)')
action('Face(Smithy,Protag)')
action('WalkTo(Smithy,Cassandra)')
action('WalkTo(Cassandra,Camp.RightLog)')
action('WalkTo(Louis,Camp.LeftLog)')
action('WalkTo(Protag,Camp.Log)') # Makes protag stand up
action('WalkTo(Clark,Louis)')
action('Face(Cassandra,Smithy)')
action('Face(Protag,Smithy)')
action('Face(Louis,Smithy)')
action('Face(Clark,Smithy)')
action('ShowNarration()')
action('SetNarration("Smithy: Cassandra! my gem has been stolen! Please help me!")')
time.sleep(5)
action('SetNarration("Protag: Calm down! When was it stolen?")')
time.sleep(5)
action('SetNarration("Smithy: It was in my chest in the shop just last night.")')
time.sleep(5)
 # action('EnableIcon(talk, talk, Smithy, Talk, true)')  don't know what to do with this yet but it works
 # add fadein and out for changes in day
action('SetNarration("Cassandra: Were there any signs of a break in last night?")')
time.sleep(5)
action('SetNarration("Smithy: No, none at all!")')
time.sleep(5)
action('SetNarration("Cassandra: Who came into your shop today?")')
time.sleep(5)
action('HideNarration()')
action('SetExpression(Smithy,sad)')
time.sleep(3)
action('ShowNarration()')
action('SetNarration("Smithy: I didnt have any customers today.")')
time.sleep(5)
action('SetNarration("Cassandra: Well, its almost dark out. We will start investigating in the morning.")')
time.sleep(5)
action('SetNarration("Smithy: Thank you Cassandra. I owe you.")')
time.sleep(5)
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

action('Enter(Louis,ForestPath.EastEnd)')
action('Enter(Clark,ForestPath.EastEnd)')
action('Enter(Protag,ForestPath.EastEnd)')
action('SetPosition(Protag,ForestPath.DirtPile)')
action('SetPosition(Louis,ForestPath.Plant)')
action('Face(Louis,ForestPath.Plant)')
action('SetPosition(Clark,ForestPath.Well)')
action('Face(Protag,Louis)')
action('FadeIn()')
action('Face(Clark,Louis)')
action('ShowNarration()')
action('SetNarration("Clark: That is clearly Nightivy, not Honeygrass.")')
time.sleep(5)
action('SetNarration("Louis: Hmm... let me get a closer look.")')
time.sleep(5)
action('HideNarration()')
action('Kneel(Louis)')
    
action('CreateItem(Scroll,Scroll)')
action('SetPosition(Scroll,ForestPath.Plant)')
time.sleep(3)
action('ShowNarration()')
action('SetNarration("Oh? That scroll looks rather suspicious...")')
time.sleep(5)
action('HideNarration()')
action('Pickup(Protag,Scroll)')
action('ShowNarration()')
action('SetNarration("This is the seal of Anglancia! Why does Louis have this? I had better hang onto it for now...")')
time.sleep(5)
action('HideNarration()')
action('AddToList(Scroll, "A scroll that you took from Louis. It has the seal of an enemy country on it.")')
    
action('ShowNarration()')
action('SetNarration("Clark: Ugh, I am done with this. It is obviously Nightivy, and we are not eating any. Come on.")')
time.sleep(5)
action('HideNarration()')
action('WalkTo(Clark, ForestPath.WestEnd')
action('WalkTo(Louis, ForestPath.Plant')
action('ShowNarration()')
action('SetNarration("Clark: There are some tracks here. Let us continue.")')
time.sleep(5)
action('HideNarration()')
action('Exit(Louis,ForestPath.WestEnd')
action('Exit(Clark,ForestPath.WestEnd)')
action('Exit(Protag,ForestPath.WestEnd,True)')
action('FadeOut()')

action('SetPosition(Witch,Ruins.Altar.Behind)')
action('SetPosition(gem,Ruins.Altar)')
action('Enter(Protag,Ruins.Exit)')
action('Enter(Louis,Ruins.Exit)')
action('Enter(Clark,Ruins.Exit,True)')
action('Walkto(Protag,Ruins.Altar)')
action('Face(Protag,Witch)')
action('SetPosition(Louis,Ruins.Plant)')
action('Face(Louis,Witch)')
action('SetPosition(Clark,Ruins.DirtPile)')
action('Face(Clark,Witch)')
action('FadeIn()')
action('ShowNarration()')
action('SetNarration("Protag: Stop, Witch! Hand over the gem!")')
time.sleep(5)
action('SetNarration("Witch: Grahaha! This is mine!")')
time.sleep(5)
action('HideNarration()')
action('CreateEffect(Witch,Aura)')
time.sleep(3)
action('ShowNarration()')
action('SetNarration("Clark: She is up to something!")')
time.sleep(5)
action('SetNarration("Protag: Not if I have anything to say about it!")')
time.sleep(5)
action('HideNarration()')
action('SetPosition(Sword,Protag)')
action('Walkto(Protag,Witch)')
action('Attack(Protag,Witch)')
action('Kneel(Witch)')
action('ShowNarration()')
action('SetNarration("Witch: Aaaargh!")')
time.sleep(2)
action('HideNarration()')
action('Die(Witch)')
time.sleep(3)
action('ShowNarration()')
action('SetNarration("Louis: Hah. That is what she deserved!")')
time.sleep(5)
action('SetNarration("He seems way too happy about this...")')
time.sleep(5)
action('HideNarration()')
action('Face(Protag,Gem)')
time.sleep(3)
action('ShowNarration()')
action('SetNarration("Protag: Well, we got what we came for. We can go back now.")')
time.sleep(5)
action('HideNarration()')
action('Face(Protag,Gem)')
action('Pickup(Protag,Gem)')
action('ShowNarration()')
action('SetNarration("Louis: Yeah, we should go. This place gives me the creeps.")')
time.sleep(5)
action('HideNarration()')
action('Exit(Louis,Ruins.Exit')
action('Exit(Clark,Ruins.Exit)')
action('Exit(Protag,Ruins.Exit,True)')
action('FadeOut()')


action('SetPosition(Smithy,Blacksmith.Anvil)')
action('SetPosition(Cassandra,Blacksmith.Target)')
action('SetPosition(Louis,Blacksmith.Table)')
action('SetPosition(Clark,Blacksmith.Chest)')
action('FadeIn()')
action('Enter(Protag,Blacksmith.Door)')
action('ShowNarration()')
action('SetNarration("Smithy: Thank you so much for returning my gem! It is a precious family heirloom to me.")')
time.sleep(5)
action('SetNarration("Louis: Of course, sir. When can we expect our reward?")')
time.sleep(5)
action('SetNarration("Smithy: Wh-what?!")')
time.sleep(5)
action('SetNarration("Cassandra: He is a close personal friend of mine. There is no reward to be had.")')
time.sleep(5)
action('SetNarration("Louis: What?!")')
time.sleep(5)
action('SetNarration("That confirms it...")')
time.sleep(5)
action('HideNarration()')
action('SetPosition(Scroll,Protag)')
action('Walkto(Protag,Cassandra)')
action('Give(Protag,Scroll,Cassandra)')
action('ShowNarration()')
action('SetNarration("Protag: I have reason to believe that Louis is the one who stole the gem in the first place. And now I know why.")')
time.sleep(5)
action('SetNarration("Louis: What are you talking about?! That is ridiculous!")')
time.sleep(5)
action('SetNarration("Protag: I found a scroll with a picture of the gem on it, and he said it was his. He also dropped that scroll, and it has the seal of the enemy on it.")')
time.sleep(7)
action('SetNarration("Protag: He also seemed like he knew the witch beforehand, and was seeking reward...")')
time.sleep(5)
action('SetNarration("Protag: I think he was sent to infiltrate us, and do good turns for us to gain our trust... as well as our money.")')
time.sleep(5)
action('HideNarration()')
action('Face(Protag,Louis)')
action('Face(Blacksmith,Louis)')
action('Face(Clark,Louis)')
action('Face(Cassandra,Louis)')
action('ShowNarration()')
action('SetNarration("Cassandra: Do you have anything to say for yourself? This scroll is pretty incriminating.")')
time.sleep(5)
action('SetNarration("Louis: Ugh...dang...fine. I surrender.")')
time.sleep(5)
action('HideNarration()')
action('Kneel(Louis)')
action('ShowNarration()')
action('SetNarration("Cassandra: Great job, Protag. I dont know what would have happened if you hadnt figured that out!")')
time.sleep(5)
action('SetNarration("The End!")')
time.sleep(20)
action('Fadeout()')




