#In this exercise I will rename number of file names

import os
def rename_files():
	#get the file names form the folder
	file_list = os.listdir(r"C:\Personal\GitHub\Udacity-Full-Stack-Web-Developer-Nanodegree\Supporting courses\Programming Foundations with Python\prank")
	print(file_list)
	saved_path = os.getcwd()
	print("Current working Directory is" +saved_path)
	#change folder directory to prank folder
	os.chdir(r"C:\Personal\GitHub\Udacity-Full-Stack-Web-Developer-Nanodegree\Supporting courses\Programming Foundations with Python\prank")
	# rename each file name in the folder
	for file_name in file_list:
		#print("Old name -" +file_name)
		#os.rename(old name,new name)
		deletedigits = str.maketrans(dict.fromkeys("0123456789"))
		os.rename(file_name, file_name.translate(deletedigits))
		print("New name -" + file_name)
rename_files()
