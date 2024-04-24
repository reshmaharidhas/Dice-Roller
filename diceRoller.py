import tkinter as tk
import random
from pygame import mixer
import base64Pictures
class DiceRoller:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Dice Roller")
        self.window.geometry("450x380")
        self.window.resizable(0,0)
        diceRollerLogoPicture = tk.PhotoImage(data=base64Pictures.diceRollerLogo)
        # dice 4 face
        self.dice4face1 = tk.PhotoImage(file="./dice4/dice-four-faces-one.png")
        self.dice4face2 = tk.PhotoImage(file="./dice4/dice-four-faces-two.png")
        self.dice4face3 = tk.PhotoImage(file="./dice4/dice-four-faces-three.png")
        self.dice4face4 = tk.PhotoImage(file="./dice4/dice-four-faces-four.png")
        # dice 6 face
        self.dice6face1 = tk.PhotoImage(file="./dice6/dice-six-faces-one.png")
        self.dice6face2 = tk.PhotoImage(file="./dice6/dice-six-faces-two.png")
        self.dice6face3 = tk.PhotoImage(file="./dice6/dice-six-faces-three.png")
        self.dice6face4 = tk.PhotoImage(file="./dice6/dice-six-faces-four.png")
        self.dice6face5 = tk.PhotoImage(file="./dice6/dice-six-faces-five.png")
        self.dice6face6 = tk.PhotoImage(file="./dice6/dice-six-faces-six.png")
        # dice 8 face
        self.dice8face1 = tk.PhotoImage(file="./dice8/dice-eight-faces-one.png")
        self.dice8face2 = tk.PhotoImage(file="./dice8/dice-eight-faces-two.png")
        self.dice8face3 = tk.PhotoImage(file="./dice8/dice-eight-faces-three.png")
        self.dice8face4 = tk.PhotoImage(file="./dice8/dice-eight-faces-four.png")
        self.dice8face5 = tk.PhotoImage(file="./dice8/dice-eight-faces-five.png")
        self.dice8face6 = tk.PhotoImage(file="./dice8/dice-eight-faces-six.png")
        self.dice8face7 = tk.PhotoImage(file="./dice8/dice-eight-faces-seven.png")
        self.dice8face8 = tk.PhotoImage(file="./dice8/dice-eight-faces-eight.png")
        #dice10
        self.dice10face1 = tk.PhotoImage(file="./dice10/dice-ten-face-one.png")
        self.dice10face2 = tk.PhotoImage(file="./dice10/dice-ten-face-two.png")
        self.dice10face3 = tk.PhotoImage(file="./dice10/dice-ten-face-three.png")
        self.dice10face4 = tk.PhotoImage(file="./dice10/dice-ten-face-four.png")
        self.dice10face5 = tk.PhotoImage(file="./dice10/dice-ten-face-five.png")
        self.dice10face6 = tk.PhotoImage(file="./dice10/dice-ten-face-six.png")
        self.dice10face7 = tk.PhotoImage(file="./dice10/dice-ten-face-seven.png")
        self.dice10face8 = tk.PhotoImage(file="./dice10/dice-ten-face-eight.png")
        self.dice10face9 = tk.PhotoImage(file="./dice10/dice-ten-face-nine.png")
        self.dice10face10 = tk.PhotoImage(file="./dice10/dice-ten-face-ten.png")
        # dice 12
        self.dice12face1 = tk.PhotoImage(file="./dice12/dice-twelve-face-1.png")
        self.dice12face2 = tk.PhotoImage(file="./dice12/dice-twelve-face-2.png")
        self.dice12face3 = tk.PhotoImage(file="./dice12/dice-twelve-face-3.png")
        self.dice12face4 = tk.PhotoImage(file="./dice12/dice-twelve-face-4.png")
        self.dice12face5 = tk.PhotoImage(file="./dice12/dice-twelve-face-5.png")
        self.dice12face6 = tk.PhotoImage(file="./dice12/dice-twelve-face-6.png")
        self.dice12face7 = tk.PhotoImage(file="./dice12/dice-twelve-face-7.png")
        self.dice12face8 = tk.PhotoImage(file="./dice12/dice-twelve-face-8.png")
        self.dice12face9 = tk.PhotoImage(file="./dice12/dice-twelve-face-9.png")
        self.dice12face10 = tk.PhotoImage(file="./dice12/dice-twelve-face-10.png")
        self.dice12face11 = tk.PhotoImage(file="./dice12/dice-twelve-face-11.png")
        self.dice12face12 = tk.PhotoImage(file="./dice12/dice-twelve-face-12.png")
        #dice 20
        self.dice20face1 = tk.PhotoImage(file="./dice20/dice-twenty-faces-1.png")
        self.dice20face2 = tk.PhotoImage(file="./dice20/dice-twenty-faces-2.png")
        self.dice20face3 = tk.PhotoImage(file="./dice20/dice-twenty-faces-3.png")
        self.dice20face4 = tk.PhotoImage(file="./dice20/dice-twenty-faces-4.png")
        self.dice20face5 = tk.PhotoImage(file="./dice20/dice-twenty-faces-5.png")
        self.dice20face6 = tk.PhotoImage(file="./dice20/dice-twenty-faces-6.png")
        self.dice20face7 = tk.PhotoImage(file="./dice20/dice-twenty-faces-7.png")
        self.dice20face8 = tk.PhotoImage(file="./dice20/dice-twenty-faces-8.png")
        self.dice20face9 = tk.PhotoImage(file="./dice20/dice-twenty-faces-9.png")
        self.dice20face10 = tk.PhotoImage(file="./dice20/dice-twenty-faces-10.png")
        self.dice20face11 = tk.PhotoImage(file="./dice20/dice-twenty-faces-11.png")
        self.dice20face12 = tk.PhotoImage(file="./dice20/dice-twenty-faces-12.png")
        self.dice20face13 = tk.PhotoImage(file="./dice20/dice-twenty-faces-13.png")
        self.dice20face14 = tk.PhotoImage(file="./dice20/dice-twenty-faces-14.png")
        self.dice20face15 = tk.PhotoImage(file="./dice20/dice-twenty-faces-15.png")
        self.dice20face16 = tk.PhotoImage(file="./dice20/dice-twenty-faces-16.png")
        self.dice20face17 = tk.PhotoImage(file="./dice20/dice-twenty-faces-17.png")
        self.dice20face18 = tk.PhotoImage(file="./dice20/dice-twenty-faces-18.png")
        self.dice20face19 = tk.PhotoImage(file="./dice20/dice-twenty-faces-19.png")
        self.dice20face20 = tk.PhotoImage(file="./dice20/dice-twenty-faces-20.png")
        self.frame1 = tk.Frame(self.window)
        self.frame1.pack(padx=10,pady=15)
        # list of dice names of the 6 types of dice used in this application
        self.diceNames = ["D4","D6","D8","D10","D12","D20"]
        # List of photoimage variables containing faces of 4 sided dice
        self.dice4ImagesList = [self.dice4face1,self.dice4face2,self.dice4face3,self.dice4face4]
        # List of photoimage variables containing faces of 6 sided dice
        self.dice6ImagesList = [self.dice6face1,self.dice6face2,self.dice6face3,self.dice6face4,self.dice6face5,self.dice6face6]
        # List of photoimage variables containing faces of 8 sided dice
        self.dice8ImagesList = [self.dice8face1,self.dice8face2,self.dice8face3,self.dice8face4,self.dice8face5,
                                self.dice8face6,self.dice8face7,self.dice8face8]
        # List of photoimage variables containing faces of 10 sided dice
        self.dice10ImagesList = [self.dice10face1,self.dice10face2,self.dice10face3,self.dice10face4,self.dice10face5,
                                 self.dice10face6,self.dice10face7,self.dice10face8,self.dice10face9,self.dice10face10]
        # List of photoimage variables containing faces of 12 sided dice
        self.dice12ImagesList = [self.dice12face1,self.dice12face2,self.dice12face3,self.dice12face4,self.dice12face5,
                                 self.dice12face6,self.dice12face7,self.dice12face8,self.dice12face9,self.dice12face10,
                                 self.dice12face11,self.dice12face12]
        # List of photoimage variables containing faces of 20 sided dice
        self.dice20ImagesList = [self.dice20face1,self.dice20face2,self.dice20face3,self.dice20face4,self.dice20face5,
                                 self.dice20face6,self.dice20face7,self.dice20face8,self.dice20face9,self.dice20face10,
                                 self.dice20face11,self.dice20face12,self.dice20face13,self.dice20face14,self.dice20face15,
                                 self.dice20face16,self.dice20face17,self.dice20face18,self.dice20face19,self.dice20face20]
        # Variable to monitor which radio button is clicked currently
        self.x = tk.IntVar()
        # Creating 6 radio buttons for every dice in the array 'diceNames'
        for ptr in range(len(self.diceNames)):
            radio = tk.Radiobutton(self.frame1,value=ptr,text=self.diceNames[ptr],variable=self.x,font=("Helvetica",14),command=self.changeDiceInitialPicture)
            radio.grid(row=0,column=ptr,padx=5)
        self.frame2 = tk.Frame(self.window)
        self.frame2.pack()
        # Picture of dice faces to display on every roll
        self.dicePicture = tk.Label(self.frame2,image=self.dice4face1)
        self.dicePicture.grid(row=1,column=2,pady=6)
        # Button to do the roll dice operation
        self.rollButton = tk.Button(self.frame2,text="Roll",command=self.chooseDice,font=("Cambria",20),bg="black",fg="white",relief=tk.RAISED,bd=3,width=7,activebackground="black",activeforeground="yellow")
        self.rollButton.grid(row=2,column=2,pady=15)
        # keyboard shortcut to perform dice rolling without clicking the button 'rollButton'.
        # On pressing the SPACE bar, the dice rolls.
        self.window.bind("<space>",self.keyShortcutToRollDice)
        # Setting the icon of this application GUI
        self.window.iconphoto(True,diceRollerLogoPicture)
        self.window.mainloop()

    # Function to roll the dice operation based on the radio button selected currently
    def chooseDice(self):
        self.playDiceSound()
        if self.x.get() == 0:
            self.rollDice4()
        elif self.x.get() == 1:
            self.rollDice6()
        elif self.x.get() == 2:
            self.rollDice8()
        elif self.x.get() == 3:
            self.rollDice10()
        elif self.x.get() == 4:
            self.rollDice12()
        elif self.x.get() == 5:
            self.rollDice20()
    # Function to roll the 4 sided dice and display random face
    def rollDice4(self):
        randomNumber = random.randrange(1, 5)
        self.dicePicture.config(image=self.dice4ImagesList[randomNumber - 1])

    # Function to roll the 6 sided dice and display random face

    def rollDice6(self):
        randomNumber = random.randrange(1, 7)
        self.dicePicture.config(image=self.dice6ImagesList[randomNumber - 1])

    # Function to roll the 8 sided dice and display random face

    def rollDice8(self):
        randomNumber = random.randrange(1, 9)
        self.dicePicture.config(image=self.dice8ImagesList[randomNumber - 1])

    # Function to roll the 10 sided dice and display random face

    def rollDice10(self):
        randomNumber = random.randrange(1, 11)
        self.dicePicture.config(image=self.dice10ImagesList[randomNumber - 1])

    # Function to roll the 12 sided dice and display random face

    def rollDice12(self):
        randomNumber = random.randrange(1, 13)
        self.dicePicture.config(image=self.dice12ImagesList[randomNumber - 1])

    # Function to roll the 20 sided dice and display random face
    def rollDice20(self):
        randomNumber = random.randrange(1, 21)
        self.dicePicture.config(image=self.dice20ImagesList[randomNumber - 1])
    # Function to play a dice rolling sound everytime button 'rollButton' or on pressing space bar in keyboard

    def playDiceSound(self):
        mixer.init()
        mixer.music.load("dice-142528.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
    # Function to call the dice rolling function when player presses the space bar as keyboard shortcut
    def keyShortcutToRollDice(self,event):
        self.chooseDice()
    # Function to change the picture displayed when any radio button is selected by player
    def changeDiceInitialPicture(self):
        if self.x.get() == 0:
            self.dicePicture.config(image=self.dice4face1)
        elif self.x.get() == 1:
            self.dicePicture.config(image=self.dice6face1)
        elif self.x.get() == 2:
            self.dicePicture.config(image=self.dice8face1)
        elif self.x.get() == 3:
            self.dicePicture.config(image=self.dice10face1)
        elif self.x.get() == 4:
            self.dicePicture.config(image=self.dice12face1)
        elif self.x.get() == 5:
            self.dicePicture.config(image=self.dice20face1)
DiceRoller()