import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve


def openform6():
    def show_new_widget():
        # Hide initial widgets

        # transition_button.pack_forget()
        # compute_button.pack_forget()
        # entry_label.pack_forget()
        # entry.pack_forget()
        # text_view.pack_forget()
        # status_label.pack_forget()
        # process_button.pack_forget()

        # Show new widget and back button

        Shift_Fold_Signal.pack(pady=10)
        SHARP.pack(pady=10)
        input_label.pack(pady=2)
        input_points.pack(pady=2)
        SMOOTH.pack(pady=10)
        delay_label.pack(pady=2)
        delay_input.pack(pady=2)
        DELAY.pack(pady=10)
        delay_fold_label.pack(pady=2)
        delay_fold_input.pack(pady=2)
        delayfoldbutton.pack(pady=10)
        CONVOLVE.pack(pady=10)
        REMOVE_DC.pack(pady=10)
        # back_button.pack(pady=10)

    # def return_to_main_widget():
    #     # Hide new widget and back button
    #     new_widget.pack_forget()
    #     back_button.pack_forget()
    #     Shift_Fold_Signal.pack_forget()
    #     SHARP.pack_forget()
    #     SMOOTH.pack_forget()
    #     DELAY.pack_forget()
    #     CONVOLVE.pack_forget()
    #     input_label.pack_forget()
    #     input_points.pack_forget()
    #     delay_input.pack_forget()
    #     delay_label.pack_forget()
    #     REMOVE_DC.pack_forget()
    #     delay_fold_label.pack_forget()
    #     delay_fold_input.pack_forget()
    #     delayfoldbutton.pack_forget()
    #     # Show initial widgets
    #     transition_button.pack(pady=10)
    #     compute_button.pack(pady=10)
    #     entry_label.pack(pady=10)
    #     entry.pack(pady=10)
    #     process_button.pack(pady=10)
    #     text_view.pack(pady=10)
    #     status_label.pack(pady=0.5)

    # def compute_dct():
    #     input_file = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text Files", "*.txt")])
    #     if input_file:
    #         try:
    #             with open(input_file, 'r') as file:
    #                 signal_values = [float(line.strip()) for line in file.readlines()]
    #
    #             N = len(signal_values)
    #             dct_values = []
    #
    #             for k in range(N):
    #                 sum_val = 0
    #                 for n in range(N):
    #                     sum_val += signal_values[n] * np.cos(np.pi / (4 * N) * (2 * n - 1) * (2 * k - 1))
    #                 dct_val = np.sqrt(2 / N) * sum_val
    #                 dct_values.append(dct_val)
    #
    #             # Display DCT result in the text view
    #             text_view.delete(1.0, tk.END)
    #             text_view.insert(tk.END, f"DCT Result:\n")
    #             for idx, val in enumerate(dct_values):
    #                 text_view.insert(tk.END, f" {0 } {val}\n")
    #
    #             # Allow user to choose the number of coefficients to save in a text file
    #             save_coefficients(dct_values)
    #
    #             status_label.config(text="DCT computed successfully!")
    #         except Exception as e:
    #             status_label.config(text=f"Error: {str(e)}")
    #
    # def save_coefficients(dct_values):
    #     try:
    #         m = int(entry.get())
    #         if m > len(dct_values):
    #             m = len(dct_values)
    #         selected_values = dct_values[:m]
    #
    #         output_file = filedialog.asksaveasfilename(title="Save Coefficients As", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    #         if output_file:
    #             with open(output_file, 'w') as file:
    #                 for idx, val in enumerate(selected_values):
    #                     file.write(f" {0 } {val}\n")
    #             status_label.config(text=f"Saved {m} coefficients to file!")
    #     except ValueError:
    #         status_label.config(text="Please enter a valid number for 'm'.")
    #
    # def calculate_mean():
    #     input_file = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text Files", "*.txt")])
    #     if input_file:
    #         try:
    #             with open(input_file, 'r') as file:
    #                 signal_values = [float(line.strip()) for line in file.readlines()]
    #
    #             mean_value = sum(signal_values) / len(signal_values)
    #             new_values = [val - mean_value for val in signal_values]
    #
    #             text_view.delete(1.0, tk.END)
    #             for idx, val in enumerate(new_values):
    #                 text_view.insert(tk.END, f"{idx}  {val}\n")
    #
    #
    #             plt.figure(figsize=(6, 4))
    #             plt.plot(new_values)
    #             plt.title("New Samples after Removing DC")
    #             plt.xlabel("Index")
    #             plt.ylabel("Value")
    #             plt.show()
    #
    #             status_label.config(text="New values displayed successfully!")
    #         except Exception as e:
    #             status_label.config(text=f"Error: {str(e)}")

    #TASK_6_FUNCTIONS:___________________________________

    def fold_signal(signal):
        folded_signal = np.flip(signal)
        return folded_signal
    def fold():
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            signal = np.loadtxt(file_path,usecols=1)
            plt.figure(figsize=(8, 4))

            plt.subplot(211)
            plt.plot(signal, label='Original Signal')
            plt.title('Original Signal')

            folded_signal = fold_signal(signal)
            plt.subplot(212)
            plt.plot(folded_signal, label='Folded Signal')
            plt.title('Folded Signal')

            plt.tight_layout()
            plt.legend()
            plt.show()
    def first_derivative(signal):
        first_deriv = np.diff(signal)
        return first_deriv
    def second_derivative(signal):
        second_deriv = np.diff(signal, n=2)
        return second_deriv
    def sharp():
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            signal = np.loadtxt(file_path,usecols=1)
            plt.figure(figsize=(8, 6))

            plt.subplot(311)
            plt.plot(signal, label='Original Signal')
            plt.title('Original Signal')

            first_deriv = first_derivative(signal)
            plt.subplot(312)
            plt.plot(first_deriv, label='First Derivative')
            plt.title('First Derivative')

            second_deriv = second_derivative(signal)
            plt.subplot(313)
            plt.plot(second_deriv, label='Second Derivative')
            plt.title('Second Derivative')

            plt.tight_layout()
            plt.legend()
            plt.show()
    def smooth(signal, num_points):
       smoothed_signal = np.convolve(signal, np.ones(num_points) / num_points, mode='valid')
       return smoothed_signal
    def browse_file():
       file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
       if file_path:
            signal = np.loadtxt(file_path,usecols=1)
            plt.figure(figsize=(8, 4))

            plt.subplot(211)
            plt.plot(signal, label='Original Signal')
            plt.title('Original Signal')

            num_points = int(input_points.get())
            smoothed_signal = smooth(signal, num_points)

            plt.subplot(212)
            plt.plot(smoothed_signal, label=f'Smoothed Signal (Moving Average {num_points})')
            plt.title(f'Smoothed Signal (Moving Average {num_points})')

            plt.tight_layout()
            plt.legend()
            plt.show()
    def shift_signal(signal, k):
        shifted_signal = np.roll(signal, k)
        return shifted_signal
    def delay():
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
             signal = np.loadtxt(file_path,usecols=1)
             k = int(delay_input.get())
             shifted_signal = shift_signal(signal, k)

             plt.figure(figsize=(8, 4))
             plt.subplot(211)
             plt.plot(signal, label='Original Signal')
             plt.title('Original Signal')

             plt.subplot(212)
             plt.plot(shifted_signal, label=f'Shifted Signal by {k} steps')
             plt.title(f'Shifted Signal by {k} steps')

             plt.tight_layout()
             plt.legend()
             plt.show()
    def convolve_signals(signal1, signal2):
        convolved_signal = np.convolve(signal1[:], signal2[:], mode='full')
        return convolved_signal
    def load_signal(file_path):
        data = np.loadtxt(file_path,usecols=1)
        return data
    def conv():
        file_path_1 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path_1:
            signal1 =np.loadtxt(file_path_1,usecols=1)

            file_path_2 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
            if file_path_2:
                signal2 =np.loadtxt(file_path_2,usecols=1)

                convolved_signal = convolve_signals(signal1, signal2)

                plt.figure(figsize=(8, 6))
                plt.subplot(311)
                plt.plot(signal1[:], label='Signal 1')
                plt.title('Signal 1')

                plt.subplot(312)
                plt.plot(signal2[:], label='Signal 2')
                plt.title('Signal 2')

                plt.subplot(313)
                plt.plot(convolved_signal, label='Convolved Signal')
                plt.title('Convolved Signal')

                plt.tight_layout()
                plt.legend()
                plt.show()


    def remove_dc(signal):
        fft_signal = np.fft.fft(signal)
        fft_signal[0] = 0  # Zero out DC component at index 0
        filtered_signal = np.fft.ifft(fft_signal)
        return filtered_signal.real  # Take the real part of the inverse FFT result
    def load(file_path):
        data = np.loadtxt(file_path,usecols=1)
        return data
    def remove():
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            signal = np.loadtxt(file_path,usecols=1)
            filtered_signal = remove_dc(signal[:])  # Assuming the second column contains samples

            plt.figure(figsize=(8, 4))
            plt.subplot(211)
            plt.plot(signal[:], label='Original Signal')
            plt.title('Original Signal')

            plt.subplot(212)
            plt.plot(filtered_signal, label='Signal with DC Component Removed')
            plt.title('Signal with DC Component Removed')

            plt.tight_layout()
            plt.legend()
            plt.show()
    def delay_advance(signal, k):
        delayed_signal = np.roll(signal, k)
        return delayed_signal
    def delayfold():
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            signal = np.loadtxt(file_path,usecols=1)
            folded_signal = fold_signal(signal)

            k = int(delay_fold_input.get())
            delayed_signal = delay_advance(folded_signal, k)

            plt.figure(figsize=(8, 4))
            plt.subplot(211)
            plt.plot(folded_signal, label='Folded Signal')
            plt.title('Folded Signal')

            plt.subplot(212)
            plt.plot(delayed_signal, label=f'Delayed/Advanced Folded Signal by {k} steps')
            plt.title(f'Delayed/Advanced Folded Signal by {k} steps')

            plt.tight_layout()
            plt.legend()
            plt.show()

    #______________________________________________________
    root = tk.Tk()
    root.title("Digital Signal Processing")

    # Main widget
    # transition_button = tk.Button(root, text=" TASK 6 ", command=show_new_widget)
    # transition_button.pack(pady=20)

    # New widget
    # new_widget = tk.Label(root, text="Task 6")
    # back_button = tk.Button(root, text=" Back ", command=return_to_main_widget)

    # compute_button = tk.Button(root, text="Compute DCT", command=compute_dct)
    # compute_button.pack(pady=20)

    Shift_Fold_Signal = tk.Button(root, text="FOLD", command=fold)
    SHARP = tk.Button(root, text="SHARP", command=sharp)
    SMOOTH = tk.Button(root, text="SMOOTH", command=browse_file)
    CONVOLVE = tk.Button(root, text="CONVOLVE", command=conv)
    DELAY = tk.Button(root, text="DELAY/ADVANCE", command=delay)
    REMOVE_DC = tk.Button(root, text="REMOVE DC", command=remove)
    input_label = tk.Label(root, text="Enter number of points for moving average:")
    input_points = tk.Entry(root)
    delay_label = tk.Label(root, text="Enter number of K Steps:")
    delay_input = tk.Entry(root)
    delay_fold_label = tk.Label(root, text="Enter number of K Steps:")
    delay_fold_input = tk.Entry(root)
    delayfoldbutton=tk.Button(root, text="DELAY/ADVANCE(folded)", command=delayfold)

    # entry_label = tk.Label(root, text="Choose number of coefficients (m) to save:")
    # entry_label.pack()
    # entry = tk.Entry(root)
    # entry.pack()


    # process_button = tk.Button(root, text="Remove DC", command=calculate_mean)
    # process_button.pack(pady=10)
    #
    # status_label = tk.Label(root, text="")
    # status_label.pack()

    # text_view = tk.Text(root, height=15, width=50)
    # text_view.pack(pady=10)

    show_new_widget()
    root.geometry('510x510')
    root.mainloop()
