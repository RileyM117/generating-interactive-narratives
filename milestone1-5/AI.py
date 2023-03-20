!pip install openai

import openai
import re

# OpenAI API credentials
openai.api_key = "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"
# OpenAI API model
model_engine = "text-davinci-003"
# Model Parameters
prompt = "One day the Smithy was busy forging a sword for the local knight. Once he finished, he went to store his handiwork in his chest for safekeeping until the knight came to visit. But upon opening the chest he found that his prized gem was missing. He exclaimed   Oh no! My precious gem is gone! I have to tell the Cassandra about this!  So the Smithy left his shop to find Cassandra at her camp. after half and hour of running, the Smithy made it to Cassandras camp to find her sitting around a fire along with Louis, Clark, and myself. We heard him running just as he had appeared and we all gawked at him. He ran right up to Cassandra and begged:  Cassandra! my gem has been stolen! Please help me!   Calm down  I said.  When was it stolen?  The Smithy breathily replied  It was in my chest in the shop just last night.   Were there any signs of a break in?  Cassandra inquired.  No, none at all  the Smithy replied. Cassandra asked one last question,   Who came into your shop today?  This seemed to upset the Smithy who answered   I didn t have any customers today.  Cassandra thought for a moment then said  Well, its getting dark out. We will help you find your gem in the morning.   Thank you Cassandra! I owe you.  whimpered the Smithy as he began walking back to his shop. As soon as he left our camp area, Cassandra yelled  You three! Get off your asses and get ready to set out in the morning!  Clark very bravely protested,  Can t we just let the castle guards handle this? This is too much effort for a rock.  Louis chided him,  Don t be difficult Clark. The man needs help and the castle guards are useless.   Fine  replied Clark begrudingly. The four of began preparing our respective inventories and went to sleep. Morning came and Cassandra was waiting as I stepped out of my tent. She turned to me and said   I am heading into town to check for clues at the Blacksmith s. Get Louis and Clark and start looking for clues elsewhere.  As she finished giving me orders, Clark emerged from his tent.  Sending us to do the hard work?  he scolded.  Just do as she says Clark  barked Louis as he emerged from his tent. Cassandra glared at Clark for a moment then set off. I turned to grab my things from behind my tent when I noticed a scroll on the ground. I unraveled it and saw a picture of what I presumed to be the Smithy s gem.  Louis, Clark, what is this scroll doing here? It has a picture of the Smithy s gem on it.  Louis quickly replied,  Ah yes, he gave me a drawing of the game as he was leaving last night.   Oh I didn t even notice him speak to you.  Clark interrupted,  Who cares, at least we have something to go on now.  We left that camp shortly after that conversation and decided to search the forest path leading into town.  That is clearly Nightivy, not Honeygrass.  argued Clark.  Move and let me look for a second.  Louis replied. As he knelt down to inspect the flora, I noticed a scroll fall out of his garb. I thought nothing of it until I recognized the small portion of the seal on it that I could make out. It was the seal of Anglancia. I picked up the scroll and hid it in my satchel.  I am done with this, thats clearly Nightivy so we are not eating it. There are some tracks leading this way. Lets continue.  said Clark. The tracks led to the old ruins outside of the city. The ruins were used long ago to commit sacrifices to gods of harvest. It is commonly avoided for fear of spirits and demons. As we came into full view of the ruins our confusion around the gem s whereabouts disappeared. Finish this story with a plot twist"
temperature = 0.4
max_tokens = 2000
# Story Generation
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
    n=1,
    stop=None,
)

# Extracting the story
story = response.choices[0].text

# Remove whitespace and newlines that are generated
story = re.sub(r"\s+", " ", story).strip()

# Print the story
print(story)

# seperate story into sentences
sentences = story.split(".")
for sentence in sentences:
  sentence = sentence.strip()

# Ideally will tweak AI to generate entire stories that will adapt to user interaction. 
