#TODO: Notebook
#TODO: Final Cutscene
#TODO: Expressions

#Imports:
import tkinter as tk
from tkinter import simpledialog
from ExpoCharacters import char_list
from ExpoCharacters import char_names
from ExpoCharacters import char_expressions
import openai
import os
import time

#OpenAI API Key:
os.environ["OPENAI_API_KEY"] = "sk-"
conversations = []

#Basic Camelot action structure.
def action(command):
    print('start ' + command)
    while (True):
        i = input()
        if (i == 'succeeded ' + command):
            return True
        elif(i == 'failed ' + command):
            return False
        elif(i.startswith('error')):
            return False

#Code that is used to make a call to the GPT API and get a response based on the prompt variable. Takes in prompt and returns GPT response.
def gpt_call(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "user", "content": prompt }
        ]
    )
    comp = completion.choices[0].message.content
    comp = comp.replace('\n', ' ')
    comp = comp.replace('\r', '')
    return(comp)

#Enable icons open icon on doors
def door_icon(door):
    action('EnableIcon("Open Door", Exit,'+door+', "Open Door")')

#Moves the player to provided destination.
def moveTo(destination):
    action("SetPosition({},{})".format(char_names[0],destination))

#Generates all locations and initializes doors
definite_locations = ['Camp','City','AlchemyShop','Blacksmith','GreatHall','Courtyard','Ruins','Tavern','Library']
city_char = False
for i in definite_locations[0:9]:
    action("CreatePlace({},{})".format(i,i))
door_list = ["City.BlueHouseDoor","AlchemyShop.Door","City.RedHouseDoor","Tavern.Door","City.GreenHouseDoor","Library.Door", "City.BrownHouseDoor","Blacksmith.Door"]
for d in door_list:
    door_icon(d)

#First two GPT calls generate a secret story that GPT knows and an introductory narrative for the player.
init_prompt = "These are the characters you can use: " +  ', '.join(char_names[1:-1]) + ". These are the locations you can use: " + ', '.join(definite_locations) + ". Write an unsolved murder set in a medieval/fantasy setting using these characters and locations. Do not include an investigation or an investigator character. The mystery you write is unsolved. "
story = gpt_call(init_prompt)
prompt2 = "This is the initial prompt that I gave you: " + init_prompt + "This is the murder mystery that you wrote: " + story + "Based on this story, provide a very short description to give to the player to initiate their investigation. The player is currently in the forest camp and should seek out other characters to gain clues from. When they want to accuse someone, they should go talk to the king in the Great Hall. Remember that they are trying to solve the murder, so do not give them too many details."
story2 = gpt_call(prompt2).strip()

#Generates our notebook, and a prop for the blacksmith
action("CreateItem(Sword,Sword)")
action("CreateItem(BlueBook,BlueBook)")

#Generates player details
for i in char_list[0:1]:
    action("CreateCharacter({},{})".format(i.name,i.body))
    action("SetEyeColor({},{})".format(i.name,i.eye_color))
    action("SetHairColor({},{})".format(i.name,i.hair_color))
    action("SetHairStyle({},{})".format(i.name,i.hairstyle))
    action("SetSkinColor({},{})".format(i.name,i.skin_color))
    action("SetClothing({},{})".format(i.name,i.outfit))
    action("AddToList(BlueBook,""BlueBook"")")

#Loading mostly complete- show menu.
print("start ShowMenu()",flush=True)

#Things that need to happen after start button is pressed:
while(True):
    conversations = []
    i = input()
    if(i == 'input Selected Start'):
        for i in char_list[0:1]:
            action("SetPosition({},{})".format(i.name,i.location))
        action('EnableIcon("Review Conversations", Research,BlueBook, "Review Conversation",true)')

        action("SetPosition(Sword,Blacksmith.Anvil)")
        action('SetCameraFocus('+char_list[0].name+')')
        action('HideMenu()')
        action("SetNarration(\""+story2+"\")")
        action('ShowNarration()')

