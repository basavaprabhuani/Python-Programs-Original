from spellchecker import SpellChecker
from tkinter import *
import time 

window = Tk()
window.title("Typing Practice")
typing_label = Label(text="Start Typing:")
typing_space = Text(width=25, height=10)
typing_label.grid(row=1, column=1)
typing_space.grid(row=1, column=2)
checker = SpellChecker()

checker.word_frequency.load_words(["asdf", ";lkj", "lkj" ])
checker.word_frequency.remove_words(["all", "lke", "adds", "ads", "aids", "ands", "and", "da"])
mistakes_words = []
mistakes = 0

result_var = StringVar()
result_label = Label(textvariable=result_var)
result_label.grid(row=3, column=2)


def check_function():
    global mistakes  # Declare mistakes as a global variable
    typing = typing_space.get("1.0", END)  # Retrieve content from Text widget
    words = checker.split_words(typing)
    mistakes_words.clear()  # Clear the mistakes list
    mistakes = 0  # Reset the mistakes count
    
    for word in words:
        if checker[word] == 0:
            mistakes += 1
            mistakes_words.append(word)
    
    result_var.set(f"Number of Mistakes: {mistakes} \n\n\n\nThe mistakes are: {', '.join(mistakes_words)}")
    
    if mistakes == 0:
        result_var.set(f"Number of Mistakes: {mistakes} \nThere are no mistakes")

check = Button(text="Check", width=10, height=3, command=check_function)
check.grid(row=2, column=2)

window.mainloop()
time.sleep(10000)