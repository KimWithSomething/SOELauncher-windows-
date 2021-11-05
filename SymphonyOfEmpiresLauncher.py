from Operations import File

from sys import platform

from pathlib import Path

from tkinter import *
import tkinter
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import datetime

import os, shutil

Rem = datetime.datetime.now()
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
p = 1
def Install(Value,Name):
    def InstallFiles(Namg,DownloadL):
        File.DownloadE(Namg+'.zip',DownloadL,'Versions')
        CockCheck=[f"\n {Namg} Created Successfiy on \n {Rem} \n"]
        File.Create(f"{Namg}_Check.txt",f"./Versions/{Namg}",CockCheck)
        File.Create(f"Version_Check.txt",f"./Versions",CockCheck)
    def GetVersionFiles(Name,link):
        InstallFiles(Name,link)
        File.Testfile(Name,'.zip','./Versions')
        File.UnzipFile(Name,'./Versions',f"./Versions/{Name}")
    FolderExists = os.path.exists(os.path.join(os.getcwd(), f"./Versions/{Name}/{Name}_Check.txt", f"./Versions/{Name}/{Name}_Check.txt"))
    print(FolderExists)
    if FolderExists == False:
        if Value == 7:   
            GetVersionFiles(Name,'https://cdn.discordapp.com/attachments/842892862743773244/902218203281899530/SoE.zip')
        if Value == 6:   
            GetVersionFiles(Name,'https://cdn.discordapp.com/attachments/842892862743773244/896863500322889819/SoE.zip')
        if Value == 5:
            GetVersionFiles(Name,'https://cdn.discordapp.com/attachments/842892862743773244/895764367142977576/SoE.zip')
        if Value == 1:
            GetVersionFiles(Name,'https://cdn.discordapp.com/attachments/842892862743773244/842893019179253790/SoE.zip')
def CloseGame():
    print("Closing The Server")
    Version3 = Inside.get()
    Ver = 0
    if Version3 =='DemoV2_7':
        Ver =+ 7
    if Version3 =='DemoV2_6':
        Ver =+ 6
    if Version3 == 'DemoV2_5':
        Ver =+ 5
    if Version3 == 'DemoV1':
        Ver =+ 1
    
    CockCheck=[f"\n \n {Version3} Closed Successfiy on \n {Rem} "]
    File.Create(f"Version_Check.txt",f"./Versions",CockCheck)
    def CloseServer():
        if platform == "win32":
            if Ver > 1:
                os.system("cd server")
                os.system("TASKKILL /F /IM server.exe")
            if Ver == 1:
                os.system("TASKKILL /F /IM main.exe")
        if platform == "linux" or platform == "linux2":
            if Ver > 1:
                os.system("kill server.exe")
            if Ver == 1:
                os.system("kill main.exe")
    print("Closing The Client")
    def CloseClient():
        if platform == "win32":
            if Ver > 1:
                os.system("cd client")
                os.system("TASKKILL /F /IM client.exe")
        if platform == "linux" or platform == "linux2":
            if Ver > 1:
                os.system("kill client.exe")
    CloseServer()
    CloseClient()
    os.system("cls")
    print("Closing the game was a success")
def LaunchGame(Version,Version32):
    def LaunchClient(Version3,Version):
        
        print("Launching Client")
        if platform == "win32":
            if Version > 1:
                print("platform =" + platform)
                os.system("start "+"Versions/"+str(Version3)+"/client/client.exe")
            if Version == 1:    
                os.system(f"start Versions/{Version3}/SoE/bin/main.exe")
        if platform == "linux" or platform == "linux2":
            if Version == 5 or 6 or 7:
                print("platform =" + platform)
                os.system("client.exe")
        
    def LaunchServer(Value,Version,Version3):
        
        Install(Value,Version3)
        print("Launching Server")
        if platform == "win32":
            if Version > 1 :
                print("platform =" + platform)
                os.system("start "+"Versions/"+str(Version3)+"/server/server.exe")
            
        if platform == "linux" or platform == "linux2":
            if Version > 1 :
                print("platform =" + platform)
                os.system("server.exe")
        LaunchClient(Version3,Version)
        
    LaunchServer(Version,Version,Version32)
SOEVersions=["DemoV2_7","DemoV2_6","DemoV2_5","DemoV1"]
        
        
def StartUp():
    Version3 = Inside.get()
        
    print("starting")
    if Version3 =='DemoV2_7':
        LaunchGame(7,Version3)
    if Version3 =='DemoV2_6':
        LaunchGame(6,Version3)
    if Version3 == 'DemoV2_5':
        LaunchGame(5,Version3)
    if Version3 == 'DemoV1':
        LaunchGame(1,Version3)
    print("finishing the startup")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def test1():
    print("test")
window = Tk()
window.title("SOE Launcher")
window.geometry("600x400")
window.configure(bg = "#FFFFFF")
window.iconbitmap("SOE.ico")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 345,
    width = 563,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    281.0,
    164.0,
    image=image_image_1
)

Inside = tkinter.StringVar(window)
  

Inside.set("Select an Version")
Version = OptionMenu(
    window,
    Inside,
    *SOEVersions,
)

Version.place(
    x = 300-30,
    y = 300,

)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= StartUp,
    relief="flat"
)
button_1.place(
    x=99.0 ,
    y=285.0+50,
    width=157.0,
    height=49.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command= CloseGame,
    relief="flat"
)
button_2.place(
    x=320.0,
    y=285.0+50  ,
    width=157.0,
    height=49.0
)

canvas.create_text(
    69.0,
    0.0,
    anchor="nw",
    text="Symphony of Empires",
    fill="#000000",
    font=("RedRose Regular", 40 * -1)
)

canvas.create_text(
    93.0,
    45.0,
    anchor="nw",
    text="Unofficial Launcher",
    fill="#000000",
    font=("RedRose Regular", 40 * -1)
)
window.resizable(False, False)
window.mainloop()
