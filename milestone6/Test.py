import tkinter as tk
from tkinter import simpledialog
from Character import char_list
from Character import char_names
import openai
import os
import time



print("start ShowMenu()",flush=True)
definite_locations = ['AlchemyShop','Blacksmith','Camp','GreatHall','City','Courtyard','Dungeon','Tavern','ForestPath','SpookyPath','Ruins','Library']
init_prompt = "These are the characters you can use: " +  ', '.join(char_names[1:-1]) + ". These are the locations you can use: " + ', '.join(definite_locations) + ". Write an unsolved murder set in a medieval/fantasy setting using these characters and locations. Do not include an investigation or an investigator character. The mystery you write is unsolved. "
# Send a command to Camelot.
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
for i in definite_locations:
  action("CreatePlace({},{})".format(i,i))
for i in char_list:
  action("CreateCharacter({},{})".format(i.name,i.body))
  action("SetEyeColor({},{})".format(i.name,i.eye_color))
  action("SetHairColor({},{})".format(i.name,i.hair_color))
  action("SetHairStyle({},{})".format(i.name,i.hairstyle))
  action("SetSkinColor({},{})".format(i.name,i.skin_color))
  action("SetClothing({},{})".format(i.name,i.outfit))
  action('EnableIcon("Talk to", Talk,'+i.name+', "Talk to")')
for i in char_list:
   action("SetPosition({},{})".format(i.name,i.location))
        
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

os.environ["OPENAI_API_KEY"]="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"
openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.ChatCompletion.create(
   model="gpt-3.5-turbo",
   messages=[
   {"role": "user", "content": "This is the initial prompt that I gave you: " + init_prompt + "This is the murder mystery that you wrote: " + story + "Based on this story, provide a very short description to give to the player to initiate their investigation. Remember that they are trying to solve the murder, so do not give them too many details."}
   ]
)
story2 = completion.choices[0].message.content

# Respond to input.
while(True):
  conversations= []
  i = input()
  if(i == 'input Selected Start'):
   action("Sit({},City.Bench)".format(char_list[6].name))
   action("Face({},City.Fountain)".format(char_list[5].name))
   action('SetCameraFocus('+char_list[0].name+')')
   action('HideMenu()')
   action("SetDialog(\""+story2+"\")")
   action("ShowDialog()")
   action('EnableInput()')
   action('EnableInput()')
   #action("SetDialog(\""+story2+"\")")
   #action("ShowDialog()")
   time.sleep(5)
   action("HideDialog()")
  if(i == 'input arrived ' + char_list[0].name + ' position Camp.Exit'):
     action("SetPosition({},ForestPath)".format(char_list[0].name))
  if(i == 'input arrived ' + char_list[0].name + ' position ForestPath.EastEnd'):
     action("SetPosition({},City.EastEnd)".format(char_list[0].name))
  if(i == 'input arrived ' + char_list[0].name +' position City.NorthEnd'):
     action("SetPosition({},SpookyPath.WestEnd)".format(char_list[0].name))
  for j in char_list:
    if(i == 'input Talk to '+j.name+''):
        ROOT = tk.Tk()
        ROOT.withdraw()
        #ask = ("What do you say?")
        #action("SetDialog("+ask+")") 
        #action('ShowDialog()')
        USER_INP = simpledialog.askstring(title="Test", prompt="What do you Say?:")
        answer = str(USER_INP)
        conversations.append(answer)
        action('SetDialog('+answer+')') 
        action('ShowDialog()')

        os.environ["OPENAI_API_KEY"]="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"
        openai.api_key = os.getenv("OPENAI_API_KEY")
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "user", "content": "This is the initial prompt that I gave you: " + init_prompt + "This is the murder mystery that you wrote: " + story + " This is the short description that you provided the player: " + story2 + ". Based on this, the player talks to " + j.name + ". They say " + answer + ". Based on: " + story + " What does " + j.name + " say in response to the player?"}
            ]
        )
        story3 = completion.choices[0].message.content
        action("SetDialog(\""+story3+"\")")
        action("ShowDialog()")
        time.sleep(12)
        action("HideDialog()")
        action('EnableInput()')
        action("EnableInput()")




        




   
