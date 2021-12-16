import os
import sys
import codecs

print("### CharsetFixer ###")

#print('Number of arguments: {}'.format(len(sys.argv)))
#print('Argument(s) passed: {}'.format(str(sys.argv)))
# Get the arguments from the command-line except the filename
#argv = sys.argv[1:]
# Get just the first argument
arg1 = sys.argv[1]

# print('First argument: ', arg1)

#filename = "napisy.srt"
filename = arg1
newfilename = filename+".old"

try:
    file = open(filename, encoding="utf8")
    print("Opened file: ", filename)
except:
    print('File not found', filename)
    quit()

# Translation table:
#ê ¹ œ ³ ¿ Ÿ æ ñ Ê ¥ Œ £ ¯ - Æ Ñ
#ę ą ś ł ż ź ć ń Ę Ą Ś Ł Ż Ź Ć Ń

source_chars = "ê ¹ œ ³ ¿ Ÿ æ ñ Ê ¥ Œ £ ¯ Ź Æ Ñ"
target_chars = "ę ą ś ł ż ź ć ń Ę Ą Ś Ł Ż Ź Ć Ń"
output = ""
newline = ""
translation = output.maketrans(source_chars, target_chars)
countLines = 0
countChars = 0

print("Translation begins...", end='')
for line in file:
    newline = line.translate(translation)  
    output += newline
    #print('.', end='')
    countLines += 1
    
    #liczenie zmian w linii
    for a, b in zip(line, newline):
        if ( a != b ):
            countChars += 1
    
print('...Translation finished.')
file.close()

print("Processed lines: ", countLines)
print("Changed chars: ", countChars)

print("Renaming original file to ", newfilename)

#rename original file to .old
os.rename(filename, newfilename)

with codecs.open(filename,"w+", "utf-8-sig") as newfile:
    # print("Opened new file: ", filename)
    newfile.write(output)
    print("Saving corrected file: ", filename)
    newfile.close   

print("### CharsetFixer Done ###")    
