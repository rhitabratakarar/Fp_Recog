# FP_RECOG

This is the Finger Print Recognition System Designed to work in a decent Computer.
Basically, it stores the fingerprint of the user inside a database along with the identifications.
If the User is Registered, it will show a fingerprint registered popup box, and if not, then will tell the user to register itself.
This code Implementation is done using Python3 and not supposed to work in python2 or lower versions...
To execute the code, the user need to run the RUN.py file from its terminal using python3 or python as a command.
The Database will be created in user Documents Folder considering fp_recog as the parent directory of the database system and database_fprecog as the storage of the database.

# REQUIREMENTS:

01. python >= v3.5
02. numpy
03. matplotlib(Optional)
04. opencv-python
05. tkinter
06. pillow
07. os Module (in-built)
08. sys Module (in-built)
09. shutil Module (in-built)
10. getpass Module (in-built)
11. random Module (in-built)
12. psutil (optional)
13. ray (optional)

# NOTE:

To Run the system, execute the RUN.py from terminal by changing the directory otherwise it may raise some FileNotFoundError.

And it *Does not Check For the Region Of Interest* thus, a lot of accuracy issues could be encountered while matching the same fingerprint twice.
