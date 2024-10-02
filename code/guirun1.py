# import all functions from the tkinter
from tkinter import *
import os

# import the random library
import random

# Function to clear both the text areas
def clearAll() :
	# whole content of text area is deleted
	text1_field.delete(1.0, END)


# Function to Generate SpongeBob Mocking Text
def generate() :

	# get a whole input content from text box
	# ignoring \n from the text box content
	input_text = text1_field.get("1.0", "end")[:-1]
	strinp=str(input_text)
	print(strinp)
	file = open("../data/birds/user_captions.txt", 'w')
	file.write(strinp)
	file.close()
	os.system("python main.py")
	
	



# Driver code
if __name__ == "__main__" :

	# Create a GUI window
	root = Tk()

	# Set the background colour of GUI window
	root.configure(background = 'light green')
	
	# Set the configuration of GUI window (WidthxHeight)
	root.geometry("400x250")

	# set the name of tkinter GUI window
	root.title("Text To Image Generation Using GAN")
	
	# Create Welcome to SpongeBob Mocking Text Generator label
	headlabel = Label(root, text = 'Text To Image Generation Using GAN',fg = 'white', bg = "blue")

	# Create a "Input Text " label
	label1 = Label(root, text = " Input Text ",fg = 'black', bg = 'dark green')
	


	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	headlabel.grid(row = 0, column = 1)
	
	# padx keyword argument used to set padding along x-axis .
	label1.grid(row = 1, column = 0, padx = 10)


	
	# Create a text area box
	# for filling or typing the information.
	text1_field = Text(root, height = 5, width = 25, font = "lucida 13")

		
	# padx keyword argument used to set padding along x-axis .
	# pady keyword argument used to set padding along y-axis .
	text1_field.grid(row = 1, column = 1, padx = 10, pady = 10)


	
	# Create a Generate Button and attached
	# with generate function
	button1 = Button(root, text = "Submit", bg = "red", fg = "black",
								command = generate)
	
	button1.grid(row = 2, column = 1)

	# Create a Clear Button and attached
	# with clearAll function
	button2 = Button(root, text = "Clear", bg = "red",
					fg = "black", command = clearAll)
	
	button2.grid(row = 1, column = 2)
	
	# Start the GUI
	root.mainloop()
