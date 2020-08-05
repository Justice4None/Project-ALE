import pickle

story = {
    1: {
        'Text': [
            "You are on a road, somewhere near the city of Answood.",
            "Next to you is another person, a man. He looks over at you and says, 'You're awake. Good. You've been out cold since we left Emitton.'",
            "You look around and take in your surroundings.",
            "The areas just beyond the road are lightly wooded, and in the distance, to your left (southward), you can see a small lake.",
            "To your right (northward), you can see the very tops of some skyscrapers, looming in the distance.",
            "You look back at the man sitting next to you. He looks over and says, 'Hey, are you okay? You've been awful quiet since we left.'",
            "How do you want to respond?"
        ],
        'Options': [
            ("'Yeah, I'm fine. At least I think I am...'", 2)
        ]
    },
    2: {
        'Text': [
            "The man looks at you.",
            "'Oh, you think? We'll see about that. Can you remember my name?'",
            "How do you want to respond?"
        ],
        'Options': [
            ("'Shawn.'", 2),
            ("'Tyler.'", 3),
            ("'Carl.'", 4),
            ("'Harry.'", 5)
        ]
    },
    3: {
        'Text': [
            "'Wait... so you really don't remember me? Huh. We've been running these logistical missions for wee-'",
            "His words are cut short as a bullet rips through the right side of his head. This man next to you is now dead. The vehicle comes to a gradual stop.",
            "After a brief moment, you look up to the passenger side mirror. You see three people approaching the vehicle slowly, MBR-45 Rifles in hand.",
            "You look down at your hip, you see a combat knife and an PA-410 sidearm.",
            "What do you want to do?",
        ],
        'Options': [
            ("Draw your sidearm and knife and ready yourself to fight.", 2)
        ]
    },
    4: {
        'Text': [
            "The first of the three assailant rounds the passenger-side window, you shoot them through the glass. The bullet enters their forehead and they fall over dead.",
            "The other two start shooting blindly at the cab of the vehicle from behind. You take as much cover as you can, but one round enters your left shoulder. It burns when it enters your body.",
            "Time passes, what seems like 10 minutes but was probably only 15 seconds. The other two rush the door. They pull it open and throw you out of the vehicle.",
            "By the time you hit the ground, you've already drawn your knife. One of the assailants tries to wrestle it away from you.",
            "What do you want to do?",
        ],
        'Options': [
            ("Stab him in the gut.", 2)
        ]
    },
    5: {
        'Text': [
            "The person on top of you fumbles, and you guide the knife into their belly. You can feel them tense up before falling limp on top of you.",
            "The third assailant walks over, rifle leveled at your head. They're about to pull the trigger when they hesitate.",
            "They reach their left hand up to their ear, and say, 'One enemy down, one wounded. Two friendly KIAs. I'm all that's left, sir.'",
            "A few seconds pass before the assailant says, 'Understood.'",
            "They flip their rifle and smash you in the head with it's stock, knocking you unconsious."
        ]
    }
}

with open('chapter1.ch', 'wb') as chapter:
    pickle.dump(story, chapter)
