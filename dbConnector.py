from tkinter import Label, Button, StringVar, Tk, Entry
import shutil
import random
import os
import getpass
import sys


def print_details(file_name: str):
    """
    If the user details exists, then this function will print the details
    of the user_added_fingerprint_details.
    :param file_name: This is the file name to print (obviously a text file).
    :return: None
    """
    if file_name.endswith(".png") or file_name.endswith(".txt"):
        file_name = file_name[:-4] + ".txt"
    name, address, phno, id_ = fetch_details(file_name)
    window = Tk()
    window.geometry("400x400")
    window.configure(background="white")
    window.resizable(0, 0)
    window.title("-: DETAILS :-")

    Label(window,
          text="FINGER MATCHED!!!!",
          bg="white",
          fg="black",
          font=("arial", 18, "bold")).pack()

    Label(window,
          text="Name :: ",
          bg="white",
          fg="black",
          font=("arial", 13, "bold")).place(x=10, y=40)

    Label(window,
          text=name,
          bg="white",
          font=("arial", 13, "italic"),
          fg="black",
          wraplength=310).place(x=80, y=40)

    Label(window,
          text="Address ::",
          bg="white",
          fg="black",
          font=("arial", 13, "bold")).place(x=10, y=90)

    Label(window,
          text=address,
          bg="white",
          fg="black",
          font=("arial", 13, "italic"),
          wraplength=290).place(x=100, y=90)

    Label(window,
          text="Contact No. :: ",
          bg="white",
          fg="black",
          font=("arial", 13, "bold")).place(x=10, y=220)

    Label(window,
          text=phno,
          bg="white",
          fg="black",
          font=("arial", 13, "italic"),
          wraplength=260).place(x=130, y=220)

    Label(window,
          text="ID :: ",
          bg="white",
          fg="black",
          font=("arial", 13, "bold")).place(x=10, y=320)

    Label(window,
          text=id_,
          bg="white",
          fg="black",
          font=("arial", 13, "italic"),
          wraplength=335).place(x=50, y=320)

    window.mainloop()


def get_name():
    """ 
    Will generate a new Random Name ...
    """

    """ Bases ::  """

    # 0 - 9 = 10
    # A - Z = 26
    # a - z = 26
    # ----------
    # Base  = 62

    """ Length of the string :: 11 digits ... """

    """ Database Can Store = 62^11 = 5.203656068E19 """

    C_ALPHABETS = [chr(x) for x in range(65, 90+1)]
    S_APLHABETS = [chr(x) for x in range(97, 122+1)]
    NUMBERS = [chr(x) for x in range(48, 57+1)]
    LETTERS = ([x for x in C_ALPHABETS], [x for x in S_APLHABETS], [x for x in NUMBERS])
    name_list = list()

    while len(name_list)!=11:
        random_point = random.choice(range(len(LETTERS)))
        random_letter = random.choice(LETTERS[random_point])
        name_list.append(random_letter)

    name = "".join(name_list)
    return name


def add_txt(file_name):
    """
    if the biometrics does not exists, and the user fingerprint is new
    in the database, then obviously, this will add the identification of the
    user_biometric.
    :param file_name: the filename that will contain the user_fp_details.
    :return: None
    """
    global database_location
    window = Tk()
    window.title("-: NEW REGISTRATION :- ")
    window.geometry("300x300")
    window.resizable(0, 0)
    window.configure(background="white")

    Label(window,
          text="WELCOME",
          font=("arial", 18, "bold"),
          bg="white",
          fg="black").pack()

    name = StringVar()
    Label(window,
          text="Name :: ",
          bg="white",
          font=("arial", 13, "bold"),
          fg="black").place(x=10, y=50)
    Entry(window, textvariable=name, width=26).place(x=81, y=50)

    address = StringVar()
    Label(window,
          text="Address :: ",
          bg="white",
          font=("arial", 13, "bold"),
          fg="black").place(x=10, y=90)
    Entry(window, textvariable=address, width=24).place(x=99, y=90)

    phone_number = StringVar()
    Label(window,
          text="Contact No. :: ",
          bg="white",
          font=("arial", 13, "bold"),
          fg="black").place(x=10, y=130)
    Entry(window, textvariable=phone_number).place(x=130, y=130)

    id_number = StringVar()
    Label(window,
          text="ID :: ",
          bg="white",
          font=("arial", 13, "bold"),
          fg="black").place(x=10, y=170)
    Entry(window, textvariable=id_number, width=30).place(x=50, y=170)

    def save_button():
        new_file = open(database_location + file_name + ".txt", "w+")
        new_file.write("name = " + name.get() + "\n")
        new_file.write("address = " + address.get() + "\n")
        new_file.write("phone_number = " + phone_number.get() + "\n")
        new_file.write("id_number = " + id_number.get() + "\n")
        window.destroy()
        new_file.close()

    Button(window,
           text="SAVE",
           fg="white",
           bg="red",
           font=("arial", 15),
           command=save_button).place(x=115, y=210)
    window.mainloop()


