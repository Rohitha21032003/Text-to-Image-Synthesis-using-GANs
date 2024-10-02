from tkinter import *
import os

def clearAll():
    text1_field.delete(1.0, END)
    error_label.config(text="")

def generate():
    input_text = text1_field.get("1.0", "end")[:-1]
    if "bird" in input_text.lower():
        strinp = str(input_text)
        print(strinp)
        file = open("../data/birds/user_captions.txt", 'w')
        file.write(strinp)
        file.close()
        os.system("python main.py")
    else:
        error_label.config(text="Error: Give Valid Input ", fg="red")

def minimize():
    root.iconify()

def close():
    root.destroy()

if __name__ == "__main__":
    root = Tk()
    root.configure(background='#FDFEFE')
    root.attributes('-fullscreen', True)
    root.title("Text To Image Generation Using GAN")

    headlabel = Label(root, text='Text To Image Generation Using GAN', fg='#17202A', bg="#AED6F1", font=("Helvetica", 24, "bold"))
    headlabel.pack(pady=20)

    label1 = Label(root, text=" Input Text ", fg='#17202A', bg='#FDFEFE', font=("Helvetica", 18))
    label1.pack(pady=10)

    text1_field = Text(root, height=5, width=50, font=("Helvetica", 16))
    text1_field.pack(pady=10)

    button_frame = Frame(root, bg='#FDFEFE')
    button_frame.pack(pady=20)

    button1 = Button(button_frame, text="Submit", bg="#58D68D", fg="#17202A", font=("Helvetica", 16), command=generate)
    button1.grid(row=0, column=0, padx=10)

    button2 = Button(button_frame, text="Clear", bg="#EC7063", fg="#17202A", font=("Helvetica", 16), command=clearAll)
    button2.grid(row=0, column=1, padx=10)

    error_label = Label(root, text="", fg="red", bg='#FDFEFE', font=("Helvetica", 16))
    error_label.pack()

    # Minimize Button
    minimize_button = Button(root, text="Minimize", bg="#5DADE2", fg="#17202A", font=("Helvetica", 16), command=minimize)
    minimize_button.place(relx=0.9, rely=0.03, anchor="ne")

    # Close Button
    close_button = Button(root, text="Close", bg="#EC7063", fg="#17202A", font=("Helvetica", 16), command=close)
    close_button.place(relx=0.97, rely=0.03, anchor="ne")

    root.mainloop()
