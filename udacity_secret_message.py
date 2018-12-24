import os


def rename_files():
	#get file names from folder
	file_list=os.listdir(r"F:\New folder (2)")
	print file_list
	file_path=os.getcwd()
	print file_path
	right_path=os.chdir("F:\New folder (2)")
	print right_path
	#for each file,rename it
	for file_name in file_list:
		os.rename(file_name, file_name.translate(None , "0123456789"))
	os.chdir(file_path)
rename_files()