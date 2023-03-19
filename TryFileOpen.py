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
action('EnableIcon("Talk to",talk Jim, "Talk to", true)')
action('CreateCharacter(Jim, B)')
action('SetClothing(Jim, Peasant)')
action('SetPosition(Jim, Camp.LeftLog)')
action('ShowMenu()')

# Respond to input.
while(True):
  i = input()
  if(i == 'input Selected Start'):
   action('SetCameraFocus(Bob)')
   action('HideMenu()')
   action('EnableInput()')
  elif(i == 'input Talk to Jim'):
    file_path = "C:/Users/riley/file.txt"
    user_input = input()
    with open(file_path, "w") as file:
      file.write(user_input)
    with open(file_path, "r") as file:
      contents = file.read()     
