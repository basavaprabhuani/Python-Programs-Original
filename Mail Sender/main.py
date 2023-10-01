REPLACER = "[name]"

with open("names.txt") as names_file:
    name = names_file.readlines()

with open("letter.txt") as letter:
    letter_c = letter.read()

    for names in name:

        stripped_name = names.strip()
        new_letter = letter_c.replace(REPLACER, stripped_name)

        with open(f"Letter_for_{stripped_name}.txt", mode="w") as completter:
            completter.write(new_letter)
