import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt

def openform5():
    signal_values = []

    def load_file():
        nonlocal signal_values
        input_file = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text Files", "*.txt")])
        if input_file:
            try:
                with open(input_file, 'r') as file:
                    signal_values = [float(line.strip().split()[1]) for line in file.readlines()]
                text_view.delete(1.0, tk.END)
                for idx, val in enumerate(signal_values):
                    text_view.insert(tk.END, f"{idx}  {val}\n")
                status_label.config(text=f"Loaded {len(signal_values)} samples successfully!")
            except Exception as e:
                status_label.config(text=f"Error: {str(e)}")

    def compute_dct():
        if not signal_values:
            status_label.config(text="Please load a signal first!")
            return
        try:
            m = int(entry.get())
        except ValueError:
            status_label.config(text="Please enter a valid number for m!")
            return

        N = len(signal_values)
        dct_values = []
        for k in range(N):
            sum_val = 0
            for n in range(N):
                sum_val += signal_values[n] * np.cos(np.pi / (4 * N) * (2 * n - 1) * (2 * k - 1))
            dct_val = np.sqrt(2 / N) * sum_val
            dct_values.append(dct_val)

        # Display DCT result
        text_view.delete(1.0, tk.END)
        text_view.insert(tk.END, "DCT Result:\n")
        for idx, val in enumerate(dct_values):
            text_view.insert(tk.END, f"{idx} {val}\n")

        # Automatically save first m coefficients
        if m > len(dct_values):
            m = len(dct_values)
        selected_values = dct_values[:m]

        output_file = "dct_coefficients.txt"
        with open(output_file, 'w') as file:
            for idx, val in enumerate(selected_values):
                file.write(f"{idx} {val}\n")

        status_label.config(text=f"DCT computed and first {m} coefficients saved to {output_file}!")

    def remove_dc():
        if not signal_values:
            status_label.config(text="Please load a signal first!")
            return
        mean_value = sum(signal_values) / len(signal_values)
        zero_mean = [val - mean_value for val in signal_values]

        text_view.delete(1.0, tk.END)
        text_view.insert(tk.END, "Zero-Mean Signal:\n")
        for idx, val in enumerate(zero_mean):
            text_view.insert(tk.END, f"{idx}  {val}\n")

        plt.figure(figsize=(8, 4))
        plt.stem(signal_values, linefmt='b-', markerfmt='bo', basefmt='b', label='Original')
        plt.stem(zero_mean, linefmt='r-', markerfmt='ro', basefmt='r', label='Zero-Mean')
        plt.title("Original vs Zero-Mean Signal")
        plt.xlabel("Index")
        plt.ylabel("Amplitude")
        plt.legend()
        plt.show()
        status_label.config(text="Zero-mean signal displayed successfully!")

    root = tk.Tk()
    root.title("Digital Signal Processing")

    load_button = tk.Button(root, text="Load Signal", command=load_file)
    load_button.pack(pady=10)

    compute_button = tk.Button(root, text="Compute DCT", command=compute_dct)
    compute_button.pack(pady=10)

    entry_label = tk.Label(root, text="Number of coefficients (m) to save:")
    entry_label.pack()
    entry = tk.Entry(root)
    entry.pack()

    dc_button = tk.Button(root, text="Remove DC (time-domain)", command=remove_dc)
    dc_button.pack(pady=10)

    status_label = tk.Label(root, text="")
    status_label.pack()

    text_view = tk.Text(root, height=15, width=50)
    text_view.pack(pady=10)

    root.geometry('500x600')
    root.mainloop()
