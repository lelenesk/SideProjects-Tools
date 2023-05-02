import random
import os
from tkinter import *
from tkinter import ttk, filedialog


def input(file):
    path = os.path.abspath(file.name)
    file.close()
    return path


def output():
    path = r"output"
    path = os.path.realpath(path)
    os.startfile(path)


def crypter1(faked_letter, mode_setter, modified_file):
    twist_number = random.randint(1, 4)
    if mode_setter == 0:
        if twist_number == 1:
            modified_file.append(faked_letter.replace(faked_letter, "l"))
        elif twist_number == 2:
            modified_file.append(faked_letter.replace(faked_letter, "z"))
        elif twist_number == 3:
            modified_file.append(faked_letter.replace(faked_letter, "s"))
        else:
            modified_file.append(faked_letter.replace(faked_letter, "b"))
    elif mode_setter == 1:
        if twist_number == 1:
            modified_file.append(faked_letter.replace(faked_letter, "i"))
        elif twist_number == 2:
            modified_file.append(faked_letter.replace(faked_letter, "u"))
        elif twist_number == 3:
            modified_file.append(faked_letter.replace(faked_letter, "e"))
        else:
            modified_file.append(faked_letter.replace(faked_letter, "o"))
    elif mode_setter == 2:
        if twist_number == 1:
            modified_file.append(faked_letter.replace(faked_letter, "6"))
        elif twist_number == 2:
            modified_file.append(faked_letter.replace(faked_letter, "2"))
        elif twist_number == 3:
            modified_file.append(faked_letter.replace(faked_letter, "8"))
        else:
            modified_file.append(faked_letter.replace(faked_letter, "4"))
    else:
        if twist_number == 1:
            modified_file.append(faked_letter.replace(faked_letter, "L"))
        elif twist_number == 2:
            modified_file.append(faked_letter.replace(faked_letter, "T"))
        elif twist_number == 3:
            modified_file.append(faked_letter.replace(faked_letter, "F"))
        else:
            modified_file.append(faked_letter.replace(faked_letter, "C"))
    return faked_letter


def convert1():
    modified_file = []
    file = filedialog.askopenfile(mode='r', filetypes=[('Text Document', '*.txt')])
    original_file = open(input(file), encoding="utf-8")
    try:
        end_file = open(f"output/{os.path.basename(input(file))}", "x", encoding="utf-8")
        for row in original_file:
            for letter in row:
                if letter in ("l", "s", "t", "r", "v", "d", "k", "g", "w", "x", "m", "h"):
                    setter = 0
                    crypter1(letter, setter, modified_file)
                elif letter in ("a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű"):
                    setter = 1
                    crypter1(letter, setter, modified_file)
                elif letter in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                    setter = 2
                    crypter1(letter, setter, modified_file)
                elif letter in ("T", "A", "M", "K", "Ó", "Z", "S", "I"):
                    setter = 3
                    crypter1(letter, setter, modified_file)
                else:
                    modified_file.append(letter)

        end_text = "".join(modified_file)
        end_file.write(end_text)
        end_file.close()
    except:
        print("ezt a fájlt már átkonvertáltad, nézd meg az output mappát")


def crypter2(message):
    key = "abcde"
    key_for_message = key*(len(message)//len(key))+key[:len(message) % len(key)]

    coded_message = ""
    for i in range(len(message)):
        coded_message += chr(ord(message[i])+ord(key_for_message[i]))

    decoded_message = ""
    for i in range(len(coded_message)):
        decoded_message += chr(ord(coded_message[i])-ord(key_for_message[i]))
    return coded_message


def convert2():
    try:
        file = filedialog.askopenfile(mode='r', filetypes=[('Text Document', '*.txt')])
        message = open(input(file), encoding="utf-8")
        message = message.read()

        end_file = open(f"output/{os.path.basename(input(file))}", "x", encoding="utf-8")
        end_file.write(crypter2(message))
        end_file.close()
    except:
        print("ezt a fájlt már átkonvertáltad, nézd meg az output mappát")


if __name__ == '__main__':

    root = Tk()
    root.geometry("200x150")
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    ttk.Label(frm, text="Szöveg átalakító program").grid(column=0, row=0, rowspan=2, columnspan=2)
    ttk.Button(frm, text="1. módszer", command=convert1).grid(column=0, row=4)
    ttk.Button(frm, text="2. módszer", command=convert2).grid(column=0, row=5)
    ttk.Button(frm, text="Kimeneti mappa megnyitása", command=output).grid(column=0, row=6)
    ttk.Button(frm, text="Alkalmazás bezárása", command=root.destroy).grid(column=0, row=7)
    root.mainloop()