fn = input('Enter the filename: ')
try:
    fh = open(fn)
except Exception as e:
    print('File cannot be opened', fn)
    quit()

fh = open(fn)
print(fh)
for lx in fh:
    ly = lx.rstrip() #Is done because the print statement puts in a newline \n in the end of every line in the text file. Without the method the file will get doubled the newline as in the original file. The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
    print(ly.upper())
