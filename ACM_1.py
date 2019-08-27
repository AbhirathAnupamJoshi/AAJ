import requests

image_url = input("Enter URL of Image :")
name = input("Enter File Name to save as :")

r = requests.get(image_url) 
fname = name + ".jpg"
with open(fname,'wb') as f: 

    f.write(r.content) 