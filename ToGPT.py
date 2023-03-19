import tkinter as tk
from tkinter import simpledialog

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
    print("Hello", USER_INP)
    file_path = "C:/Users/Alex/file.txt"
    user_input = input()
    contents = ''
    with open(file_path, "w") as file:
      file.write(user_input)
    with open(file_path, "r") as file:
      contents = file.read()
    action('SetDialogue(contents)') 
    action('ShowDialogue()')
