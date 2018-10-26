import pickle,sys
from pathlib import Path
from pandas import DataFrame

def exit_message():
	sys.exit("Command line syntax: find.py [filelist file] [filename.csv for files with same name] [filename.csv for files with same checksum]")

if (len(sys.argv) <4): exit_message()

#settings
filelist=sys.argv[1]
filesamename=sys.argv[2]
filesamecrc=sys.argv[3]
files = []

#loading data and putting it to dataframe
files = pickle.load(open(filelist, "rb"))
df = DataFrame(data = files, columns=['Path', 'file', 'hash'])

print ('Same name:')
#sorting by file name
df.sort_values("file", inplace = True)
bool_series = df["file"].duplicated(keep = False) 
#putting list to screen
print(df[bool_series])
#saving results to csv file
df[bool_series].to_csv(filesamename, sep='\t', index=False, header=False)

print('Same checksum(files are same):')
#sorting by checksum
df.sort_values("hash", inplace = True)
bool_series = df["hash"].duplicated(keep = False) 
#putting list to screen
print(df[bool_series])
#saving results to csv file
df[bool_series].to_csv(filesamecrc, sep='\t', index=False, header=False)
