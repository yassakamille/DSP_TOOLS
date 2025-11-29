import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
import warnings as wrng

wrng.filterwarnings("ignore")


def openform1():
    def plot_signal():
        def read_signal_samples():
            input_file = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text Files", "*.txt")])
            if input_file:
                try:
                    with open(input_file, 'r') as file:
                        signal_values = [float(line.strip().split()[1]) for line in file.readlines()]
                        return signal_values
                except Exception:
                    print("error read from text only")

        data = read_signal_samples()
        plt.figure()

        # Continuous representation
        plt.subplot(2, 1, 1)
        plt.plot(data, 'b-', label='Continuous')
        plt.title('Continuous Representation')
        plt.xlabel('Sample Index')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.legend()

        # Discrete representation
        plt.subplot(2, 1, 2)
        plt.stem(data, linefmt='g-', markerfmt='go', basefmt='r-')
        plt.title('Discrete Representation')
        plt.xlabel('Sample Index')
        plt.ylabel('Amplitude')
        plt.grid(True)

        plt.tight_layout()
        plt.show()

    def generate_signal():
        amplitude = float(amplitude_entry.get())
        analog_frequency = float(frequency_entry.get())
        phase_shift = float(duration_entry.get())
        sampling_frequency = float(sample_rate_entry.get())

        t = np.arange(0, 1, 1 / sampling_frequency)  # Time vector

        if signal_type_var.get() == "Sine":
            signal = amplitude * np.sin(2 * np.pi * analog_frequency * t + phase_shift)
        else:
            signal = amplitude * np.cos(2 * np.pi * analog_frequency * t + phase_shift)

        if signal_mode_var.get() == "Discrete":
            print("asd")
            plt.clf()  # Clear the current plot
            plt.stem(t, signal, linefmt='b-', markerfmt='bo', basefmt='r-')
            plt.xlabel('Sample')
            plt.ylabel('Amplitude')
            plt.title('Discrete Signal')
            plt.grid(True)
            fig = plt
            fig.show()

            plt.close()
        else:
            plt.clf()  # Clear the current plot
            plt.plot(t, signal)
            plt.xlabel('Time')
            plt.ylabel('Amplitude')
            plt.title('Continuous Signal')
            plt.grid(True)
            fig2 = plt
            fig2.show()

            plt.close()

    app = tk.Tk()
    app.title("Signal Generator")

    frame = ttk.Frame(app)
    frame.grid(row=0, column=0)

    btn = tk.Button(app, text="read samples", command=plot_signal)
    btn.grid(row=8, column=0)

    signal_type_label = ttk.Label(frame, text="Signal Type:")
    signal_type_label.grid(row=0, column=0)
    signal_type_var = tk.StringVar(value="Sine")
    sine_radio = ttk.Radiobutton(frame, text="Sine", variable=signal_type_var, value="Sine")
    cosine_radio = ttk.Radiobutton(frame, text="Cosine", variable=signal_type_var, value="Cosine")
    sine_radio.grid(row=0, column=1)
    cosine_radio.grid(row=0, column=2)

    signal_mode_label = ttk.Label(frame, text="Signal Mode:")
    signal_mode_label.grid(row=1, column=0)
    signal_mode_var = tk.StringVar(value="")
    continuous_radio = ttk.Radiobutton(frame, text="Continuous", variable=signal_mode_var, value="Continuous")
    discrete_radio = ttk.Radiobutton(frame, text="Discrete", variable=signal_mode_var, value="Discrete")
    continuous_radio.grid(row=1, column=1)
    discrete_radio.grid(row=1, column=2)

    amplitude_label = ttk.Label(frame, text="Amplitude(A):")
    amplitude_label.grid(row=2, column=0)
    amplitude_entry = ttk.Entry(frame)
    amplitude_entry.grid(row=2, column=1)

    frequency_label = ttk.Label(frame, text="Analog Frequency (Hz):")
    frequency_label.grid(row=3, column=0)
    frequency_entry = ttk.Entry(frame)
    frequency_entry.grid(row=3, column=1)

    duration_label = ttk.Label(frame, text="PhaseShift :")
    duration_label.grid(row=4, column=0)
    duration_entry = ttk.Entry(frame)
    duration_entry.grid(row=4, column=1)

    sample_rate_label = ttk.Label(frame, text="Sampling Frequency (Hz):")
    sample_rate_label.grid(row=5, column=0)
    sample_rate_entry = ttk.Entry(frame)
    sample_rate_entry.grid(row=5, column=1)

    generate_button = ttk.Button(frame, text="Generate Signal", command=generate_signal)
    generate_button.grid(row=6, column=0, columnspan=3)

    app.mainloop()
# openform1()
