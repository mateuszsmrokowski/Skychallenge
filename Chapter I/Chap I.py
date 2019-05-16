ListOfWords = []
counter = 0
with open("C:\Users\DieTenshi\Documents\GitHub\Skychallenge\Chapter I\Words.txt") as openfileobject:
    for line in openfileobject:
        ListOfWords.append(line.rstrip('\n').split(' '))

for i in ListOfWords:
    if (len(i) != len(set(i))) == True:
        counter +=1

print "File have ", counter, " valid skyphrases"
