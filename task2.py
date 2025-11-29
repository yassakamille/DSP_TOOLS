import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to load a text file and extract signal data


def openform2():

    def load_signal(file_path):
        x = []
        y = []
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split()
                if len(data) == 2:
                    x.append(float(data[0]))
                    y.append(float(data[1]))
        return x, y

    # Function to perform arithmetic operations and update the plot
    def perform_operation():
        selected_operation = operation_var.get()
        result_label.config(text="Operation Result:")

        if selected_operation == "Load Signal":
            file_path = file1_entry.get()
            x, y = load_signal(file_path)
            ax.clear()
            ax.plot(x, y)
            ax.set_title("Loaded Signal")
            ax.set_xlabel("X-axis")
            ax.set_ylabel("Y-axis")
            canvas.draw()
        else:
            result = None
            if selected_operation == "Multiplication":
                file1_path = file1_entry.get()
                constant = float(constant_entry.get())
                x1, y1 = load_signal(file1_path)
                result = np.array(y1) * constant
            elif selected_operation == "Squaring":
                file1_path = file1_entry.get()
                x1, y1 = load_signal(file1_path)
                result = np.array(y1) ** 2
            elif selected_operation == "Shifting":
                file1_path = file1_entry.get()
                shift_value = int(shift_entry.get())
                x1, y1 = load_signal(file1_path)
                result = np.interp(np.array(x1) + shift_value, x1, y1)
            elif selected_operation == "Normalization":
                file1_path = file1_entry.get()
                x1, y1 = load_signal(file1_path)
                result = (np.array(y1) - min(y1)) / (max(y1) - min(y1))
            elif selected_operation == "Accumulation":
                file1_path = file1_entry.get()
                x1, y1 = load_signal(file1_path)
                result = np.cumsum(y1)

            if result is not None:
                ax.clear()
                ax.plot(x1, result)
                ax.set_title("Output Signal")
                ax.set_xlabel("X-axis")
                ax.set_ylabel("Y-axis")
                canvas.draw()

    # Create the main window
    root = tk.Tk()
    root.title("Deterministic Operations")

    # Create a label for the operation
    operation_label = tk.Label(root, text="Select Operation:")
    operation_label.pack()

    # Create a dropdown for selecting the operation
    operation_var = tk.StringVar()
    operation_dropdown = tk.OptionMenu(root, operation_var,  "Multiplication", "Squaring", "Shifting", "Normalization", "Accumulation")
    operation_dropdown.pack()

    # Create labels and entry widgets for file selection
    file1_label = tk.Label(root, text="Select Signal File:")
    file1_label.pack()
    file1_entry = tk.Entry(root, width=40)
    file1_entry.pack()

    # Create a button to browse for the signal file
    browse_button1 = tk.Button(root, text="Browse", command=lambda: file1_entry.insert(0, filedialog.askopenfilename()))
    browse_button1.pack()

    # Entry widget for constant value (for multiplication) or shift value
    constant_label = tk.Label(root, text="Constant (for Multiplication):")
    constant_label.pack()
    constant_entry = tk.Entry(root)
    constant_entry.pack()

    # Entry widget for shifting value
    shift_label = tk.Label(root, text="Shift Value (for Shifting):")
    shift_label.pack()
    shift_entry = tk.Entry(root)
    shift_entry.pack()

    # Create labels for the result
    result_label = tk.Label(root, text="Operation Result:")
    result_label.pack()

    # Create a button to perform the selected operation
    calculate_button = tk.Button(root, text="Perform Operation", command=perform_operation)
    calculate_button.pack()

    # Create a matplotlib figure and canvas for plotting
    fig, ax = plt.subplots(figsize=(6, 4))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()

    # Start the GUI main loop
    root.mainloop()
