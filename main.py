from PIL import ImageGrab
import time
from tkinter import *
import pyautogui
import keyboard

locations = [50,150,250,350]
locationKeys = {
	50:"a",
	150:"s",
	250:"d",
	350:"f"
}

def GetWindow():
	xPos = window.winfo_x()+107
	yPos = window.winfo_y()+32
	locations = [50,150,250,350]
	window.destroy()
	while True:
		current = time.time()
		if keyboard.is_pressed("f2"):
			exit()
		else:
			img = ImageGrab.grab(bbox=(xPos,yPos,xPos+400, yPos+600))
			for pos in locations:
				color = img.getpixel((pos, 310))
				if color == (17,17,17):
					pyautogui.click(x=xPos+pos,y=yPos+350)
					print("Delay:", round((time.time() - current),6))
					break

window = Tk()
window.resizable(0,0)
window.geometry("500x604")
window.title("Piano Tiles Bot by Pstefa")
Button(text="Target", command=GetWindow, bg="red").pack(side=LEFT, anchor=N, fill=Y, ipadx=25)
w = Canvas(window, width=500, height=600)
w.create_rectangle((2,2,400,600),fill="green")
w.pack(side=TOP,anchor=E)
window.wm_attributes("-transparentcolor", "green")
window.mainloop()
