#George Curry
#make a dictionary code for each letter of alpabet
#for this project, lower and uppercase is the same
alphaCodes = {
    "A":"~", "B":"!", "C":"@", "D":"#", "E":"$", "F":"^", "G":"&", 
    "H":"-", "I":"+", "J":"/", "K":"{", "L":"}", "M":"[", "N":"]", 
    "O":"*", "P":":", "Q":";", "R":"`", "S":"<", "T":">", "U":".", 
    "V":"?", "W":"|", "X":"=", "Y":"1", "Z":"2",
}
#open a file, read contents, use dictionary to write an encrypted
#version of the file to a new file, each letter should be in the code
#read encrypt, and put new encryption into decrypt

inputFile = open('Encrypt.txt','r')
outputFile = open('Decrypt.txt','w')

def encryptAndWrite(string):
    for letter in string:
        #ignore whte space
        if letter!= " ":
            if letter.upper()in alphaCodes:
                #write value into file
                outputFile.write(alphaCodes[letter.upper()])
        else:
            outputFile.write(" ")#re-add space

#read every line in file, transform line, 
#write to new file
for line in inputFile:
    encryptAndWrite(line)

print("Encryption successful!")
inputFile.close()
outputFile.close()