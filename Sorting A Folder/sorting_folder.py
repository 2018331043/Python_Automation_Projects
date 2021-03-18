import os
import shutil

path="E:\Python Automation Projects\Python_Automation_Projects\Sorting A Folder\TestFolder"
filenames=os.listdir(path);
if not os.path.exists(path+"\Images"):
	os.makedirs(path+"\Images")
	print("Entered")
for name in filenames:
	temp=name.endswith(".JPG") or name.endswith(".jpeg") or name.endswith(".png") or name.endswith(".jpg")
	temp= temp and not os.path.exists(path+"\Images"+"\\"+name)
	if temp:
		print("Entered")
		shutil.move(path+"\\"+name,path+"\Images"+"\\"+name) 
