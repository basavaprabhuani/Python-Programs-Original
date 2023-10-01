import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as K
from tkinter import *
from selenium.webdriver.firefox.options import Options
import pyautogui as pg
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import math
import threading
from turtle import Turtle, Screen
def function_window():
    global functionwindow
    functionwindow = Tk()
    
    functionwindow.title("Functions")
    Degreedecimal_to_Degreeminute = Radiobutton(text="Degree in decimals to degree in minutes and seconds", command=degreeto_minutes)
    Degreeminute_to_Degreedecimal = Radiobutton(text="Degree in minutes and seconds to degree in decimals", command=minutes_to_degrees_in_decimals)
    radian_to_Degree = Radiobutton(text="Convert Radians to Degrees", command=rtod)
    degree_toradian = Radiobutton(text="Convert degrees to radians.", command=dtor)
    solve_right_angles = Radiobutton(text="Solve Right Angles", command=solve_right_angled_triangles)
    solve_right_angles.grid(column=0, row=4)
    radian_to_Degree.grid(column=0, row=2)
    degree_toradian.grid(column=0,row=3)
    Degreedecimal_to_Degreeminute.grid(column=0, row=0)
    Degreeminute_to_Degreedecimal.grid(column=0, row=1)
def solve_right_angled_triangles():
    window = Tk()
    window.maxsize
    window.title("Solution for right angles: ")
    messagebox.showinfo(title="Message", message="You only need to enter two values, but both cannot be angles (A and B)")
    a = Label(window, text="a:")
    b = Label(window, text="b:")
    c = Label(window, text="c:")
    A = Label(window, text="A:")
    B = Label(window, text="B:")

    a.grid(column=0, row=0)
    b.grid(column=0, row=1)
    c.grid(column=0, row=2)
    A.grid(column=0, row=3)
    B.grid(column=0, row=4)

    a_entry = Entry(window)
    b_entry = Entry(window)
    c_entry = Entry(window)
    A_entry = Entry(window)
    B_entry = Entry(window)

    a_entry.grid(column=1, row=0)
    b_entry.grid(column=1, row=1)
    c_entry.grid(column=1, row=2)
    A_entry.grid(column=1, row=3)
    B_entry.grid(column=1, row=4)

    def all_functions():
        # def get_values():
        #     global a_value, b_value, c_value, A_value, B_value
        #     a_value = float(a_entry.get())
        #     b_value = float(b_entry.get())
        #     c_value = float(c_entry.get())
        #     A_value = float(A_entry.get())
        #     B_value = float(B_entry.get())

        def calculate():
            
            if a_entry.get() != "" and b_entry.get() != "":
                arctanfind = float(a_entry.get()) / float(b_entry.get())
                A = math.atan(arctanfind)
                c = math.sqrt((float(a_entry.get()) ** 2) + (float(b_entry.get()) ** 2))
                answer = Label(window, text=f"A = {A * (180 / (22 / 7))}, c = {c}, B = {90 - A * (180 / (22 / 7))}")
                answer.grid(column=2, row=0)

            elif a_entry.get() != "" and c_entry.get() != "":
                # Execute code when both conditions are satisfied
                arcsinfind = float(a_entry.get()) / float(c_entry.get())
                A = math.asin(arcsinfind)
                b = math.sqrt((float(c_entry.get()) ** 2) - (float(a_entry.get()) ** 2))
                answer = Label(window, text=f"A = {A * (180 / (22 / 7))}, b = {b}, B = {90 - A * (180 / (22 / 7))}")
                answer.grid(column=2, row=0)

            elif b_entry.get() != "" and c_entry.get() != "":
                # Execute code when both conditions are satisfied
                arccosfind = float(b_entry.get()) / float(c_entry.get())
                Ae = math.acos(arccosfind)
                a = math.sqrt((float(c_entry.get()) ** 2) - (float(b_entry.get()) ** 2))
                answer = Label(window, text=f"A = {Ae * (180 / (22 / 7))}, a = {a}, B = {90 - Ae * (180 / (22 / 7))}")
                answer.grid(column=2, row=0)

            elif a_entry.get() != "" and A_entry.get() != "":
                # Execute code when both conditions are satisfied
                angle_in_radian = math.radians(float(A_entry.get()))
                b = float(a_entry.get()) / (math.tan(angle_in_radian))
                c = math.sqrt((b ** 2) + ((float(a_entry.get())) ** 2))
                answer = Label(window, text=f"side b: {b}, side c: {c}, Angle B: {90 - float(A_entry.get())}")
                answer.grid(column=4, row=1)

            elif a_entry.get() != "" and B_entry.get() != "":
                # Execute code when both conditions are satisfied
                angle_in_radian = math.radians(float(B_entry.get()))
                b = float(a_entry.get()) / (math.tan(angle_in_radian))
                c = math.sqrt((b ** 2) + ((float(a_entry.get())) ** 2))
                answer = Label(window, text=f"side b: {b}, side c: {c}, Angle A: {90 - float(B_entry.get())}")
                answer.grid(column=4, row=1)

            elif b_entry.get() != "" and A_entry.get() != "":
                # Execute code when both conditions are satisfied
                angle_in_radian = math.radians(float(A_entry.get()))
                a = math.tan(angle_in_radian) * float(b_entry.get())
                c = math.sqrt((a ** 2) + ((float(b_entry.get())) ** 2))
                answer = Label(window, text=f"side a: {a}, side c: {c}, Angle B: {90 - float(A_entry.get())}")
                answer.grid(column=4, row=1)

            elif b_entry.get() != "" and B_entry.get() != "":
                # Execute code when both conditions are satisfied
                angle_in_radian = math.radians(float(B_entry.get()))
                a = float(b_entry.get()) / math.tan(angle_in_radian) 
                c = math.sqrt((a ** 2) + ((float(b_entry.get())) ** 2))
                answer = Label(window, text=f"side a: {a}, side c: {c}, Angle A: {90 - float(B_entry.get())}")
                answer.grid(column=4, row=1)

            elif c_entry.get() != "" and A_entry.get() != "":
                # Execute code when both conditions are satisfied
                angle_in_radian = math.radians(float(A_entry.get()))
                a = math.sin(angle_in_radian) * float(c_entry.get())
                c = math.sqrt((float(c_entry.get()) ** 2) - (a ** 2))
                answer = Label(window, text=f"side a: {a}, side b: {c}, Angle B: {90 - float(A_entry.get())}")
                answer.grid(column=4, row=1)

            elif c_entry.get() != "" and B_entry.get() != "":
                # Execute code when both conditions are satisfied
                angle_in_radian = math.radians(float(B_entry.get()))
                a = math.sin(angle_in_radian) * float(c_entry.get())
                c = math.sqrt((float(c_entry.get()) ** 2) - (a ** 2))
                answer = Label(window, text=f"side b: {a}, side a: {c}, Angle B: {90 - float(B_entry.get())}")
                answer.grid(column=4, row=1)

            # if A_entry != "" and B_entry != "":
            #     messagebox.showerror(title="Cannot solve", message="You cannot enter two angles since the answer cannot be found with only two angles. However, you may add an angle and a length of side, else, you have insufficient info and thus cannot solve this. ")


            
        # get_values()
        calculate()

    calculate_button = Button(window, text="Calculate", command=all_functions)
    calculate_button.grid(column=0, row=5)

 

    # if A_entry.get() == "" or B_entry.get() == "" and a_entry.get() == "" or b_entry.get() == "":
    #     messagebox.showerror(title="Insufficient Info", message="An angle must be provided ")
    # else:
    #     pass
