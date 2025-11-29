import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np

def openform8():
    signal_file1 = ""
    signal_file2 = ""

    def open_file(index):
        nonlocal signal_file1, signal_file2
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            if index == 1:
                entry_file1.delete(0, tk.END)
                entry_file1.insert(tk.END, file_path)
                signal_file1 = file_path
            elif index == 2:
                entry_file2.delete(0, tk.END)
                entry_file2.insert(tk.END, file_path)
                signal_file2 = file_path

    def zero_pad_and_convolve(file_path1, file_path2):
        try:
            signal1 = np.loadtxt(file_path1)[:, 1]
            signal2 = np.loadtxt(file_path2)[:, 1]

            new_size = len(signal1) + len(signal2) - 1
            padded1 = np.pad(signal1, (0, new_size - len(signal1)))
            padded2 = np.pad(signal2, (0, new_size - len(signal2)))

            conv_time = np.fft.ifft(np.fft.fft(padded1) * np.fft.fft(padded2)).real
            new_indices = np.arange(new_size)
            return new_indices, conv_time
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            return None, None

    def correlation(file_path1, file_path2):
        try:
            signal1 = np.loadtxt(file_path1)[:, 1]
            signal2 = np.loadtxt(file_path2)[:, 1]

            corr_time = np.fft.ifft(np.conj(np.fft.fft(signal1)) * np.fft.fft(signal2)).real
            indices = np.arange(len(corr_time))
            return indices, corr_time
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            return None, None

    def perform_convolution():
        if not signal_file1 or not signal_file2:
            messagebox.showwarning("Warning", "Please select both signal files!")
            return
        indices, samples = zero_pad_and_convolve(signal_file1, signal_file2)
        if samples is not None:
            plt.figure(figsize=(8,4))
            plt.stem(indices, samples)
            plt.title("Fast Convolution Result")
            plt.xlabel("Index")
            plt.ylabel("Amplitude")
            plt.show()

    def perform_correlation():
        if not signal_file1 or not signal_file2:
            messagebox.showwarning("Warning", "Please select both signal files!")
            return
        indices, samples = correlation(signal_file1, signal_file2)
        if samples is not None:
            plt.figure(figsize=(8,4))
            plt.stem(indices, samples)
            plt.title("Fast Correlation Result")
            plt.xlabel("Index")
            plt.ylabel("Amplitude")
            plt.show()

    root = tk.Tk()
    root.title("Fast Convolution and Correlation")

    # File selection
    tk.Label(root, text="Select File 1:").grid(row=0, column=0)
    entry_file1 = tk.Entry(root, width=50)
    entry_file1.grid(row=0, column=1)
    tk.Button(root, text="Browse", command=lambda: open_file(1)).grid(row=0, column=2)

    tk.Label(root, text="Select File 2:").grid(row=1, column=0)
    entry_file2 = tk.Entry(root, width=50)
    entry_file2.grid(row=1, column=1)
    tk.Button(root, text="Browse", command=lambda: open_file(2)).grid(row=1, column=2)

    # Operation buttons
    tk.Button(root, text="Perform Fast Convolution", command=perform_convolution).grid(row=2, column=0, columnspan=3, pady=10)
    tk.Button(root, text="Perform Fast Correlation", command=perform_correlation).grid(row=3, column=0, columnspan=3, pady=10)

    root.geometry('425x150')
    root.mainloop()
