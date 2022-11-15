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
