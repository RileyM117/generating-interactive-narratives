# Creation of characters, items, places, etc... as objects

# atttributes in the format: name, body type, hairstyle, outfit, hair color, eye color, skin color.
protag = CreateCharacter('Protag','B','Spiky','LightArmour','red','blue',5).get() 
smithy = CreateCharacter('Smithy','F', 'Short_Full', 'Peasant','black','brown',3).get()
louis = CreateCharacter('Louis', 'D', 'Long', 'Merchant', 'black', 'green', 1).get()
clark = CreateCharacter('Clark', 'H', 'Musketeer', 'Bandit', 'black', 'brown',1).get()
cassandra = CreateCharacter('Cassandra', 'A', 'Long', 'Noble', 'blonde', 'blue', 5).get()
witch = CreateCharacter('Witch', 'G', 'Short', 'Witch', 'black', 'green', 3).get()

blacksmith = CreatePlace('Blacksmith','Blacksmith').get()
camp = CreatePlace('Camp','Camp').get()
forest_path = CreatePlace('ForestPath','ForestPath').get()
ruins = CreatePlace('Ruins','Ruins')

sword = CreateItem('Sword','Sword').get()
hammer = CreateItem('hammer', 'Hammer').get()
gem = CreateItem('gem','JewelKey').get()

char_list = [protag,smithy,louis,clark,cassandra,witch]
place_list = [blacksmith,camp,forest_path,ruins]
item_list = [sword,hammer,gem]