def del_txt(file_name):
    """
    This will delete the text of the existing biometric.
    :param file_name: the file to delete(obviously a text file.)
    :return: None
    """
    global database_location
    if os.path.exists(database_location + file_name + ".txt"):
        os.remove(database_location + file_name + ".txt")
        print(f"Done! {file_name} text removed")
    else:
        print(f"{file_name} text don't exists!")


def del_fp_img(file_name):
    """
    This function is usefull if we want to delete its biometric identification.
    :param file_name: The filename to delete(a png or tif file).
    :return: None.
    """
    global database_location
    if os.path.exists(database_location + file_name):
        os.remove(database_location + file_name)
        print(f"Done! {file_name} image removed")
    else:
        print(f"{file_name} image don't exists!")


def all_details(file_name: str):
    """
    This is a special method that will check if all the details of the person's identification
    are present or not.
    if all are not present, and if the fingerprint exists,
    then the user will be allowed to edit its identity.
    :param file_name: file_name from where to fetch the details.
    :return: "are present" or "are not present".
    """
    if file_name.endswith(".png") or file_name.endswith(".tif"):
        file_name = file_name[:-4] + ".txt"
    got_name = got_address = got_id = got_phno = False
    if os.path.exists(database_location + file_name):
        file = open(database_location + file_name)
        for sentence in file:
            my_sentence = sentence.strip()
            my_list = my_sentence.split(" ")
            if len(my_list) > 2:
                if "name = " in sentence and not got_name:
                    got_name = True
                elif "address = " in sentence and not got_address:
                    got_address = True
                elif "phone_number = " in sentence and not got_phno:
                    got_phno = True
                elif "id_number = " in sentence and not got_id:
                    got_id = True
                else:
                    continue
            else:
                return "are not present"
        if all((
                got_name,
                got_address,
                got_phno,
                got_id,
        )) is True:
            return "are present"
        else:
            return "are not present"
    else:
        edit_exstng_file(file_name)


def edit_exstng_file(file_name: str):
    """
    This function will edit the existing text file.
    this will get executed if there is some identity missing,
    or the details.txt file doesnot exists.
    :param file_name: The file_name to edit(a text file.).
    :return: None
    """
    global database_location

    if file_name.endswith(".png") or file_name.endswith(".tif"):
        file_name = file_name[:-4] + ".txt"

    window = Tk()
    window.title("-: FINGER MATCHED :- ")
    window.geometry("300x300")
    window.resizable(0, 0)
    window.configure(background="white")

    Label(window,
          text="Enter The Details...",
          font=("arial", 18, "bold"),
          bg="white",
          fg="black").pack()

    name = StringVar()
    Label(window,
          text="Name :: ",
          bg="white",
          font=("arial", 13, "bold"),
          fg="black").place(x=10, y=50)
    Entry(window, textvariable=name, width=26).place(x=81, y=50)

    address = StringVar()
    Label(window,
          text="Address :: ",
          bg="white",
          font=("arial", 13, "bold"),
          fg="black").place(x=10, y=90)
    Entry(window, textvariable=address, width=24).place(x=99, y=90)

    phone_number = StringVar()
    Label(window,
          text="Contact No. :: ",
          bg="white",
          font=("arial", 13, "bold"),
          fg="black").place(x=10, y=130)
    Entry(window, textvariable=phone_number).place(x=130, y=130)

    id_number = StringVar()
    Label(window,
          text="ID :: ",
          bg="white",
          font=("arial", 13, "bold"),
          fg="black").place(x=10, y=170)
    Entry(window, textvariable=id_number, width=30).place(x=50, y=170)

    def save_button():
        """
        This is the save button that will overwrite the
        existing file details.
        """
        new_file = open(database_location + file_name, "w")
        new_file.write("name = " + name.get() + "\n")
        new_file.write("address = " + address.get() + "\n")
        new_file.write("phone_number = " + phone_number.get() + "\n")
        new_file.write("id_number = " + id_number.get() + "\n")
        window.destroy()
        new_file.close()

    Button(window,
           text="SAVE",
           fg="white",
           bg="red",
           font=("arial", 15),
           command=save_button).place(x=115, y=210)
    window.mainloop()


def add_fp_img(current_directory, new_name):
    if current_directory[-1] == "/":
        current_directory = current_directory[:len(current_directory) - 1]
    if current_directory.endswith(".png"):
        shutil.copy(current_directory, database_location + new_name + ".png")
    else:
        shutil.copy(src=current_directory,
                    dst=database_location + new_name + ".tif")


