#TODO: Notebook
#TODO: Final Cutscene
#TODO: Fix Expressions

#Imports:
import tkinter as tk
from tkinter import simpledialog
from ExpoCharacters import char_list
from ExpoCharacters import char_names
from ExpoCharacters import gpt_char_list
import openai
import backoff
import os
import time

#OpenAI API Key:
os.environ["OPENAI_API_KEY"] = "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"

#Initialization
conversations = []
player = char_list[0].name
king = char_list[3].name

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
@backoff.on_exception(backoff.constant, openai.error.RateLimitError, jitter=None, interval=0.01) #prevents crashes from rate limiting by automatically retrying
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
    comp = comp.strip()
    return(comp)

#Enable icons open icon on doors
def door_icon(door):
    action('EnableIcon("Open Door", Exit,'+door+', "Open Door", True)')

#Moves the player to provided destination.
def moveTo(destination):
    action("SetPosition({},{})".format(char_names[0],destination))

#Generates all locations and initializes doors
definite_locations = ['Camp','City','AlchemyShop','Blacksmith','GreatHall','Courtyard','Ruins','Tavern','Library']
city_char = False
for i in definite_locations[0:9]:
    action("CreatePlace({},{})".format(i,i))
door_list = ["City.BlueHouseDoor","AlchemyShop.Door","City.RedHouseDoor","Tavern.Door","City.GreenHouseDoor","Library.Door", "City.BrownHouseDoor","Blacksmith.Door","Courtyard.Gate","GreatHall.Gate"]
for d in door_list:
    door_icon(d)

#First two GPT calls generate a secret story that GPT knows and an introductory narrative for the player.
init_prompt = "These are the characters you can use: " +  ', '.join(gpt_char_list[1:]) + ". These are the locations you can use: " + ', '.join(definite_locations) + ". Write an unsolved murder mystery set in a medieval/fantasy setting using these characters and locations. Do not include an investigation or an investigator character. The murder should remain unsolved, but you should know who the murderer is."
story = gpt_call(init_prompt)
prompt2 = "This is the initial prompt that I gave you: " + init_prompt + "This is the murder mystery that you wrote: " + story + "Based on this story, provide a very short description to give to the player to initiate their investigation. The player is currently in the forest camp and should seek out other characters to gain clues from. When they want to accuse someone, they should go talk to the king in the Great Hall. Tell the player all of this in a short description that doesn't give away the mystery. Respond only with the description."
story2 = gpt_call(prompt2)

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
    i = input()
    if(i == 'input Selected Start'):
        for i in char_list[0:1]:
            action("SetPosition({},{})".format(i.name,i.location))
        action('EnableIcon("Review Conversations", Research,BlueBook, "Review Conversation",true)')
        action("SetPosition(Sword,Blacksmith.Anvil)")
        action('SetCameraFocus('+player+')')
        action("EnableInput()")
        action('HideMenu()')
        action("SetNarration(\""+story2+"\")")
        action('ShowNarration()')

#Dialogue code.
    for j in char_list:
        if(i == 'input Talk to ' + j.name): #For all characters but the king:
            #A dialog box is created asking the user what they would like to say to the character they are interacting with.
            ROOT = tk.Tk()
            ROOT.withdraw()
            if j.name != king:
                action("DisableInput()")
                USER_INP = simpledialog.askstring(title="Response", prompt="What do you Say?:\t\t\t")
                answer = str(USER_INP)
                answer = answer.replace(',','')

                action("SetDialog(\""+player+": " + answer+"\")")
                action("SetLeft(\""+player+"\")")
                action('ShowDialog()')

                #GPT call to generate character's response
                story3 = gpt_call("This is the initial prompt that I gave you: " + init_prompt + "This is the murder mystery that you wrote: " + story + ". Based on this, the player talks to " + j.name + ", the " + j.role + ". They say " + answer + ". Respond with only the words that " + j.name + " says to the player.")
                expression = gpt_call("This is a line of dialogue: " + story3 + "Would you consider the person who said this to be neutral, happy, sad, angry, disgusted, scared, surprised, or asleep? Respond with only your one word choice. It should be lowercase with no puncuation.")
                story3 = story3.replace('"','')
                expression = expression.replace('"', '')
                action("SetExpression(\""+j.name+"\",\""+expression+"\")")
                action("SetDialog(\""+j.name+": "+story3+" [Close|Close]\")")
                action("SetRight(\""+j.name+"\")")
                action("ShowDialog()")

                conversations.append(player + ": " + answer)
                conversations.append(j.name + ": " + story3)
            else:
                #Can choose to start accusation process or speak to him like other NPCs.
                action("SetDialog(\"" + king + ": Are you here to make an accusation? [Yes|Yes my lord.] [No|No my lord.]"+"\")")
                action("SetRight(\""+king+"\")")
                action("SetLeft(\""+player+"\")")
                action("ShowDialog()")
        
    #After you accuse someone:
        if(i == "input Accuse " + j.name + " " + king):
            accused = j
            action("FadeOut()")
            action("HideDialog()")
            action("ClearDialog()")
            action("SetRight(null)")
            action("SetLeft(null)")
            action("DisableInput()")
            action("SetPosition("+j.name+",GreatHall.Supplicant)")
            action("SetPosition("+char_names[0]+",GreatHall.LeftSupplicant)")
            action("Face("+player+",GreatHall.RightThrone)")
            action("FadeIn()")
            accuse = gpt_call("This is the initial prompt that I gave you: " + init_prompt + "This is the murder mystery that you wrote: " + story + " The player has accused " + accused.name + ", the " + accused.role + ", to the King, and that character is about to be put into jail. Respond with only the words that the king, " + king + ", says to the accused. The King believes the player no matter what and will put "+accused.name+" in jail even if they are innocent.")
            accuse = accuse.replace('"','')
            action("SetDialog(\""+king+": "+accuse+" [Next|Next]\")")
            action("SetLeft(\""+king+"\")")
            action("ShowDialog()")