#Dialogue code.
    for j in char_list:
        if(i == 'input Talk to '+j.name+''): #For all characters but the king:
            #A dialog box is created asking the user what they would like to say to the character they are interacting with.
            ROOT = tk.Tk()
            ROOT.withdraw()
            if j.name != char_names[3]:
                USER_INP = simpledialog.askstring(title="Test", prompt="What do you Say?:")
                answer = str(USER_INP)
                answer = answer.replace(',','')

                action("SetDialog(\""+char_list[0].name+": " + answer+"\")")
                action("SetLeft(\""+char_list[0].name+"\")")
                action('ShowDialog()')

                #GPT call to generate character's response
                story3 = gpt_call("This is the initial prompt that I gave you: " + init_prompt + "This is the murder mystery that you wrote: " + story + " This is the short description that you provided the player: " + story2 + ". Based on this, the player talks to " + j.name + ". They say " + answer + ". Based on: " + story + " Respond with only the words that " + j.name + " says to the player.")
                story3 = story3.replace('"','')
                action("SetDialog(\""+story3+" [Close|Close]\")")
                action("SetRight(\""+j.name+"\")")

                #GPT call to get character's expression
                expression = gpt_call("This is a line of dialogue: " + story3 + "Would you consider the person who said this to be neutral, happy, sad, angry, disgusted, scared, surprised, or asleep? Respond with only your one word choice. It should be lowercase with no puncuation.")
                action("SetExpression(\""+j.name+"\",\""+expression+"\")")

                action("ShowDialog()")
                conversations.append((char_list[0].name + ":"  + answer, j.name +":" + story3))
            else:
                #Can choose to start accusation process or speak to him like other NPCs.
                action("SetDialog(\"" + j.name + ": Are you here to make an accusation? [Yes|Yes my lord.] [No|No my lord.]"+"\")")
                action("SetRight(\""+j.name+"\")")
                action("SetLeft(\""+char_list[0].name+"\")")
                action("ShowDialog()")
                action("EnableInput()")

#After you accuse someone:
       # if(i == "input Accuse " + j.name + " " + char_name[3]):
        #    action("SetNarration('thank god.')")

#Generates NPCs when the player leaves the camp in order to save on loading time at the beginning.
    if(i == 'input arrived ' + char_list[0].name + ' position Camp.Exit'):
        moveTo("City")
        if city_char == False:
            for i in char_list[1:19]:
                action("CreateCharacter({},{})".format(i.name,i.body))
                action("SetEyeColor({},{})".format(i.name,i.eye_color))
                action("SetHairColor({},{})".format(i.name,i.hair_color))
                action("SetHairStyle({},{})".format(i.name,i.hairstyle))
                action("SetSkinColor({},{})".format(i.name,i.skin_color))
                action("SetClothing({},{})".format(i.name,i.outfit))
                action("SetPosition({},{})".format(i.name,i.location))
                action('EnableIcon("Talk to", Talk,'+i.name+', "Talk to '+i.name+'")')
                city_char = True;


    if(i == 'input Key Inventory'):
        action("ShowList({})".format(char_list[0].name))

    if(i =='input Close List'):
        action("HideList()")

    if(i == 'input Review Conversations BlueBook'):
        action("SetNarration(\""+' '.join(conversations)+"\")")
        action("ShowNarration()")
        
    if(i == 'input Close Narration'):
        action("HideNarration()")
        action("EnableInput()")
        action("EnableInput()")

    if(i == 'input Selected Close'):
        action("HideDialog()")
        action("EnableInput()")


