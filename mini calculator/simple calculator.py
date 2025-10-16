#simple calculator

import tkinter as tk

# Function to update expression in text entry box
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate the expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))  # evaluate string expression
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the entry
def clear():
    global expression
    expression = ""
    equation.set("")

# main driver code
if __name__ == "__main__":
    # create GUI window
    root = tk.Tk()
    root.title("Simple Calculator")
    root.geometry("320x400")

    expression = ""

    # StringVar() is used to get the instance of input field
    equation = tk.StringVar()

    # Entry field
    entry_field = tk.Entry(root, textvariable=equation, font=('Arial', 18), bd=10, insertwidth=2, width=14,
                           borderwidth=4, relief="ridge", justify='right')
    entry_field.grid(row=0, column=0, columnspan=4)

    # Buttons
    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    ]

    row_val = 1
    col_val = 0

    for button in buttons:
        if button == "=":
            b = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14), bg="lightgreen",
                          command=equalpress)
        else:
            b = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14),
                          command=lambda btn=button: press(btn))

        b.grid(row=row_val, column=col_val, sticky="nsew")

        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1 #

    # Clear button
    clear_btn = tk.Button(root, text="C", padx=20, pady=20, font=('Arial', 14), bg="tomato", command=clear)
    clear_btn.grid(row=row_val, column=0, sticky="nsew")

    # Adjust row & column weights for resizing
    for i in range(5):
        root.rowconfigure(i, weight=1)
    for j in range(4):
        root.columnconfigure(j, weight=1)

    root.mainloop()
