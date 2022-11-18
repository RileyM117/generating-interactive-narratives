# Simple command function to communicate with Camelot. Likely needs wait parameter to delay certain actions.

def action(command):
    
      print('start ' + command)
      # Get responses until success or failure response is received from Camelot
      while(True):  
        # Get response from Camelot    
        i = input()
         # Return True if succeeds and False if fails.
        if(i == 'succeeded ' + command):
          return True
        elif(i == 'failed ' + command):
          return False
        elif(i.startswith('error')):
          return False
