import random

subject = [
    # Bollywood
    "Shahrukh Khan",
    "Salman Khan",
    "Ranveer Singh",
    "Alia Bhatt",
    "Kangana Ranaut",
    
    # Cricket
    "Virat Kohli",
    "Sachin Tendulkar",
    "MS Dhoni",
    "Rohit Sharma",
    "Ravindra Jadeja",

    # Politics
    "PM Modi",
    "Rahul Gandhi",
    "Aam Aadmi Party",
    "Parliament Speaker",
    "A Rajya Sabha MP",

    # Hollywood
    "Tom Cruise",
    "Will Smith",
    "Robert Downey Jr.",
    "Taylor Swift",
    "Barbie",

    # Funny/Animals
    "A Mumbai cat",
    "A Delhi dog",
    "A Bangalore elephant",
    "A Chennai parrot",
    "An angry pigeon",

    # Vehicles/Random
    "Auto rickshaw",
    "A Mumbai taxi",
    "A self-driving car",
    "AI Robot",
    "A haunted washing machine",
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates",
    "accidentally tweets about",
    "challenges to a duel",
    "starts a podcast with",
    "buys 1000 shares of",
    "mistakes as their twin",
    "sues",
    "investigates",
    "breaks up with",
]

places_or_things = [
    # Places
    "at Red Fort",
    "in Mumbai Local Train",
    "inside Parliament",
    "at India Gate",
    "on the moon",
    "during IPL Match",
    "at Ganga Ghat",
    "at a Goa beach",
    "on top of Burj Khalifa",
    "inside a submarine",

    # Things
    "a plate of samosa",
    "a UFO",
    "a haunted mirror",
    "a ghost named Bhootnath",
    "a 90s Nokia phone",
    "a cricket bat signed by Sachin",
    "a toaster that talks",
    "a TikTok dance trend",
    "a broken Jio SIM card",
    "a spicy biryani challenge"
]

while True:
    selected_subject = random.choice(subject)
    selected_action = random.choice(actions)
    selected_place_or_thing = random.choice(places_or_things)

    headline = f"\n📰 Breaking News: {selected_subject} {selected_action} {selected_place_or_thing}"
    print(headline)

    user_input = input("\nDo you want to generate another headline? (yes/no): ").strip().lower()
    if user_input == 'no':
        print("\nThank you for using the Fake Headline Generator! Stay curious 🤪")
        break
    