import os,pickle,sys
from py_essentials import hashing as hasher
from pathlib import Path

def exit_message():
	sys.exit("Command line syntax: checksum.py [filelistname] [starting directory]")

if (len(sys.argv) == 1): exit_message()

#settings
filelist = sys.argv[1]
if (len(sys.argv)==3): rootDir=sys.argv[2]
else: rootDir = '.'
files = []

#walking script
for dirName, subdirList, fileList in os.walk(rootDir):
	for fname in fileList:
		#creating correct formatting for folder path with pathlib
		data_folder = Path(dirName)
		#correct path format for fileChecksum
		current_file = ((data_folder / fname).resolve()).as_posix()
		#generating checksum with sha256
		try:
			h = hasher.fileChecksum(str(current_file), "sha256")
		except:
			print ('Checksum counting error')
		#adding new values to array
		files.append((str((data_folder.resolve()).as_posix()), fname, h))
		#putting results on screen
		print (str((data_folder.resolve()).as_posix())+' '+fname+' '+h)

#dumping data with pickle
pickle.dump(files, open(filelist, "wb"))