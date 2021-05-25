
#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


def run():

    names_list = []
    with open("./Input/Names/invited_names.txt", mode="r", encoding="utf-8") as names:
        for name in names:
            stripped_name = name.strip()
            names_list.append(stripped_name)
    print(names_list)

    with open("./Input/Letters/starting_letter.txt", mode="r", encoding="utf-8") as outline:
        letter_content = outline.read()
        for the_name in names_list:
            new_letter = letter_content.replace("[name]", the_name)
            with open(f"./Output/ReadyToSend/Letter_To_{the_name.strip()}.txt", mode="w", encoding="utf-8") as l:
                l.write(new_letter)


if __name__ == '__main__':
    run()
