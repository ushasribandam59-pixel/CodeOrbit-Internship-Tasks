
import tkinter as tk
from operations import add, subtract, multiply, divide

# Create calculator window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x480")
root.resizable(False, False)
root.configure(bg="#FCE4EC")

first_number = None
operator = None

# Display numbers
def button_click(value):
    display.insert(tk.END, str(value))

# Clear display
def clear():
    global first_number, operator
    display.delete(0, tk.END)
    first_number = None
    operator = None

# Select arithmetic operator
def select_operator(op):
    global first_number, operator

    try:
        first_number = float(display.get())
        operator = op

        # Keep the first number visible
        display.delete(0, tk.END)
        display.insert(0, str(first_number) + " " + op + " ")

    except ValueError:
        display.delete(0, tk.END)
        display.insert(0, "Invalid Input")

# Calculate result
def calculate():
    global first_number, operator

    try:
        # Get second number after the operator
        expression = display.get()
        second_number = float(expression.split()[-1])

        if operator == "+":
            result = add(first_number, second_number)

        elif operator == "-":
            result = subtract(first_number, second_number)

        elif operator == "*":
            result = multiply(first_number, second_number)

        elif operator == "/":
            result = divide(first_number, second_number)

        else:
            return

        display.delete(0, tk.END)
        display.insert(0, str(result))

        first_number = None
        operator = None

    except (ValueError, IndexError):
        display.delete(0, tk.END)
        display.insert(0, "Invalid Input")

# Delete last character
def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

# Calculator display
display = tk.Entry(
    root,
    font=("Arial", 24, "bold"),
    justify="right",
    bd=8,
    bg="#FFF5F8",
    fg="#880E4F",
    insertbackground="#880E4F"
)
display.pack(fill="x", padx=15, pady=20, ipady=10)
# Calculator buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "⌫", "+"],
    ["="]
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root, bg="#FCE4EC")
    frame.pack(expand=True, fill="both", padx=10)

    for item in row:

        if item == "C":
            command = clear

        elif item == "⌫":
            command = backspace

        elif item == "=":
            command = calculate

        elif item in ["+", "-", "*", "/"]:
            command = lambda x=item: select_operator(x)

        else:
            command = lambda x=item: button_click(x)

        button = tk.Button(
            frame,
            text=item,
            font=("Arial", 18, "bold"),
            bg="#F8BBD0",
    fg="#880E4F",
    activebackground="#F48FB1",
    activeforeground="white",
    relief="flat",
    bd=0,
    cursor="hand2",
    command=command
)

        button.pack(
            side="left",
            expand=True,
            fill="both",
            padx=3,
            pady=3
        )
