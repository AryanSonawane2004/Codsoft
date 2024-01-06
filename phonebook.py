import tkinter as tk
from tkinter import messagebox

def add_contact():
    name = entry_name.get()
    number = entry_number.get()
    if name and number:
        contact_list.insert(tk.END, f"{name}: {number}")
        entry_name.delete(0, tk.END)
        entry_number.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Please enter both name and number.")

# Create the main window
root = tk.Tk()
root.title("Phonebook")

# Create widgets
label_name = tk.Label(root, text="Name:")
label_number = tk.Label(root, text="Number:")
entry_name = tk.Entry(root)
entry_number = tk.Entry(root)
add_button = tk.Button(root, text="Add Contact", command=add_contact)
contact_list = tk.Listbox(root)

# Place widgets on the grid
label_name.grid(row=0, column=0, padx=5, pady=5)
label_number.grid(row=1, column=0, padx=5, pady=5)
entry_name.grid(row=0, column=1, padx=5, pady=5)
entry_number.grid(row=1, column=1, padx=5, pady=5)
add_button.grid(row=2, column=0, columnspan=2, pady=10)
contact_list.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
