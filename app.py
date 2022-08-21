from tkinter import *
import random

class myApp:
    OPTIONS = ["McDonalds", "Chick-fil-a", "Dominos", "The Habit", "Panera Bread", "Wendy's", "In-n-Out", 
               "Taco Bell", "Jack-in-the-Box", "Subway"]

    def __init__(self):
        self.myGui = Tk()
        self.myGui.title("Food Generator")
        self.myGui.geometry("400x400")
        self.option = StringVar()

        topLabel = Label(text="Let's pick\nsomewhere to eat!\n🤤🍕🍟🥤", font=("Helvetica", 24)).pack(pady=20)
        selectButton = Button(text="Click to Select", font=("Helvetica", 24), command=self.pick).pack(pady=20)
        self.optionLabel = Label(textvariable = self.option, fg='red', justify='center', font=("Helvetica", 20)).place(x=155, y=250)
        
        reset = Button(text = "Reset", command = self.reset_values).place(x=0,y=368)
        quit = Button(text="Quit", command = self.close_win).place(x=338,y=368)

        self.myGui.mainloop()

    def pick(self):
        options_set = set(myApp.OPTIONS)
        unique_options = list(options_set)
        selected_choice = random.choice(unique_options)
        self.option.set(selected_choice)

    def reset_values(self):
        self.option.set("")

    def close_win(self):
        self.myGui.destroy()

if __name__ == '__main__':
    Gui = myApp()