# Class to define character attributes
class Character(object):
    def __init__(self, name, body_type, hairstyle, outfit, hair_color, eye_color, skin_color):
        self.name = name    # Character name
        self.body_type = body_type    # Character body type
        self.hairstyle = hairstyle    # Character hairstyle
        self.outfit = outfit    # Character outfit
        self.hair_color = hair_color    # Character hair color
        self.eye_color = eye_color    # Character eye color
        self.skin_color = skin_color    # Character skin color
    def set_name_body(self):
      return self.entity,self.body_type
    def set_hairstyle(self):
      return self.entity,self.hairstyle
    def set_outfit(self):
      return self.entity,self.outfit
    def set_hair_color(self):
      return self.entity,self.hair_color
    def set_eye_color(self):
      return self.entity,self.eye_color
    def set_skin_color(self):
      return self.entity,self.skin_color
    def __repr__(self):
      # returns character attributes in format: name,body_type,hairstyle,outfit,hair_color,eye_color,skin_color
      return f"{self.name},{self.body_type},{self.hairstyle},{self.outfit},{self.hair_color},{self.eye_color},{self.skin_color}"
