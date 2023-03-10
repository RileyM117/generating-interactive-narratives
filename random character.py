class RandomCharacter(object):
  male_body_types = ['B','D','F','H']
  female_body_types = ['A','C','E','G']
  eye_colors = ['white', 'black', 'blue', 'red', 'brown', 'green']
  hair_colors = ['gray', 'black', 'brown', 'red', 'blonde']
  skin_colors = [0,1,2,3,4,5,6,7,8,9,10]
  hairstyles = ['Long','Spiky','Short','Short_Beard','Short_Full','bald']
  hairstyles_female = ['Ponytail','Straight']
  hairstyles_male = ['Mage','Mage_Beard','Mage_Full','Musketeer','Musketeer_Beard','Musketeer_Full']
  outfits = ['Bandit','Beggar','HeavyArmour','LightArmour','Merchant','Naked','Noble','Peasant','Priest']
  outfits_female = ['Queen','Witch']
  outfits_male = ['King','Warlock']
  male_names_list = []
  female_names_list = []
  i = 0
  while i < 100:
    male_names_list.append(names.human('male'))
    i = i + 1

  female_names_list = []
  while i < 200:
    female_names_list.append(names.human('female'))
    i = i + 1
  def get_rand_male(self):
    return [random.choice(self.male_names_list),random.choice(self.male_body_types),random.choice(self.eye_colors),random.choice(self.hair_colors),
            random.choice(skin_colors),random.choice(self.hairstyles + self.hairstyles_male),random.choice(self.outfits + self.outfits_male)]
  def get_rand_female(self):
    return [random.choice(self.female_names_list),random.choice(self.female_body_types),random.choice(self.eye_colors),random.choice(self.hair_colors),
            random.choice(skin_colors),random.choice(self.hairstyles + self.hairstyles_female),random.choice(self.outfits + self.outfits_female)]
