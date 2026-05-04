import qrcode
import ProjectQR
from tkinter import*
from tkinter import messagebox
import os

# Initialize the main window
root = Tk()
root.title("QR Code Generator")  # Fixed typo: 'tittle' -> 'title'
root.geometry("600x600")
root.configure(bg="Steelblue")

def code():
    try:
        qr = qrcode.QRCode(
            version=int(size.get()),
            box_size=5,
            border=5
        )
        qr.add_data(text.get())
        qr.make(fit=True)

        img = qr.make_image()

        if name.get() == "":
            filename = "QR_Code.png"
        else:
            filename = name.get() + ".png"

        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        full_path = os.path.join(desktop_path, filename)

        img.save(full_path)

        messagebox.showinfo("QR Code Generator", f"Saved at:\n{full_path}")

    except:
        messagebox.showerror("Error", "Please enter valid inputs")


#Main Frame for QR GENERATOR
frame1 = Frame(root, bg='Black', bd=10)
frame1.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.1)

#heading "QR Code Generator"
label1 = Label(frame1, text="QR CODE GENERATOR", bg="White", font="Times 20 bold")
label1.place(relx=0, rely=0, relwidth=1, relheight=1)

#to take input
frame2 = Frame(root, bg='SteelBlue')
frame2.place(relx=0.1, rely=0.15, relwidth=0.7, relheight=0.3)
label2 = Label(frame2, text="Enter the text/URL: ", bg="SteelBlue", fg='black', font="Times 15 bold")
label2.place(relx=0.05, rely=0.2, relheight=0.08)
text = Entry(frame2, font='Century 12')
text.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

#to take input image name
frame3 = Frame(root, bg='SteelBlue')
frame3.place(relx=0.1, rely=0.35, relwidth=0.7, relheight=0.3)
label3 = Label(frame3, text="Enter the name/link of the QR Code: ", bg="SteelBlue", fg='Black', font="Times 15 bold")
label3.place(relx=0.05, rely=0.2, relheight=0.2)
name = Entry(frame3, font='Century 12')
name.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

#to take input of the size of QR Code
frame4 = Frame(root, bg='SteelBlue')
frame4.place(relx=0.1, rely=0.55, relwidth=0.7, relheight=0.3)
label4 = Label(frame4, text="Enter the size from 1 to 50: ", bg="SteelBlue", fg='black', font="Times 14 bold")
label4.place(relx=0.05, rely=0.2, relheight=0.2)
size = Entry(frame4, font='Century 12')
size.place(relx=0.05, rely=0.4, relwidth=0.5, relheight=0.2)

#button can use for showing msg QR generated or not
button = Button(root, text="QR Code Generated", font="Times 15 normal", command=code)
button.place(relx=0.3, rely=0.9, relwidth=0.30, relheight=0.05)

# Start the GUI loop
root.mainloop()