import qrcode
from tkinter import *

def generate_qr():
    # Get text input from the user
    text = input_box.get()
    
    # Generate the QR code image
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Display the QR code image
    img.show()

# Create the main window
root = Tk()
root.title("QR Code Generator")

# Create the input box and label
input_label = Label(root, text="Enter text to generate QR code:")
input_label.pack()
input_box = Entry(root)
input_box.pack()

# Create the button to generate the QR code
generate_button = Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack()

# Start the main loop
root.mainloop()
