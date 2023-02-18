#TODO: Create a letter using starting_letter.txt 

with open("./input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

with open("./input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

for name in names:
    striped_name = name.strip()
    with open(f"./Output/ReadyToSend/TO_{striped_name}.txt", mode="w") as file:
        file.write(letter.replace("[name]", striped_name))

