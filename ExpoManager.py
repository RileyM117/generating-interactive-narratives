import tkinter as tk
from tkinter import simpledialog
from ExpoCharacters import char_list
from ExpoCharacters import char_names
import openai
import os
import time

print("start ShowMenu()",flush=True)
conversations = []
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


definite_locations = ['Camp','City','AlchemyShop','Blacksmith','GreatHall','Courtyard','Ruins','Tavern','Library']
city_char = False
init_prompt = "These are the characters you can use: " +  ', '.join(char_names[1:16]) + ". These are the locations you can use: " + ', '.join(definite_locations) + ". Write an unsolved murder set in a medieval/fantasy setting using these characters and locations. Do not include an investigation or an investigator character. The mystery you write is unsolved. "
os.environ["OPENAI_API_KEY"]="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"
openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.ChatCompletion.create(
   model="gpt-3.5-turbo",
   messages=[
   {"role": "user", "content": init_prompt }
   ]
)
story = completion.choices[0].message.content
with open("C:/Users/riley/OneDrive/Desktop/AIOutput.txt", "w") as f:
    response = f.write(story)


openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.ChatCompletion.create(
   model="gpt-3.5-turbo",
   messages=[
   {"role": "user", "content": "This is the initial prompt that I gave you: " + init_prompt + "This is the murder mystery that you wrote: " + story + "Based on this story, provide a very short description to give to the player to initiate their investigation. Remember that they are trying to solve the murder, so do not give them too many details."}
   ]
)
story2 = completion.choices[0].message.content

action("CreatePlace(Camp,Camp)")
action("CreatePlace(City,City)")
action("CreateItem(Sword,Sword)")
action("CreateItem(BlueBook,BlueBook)")

for i in char_list[0:1]:
  action("CreateCharacter({},{})".format(i.name,i.body))
  action("SetEyeColor({},{})".format(i.name,i.eye_color))
  action("SetHairColor({},{})".format(i.name,i.hair_color))
  action("SetHairStyle({},{})".format(i.name,i.hairstyle))
  action("SetSkinColor({},{})".format(i.name,i.skin_color))
  action("SetClothing({},{})".format(i.name,i.outfit))
  action("AddToList(BlueBook,""BlueBook"")")
#for i in char_list[0:1]:
#   action("SetPosition({},{})".format(i.name,i.location))


