#prompting and passing
from sys import argv

script, Pharoah_Yamses_III, Play = argv
prompt = ' '

print(f"Hi {Pharoah_Yamses_III}, I'm the {script} script.")

print("I'd like to ask you a few questions.")
print(f"Do you like me {Pharoah_Yamses_III}?")
likes = input(prompt)
print(f"Where do you live {Pharoah_Yamses_III}?")
lives = input(prompt)

Play = input("What is your favorite Shakespearean play?")

print("What kind computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Trash.
""")