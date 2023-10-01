import tkinter
import pandas as pd
from prettytable import PrettyTable

window = tkinter.Tk(screenName="Calculation")
window.configure(bg="orange", background="#87CEEB")

event_text = tkinter.Label(text="Enter where you spent money: ", font="italic", background="#87CEEB")
event_text.grid(column=1, row=1)

amount_text = tkinter.Label(text="How much did you spend:", font="italic", background="#87CEEB", anchor="e")
amount_text.grid(column=1, row=2)

event = tkinter.Entry()
event.grid(column=2, row=1)

amount_spent = tkinter.Entry()
amount_spent.grid(column=2, row=2)

events = []
amount = []

def add_items():
    eventa = event.get()
    amounta = amount_spent.get()
    events.append(eventa)
    amount.append(amounta)
    event.delete(0, tkinter.END)
    amount_spent.delete(0, tkinter.END)

def finished():
    total = 0
    for i in amount:
        i = int(i)
        total += i
    
    events.append("___________\nTOTAL")
    amount.append(f"___________\n{total}")      
    global dataframe
    dataframe = pd.DataFrame({
        "Events": events,
        "Amount Spent": amount,
    })

    # Create a PrettyTable
    table = PrettyTable()
    table.field_names = ["Events", "Amount Spent"]

    # Add data to the PrettyTable
    for i in range(len(dataframe)):
        table.add_row([dataframe.iloc[i]["Events"], dataframe.iloc[i]["Amount Spent"]])

    # Print or do whatever you want with the PrettyTable
    print(table)
    
add = tkinter.Button(text="Add", command=add_items)
add.grid(column=2, row=3)

finish = tkinter.Button(text="finish", command=finished)
finish.grid(column=2, row=4)


# Start the tkinter event loop
window.mainloop()
