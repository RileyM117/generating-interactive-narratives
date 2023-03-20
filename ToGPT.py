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
    file_path = "outputc.txt"
    with open(file_path, "w") as file:
      file.write(USER_INP)
    #with open(file_path, "r") as file:
    #  contents = file.read()
    action('SetDialog('+str(USER_INP)+')') 
    action('ShowDialog()')
    
    # %%capture gpt_output --no-stderr
    os.environ["OPENAI_API_KEY"]="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"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "user", "content": "Hello! Testing!"}
        ]
    )
    story = completion.choices[0].message.content
    with open('outputg.txt', 'w') as f:
        f.write(str(story))
        f.close()
    action("SetDialog({})".format(story))
    action("ShowDialog()")
