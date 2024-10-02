

# importing required packages
import tkinter
from PIL import ImageTk, Image
import os

from PIL import Image, ImageTk
import tkinter as tk
import os

root = tk.Tk()
root.title("Photo Gallery")
root.geometry("655x350")



img_list=[]
path = "../outputresult/user_captions" # my folder
n_row = 0
n_col = 0
index = 0
x = tk.IntVar()
for f in os.listdir(path):
    img_list.append(ImageTk.PhotoImage(Image.open(os.path.join(path,f))))
    n_col +=1
    index +=1
    if n_col > 9:
        n_row +=1
        n_col = 1
    radio_button = tk.Radiobutton(text = 'Output Images', image=img_list[index-1], indicatoron=0, bd=2, variable = x, value = index)
    radio_button.grid(row=n_row, column = n_col)
  

  
# running the application
root.mainloop()