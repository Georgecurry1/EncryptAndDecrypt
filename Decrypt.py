#George Curry
#write a second program that opens an encrypted file and display 

#make a dictionary code for each letter of alpabet


def getKeyFromValue(val):#checks every set to see if val argument matches the value in the set of lists[(x,y),(x,y)]
    for key,value in alphaCodes.items():#returns list of each pair inside alphaCodes
        if val == value:
            return key
    return "Key Not Found"

alphaCodes = {
    "A":"~", "B":"!", "C":"@", "D":"#", "E":"$", "F":"^", "G":"&", 
    "H":"-", "I":"+", "J":"/", "K":"{", "L":"}", "M":"[", "N":"]", 
    "O":"*", "P":":", "Q":";", "R":"`", "S":"<", "T":">", "U":".", 
    "V":"?", "W":"|", "X":"=", "Y":"1", "Z":"2",
}
finishedString = ""
inputFile = open('Decrypt.txt','r')
#read line, check if value is in alpha code

for line in inputFile:
    string = line
    for letter in string:
        if letter!=" ":
            if letter in alphaCodes.values():
                keyOfLetter = getKeyFromValue(letter)
                finishedString+=keyOfLetter.lower()#concatenates current string with current key (saves it all together)
        else:
            finishedString+=" "

print("Decryption finished:\n")
print(finishedString)
inputFile.close()