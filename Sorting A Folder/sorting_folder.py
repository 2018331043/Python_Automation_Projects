import os
import shutil
import time

path="C:\\Users\\ASUS\\Downloads"
Extenstions=[[".JPEG",".jpg",".jpeg",".png",".JPG"],[".mkv",".mp4",".mpeg"],[".txt",".doc",".docx",".pptx",".pdf"],[".exe"],[".torrent"],[".zip"]]
Formats=["Images","Videos","Documents","Executables","Torrents","Zip Files","Others"]

for i in Formats:
	if not os.path.exists(path+"\\"+i):
		os.makedirs(path+"\\"+i)
		print("Entered in making folder")

while True:
	time.sleep(2)
	x=0
	filenames=os.listdir(path);
	for i in Extenstions:
		for j in i:
			for name in filenames:
				if name.endswith(j) and not os.path.exists(path+"\\"+Formats[x]+"\\"+name):
					print("Entered")
					shutil.move(path+"\\"+name,path+"\\"+Formats[x]+"\\"+name) 
		x=x+1


"""if not os.path.exists(path+"\Images"):
	os.makedirs(path+"\Images")
	print("Entered")
for name in filenames:
	temp=name.endswith(".JPG") or name.endswith(".jpeg") or name.endswith(".png") or name.endswith(".jpg")
	temp= temp and not os.path.exists(path+"\Images"+"\\"+name)
	if temp:
		print("Entered")
		shutil.move(path+"\\"+name,path+"\Images"+"\\"+name) """
