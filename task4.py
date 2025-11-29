import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to load a text file and extract signal data
def openform4():
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
        file1_path = file1_entry.get()
        file2_path = file2_entry.get()
        operation = operation_var.get()

        x1, y1 = load_signal(file1_path)
        x2, y2 = load_signal(file2_path)

        if operation == "Addition":
            result = np.array(y1) + np.array(y2)
            operation_label.config(text="Operation: Addition")
        elif operation == "Subtraction":
            result = np.array(y1) - np.array(y2)
            operation_label.config(text="Operation: Subtraction")

        ax.clear()
        ax.plot(x1, result)
        ax.set_title("Result Signal")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        canvas.draw()

    # Create the main window
    root = tk.Tk()
    root.title("Arethmetic Operations")

    # Create frames
    frame1 = tk.Frame(root)
    frame1.pack()

    frame2 = tk.Frame(root)
    frame2.pack()

    # Create labels and entry widgets for file selection
    file1_label = tk.Label(frame1, text="Select File 1:")
    file1_label.grid(row=0, column=0)

    file1_entry = tk.Entry(frame1, width=40)
    file1_entry.grid(row=0, column=1)

    file2_label = tk.Label(frame1, text="Select File 2:")
    file2_label.grid(row=1, column=0)

    file2_entry = tk.Entry(frame1, width=40)
    file2_entry.grid(row=1, column=1)

    # Create a button to browse for text files
    browse_button1 = tk.Button(frame1, text="Browse", command=lambda: file1_entry.insert(0, filedialog.askopenfilename()))
    browse_button1.grid(row=0, column=2)

    browse_button2 = tk.Button(frame1, text="Browse", command=lambda: file2_entry.insert(0, filedialog.askopenfilename()))
    browse_button2.grid(row=1, column=2)

    # Create a dropdown for selecting the operation
    operation_var = tk.StringVar()
    operation_label = tk.Label(frame2, text="Select Operation:")
    operation_label.grid(row=0, column=0)

    operation_dropdown = tk.OptionMenu(frame2, operation_var, "Addition", "Subtraction")
    operation_dropdown.grid(row=0, column=1)

    # Create a button to perform the selected operation
    calculate_button = tk.Button(frame2, text="Perform Operation", command=perform_operation)
    calculate_button.grid(row=1, column=0)

    # Create a matplotlib figure and canvas for plotting
    fig, ax = plt.subplots(figsize=(6, 4))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()

    # Start the GUI main loop
    root.mainloop()
