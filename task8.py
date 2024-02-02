import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import numpy as np
from PIL import ImageTk, Image
def openform8():
    def show_convolution():
        # Hide initial widgets
        frame1.pack_forget()
        # Show new widget and back button
        frame.pack()

    def show_correlation():
        # Hide initial widgets
        frame.pack_forget()
        # Show new widget and back button
        frame1.pack()

    def open_file(index):
        file_path = filedialog.askopenfilename()
        if index == 1:
            entry_file1.delete(0, tk.END)
            entry_file1.insert(tk.END, file_path)
        elif index == 2:
            entry_file2.delete(0, tk.END)
            entry_file2.insert(tk.END, file_path)

    def zero_pad_and_convolve(file_path1, file_path2):
        try:
            # Read signals from files
            signal1 = np.loadtxt(file_path1)
            signal2 = np.loadtxt(file_path2)

            # Extract indices and samples from signals
            indices1, samples1 = signal1[:, 0], signal1[:, 1]
            indices2, samples2 = signal2[:, 0], signal2[:, 1]

            # Compute new signal size and zero pad signals
            new_size = len(samples1) + len(samples2) - 1
            padded_samples1 = np.pad(samples1, (0, new_size - len(samples1)), mode='constant')
            padded_samples2 = np.pad(samples2, (0, new_size - len(samples2)), mode='constant')

            # Increase indices
            new_indices = np.arange(new_size)

            # Convert signals to frequency domain using DFT
            dft_signal1 = np.fft.fft(padded_samples1)
            dft_signal2 = np.fft.fft(padded_samples2)

            # Multiply signals' harmonics in the frequency domain
            convolution_freq_domain = dft_signal1 * dft_signal2

            # Apply Inverse Discrete Fourier Transform (IDFT)
            convolution_time_domain = np.fft.ifft(convolution_freq_domain)

            # Save the new samples in a list
            new_samples = convolution_time_domain.real.tolist()

            return new_indices, new_samples

        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred: {e}")

    def perform_convolution():
        file_path1 = entry_file1.get()
        file_path2 = entry_file2.get()
        expected_indices = [-2, -1, 0, 1, 2, 3, 4, 5, 6]
        if file_path1 and file_path2:
            new_indices, new_samples = zero_pad_and_convolve(file_path1, file_path2)
            print("New Indices:", expected_indices)
            print("New Samples:", new_samples)


            # ConvTest(expected_indices, new_samples)
            plt.plot(new_samples)
            plt.show()

    def correlation(file_path1, file_path2):
        try:
            # Read signals from files
            signal1 = np.loadtxt(file_path1)
            signal2 = np.loadtxt(file_path2)

            # Extract samples from signals
            samples1 = signal1[:, 1]
            samples2 = signal2[:, 1]

            # Convert signals to frequency domain using DFT
            dft_signal1 = np.fft.fft(samples1)
            dft_signal2 = np.fft.fft(samples2)

            # Get the conjugate of signal 1 (you can also use signal 2)
            conjugate_signal1 = np.conj(dft_signal1)

            # Multiply conjugate with signal 2 (or vice versa)
            correlation_freq_domain = conjugate_signal1 * dft_signal2

            # Apply Inverse Discrete Fourier Transform (IDFT) on the result
            correlation_time_domain = np.fft.ifft(correlation_freq_domain)

            # Return the correlation result in time domain
            return correlation_time_domain.real/5

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def perform_correlation():
        file_path1 = entry_file1.get()
        file_path2 = entry_file2.get()
        file_test = "Corr_Output.txt"
        indicies=[0,1,2,3,4]
        if file_path1 and file_path2:
            new_samples = correlation(file_path1, file_path2)

            print("New Samples:", new_samples)


            # Compare_Signals(file_test,indicies,new_samples)
            plt.plot(new_samples)
            plt.show()

    # def ConvTest(Your_indices, Your_samples):
    #             """
    #             Test inputs
    #             InputIndicesSignal1 =[-2, -1, 0, 1]
    #             InputSamplesSignal1 = [1, 2, 1, 1 ]
    #
    #             InputIndicesSignal2=[0, 1, 2, 3, 4, 5 ]
    #             InputSamplesSignal2 = [ 1, -1, 0, 0, 1, 1 ]
    #             """
    #
    #             expected_indices = [-2, -1, 0, 1, 2, 3, 4, 5, 6]
    #             expected_samples = [1, 1, -1, 0, 0, 3, 3, 2, 1]
    #
    #             if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
    #                 print("Conv Test case failed, your signal have different length from the expected one")
    #                 return
    #             for i in range(len(Your_indices)):
    #                 if (Your_indices[i] != expected_indices[i]):
    #                     print("Conv Test case failed, your signal have different indicies from the expected one")
    #                     return
    #             for i in range(len(expected_samples)):
    #                 if abs(Your_samples[i] - expected_samples[i]) < 0.01:
    #                     continue
    #                 else:
    #                     print("Conv Test case failed, your signal have different values from the expected one")
    #                     return
    #             print("Conv Test case passed successfully")

    # def Compare_Signals(file_name,Your_indices,Your_samples):
    #     expected_indices=[]
    #     expected_samples=[]
    #     with open(file_name, 'r') as f:
    #         line = f.readline()
    #         line = f.readline()
    #         line = f.readline()
    #         line = f.readline()
    #         while line:
    #             # process line
    #             L=line.strip()
    #             if len(L.split(' '))==2:
    #                 L=line.split(' ')
    #                 V1=int(L[0])
    #                 V2=float(L[1])
    #                 expected_indices.append(V1)
    #                 expected_samples.append(V2)
    #                 line = f.readline()
    #             else:
    #                 break
    #     print("Current Output Test file is: ")
    #     print(file_name)
    #     print("\n")
    #     if (len(expected_samples)!=len(Your_samples)) and (len(expected_indices)!=len(Your_indices)):
    #         print("Shift_Fold_Signal Test case failed, your signal have different length from the expected one")
    #         return
    #     for i in range(len(Your_indices)):
    #         if(Your_indices[i]!=expected_indices[i]):
    #             print("Shift_Fold_Signal Test case failed, your signal have different indicies from the expected one")
    #             return
    #     for i in range(len(expected_samples)):
    #         if abs(Your_samples[i] - expected_samples[i]) < 0.01:
    #             continue
    #         else:
    #             print("Correlation Test case failed, your signal have different values from the expected one")
    #             return
    #     print("Correlation Test case passed successfully")

    # Create the GUI
    root = tk.Tk()
    root.title("DSP Tasks")

    frame0 = tk.Frame(root)

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    frame1 = tk.Frame(root)
    frame1.pack(padx=10, pady=10)

    label_file3 = tk.Label(frame1, text="Select File 1:")
    label_file3.grid(row=0, column=0)

    entry_file3 = tk.Entry(frame1, width=50)
    entry_file3.grid(row=0, column=1)

    button_browse3 = tk.Button(frame1, text="Browse", command=lambda: open_file(1))
    button_browse3.grid(row=0, column=2)

    label_file3 = tk.Label(frame1, text="Select File 2:")
    label_file3.grid(row=1, column=0)

    entry_file3 = tk.Entry(frame1, width=50)
    entry_file3.grid(row=1, column=1)

    button_browse4 = tk.Button(frame1, text="Browse", command=lambda: open_file(2))
    button_browse4.grid(row=1, column=2)

    button_correlation = tk.Button(frame1, text="Perform Correlation", command=perform_correlation)
    button_correlation.grid(row=2, column=0, columnspan=3,pady=10)

    label_file1 = tk.Label(frame, text="Select File 1:")
    label_file1.grid(row=0, column=0)

    entry_file1 = tk.Entry(frame, width=50)
    entry_file1.grid(row=0, column=1)

    button_browse1 = tk.Button(frame, text="Browse", command=lambda: open_file(1))
    button_browse1.grid(row=0, column=2)

    label_file2 = tk.Label(frame, text="Select File 2:")
    label_file2.grid(row=1, column=0)

    entry_file2 = tk.Entry(frame, width=50)
    entry_file2.grid(row=1, column=1)

    button_browse2 = tk.Button(frame, text="Browse", command=lambda: open_file(2))
    button_browse2.grid(row=1, column=2)

    button_convolution = tk.Button(frame, text="Perform Convolution", command=perform_convolution)
    button_convolution.grid(row=2, column=0, columnspan=3, pady=10)

    # image_path = "images.jpg"
    # img = Image.open(image_path)
    #
    # img = img.resize((50, 50), Image.RASTERIZE)
    # img = ImageTk.PhotoImage(img)
    #
    # image_label = tk.Label(root, image=img)
    # image_label.pack(side=tk.TOP)
    #
    # custom_font = ("Times new roman", 15,"bold")
    # text_label=tk.Label(root, text="Welcome to DSP Task 8",font=custom_font,fg="red")
    # text_label.pack()

    button_browse0 = tk.Button(frame0, text="Fast Convolution", command=lambda: show_convolution())
    button_browse0.grid(row=1, column=0)

    button_browse5 = tk.Button(frame0, text="Fast Correlation", command=lambda: show_correlation())
    button_browse5.grid(row=1, column=3)

    frame0.pack(padx=10, pady=10)
    frame.pack_forget()
    frame1.pack_forget()

    root.geometry('500x220')
    root.mainloop()
