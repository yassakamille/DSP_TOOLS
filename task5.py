import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
def openform5():
    def compute_dct():
        input_file = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text Files", "*.txt")])
        if input_file:
            try:
                with open(input_file, 'r') as file:
                    signal_values = [float(line.strip().split()[1])for line in file.readlines()]

                N = len(signal_values)
                dct_values = []

                for k in range(N):
                    sum_val = 0
                    for n in range(N):
                        sum_val += signal_values[n] * np.cos(np.pi / (4 * N) * (2 * n - 1) * (2 * k - 1))
                    dct_val = np.sqrt(2 / N) * sum_val
                    dct_values.append(dct_val)

                # Display DCT result in the text view
                text_view.delete(1.0, tk.END)
                text_view.insert(tk.END, f"DCT Result:\n")
                for idx, val in enumerate(dct_values):
                    text_view.insert(tk.END, f" {0 } {val}\n")

                # Allow user to choose the number of coefficients to save in a text file
                save_coefficients(dct_values)

                status_label.config(text="DCT computed successfully!")
            except Exception as e:
                status_label.config(text=f"Error: {str(e)}")

    def save_coefficients(dct_values):
        try:
            m = int(entry.get())
            if m > len(dct_values):
                m = len(dct_values)
            selected_values = dct_values[:m]

            output_file = filedialog.asksaveasfilename(title="Save Coefficients As", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            if output_file:
                with open(output_file, 'w') as file:
                    for idx, val in enumerate(selected_values):
                        file.write(f" {0 } {val}\n")
                status_label.config(text=f"Saved {m} coefficients to file!")
        except ValueError:
            status_label.config(text="Please enter a valid number for 'm'.")

    def calculate_mean():
        input_file = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text Files", "*.txt")])
        if input_file:
            try:
                with open(input_file, 'r') as file:
                    signal_values = [float(line.strip().split()[1]) for line in file.readlines()]

                mean_value = sum(signal_values) / len(signal_values)
                new_values = [val - mean_value for val in signal_values]

                text_view.delete(1.0, tk.END)
                for idx, val in enumerate(new_values):
                    text_view.insert(tk.END, f"{idx}  {val}\n")


                plt.figure(figsize=(6, 4))
                plt.plot(new_values)
                plt.title("New Samples after Removing DC")
                plt.xlabel("Index")
                plt.ylabel("Value")
                plt.show()

                status_label.config(text="New values displayed successfully!")
            except Exception as e:
                status_label.config(text=f"Error: {str(e)}")

    root = tk.Tk()
    root.title("Digital Signal Processing")


    compute_button = tk.Button(root, text="Compute DCT", command=compute_dct)
    compute_button.pack(pady=20)

    entry_label = tk.Label(root, text="Choose number of coefficients (m) to save:")
    entry_label.pack()
    entry = tk.Entry(root)
    entry.pack()

    process_button = tk.Button(root, text="Remove DC", command=calculate_mean)
    process_button.pack(pady=10)

    status_label = tk.Label(root, text="")
    status_label.pack()

    text_view = tk.Text(root, height=15, width=50)
    text_view.pack(pady=10)

    root.geometry('500x520')
    root.mainloop()
