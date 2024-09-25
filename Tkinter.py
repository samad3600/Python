import tkinter as tk
from functools import partial

def printDetails(usernameEntry):
    usernameText = usernameEntry.get()
    print("User entered:", usernameText)

# Create the main Tkinter window
tkWindow = tk.Tk()
tkWindow.geometry('400x150')
tkWindow.title('Python Examples')

# Label for user input
usernameLabel = tk.Label(tkWindow, text="Enter your name")

# Entry widget for user input
usernameEntry = tk.Entry(tkWindow)

# Define a callable function with printDetails function and usernameEntry argument
printDetailsCallable = partial(printDetails, usernameEntry)

# Submit button
submitButton = tk.Button(tkWindow, text="Submit", command=printDetailsCallable)

# Place label, entry, and button in a grid
usernameLabel.grid(row=0, column=0)
usernameEntry.grid(row=0, column=1)
submitButton.grid(row=1, column=1)

# Start the Tkinter event loop
tkWindow.mainloop()
