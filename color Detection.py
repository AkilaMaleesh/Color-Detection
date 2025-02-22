import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief

# Initialize Tkinter window
root = Tk()
root.title("Color Picker from Image")
root.geometry("800x470+100+100")
root.configure(bg="#e4e8eb")
root.resizable(False, False)

# Global variable for selected file path
filename = None

def showimage():
    """Function to select an image and display it in the UI."""
    global filename
    filename = filedialog.askopenfilename(
        filetypes=[("JPG file", "*.jpg"), ("PNG file", "*.png")]
    )

    if filename:
        img = Image.open(filename)
        img = img.resize((310, 270))  # Resize image
        img = ImageTk.PhotoImage(img)

        lbl.configure(image=img, width=310, height=270)
        lbl.image = img  # Prevent garbage collection

def Findcolor():
    """Function to extract colors from the selected image."""
    if not filename:
        print("No image selected!")
        return

    ct = ColorThief(filename)
    palette = ct.get_palette(color_count=10)  # Get top 10 colors

    hex_colors = []  # List to store HEX colors
    for rgb in palette:
        hex_color = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"  # Convert RGB to HEX
        hex_colors.append(hex_color)

    print(hex_colors)  # Debugging: Print colors to console

    # Update UI with extracted colors
    update_color_boxes(hex_colors)

def update_color_boxes(colors):
    """Update the UI with extracted colors."""
    for i in range(10):  # Loop through 10 colors
        color = colors[i] if i < len(colors) else "#ffffff"  # Default to white if fewer colors
        colors_canvas.itemconfig(ids[i], fill=color)  # Update canvas color
        hex_labels[i].config(text=color)  # Update label text

# Set app icon (Make sure the path is correct)
image_icon = PhotoImage(file=r"C:\Users\akila\Downloads\Edit\logo.png")
root.iconphoto(False, image_icon)

Label(root, width=120, height=10, bg="#4272f9").pack()

# Frame for UI
frame = Frame(root, width=700, height=370, bg="#fff")
frame.place(x=50, y=50)

logo = PhotoImage(file=r"C:\Users\akila\Downloads\Edit\icon.png")
Label(frame, image=logo, bg="#fff").place(x=10, y=10)

Label(frame, text="Color Finder", font="arial 25 bold", bg="white").place(x=100, y=20)

# Color palette canvas
colors_canvas = Canvas(frame, bg="#fff", width=150, height=265, bd=0)
colors_canvas.place(x=20, y=90)

# Create rectangles for colors
ids = []
hex_labels = []

for i in range(10):
    rect = colors_canvas.create_rectangle(10, 10 + (i * 25), 50, 30 + (i * 25), fill="#ffffff")  # Color boxes
    ids.append(rect)

    label = Label(colors_canvas, text="#ffffff", fg="#000", font="arial 12 bold", bg="white")  # HEX labels
    label.place(x=60, y=10 + (i * 25))
    hex_labels.append(label)

# Select Image Frame
selectimage = Frame(frame, width=340, height=350, bg="#d6dee5")
selectimage.place(x=350, y=10)

f = Frame(selectimage, bd=3, bg="black", width=320, height=280, relief=GROOVE)
f.place(x=10, y=10)

lbl = Label(f, bg="black")
lbl.place(x=0, y=0)

# Buttons
Button(selectimage, text="Select Image", width=12, height=1, font="arial 14 bold", command=showimage).place(x=10, y=300)
Button(selectimage, text="Find Colors", width=12, height=1, font="arial 14 bold", command=Findcolor).place(x=176, y=300)

root.mainloop()
