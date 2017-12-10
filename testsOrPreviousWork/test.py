import io
import base64
from imgurpython import ImgurClient
try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen
root = tk.Tk()
root.title("display a website image")
# a little more than width and height of image
w = 520
h = 320
x = 80
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
# this GIF picture previously downloaded to tinypic.com
#image_url = "http://i46.tinypic.com/r9oh0j.gif"

client_id = 'c2058ecfc76d75f'
client_secret = '5fe636c3e7a032b56b2120fe82eb3071c790c5ff'

client = ImgurClient(client_id, client_secret)

item = client.get_image("nhTyj4d.jpg")
image_url = item.link
image_byt = urlopen(image_url).read()
image_b64 = base64.encodestring(image_byt)
photo = tk.PhotoImage(data=image_b64)
# create a white canvas
cv = tk.Canvas(bg='white')
cv.pack(side='top', fill='both', expand='yes')
# put the image on the canvas with
# create_image(xpos, ypos, image, anchor)
cv.create_image(10, 10, image=photo, anchor='nw')
root.mainloop()