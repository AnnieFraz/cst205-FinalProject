from PIL import Image
import webbrowser
from imgurpython import ImgurClient

client_id = 'c2058ecfc76d75f'
client_secret = '5fe636c3e7a032b56b2120fe82eb3071c790c5ff'

client = ImgurClient(client_id, client_secret)

# Example request
#items = client.gallery()
items = client.get_album_images("f0H0u")
for item in items:
    link = item.link
    #if link.find('.jpg')  == -1:
        #print("no")

    #else:
       # print("yes")
    print(item.link)
    print(item)
    webbrowser.open_new(item.link)  # +".jpg")