def rtod():
    global answer
    radian_window = Tk()
    ask_l = Label(radian_window, text="Enter the measure of the angle in radians: ")
    ask_l.grid(column=0, row=0)
    radian = Entry(radian_window)
    radian.grid(column=0, row=1)

    def calculatea():
        global answer
        measure = float(radian.get())
        answer = round(measure * (180/(22/7)), 3)
        answer_label = Label(radian_window, text=f"Answer is {answer} Degrees")
        trigonometric_function = Label(radian_window, text=f"Values of trigonometric functions are: \n\nSin({answer}): ")
        answer_label.grid(column=2, row=2)
        trigonometric_function.grid(column=0, row=3)

    def all():
        measure = float(radian.get())
        answer = round(measure * (180/(22/7)), 3)
        global answers
        answers = []

        URLA = f"https://www.google.com/search?q=cos{answer}degrees&oq=sin+15&aqs=chrome..69i57j69i59.1949j0j1&sourceid=chrome&ie=UTF-8"
        requests.get(URLA)
        cos = soup.find(name="span", class_="qv3Wpe")
        cosonly = f"cos{answer}: \n{cos}\n"
        answers.append(cosonly)

        URLB = f"https://www.google.com/search?q=sin{answer}degrees&oq=sin+15&aqs=chrome..69i57j69i59.1949j0j1&sourceid=chrome&ie=UTF-8"
        requests.get(URLB)
        sin = soup.find(name="span", class_="qv3Wpe")
        sinonly = f"sin {answer}: \n{sin}\n"
        answers.append(sinonly)

        URLC = f"https://www.google.com/search?q=tan{answer}degrees&oq=sin+15&aqs=chrome..69i57j69i59.1949j0j1&sourceid=chrome&ie=UTF-8"
        requests.get(URLC)
        tan = soup.find(name="span", class_="qv3Wpe")
        tanonly = f"tan {answer}: \n{tan}\n"
        answers.append(tanonly)
        # cot = (f"cot {answer}: \n{1/tanonly}\n")
        # sec = (f"sec {answer}: \n{1/cosonly}\n")
        # csc = (f"csc {answer}: \n{1/sinonly}\n")
        # answers += [cot, sec, csc]
        
        text = Label(text=answers)
        text.grid(column=0, row=5)

    def calculatealla():
        calculatea()
        all()

    calculate_button = Button(radian_window, text="Calculate", command=calculatealla)
    calculate_button.grid(column=1, row=1)
