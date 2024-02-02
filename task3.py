import tkinter as tk
from tkinter import filedialog
import numpy as np
def openform3():
    def import_samples():
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                global signal_samples
                signal_samples = [float(line.strip().split()[1]) for line in file]
            status_label.config(text=f"Samples imported from {file_path}")

    def calculate_intervals_and_replace_samples():
        if not signal_samples:
            status_label.config(text="Please import signal samples first.")
            return

        try:
            num_bits = int(bits_entry.get())
            if num_bits <= 0:
                status_label.config(text="Number of bits should be a positive integer.")
                return
        except ValueError:
            status_label.config(text="Please enter a valid number of bits.")
            return

        max_value = max(signal_samples)
        min_value = min(signal_samples)
        step_size = (max_value - min_value) / (2 ** num_bits)

        intervals = [min_value + i * step_size for i in range(2**num_bits)]
        interval_binaries = [format(i, f'0{num_bits}b') for i in range(2**num_bits)]

        sample_intervals = {}
        for sample in signal_samples:
            index = 0
            while index < len(intervals) - 1 and sample > intervals[index + 1]:
                index += 1
            sample_intervals[sample] = interval_binaries[index]

        quantized_samples = [min(intervals, key=lambda x: abs(x - sample.__round__(3))) for sample in signal_samples]

        display_intervals_and_samples(sample_intervals, quantized_samples)

    def display_intervals_and_samples(sample_intervals, quantized_samples):
        result_text.delete(1.0, tk.END)

        result_text.insert(tk.END, "\nQuantized Samples: \n")
        for sample in quantized_samples:
            result_text.insert(tk.END, f"{sample.__round__(4)}\t\n")

        result_text.insert(tk.END, "\nQuantization error: \n")
        error_sum = 0
        for sample, interval in sample_intervals.items():
            quantized_sample = min(quantized_samples, key=lambda x: abs(x - sample))
            error = sample - quantized_sample
            error_sum += error.__round__(4)
            result_text.insert(tk.END, f" Interval: {interval}, Quantized: {quantized_sample.__round__(3)}, Error: {-error.__round__(3)}\n")
        result_text.insert(tk.END, f"\nTotal Quantization Error: {error_sum}\n")



    root = tk.Tk()
    root.title("Signal Sample Analyzer")
    import_button = tk.Button(root, text="Import Signal Samples", command=import_samples)
    bits_label = tk.Label(root, text="Enter the number of bits:")
    bits_entry = tk.Entry(root)
    calculate_button = tk.Button(root, text="Calculate Intervals and Replace Samples",
                                 command=calculate_intervals_and_replace_samples)
    status_label = tk.Label(root, text="")
    result_text = tk.Text(root, height=30, width=80)
    import_button.pack()
    bits_label.pack()
    bits_entry.pack()
    calculate_button.pack()
    status_label.pack()
    result_text.pack()
    # signal_samples = None
    # Create widgets
    root.mainloop()



