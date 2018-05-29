from tkinter import *
from PIL import Image, ImageTk


def showimge(event):
    print("Single Click, Button-l")


root = Tk()  #create object of window
root.title('应用程序窗口')
root.resizable(False, False)
windowWidth = 800
windowHeight = 800
screenWidth, screenHeight = root.maxsize()
geotryParam = '%dx%d+%d+%d' % (windowWidth, windowHeight, (screenWidth-windowWidth)/2, (screenHeight-windowHeight)/2)
root.geometry(geotryParam) #窗口大小以及偏移坐标
root.wm_attributes('-topmost', 1)

image = Image.open('img.jpg')
photo = ImageTk.PhotoImage(image)
#label_img = Label(root, image=photo)
#label_img.pack()
#label_text = Label(root, text='显示照片')
#label_text.pack()


button = Button(root, text = '显示图片')
button.pack()
button.bind('&lt;Button-1&gt', showimge)

root.mainloop()