#If you say no when the king asks you if you are here to make an accusation, you can talk to him like a normal character.
    if i == "input Selected No":
        action("SetDialog(\""+player+": No my lord."+"\")")

        USER_INP = simpledialog.askstring(title="Response", prompt="What do you Say?:")
        answer = str(USER_INP)
        answer = answer.replace(',','')
        action("SetDialog(\""+player+": " + answer+"\")")
        action("SetLeft(\""+player+"\")")
        action('ShowDialog()')

        story3 = gpt_call("This is the initial prompt that I gave you: " + init_prompt + "This is the murder mystery that you wrote: " + story + " Based on this, the player talks to " + king + ", the king. They say " + answer + " Respond with only the words that the king says to the player.")
        story3 = story3.replace('"','')
        action("SetDialog(\""+king+": "+story3+" [Close|Close]\")")
        action("SetRight(\""+king+"\")")
        action("ShowDialog()")

        conversations.append(player + ": " + answer)
        conversations.append(king + ": " + story3)

#Beginning of accusation process (what happens when you tell the king you are ready to accuse).
    if i == "input Selected Yes":
        action("SetDialog(\""+player+": Yes my lord."+"\")")
        action('SetDialog("Alright. Right click me again to choose the murderer. [Understood|Understood]"')

    if i == "input Selected Understood":
        action('HideDialog()')
        action('EnableInput()')
        action('DisableIcon("Talk to",' + king+')')
        action('EnableIcon("Accuse '+char_names[1]+'", Forge,'+king+', Accuse '+char_names[1]+')') #blacksmith
        action('EnableIcon("Accuse '+char_names[2]+'", Potion,'+king+', Accuse '+char_names[2]+')') #alchemist
        action('EnableIcon("Accuse '+char_names[3]+'", Throne,'+king+', Accuse '+char_names[3]+')') #king
        action('EnableIcon("Accuse '+char_names[4]+'", Crown,'+king+', Accuse '+char_names[4]+')') #queen
        action('EnableIcon("Accuse '+char_names[5]+'", Hand,'+king+', Accuse '+char_names[5]+')') #city_rando
        action('EnableIcon("Accuse '+char_names[6]+'", Coins,'+king+', Accuse '+char_names[6]+')') #noble
        action('EnableIcon("Accuse '+char_names[7]+'", Chest,'+king+', Accuse '+char_names[7]+')') #merchant
        action('EnableIcon("Accuse '+char_names[8]+'", Cauldron,'+king+', Accuse '+char_names[8]+')') #witch
        action('EnableIcon("Accuse '+char_names[9]+'", Book,'+king+', Accuse '+char_names[9]+')') #librarian
        action('EnableIcon("Accuse '+char_names[10]+'", Scroll,'+king+', Accuse '+char_names[10]+')') #student
        action('EnableIcon("Accuse '+char_names[11]+'", Mug,'+king+', Accuse '+char_names[11]+')') #barkeep
        action('EnableIcon("Accuse '+char_names[12]+'", Flask,'+king+', Accuse '+char_names[12]+')') #drunk

    if(i == 'input arrived ' + player + ' position Camp.Exit'):
        moveTo("City")

    if(i == 'input Key Inventory'):
        action("ShowList({})".format(player))

    if(i == 'input Close List'):
        action("HideList()")

    if(i == 'input Review Conversations BlueBook'):
        action("SetNarration(\""+' '.join(conversations)+"\")")
        action("ShowNarration()")
        
    if(i == 'input Close Narration'):
        action("HideNarration()")
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

    if(i == 'input Selected Close'):
        action("HideDialog()")
        action("ClearDialog()")
        action("SetRight(null)")
        action("SetLeft(null)")
        action("EnableInput()")
        action("EnableInput()")
        
    if(i == 'input Selected Next'):
        accused_response = gpt_call("This is the initial prompt that I gave you: " + init_prompt + "This is the murder mystery that you wrote: " + story + " The player has accused " + accused.name + ", the " + accused.role + ", to the King, and that character is about to be put into jail. Respond with only the words that the accused character says before they are sent to jail.")
        accused_response = accused_response.replace('"','')
        action("SetDialog(\""+accused.name+": "+accused_response+" [To Jail|To Jail!]\")")
        action("SetRight("+accused.name+")")
        action("ShowDialog()")

    if(i == 'input Selected To Jail'):
        action("HideDialog()")
        action("ClearDialog()")
        action("SetRight(null)")
        action("SetLeft(null)")
        action("FadeOut()")
        action("CreatePlace(Dungeon,Dungeon")
        moveTo("Dungeon.CellDoor")
        action("SetPosition("+accused.name+",Dungeon.RoundTable)")
        action("Face("+player+","+accused.name+")")
        action("Face("+accused.name+","+player+")")
        correct = gpt_call("This is the initial prompt that I gave you: " + init_prompt + "This is the murder mystery that you wrote: " + story + " The player has accused " + accused.name + " of the crime. Answer /""Yes/"" or /""No/"" only- was the player correct?")
        if("Yes" in correct):
            win = True
            action("FadeIn()")
            confession = gpt_call("This is the initial prompt that I gave you: " + init_prompt + "This is the murder mystery that you wrote: " + story + " The player has correctly accused " + accused.name + ", the " + accused.role + " of the crime. "+accused.name +" is now in jail. Respond with the words of this characters confession to the crime.")
            confession = confession.replace('"','')
            action("SetDialog(\""+accused.name+": "+confession+" [Finish|Finish]\")")
            action("ShowDialog()")
        if("No" in correct):
            win = False
            action("FadeIn()")
            plea = gpt_call("This is the initial prompt that I gave you: " + init_prompt + "This is the murder mystery that you wrote: " + story + " The player has incorrectly accused " + accused.name + ", the " + accused.role + " of the crime. "+accused.name +" is now in jail. Respond with only the words of what this character has to say to the player for throwing them in jail.")
            plea = plea.replace('"','')
            action("SetDialog(\""+accused.name+": "+plea+" [Finish|Finish]\")")
            action("ShowDialog()")
            
    if(i == 'input Selected Finish'):
        action("HideDialog()")
        action("ClearDialog()")
        action("SetRight(null)")
        action("SetLeft(null)")
        action("FadeOut()")
        story = story.replace('"','')
        if win == True:
            action("SetDialog(\"Congratulations! You correctly identified the murderer. After more investigation, you are able to uncover the full story: " + story+"\")")
            action("ShowDialog()")
        if win == False:
            action("SetDialog(\"You were unable to identify the correct murderer. Feeling that something was wrong, the king brought in another investigator who revealed the truth: " +story + "You are placed in jail for your gross incompetence. Better luck next time!\")")
            action("ShowDialog()")
        
        
#These if statements tie different parts of the map to different doors.
    if(i == 'input Open Door City.BlueHouseDoor'):
        moveTo("AlchemyShop.Door")
    if(i == 'input Open Door AlchemyShop.Door'):
        moveTo("City.BlueHouseDoor")
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
        moveTo("City.RedHouseDoor")
    if(i == 'input Open Door Courtyard.Gate'):
        moveTo("GreatHall.Gate")
    if(i == 'input Open Door GreatHall.Gate'):
        moveTo("Courtyard.Gate")
    if(i == 'input arrived ' + player + ' position City.EastEnd'):
        moveTo("Camp.Exit")
    if(i == 'input arrived ' + player + ' position City.WestEnd'):
        moveTo("Courtyard.Exit")
    if(i == 'input arrived ' + player + ' position Courtyard.Exit'):
        moveTo("City.WestEnd")
    if(i == 'input arrived ' + player + ' position City.NorthEnd'):
        moveTo("Ruins.Exit")
    if(i == 'input arrived ' + player + ' position Ruins.Exit'):
        moveTo("City.NorthEnd")
