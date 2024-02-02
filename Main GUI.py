import tkinter as tk
from PIL import ImageTk, Image
import requests
from io import BytesIO
from task1 import openform1
from task3 import openform3
from task5 import openform5
from task6 import openform6
from task8 import openform8
def start():
    frame.pack_forget()
    frame2.pack()
def about():
   frame.pack_forget()
   frame1.pack()
def exit():
  window.quit()
  window.destroy()
def back():
    frame2.pack_forget()
    frame1.pack_forget()
    frame.pack()
def task1():
   openform1()
def task2():
       pass
def task3():
   openform3()
def task4():
   pass
def task5():
   openform5()
def task6():
   openform6()
def task7():
   pass
def task8():
 openform8()

window = tk.Tk()
window.title("DSP TOOLS")
window.geometry('500x550')
custom_font = ("Times new roman", 15, "bold")
custom_font1 = ("Times new roman", 12, "bold")

bkg_url = "https://www.sintef.no/contentassets/151f67a6a457473eabb34c5de9e022ea/shutterstock_1236109669.jpg?width=1600&height=500&mode=crop&quality=50"
bkg_response = requests.get(bkg_url)

if bkg_response.status_code == 200:
        img_bkg_data = bkg_response.content
        bkg_image = Image.open(BytesIO(img_bkg_data))

width, height = window.winfo_screenwidth(), window.winfo_screenheight()
image = bkg_image.resize((width, height), Image.ADAPTIVE)

# Convert the image to a Tkinter-compatible format
photo_bkg = ImageTk.PhotoImage(image)

# Create a label to display the image as a background
background_label = tk.Label(window, image=photo_bkg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Ensure the image persists by keeping a reference
background_label.image = photo_bkg
# window.config(background=background_label)

url = "https://play-lh.googleusercontent.com/EsdGgqowTqXPya8AKFE1V0zh2_fkOLA6H6C-JKiiOmJFf__MogG9wsI_ASIyLXGIVdM=w240-h480-rw"
response = requests.get(url)

if response.status_code == 200:
        img_data = response.content
        image = Image.open(BytesIO(img_data))
        image =image.resize((110,110),Image.ADAPTIVE)
        photo = ImageTk.PhotoImage(image)

frame1=tk.Frame(window,width=300,bg="purple")
frame=tk.Frame(window,width=310,height=55)
frame2=tk.Frame(window,width=310,height=370,bg="white")

#about
start = tk.Button(frame, text="START", command= start,fg="blue",background="lightblue",font=custom_font1)
start.place(x=10, y=10, width=90)
about = tk.Button(frame, text="ABOUT", command= about,font=custom_font1)
about.place(x=110, y=10, width=90)
exit_button = tk.Button(frame, text="EXIT", command= exit,fg="red",background="Black",font=custom_font1)
exit_button.place(x=210, y=10, width=90)

#start
t1 = tk.Button(frame2, text="Sampling", command=task1)
t1.place(x=50, y=10, width=200)
t2 = tk.Button(frame2, text="Arithmetic Operations", command= task2)
t2.place(x=50, y=50, width=200)
t3 = tk.Button(frame2, text="Quantization", command= task3)
t3.place(x=50, y=90, width=200)
t4 = tk.Button(frame2, text="DFT & IDFT", command= task4)
t4.place(x=50, y=130, width=200)
t5 = tk.Button(frame2, text="Compute DCT & Remove DC", command= task5)
t5.place(x=50, y=170, width=200)
t6 = tk.Button(frame2, text="Operations", command= task6)
t6.place(x=50, y=210, width=200)
t7 = tk.Button(frame2, text="Time delay & Correlation", command= task7)
t7.place(x=50, y=250, width=200)
t8 = tk.Button(frame2, text="Fast convolution & Fast correlation", command= task8)
t8.place(x=50, y=290, width=200)
back_button = tk.Button(frame2, text="back", command= back,fg="white",background="green",font=custom_font1)
back_button.place(x=110, y=330, width=90)

img_label = tk.Label(window, image=photo)
img_label.pack(pady=5)  # By default, it will pack at the top

label = tk.Label(window, text="WELCOME TO DSP TOOLS", bg="orange", fg="green", font=custom_font, compound='center')
label.pack(pady=5)

abt_label=tk.Label(frame1, text="ABOUT :", fg="white", bg="BLACK", font=custom_font, compound='center')
abt_label.pack(pady=5)

#About section
about0_label=tk.Label(frame1, text="DSP TOOLS", fg="white", bg="purple", font=custom_font, compound='center')
about0_label.pack(pady=5)
about1_label=tk.Label(frame1, text="Git Hub : https://github.com/yassakamille", fg="white", bg="purple",  font=custom_font, compound='center')
about1_label.pack(pady=5)
about2_label=tk.Label(frame1, text="Gmail : yassakamille@gmail.com", fg="white", bg="purple",  font=custom_font, compound='center')
about2_label.pack(pady=5)
about3_label=tk.Label(frame1, text="copyright © all rights reserved", fg="white", bg="purple",  font=custom_font, compound='center')
about3_label.pack(pady=5)

back_button = tk.Button(frame1, text="back", command= back,fg="white",background="green",font=custom_font1)
back_button.pack(side=tk.BOTTOM)

frame.pack()
def main():
    window.mainloop()

if __name__== "__main__":
    main()