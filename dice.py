from tkinter import *
from PIL import ImageTk, Image
import itertools
import random

background_color = "#0D865D"

root = Tk()
root.geometry("960x720")
root.configure(bg=background_color)
root.title("Let's try out your Luck!")

first_image_path = '1.png'
second_image_path = '2.png'

first_dice_image = ImageTk.PhotoImage(Image.open(first_image_path))
first_dice_label = Label(root, image=first_dice_image, bg=background_color)
first_dice_label.pack()

second_dice_image = ImageTk.PhotoImage(Image.open(second_image_path))
second_dice_label = Label(root, image=second_dice_image, bg=background_color)
second_dice_label.pack()

'''
    This function will return me a dice combination bt a tuple.
    e.g. (6,1) or (4,4)
'''


def roll_dice():
    dice_number = list(range(1, 7))  # returns us 1,2,3,4,5,6
    combinations = list(itertools.product(dice_number, repeat=2))
    rolled_dice = random.choice(combinations)
    return rolled_dice


def update_rolled_dice_image():
    rolled_dice = list(roll_dice())  # e.g. will return [4,4]
    print(rolled_dice)

    new_first_image_path = f"{rolled_dice[0]}.png"
    new_second_image_path = f"{rolled_dice[1]}.png"

    new_first_dice_image = ImageTk.PhotoImage(Image.open(new_first_image_path))
    new_second_dice_image = ImageTk.PhotoImage(Image.open(new_second_image_path))
    first_dice_label.configure(image=new_first_dice_image)
    second_dice_label.configure(image=new_second_dice_image)

    first_dice_label.image = new_first_dice_image
    second_dice_label.image = new_second_dice_image


roll_button = Button(root, text="Roll Dices!", command=update_rolled_dice_image)
roll_button.pack(side=BOTTOM)

root.mainloop()
