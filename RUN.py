from tkinter import Tk, Label, Button, filedialog, DISABLED, NORMAL, SOLID
from PIL import Image, ImageTk
import multiprocess_main 
import sys
import main


file_name = ""

if __name__ == "__main__":
    if sys.platform in ("win32", "win64"):
        admin_pic = Image.open(f"{multiprocess_main.database_location}other_files\\admin.png")
        ref_file = f"{multiprocess_main.database_location}other_files\\whitebox.jpg"
    elif sys.platform in ('linux', 'linux2'):
        admin_pic = Image.open(f"{multiprocess_main.database_location}other_files/admin.png")
        ref_file = f"{multiprocess_main.database_location}other_files/whitebox.jpg"
    else:
        print("NOT AVAILABLE FOR THIS PLATFORM...")
        sys.exit()

    if __name__ == "__main__":

        window = Tk()
        window.title('-: CHECK YOUR FINGERPRINT :-')
        window.geometry("500x500")
        window.configure(background="white")
        window.resizable(0, 0)


        def apply_button_command():
            window.destroy()
            main.user_file_path = file_name
            main.start_execution()


        error_label = Label(window, bg="white", text="")
        error_label.place(x=20, y=380)


        def browse_func():
            global file_name
            global error_label
            filename = filedialog.askopenfilename()
            if not filename.endswith(".png") and not filename.endswith(".tif"):
                error_label.configure(text="⚠ filename should endswith('.png' or '.tif')")
                apply_button.configure(state=DISABLED)
                panel.configure(image=ref_img)
                picture_path.config(text=filename)
            else:
                error_label.configure(text="")
                si = Image.open(filename)
                h = panel.winfo_height()  # label's current height
                w = panel.winfo_width()
                si = si.resize((h, w))
                ss = ImageTk.PhotoImage(si)
                panel.image = ss
                panel.configure(image=ss)
                picture_path.config(text=filename)
                if len(filename) > 0:
                    apply_button.configure(state=NORMAL)
                    file_name = filename


        # image insertion...

        admin = ImageTk.PhotoImage(admin_pic)
        pic2cmpdir_label = Label(window, image=admin, bg="white")
        pic2cmpdir_label.place(x=192, y=0)

        # exit button...

        Button(window, text="exit".upper(), fg="white", bg="red", font=("arial", 14, "italic"), command=window.destroy).place(
            x=429, y=461)

        apply_button = Button(window, text="APPLY", fg="white", bg="blue", font=("arial", 14, "italic"), state=DISABLED,
                            command=apply_button_command)
        apply_button.place(x=340, y=461)

        browse_button = Button(window, text="Browse", bg="white", command=browse_func, fg="black")
        browse_button.place(x=225, y=138)

        Label(window, text="Select The Picture :: ", font=("arial", 15, "bold"), bg="white", fg="black").place(x=20, y=138)

        picture_path = Label(window, bg="white", wraplength=370, fg="black")
        picture_path.place(x=125, y=181)

        Label(window, text="File Selected :: ", font=("arial", 12, "italic"), bg="white", fg="black").place(x=20, y=180)

        ref_img = ImageTk.PhotoImage(Image.open(ref_file))
        Label(window, text="Selected Image :: ", font=("arial", 13, "bold"), bg="white", fg="black").place(x=20, y=290)

        panel = Label(window, height="100", width="100", image=ref_img, bg="white", fg="black", relief=SOLID)
        panel.place(x=200, y=250)

        Label(window, text="", bg="white").place(x=250, y=120)

        window.mainloop()
