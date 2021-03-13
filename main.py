import pyshorteners
import pyperclip
from tkinter import *

root =Tk()

root.title("kavi B URL shortener")
root.config(bg="#49A")

url = StringVar()
url_address = StringVar()

def urlshortener():
    url_add=url.get()
    url_short=pyshorteners.Shortener().tinyurl.short(url_add)
    url_address.set(url_short)

def copyurl():
    url_short=url_address.get()
    pyperclip.copy(url_short)

Label(root, text="KaviB URL shortener" , font="popins" ).pack(pady=10)
Entry(root,textvariable=url ,width=50).pack(pady=5 )
Button(root, text="Generate short URL" ,command=urlshortener, ).pack(pady=7)
Entry(root,textvariable=url_address ,width=50).pack(pady=5)
Button(root, text="copy URL" ,command=copyurl).pack(pady=7)

root.mainloop()