def fetch_details(file_name):
    """
    This function will fetch details from the file(iff the biometric of the user exists).
    first it will open the file in read mode,
    then it will fetch the details.
    :param file_name: the name of the file, to open and fetch details is required.
    :return: person identity(ies).
    """
    file = open(database_location + file_name, "r")
    name_sentence = address_sentence = phone_number_sentence = id_number_sentence = ""
    got_name = got_id = got_address = got_phno = False
    for sentence in file:
        sentence = sentence.lower()
        if "name" in sentence and not got_name:
            got_name = True
            name_sentence = sentence
        elif "address" in sentence and not got_address:
            got_address = True
            address_sentence = sentence
        elif "phone_number" in sentence and not got_phno:
            phone_number_sentence = sentence
            got_phno = True
        elif "id_number" in sentence and not got_id:
            got_id = True
            id_number_sentence = sentence
        else:
            continue
    file.close()  # close the files after extracting details.
    name_list = name_sentence.split(" ")
    address_list = address_sentence.split(" ")
    id_list = id_number_sentence.split(" ")
    phone_list = phone_number_sentence.split(" ")
    person_name = person_address = person_id = person_number = ""
    for item in name_list[2:]:
        person_name = person_name + " " + item
    for item in address_list[2:]:
        person_address = person_address + " " + item
    for item in id_list[2:]:
        person_id = person_id + " " + item
    for item in phone_list[2:]:
        person_number = person_number + item
    return person_name.title().strip(), person_address.title().strip(
    ), person_number.strip(), person_id.strip()


def transfer_image_to_database(source, destination):
    """
    This will transfer some images to the given destination from particular source.
    """
    if os.path.exists(path=source):
        shutil.copy(src=source, dst=destination)
    else:
        raise FileNotFoundError(
            "source file is missing. go to the location where the file is present using terminal and then execute."
        )


if __name__ == "dbConnector":
    if sys.platform in (
            "linux",
            "linux2",
    ):
        # For Linux.
        #global database_location
        DATABASE_PARENT_DIR = f"/home/{getpass.getuser()}/Documents/fp_recog/"
        database_location = DATABASE_PARENT_DIR + "database_fprecog/"
        if not os.path.exists(DATABASE_PARENT_DIR):
            os.mkdir(DATABASE_PARENT_DIR)
            os.mkdir(database_location)
            os.mkdir(DATABASE_PARENT_DIR + "other_files")
            transfer_image_to_database(
                source=f"{os.getcwd()}/admin.png",
                destination=f"{DATABASE_PARENT_DIR}other_files/")
            transfer_image_to_database(
                source=f"{os.getcwd()}/whitebox.jpg",
                destination=f"{DATABASE_PARENT_DIR}other_files/")
        else:
            # check if the other files exists or not.
            list_ = os.listdir(DATABASE_PARENT_DIR + "other_files/")
            if len(list_) != 2:
                for item in list_:
                    os.remove(DATABASE_PARENT_DIR + "other_files/" + item)
                transfer_image_to_database(
                    source=f"{os.getcwd()}/admin.png",
                    destination=f"{DATABASE_PARENT_DIR}other_files/")
                transfer_image_to_database(
                    source=f"{os.getcwd()}/whitebox.jpg",
                    destination=f"{DATABASE_PARENT_DIR}other_files/")
            else:
                pass

    elif sys.platform in (
            "win64",
            "win32",
    ):
        # for windows Platform.
        #global database_location
        DATABASE_PARENT_DIR = f"C:\\Users\\{getpass.getuser()}\\Documents\\fp_recog\\"
        database_location = DATABASE_PARENT_DIR + "database_fprecog\\"
        if not os.path.exists(DATABASE_PARENT_DIR):
            os.mkdir(DATABASE_PARENT_DIR)
            os.mkdir(database_location)
            os.mkdir(DATABASE_PARENT_DIR + "other_files")
            transfer_image_to_database(
                source=f"{os.getcwd()}\\admin.png",
                destination=f"{DATABASE_PARENT_DIR}other_files\\")
            transfer_image_to_database(
                source=f"{os.getcwd()}\\whitebox.jpg",
                destination=f"{DATABASE_PARENT_DIR}other_files\\")
        else:
            # check if the other files exists or not.
            list_ = os.listdir(DATABASE_PARENT_DIR + "other_files\\")
            if len(list_) != 2:
                for item in list_:
                    os.remove(DATABASE_PARENT_DIR + "other_files\\" + item)
                transfer_image_to_database(
                    source=f"{os.getcwd()}\\admin.png",
                    destination=f"{DATABASE_PARENT_DIR}other_files\\")
                transfer_image_to_database(
                    source=f"{os.getcwd()}\\whitebox.jpg",
                    destination=f"{DATABASE_PARENT_DIR}other_files\\")
            else:
                pass
    else:
        print(
            "SORRY.\r NOT SUPPORTED IN OTHER OPERATING SYSTEMS EXCEPT WINDOWS AND LINUX AND MACOS."
        )
        sys.exit()