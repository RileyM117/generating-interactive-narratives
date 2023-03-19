import tkinter as tk
from tkinter import simpledialog
import openai
import os

print("start ShowMenu()",flush=True)

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
# Set up a small house with a door.
action('CreatePlace(Camp, Camp)')
action('CreateCharacter(Bob, B)')
action('SetClothing(Bob, Peasant)')
action('SetPosition(Bob, Camp)')
action('CreateCharacter(Jim, B)')
action('SetClothing(Jim, Peasant)')
action('SetPosition(Jim, Camp.LeftLog)')
action('EnableIcon("Talk to", Talk, Jim, "Talk to")')
action('ShowMenu()')

# Respond to input.
while(True):
  conversations= []
  i = input()
  if(i == 'input Selected Start'):
   action('SetCameraFocus(Bob)')
   action('HideMenu()')
   action('EnableInput()')
   action('EnableInput()')
  if(i == 'input Talk to Jim'):
    ROOT = tk.Tk()
    ROOT.withdraw()
    USER_INP = simpledialog.askstring(title="Test", prompt="What's your Name?:")
    conversations.append(USER_INP)
    print("Hello", USER_INP)
    file_path = "C:/Users/Alex/file.txt"
    user_input = input()
    contents = ''
    with open(file_path, "w") as file:
      file.write(user_input)
    with open(file_path, "r") as file:
      contents = file.read()
    #action('SetDialogue(contents)') 
    #action('ShowDialogue()')
    
    # %%capture gpt_output --no-stderr
    openai.api_key = os.getenv("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")
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "user", "content": conversations + " respond angrily to this."}
        ]
    )
    story = completion.choices[0].message.content
    action("SetDialog({})".format(story))
    action("ShowDialog()")