#Beginning of accusation process (what happens when you tell the king you are ready to accuse).
    if i == "input Selected Yes":
        action('SetDialog("Alright. Right click me again to choose the murderer.[Understood|Understood]"')
    if i == "input Selected Understood":
        action('HideDialog()')
        action('DisableIcon("Talk to",' + char_names[3]+')')
        action('EnableIcon("Accuse '+char_names[1]+'", Forge,'+char_names[3]+', Accuse '+char_names[1]+')') #blacksmith
        action('EnableIcon("Accuse '+char_names[2]+'", Potion,'+char_names[3]+', Accuse '+char_names[2]+')') #alchemist
        action('EnableIcon("Accuse '+char_names[3]+'", Throne,'+char_names[3]+', Accuse '+char_names[3]+')') #king
        action('EnableIcon("Accuse '+char_names[4]+'", Crown,'+char_names[3]+', Accuse '+char_names[4]+')') #queen
        action('EnableIcon("Accuse '+char_names[5]+'", Hand,'+char_names[3]+', Accuse '+char_names[5]+')') #city_rando
        action('EnableIcon("Accuse '+char_names[6]+'", Coins,'+char_names[3]+', Accuse '+char_names[6]+')') #noble
        action('EnableIcon("Accuse '+char_names[7]+'", Chest,'+char_names[3]+', Accuse '+char_names[7]+')') #merchant
        action('EnableIcon("Accuse '+char_names[8]+'", Cauldron,'+char_names[3]+', Accuse '+char_names[8]+')') #witch
        action('EnableIcon("Accuse '+char_names[9]+'", Book,'+char_names[3]+', Accuse '+char_names[9]+')') #librarian
        action('EnableIcon("Accuse '+char_names[10]+'", Scroll,'+char_names[3]+', Accuse '+char_names[10]+')') #student
        action('EnableIcon("Accuse '+char_names[11]+'", Mug,'+char_names[3]+', Accuse '+char_names[11]+')') #barkeep
        action('EnableIcon("Accuse '+char_names[12]+'", Flask,'+char_names[3]+', Accuse '+char_names[12]+')') #drunk

#If you say no when the king asks you if you are here to make an accusation, you can talk to him like a normal character.
    if i == "input Selected No":
        USER_INP = simpledialog.askstring(title="Test", prompt="What do you Say?:")
        answer = str(USER_INP)
        answer = answer.replace(',','')

        action("SetDialog(\""+char_list[0].name+answer+"\")")
        action("SetLeft(\""+char_list[0].name+"\")")
        action('ShowDialog()')
        story3 = gpt_call("This is the initial prompt that I gave you: " + init_prompt + "This is the murder mystery that you wrote: " + story + " This is the short description that you provided the player: " + story2 + ". Based on this, the player talks to " + j.name + ". They say " + answer + ". Based on: " + story + " Respond with only the words that " + j.name + " says to the player.")
        story3 = story3.replace('"','')
        action("SetDialog(\""+story3+" [Close|Close]\")")
        action("SetRight(\""+j.name+"\")")
        action("ShowDialog()")
        conversations.append((char_list[0].name + ":"  + answer, j.name +":" + story3))
        
#These if statements tie different parts of the map to different doors.
    if(i == 'input Open Door City.BlueHouseDoor'):
        moveTo("AlchemyShop.Door")
    if(i == 'input Open Door AlchemyShop.Door'):
        moveTo("BlueHouseDoor")
    if(i == 'input Open Door City.GreenHouseDoor'):
        moveTo("Library.Door")
    if(i == 'input Open Door Library.Door'):
        moveTo("City.GreenHouseDoor")
    if(i == 'input Open Door City.BrownHouseDoor'):
        moveTo("Blacksmith.Door")
    if(i == 'input Open Door Blacksmith.Door'):
        moveTo("City.BrownHouseDoor")
    if(i == 'input Open Door City.RedHouseDoor'):
        moveTo("Tavern.Door")
    if(i == 'input Open Door Tavern.Door'):
        moveTo("RedHouseDoor")
    if(i == 'input arrived ' + char_list[0].name + ' position City.EastEnd'):
        moveTo("Camp.Exit")
    if(i == 'input arrived ' + char_list[0].name + ' position City.WestEnd'):
        moveTo("Courtyard.Exit")
    if(i == 'input arrived ' + char_list[0].name + ' position Courtyard.Exit'):
        moveTo("City.WestEnd")
    if(i == 'input arrived ' + char_list[0].name + ' position Courtyard.Gate'):
        moveTo("GreatHall.Gate")
    if(i == 'input arrived ' + char_list[0].name + ' position GreatHall.Gate'):
        moveTo("Courtyard.Gate")
    if(i == 'input arrived ' + char_list[0].name + ' position City.NorthEnd'):
        moveTo("Ruins.Exit")
    if(i == 'input arrived ' + char_list[0].name + ' position Ruins.Exit'):
        moveTo("City.NorthEnd")
