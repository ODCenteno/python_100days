# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt", mode="r", encoding="utf-8") as names:
    names_list = names.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r", encoding='utf-8') as l:
    outline = l.read()
    for name in names_list:
        with open(f'./Output/Secondround/letter_to_{name.strip()}.txt', mode='w', encoding='utf-8') as the_l:
            the_l.write(outline.replace('[name]', name))
