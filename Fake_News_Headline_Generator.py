# Fake News Headline Generator 

# object , action, place

import random

subjects = [
    "Shahrukh khan",
    "Virat kohli",
    "Nirmala sitaraman",
    "A mumbai Cat",
    "A group of monkey",
    "Prime minister Modi",
    "Auto rikshaw driver from delhi"


]

actions = [
    " launches",
    " cancels",
    " dances with",
    " eats",
    " declares war on",
    " orders",
    " celebrates"

]

places_or_things = [
    " at red fort",
    " in mumbai local train",
    " a plate of samosa",
    " inside parliament",
    " at Ganga ghat",
    " at India gate",
    " during IPL Match"
]


# start the headline generation loop

while   True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)


    headline = f"BREAKING NEWS : { subject}{action}{places_or_thing}"
    print("\n"+ headline)
                                 
    user_input = input("\n Do you want another headline ? (yes / no)").strip().lower()              
    if user_input == "no":
        break

# print goodbye message

print("\n Thanks for using the Fake News Headline Generator. Have a fun day.")
