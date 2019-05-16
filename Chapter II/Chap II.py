import re
Result = 0
file = open("C:\Users\DieTenshi\Documents\GitHub\Skychallenge\Chapter II\Cipher.txt", "r")
numbers = [int(d) for d in re.findall(r'-?\d+', file.read())]

for i in numbers:
    Result += i;

print Result
