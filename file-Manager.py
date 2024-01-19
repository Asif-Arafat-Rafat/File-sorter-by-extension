import os
import tkinter as tk
import shutil

path= input("Enter your path: ")

root=tk.Tk()
root.geometry("720x360")
files=os.listdir(path)
i=1
for file in files:
    filename,extention=os.path.splitext(file)
    extention=extention[1:]
    List=tk.Listbox(root)
    List.insert(tk.END,f"{filename} and {extention}")
    new_path = path+"\\"+extention
    if not os.path.exists(new_path):
        print("creating "+extention)
        os.mkdir(extention)
        shutil.move(path+"\\"+file,new_path)
    else:
        shutil.move(path+"\\"+file,new_path)
        print("Already there")
    List.pack(fill="x")
    i+=1
root.mainloop()