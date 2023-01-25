# Class to define character attributes
class CreateCharacter(object):
  def __init__(self, name, body_type = None, hairstyle = None, outfit = None, hair_color = None, eye_color = None, skin_color = None):
    self.name = name  # name not set to None because it does not have default value
    self.body_type = None if body_type is None else body_type 
    self.hairstyle = None if hairstyle is None else hairstyle  
    self.outfit = None if outfit is None else outfit   
    self.hair_color = None if hair_color is None else hair_color    
    self.eye_color = None if eye_color is None else eye_color    
    self.skin_color = None if skin_color is None else skin_color
  def get(self):
    if self.body_type == None: # setting default body_type
      self.body_type = 'A'  
    if self.hairstyle == None: # default hairstyle
      self.hairstyle = 'bald'
    if self.outfit == None:  # default outfit
      self.outfit = 'naked'
    if self.hair_color == None:  # default hair_color
      self.hair_color = 'black'
    if self.eye_color == None:  # default eye_color
      self.eye_color = 'black' 
    if self.skin_color == None:  # default skin_color
      self.skin_color = 0
    # return attributes in list format
    return [self.name,self.body_type,self.hairstyle,self.outfit,self.hair_color,self.eye_color,self.skin_color] 
