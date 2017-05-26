#!/usr/bin/env python

import urllib.request
import random
import os

print("\t\t########################################")
print("\t\t#                                      #")
print("\t\t#       Image And Pdf Downloader       #")
print("\t\t#                          v1.17       #")
print("\t\t#                                      #")
print("\t\t########################################\n\n")


print('''What Do You Want To Download?
         1.Image
         2.PDF ''')

ans = int(input("-> "))

if ans == 1:
    def img_down(img_link):
        name = random.randrange(1,1000)
        file_name = str(name) + '.jpg'
        urllib.request.urlretrieve(img_link, file_name)

    img = input("Enter URL: ")
    cdir = os.getcwd()
    print("Your Current dir: " + cdir)
    img_down(img)
    print("Download Completed on Current Directory!")

if ans == 2:
    def file_down(file_link):
        response = urllib.request.urlopen(file_link)
        rfile = response.read()
        file_name = input("Give You File Title: ")
        full_name = (file_name + '.pdf')
        dest_file = open(full_name, "wb")
        dest_file.write(rfile)
        dest_file.close()

    get_link = input("Give Your URL: ")
    file_down(get_link)
    print("Download Completed!")
    


	

