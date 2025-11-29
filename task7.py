import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Each window will have its own state
def openform7():
    # New window
    new_root = tk.Toplevel()
    new_root.title("Signal Toolbox")

    # State for this window
    state = {
        "signal": None,
        "indices": None,
        "X": None,
        "N": 0,
        "canvas": None,
        "fig": None,
        "edit_entries": [],
    }

    # Frame for buttons and plots
    frame = tk.Frame(new_root)
    frame.pack(fill="both", expand=True)

    # --- Functions using state dict ---
    def close_canvas():
        if state["canvas"] is not None:
            try:
                state["canvas"].get_tk_widget().pack_forget()
            except:
                pass
            state["canvas"] = None
        state["fig"] = None

    def plot_time_signal():
        if state["signal"] is None:
            return
        close_canvas()
        state["fig"] = plt.Figure(figsize=(6,3))
        ax = state["fig"].add_subplot(111)
        ax.plot(state["indices"], state["signal"], marker='o')
        ax.set_title("Time-domain signal")
        ax.set_xlabel("Sample index")
        ax.set_ylabel("Amplitude")
        ax.grid(True)
        state["canvas"] = FigureCanvasTkAgg(state["fig"], master=frame)
        state["canvas"].get_tk_widget().pack(fill="both", expand=True)
        state["canvas"].draw()

    def load_signal_file():
        path = filedialog.askopenfilename(filetypes=[("Text Files","*.txt"),("All files","*.*")])
        if not path:
            return
        inds, vals = [], []
        with open(path,'r') as f:
            for line in f:
                s=line.strip()
                if not s: continue
                parts=s.split()
                if len(parts)>=2:
                    try:
                        inds.append(int(parts[0]))
                        vals.append(float(parts[1]))
                    except:
                        try:
                            vals.append(float(parts[0]))
                        except:
                            continue
        if len(vals)==0:
            messagebox.showerror("Error","No numeric samples found")
            return
        state["signal"] = np.array(vals)
        state["indices"] = np.array(inds) if len(inds)==len(vals) else np.arange(len(state["signal"]))
        messagebox.showinfo("Loaded","Signal loaded: {} samples".format(len(state["signal"])))
        plot_time_signal()

    def apply_fft():
        if state["signal"] is None:
            messagebox.showwarning("No signal","Load a time signal first")
            return
        state["X"] = np.fft.fft(state["signal"])
        state["N"] = len(state["signal"])
        messagebox.showinfo("DFT","DFT computed for N={} bins".format(state["N"]))

    def show_freq_plots():
        if state["X"] is None:
            messagebox.showwarning("No DFT","Apply Fourier Transform first")
            return
        mag = np.abs(state["X"])
        phase = np.angle(state["X"])
        close_canvas()
        state["fig"] = plt.Figure(figsize=(8,6))
        ax1 = state["fig"].add_subplot(211)
        k = np.arange(len(mag))
        ax1.stem(k, mag)
        ax1.set_title("DFT magnitude |X[k]|")
        ax1.set_xlabel("Bin index k")
        ax1.set_ylabel("Magnitude")
        ax1.grid(True)
        ax2 = state["fig"].add_subplot(212)
        ax2.stem(k, phase)
        ax2.set_title("DFT phase ∠X[k] (radians)")
        ax2.set_xlabel("Bin index k")
        ax2.set_ylabel("Phase")
        ax2.grid(True)
        state["canvas"] = FigureCanvasTkAgg(state["fig"], master=frame)
        state["canvas"].get_tk_widget().pack(fill="both", expand=True)
        state["canvas"].draw()

    def reconstruct_and_plot():
        if state["X"] is None:
            messagebox.showwarning("No DFT","Apply Fourier Transform or load components first")
            return
        x_rec = np.fft.ifft(state["X"])
        x_rec = np.real_if_close(x_rec, tol=1000)
        close_canvas()
        state["fig"] = plt.Figure(figsize=(6,3))
        ax = state["fig"].add_subplot(111)
        x_idx = state["indices"] if state["indices"] is not None else np.arange(len(x_rec))
        ax.plot(x_idx, x_rec, marker='o')
        ax.set_title("Reconstructed signal (IDFT)")
        ax.set_xlabel("Sample index")
        ax.set_ylabel("Amplitude")
        ax.grid(True)
        state["canvas"] = FigureCanvasTkAgg(state["fig"], master=frame)
        state["canvas"].get_tk_widget().pack(fill="both", expand=True)
        state["canvas"].draw()
        if state["signal"] is not None and len(state["signal"])==len(x_rec):
            err = np.max(np.abs(state["signal"]-x_rec))
            messagebox.showinfo("Reconstruction","IDFT complete. Max abs error: {:.3e}".format(err))
        else:
            messagebox.showinfo("Reconstruction","IDFT complete")

    # --- Buttons ---
    btn_frame = tk.Frame(frame)
    btn_frame.pack(side="top", fill="x", padx=6, pady=6)
    tk.Button(btn_frame, text="Load time signal", command=load_signal_file).pack(side="left", padx=4)
    tk.Button(btn_frame, text="Apply FFT", command=apply_fft).pack(side="left", padx=4)
    tk.Button(btn_frame, text="Show plots", command=show_freq_plots).pack(side="left", padx=4)
    tk.Button(btn_frame, text="Reconstruct (IDFT)", command=reconstruct_and_plot).pack(side="left", padx=4)

# Example usage: open multiple independent windows
if __name__=="__main__":
    root = tk.Tk()
    root.withdraw()  # hide main root if you want only child windows
    tk.Button(root, text="Open Signal Toolbox", command=openform7).pack(padx=20, pady=20)
    root.mainloop()
