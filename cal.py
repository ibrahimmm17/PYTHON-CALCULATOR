import tkinter as tk

# Function to handle button clicks
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_operator(operator):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + operator)

def button_equal():
    current = entry.get()
    try:
        result = str(eval(current))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Entry field for input
entry = tk.Entry(window, font=("Helvetica", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

# Create buttons for digits and operations
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(
        window, 
        text=button, 
        padx=20, 
        pady=20, 
        font=("Helvetica", 16), 
        command=lambda b=button: button_click(b) if b not in {"=", "+", "-", "*", "/"} else button_operator(b) if b != "=" else button_equal()
    ).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the GUI application
window.mainloop()