while(True):
  #conversations = []
  i = input()
  if(i == 'input Selected Start'):
   for i in definite_locations[2:9]:
        action("CreatePlace({},{})".format(i,i))
   #action("CreatePlace(Camp,Camp)")
   #action("CreatePlace(City,City)")
   for i in char_list[0:1]:
      action("SetPosition({},{})".format(i.name,i.location))
   action('EnableIcon("Open Door", Exit,City.BlueHouseDoor, "Open Door")')
   action('EnableIcon("Open Door", Exit,AlchemyShop.Door, "Open Door")')

   action('EnableIcon("Open Door", Exit,City.RedHouseDoor, "Open Door")')
   action('EnableIcon("Open Door", Exit,Tavern.Door, "Open Door")')

   action('EnableIcon("Open Door", Exit,City.GreenHouseDoor, "Open Door")')
   action('EnableIcon("Open Door", Exit,Library.Door, "Open Door")')

   action('EnableIcon("Open Door", Exit,City.BrownHouseDoor, "Open Door")')
   action('EnableIcon("Open Door", Exit,Blacksmith.Door, "Open Door")')

   action('EnableIcon("Review Conversations", Research,BlueBook, "Review Conversation",true)')

   #action('EnableIcon("Review Notes", Research,BlueBook, "Review Notes",true)')
 
   action("SetPosition(Sword,Blacksmith.Anvil)")
   action('SetCameraFocus('+char_list[0].name+')')
   action('HideMenu()')
   #action("SetDialog(\""+story2+"\")")
   #action("ShowDialog()")
   action('EnableInput()')
   action('EnableInput()')

  for j in char_list:
     if(i == 'input Talk to '+j.name+''):
        ROOT = tk.Tk()
        ROOT.withdraw()
        #ask = ("What do you say?")
        #action("SetDialog("+ask+")") 
        #action('ShowDialog()')
        USER_INP = simpledialog.askstring(title="Test", prompt="What do you Say?:")
        answer = str(USER_INP)
        answer = answer.replace(',','')
       
        action("SetDialog("+char_list[0].name+": "+answer+")")
        action("SetLeft(\""+char_list[0].name+"\")")
        action('ShowDialog()')
     
        #

        openai.api_key = os.getenv("OPENAI_API_KEY")
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "user", "content": "This is the initial prompt that I gave you: " + init_prompt + "This is the murder mystery that you wrote: " + story + " This is the short description that you provided the player: " + story2 + ". Based on this, the player talks to " + j.name + ". They say " + answer + ". Based on: " + story + " What does " + j.name + " say in response to the player in a dialogue format?"}
            ]
        )
        story3 = completion.choices[0].message.content
        story3 = story3.replace('"','')
        story3 = story3.replace(',','')
        #conversations.append((char_list[0].name + ":"  + answer, j.name +":" + story3))
        with open("C:/Users/riley/OneDrive/Desktop/AIOutput.txt", "w") as f:
          response = f.write(story)
        #action("SetDialog(\""+story3+"\"[Leave Chat|Leave Chat])")
        action("SetDialog("+story3+"[Respond|Respond] [Leave Chat|Leave Chat])")
        action("SetRight(\""+j.name+"\" )")
        action("ShowDialog()")
        action("EnableInput()")
        
        #time.sleep(7)
        #action("HideDialog()")
        
        #action('EnableInput()')
        #action("EnableInput()")
     
        conversations.append("Player: " + answer)
        conversations.append("NPC: " + story3)
        #for i in conversations:
        #   i = i.replace(',','')
        #   i = i.replace('"','')

  if(i == 'input arrived ' + char_list[0].name + ' position Camp.Exit'): 
     action("SetPosition({},City)".format(char_list[0].name))
     if city_char == False:
        for i in char_list[1:16]:
            action("CreateCharacter({},{})".format(i.name,i.body))
            action("SetEyeColor({},{})".format(i.name,i.eye_color))
            action("SetHairColor({},{})".format(i.name,i.hair_color))
            action("SetHairStyle({},{})".format(i.name,i.hairstyle))
            action("SetSkinColor({},{})".format(i.name,i.skin_color))
            action("SetClothing({},{})".format(i.name,i.outfit))
            action("SetPosition({},{})".format(i.name,i.location))
            action('EnableIcon("Talk to", Talk,'+i.name+', "Talk to")')
            city_char = True;
  if(i == 'input Selected Leave Chat'):
     #action("EnableInput()")
     action("HideDialog()")
  if(i == 'input Selected Respond'):
      ROOT = tk.Tk()
      ROOT.withdraw()
      #ask = ("What do you say?")
      #action("SetDialog("+ask+")") 
      #action('ShowDialog()')
      USER_INP = simpledialog.askstring(title="Test", prompt="What do you Say?:")
      answer = str(USER_INP)
      answer = answer.replace(',','')
      
      action("SetDialog("+char_list[0].name+": "+answer+")")
      action("SetLeft(\""+char_list[0].name+"\")")
      action('ShowDialog()')
     
      

      openai.api_key = os.getenv("OPENAI_API_KEY")
      completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
      {"role": "user", "content": "This is the initial prompt that I gave you: " + init_prompt + "This is the murder mystery that you wrote: " + story + " This is the short description that you provided the player: " + story2 + ". Based on this, the player talks to " + j.name + ". They say " + answer + ". Based on: " + story + " What does " + j.name + " say in response to the player in a dialogue format?"}
          ]
      )
      story3 = completion.choices[0].message.content
      story3 = story3.replace('"','')
      story3 = story3.replace(',','')
      #conversations.append((char_list[0].name + ":"  + answer, j.name +":" + story3))
      with open("C:/Users/riley/OneDrive/Desktop/AIOutput.txt", "w") as f:
        response = f.write(story)
      #action("SetDialog(\""+story3+"\"[Leave Chat|Leave Chat])")
      action("SetDialog("+story3+"[Respond|Respond] [Leave Chat|Leave Chat])")
      action("SetRight(\""+j.name+"\" )")
      action("ShowDialog()")
      action("EnableInput()")
      
      #time.sleep(7)
      #action("HideDialog()")
      
      #action('EnableInput()')
      #action("EnableInput()")
     
      conversations.append("Player: " + answer)
      conversations.append("NPC: " + story3)
  if(i == 'input Key Inventory'):
     action("ShowList({})".format(char_list[0].name))

  if(i =='input Close List'):
     action("HideList()")

  if(i == 'input Review Conversations BlueBook'):
     action("SetNarration(\""+' '.join(conversations)+"\")")
     action("ShowNarration()")
 
  if(i == 'input Close Narration'):
     action("HideNarration()")

  if(i == 'input arrived ' + char_list[0].name + ' position City.EastEnd'):
     action("SetPosition({},Camp.Exit)".format(char_list[0].name))
    
  
  if(i == 'input arrived ' + char_list[0].name + ' position City.WestEnd'):
     action("SetPosition({},Courtyard.Exit)".format(char_list[0].name))
  if(i == 'input arrived ' + char_list[0].name + ' position Courtyard.Exit'):
     action("SetPosition({},City.WestEnd)".format(char_list[0].name))

  if(i == 'input arrived ' + char_list[0].name + ' position Courtyard.Gate'):
     action("SetPosition({},GreatHall.Gate)".format(char_list[0].name))
  if(i == 'input arrived ' + char_list[0].name + ' position GreatHall.Gate'):
     action("SetPosition({},Courtyard.Gate)".format(char_list[0].name))
  
  if(i == 'input arrived ' + char_list[0].name + ' position City.NorthEnd'):
     action("SetPosition({},Ruins.Exit)".format(char_list[0].name))
  if(i == 'input arrived ' + char_list[0].name + ' position Ruins.Exit'):
     action("SetPosition({},City.NorthEnd)".format(char_list[0].name))

