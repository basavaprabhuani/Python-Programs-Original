alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z"]

plain_text = input("Enter the text you want to convert:")
shift = int(input("Enter the shift"))


def encode(text, shift):
    caesar_text = []


    for letter in plain_text:
        position = alphabets.index(letter)
        new_position = position + shift
        new_letter = alphabets[new_position]
        caesar_text += new_letter
    print(caesar_text)

encode(plain_text, shift)


