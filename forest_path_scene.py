def forest_path_scene():
    action('SetPosition(Protag,ForestPath.DirtPile)')
    action('Face(Protag,Louis)')
    action('SetPosition(Louis,ForestPath.Plant)')
    action('Face(Louis,ForestPath.Plant)')
    action('SetPosition(Clark,ForestPath.Well)')
    action('Face(Clark,Louis)')
    action('SetNarration("Clark: That is clearly Nightivy, not Honeygrass.")')
    action('SetNarration("Louis: Hmm... let me get a closer look.")')
    action('Kneel(Louis)')
    
    action('CreateItem(Scroll,Scroll)')
    action('SetPosition(Scroll,ForestPath.DirtPile)')
    action('Face(Protag,Scroll)')
    action('SetNarration("Oh? That scroll looks rather suspicious...")')
    action('Pickup(Protag,Scroll)')
    action('SetNarration("This is the seal of Anglancia! Why does Louis have this? I had better hang onto it for now...")')
    action('AddToList(Scroll, "A scroll that you took from Louis. It has the seal of an enemy country on it.")')
    
    action('SetNarration("Ugh, I am done with this. It is obviously Nightivy, and we are not eating any. Come on.")')
    action('WalkTo(Clark, ForestPath.WestEnd')
    action('WalkTo(Louis, ForestPath.Plant')
    action('SetNarration("Clark: There are some tracks here. Let us continue.")')