# POSSIBLY CHANGE DUNGEON LOCATION. doesnt make much sense to go from northend in city to inside a dungeon?

  if(i == 'input Open Door City.BlueHouseDoor'):
     #action("OpenFurniture({},City.BlueHouseDoor)".format(char_list[0].name))
     action("SetPosition({},AlchemyShop.Door)".format(char_list[0].name))
  if(i == 'input Open Door AlchemyShop.Door'):
     #action("OpenFurniture({},AlchemyShop.Door)".format(char_list[0].name))
     action("SetPosition({},City.BlueHouseDoor)".format(char_list[0].name))

    
  if(i == 'input Open Door City.GreenHouseDoor'):
     #action("OpenFurniture({},City.GreenHouseDoor)".format(char_list[0].name))
     action("SetPosition({},Library.Door)".format(char_list[0].name))
  if(i == 'input Open Door Library.Door'):
    # action("OpenFurniture({},Library.Door)".format(char_list[0].name))
     action("SetPosition({},City.GreenHouseDoor)".format(char_list[0].name))



  if(i == 'input Open Door City.BrownHouseDoor'):
     #action("WalkTo({},City.BrownHouseDoor)".format(char_list[0].name))
     #action("OpenFurniture({},City.BrownHouseDoor)".format(char_list[0].name))
     action("SetPosition({},Blacksmith.Door)".format(char_list[0].name))
  if(i == 'input Open Door Blacksmith.Door'):
    # action("OpenFurniture({},Blacksmith.Door)".format(char_list[0].name))
     action("SetPosition({},City.BrownHouseDoor)".format(char_list[0].name))


  if(i == 'input Open Door City.RedHouseDoor'):
     #action("OpenFurniture({},City.RedHouseDoor)".format(char_list[0].name))
     action("SetPosition({},Tavern.Door)".format(char_list[0].name))
  if(i == 'input Open Door Tavern.Door'):
     #action("OpenFurniture({},Tavern.Door)".format(char_list[0].name))
     action("SetPosition({},City.RedHouseDoor)".format(char_list[0].name))