def dtor():
    degree_window = Tk()
    ask = Label(degree_window, text="Enter the measure of the angle in degrees: ")
    ask.grid(column=0, row=0)
    degree = Entry(degree_window)
    degree.grid(column=0, row=1)

    def calculate():
        measure = float(degree.get())
        answer = round(measure * ((22/7)/180), 3)
        answer_window = Label(degree_window, text=f"Answer is: {answer} radians.")
        answer_window.grid(column=0, row=3)
        
    global answers
    answers =  []

    def find_cos():
        global cosonly
        URL = f"https://www.google.com/search?q=cos{answer}degrees&oq=sin+15&aqs=chrome..69i57j69i59.1949j0j1&sourceid=chrome&ie=UTF-8"
        requests.get(URL)
        soup = BeautifulSoup(URL, "html.parser")
        cos = soup.find(name="span", class_="qv3Wpe")
        cosonly = (f"cos{answer}: \n{cos.text}\n")
        answers.append(cosonly)
        
    def find_sin():
        global sinonly
        URL = f"https://www.google.com/search?q=sin{answer}degrees&oq=sin+15&aqs=chrome..69i57j69i59.1949j0j1&sourceid=chrome&ie=UTF-8"
        requests.get(URL)
        soup = BeautifulSoup(URL, "html.parser")
        sin = soup.find(name="span", class_="qv3Wpe")
        sinonly = (f"sin {answer}: \n{sin.text}\n")
        answers.append(sinonly)
        
    def find_tan():
        global tanonly
        URL = f"https://www.google.com/search?q=tan{answer}degrees&oq=sin+15&aqs=chrome..69i57j69i59.1949j0j1&sourceid=chrome&ie=UTF-8"
        requests.get(URL)
        soup = BeautifulSoup(URL, "html.parser")
        tan = soup.find(name="span", class_="qv3Wpe")
        tanonly = (f"tan {answer}: \n{tan.text}\n")
        answers.append(tanonly)

        # cot = (f"cot {answer}: \n{1/tanonly}\n")
        # sec = (f"sec {answer}: \n{1/cosonly}\n")
        # csc = (f"csc {answer}: \n{1/sinonly}\n")
        # answers += [cot, sec, csc]

        text = Label(text=answers)
        text.grid(column=0, row=5)
    global all_functions
    def all_functions():
        calculate()
        find_cos()
        find_sin()
        find_tan()

            
    calculate_button = Button(degree_window, text="Calculate", command=all_functions)
    calculate_button.grid(column=0, row=2)
def degreeto_minutes():
    functionwindow.destroy()
    global first_window
    first_window = Toplevel()
    dl = Label(first_window, text="Enter the measure of degree:")
    ml = Label(first_window, text="Enter the measure of minutes:")
    sl = Label(first_window, text="Enter the measure of seconds: ")
    dl.grid(column=0, row=0)
    ml.grid(column=0, row=1)
    sl.grid(column=0, row=2)

    de = Entry(first_window)
    de.grid(column=1, row=0)
    me = Entry(first_window)
    me.grid(column=1, row=1)
    se = Entry(first_window)
    se.grid(column=1, row=2)

    def calculate():
        dget = float(de.get())
        meget = float(me.get())
        try:
            seget = float(se.get())
        except:
            seget = 0
            
        answer = dget + (meget/60) + (seget/3600)
        # answerlabel
        answerlabel = Label(first_window, text=f"Answer = {answer} Degrees")
        answerlabel.grid(row=3, column=0)
        if meget >= 60 or seget >= 60:
            messagebox.showinfo(message="The minutes and seconds should not be greater than 60. ")
        
    calculater = Button(first_window, text="Calculate", command=calculate)
    calculater.grid(row=4, column=0)
def minutes_to_degrees_in_decimals():
    new_window = Toplevel()
    ask = Label(new_window, text="Enter the measure of the angle in degrees (decimal)")
    ask.grid(column=0, row=0)
    aske = Entry(new_window)
    #
    aske.grid(column=1, row=0)

    def find_answer():
        theta = aske.get()
        options = Options()
        options.add_argument('headless')
        driverpath = "C:/Program Files/Mozilla Firefox/geckodriver"
        
        driver = webdriver.Firefox(executable_path=driverpath)
        
        time.sleep(0.5)
        pg.click(919, 783)
        pg.click(x=590, y=838)
        time.sleep(1)
        pg.click(x=644, y=796)
        time.sleep(2)
        driver.get("https://www.calculatorsoup.com/calculators/conversions/convert-decimal-degrees-to-degrees-minutes-seconds.php")
        
        
        reset = driver.find_element("name", "reset")
        reset.click()
        area = driver.find_element("id", "decimal")
        area.send_keys(theta)
        aclick = driver.find_element("name", "calculateButton")
        aclick.click()

        result = driver.find_element("id", "answer")
        answer = result.text[:15].replace("DMS", "")
        answeraa = Label(new_window, text=f"The answer is: {answer}")
        answeraa.grid(row=1, column=0)

    calculatew = Button(new_window, text="Calculate", command=find_answer)
    calculatew.grid(column=2, row=2)
while True:
    function_window()
    # solve_right_angled_triangles()
    mainloop()

