#This file simply converts a text ascii art file into a single line to be printed
#I like to use one of these guys, sorry Liam Flan.:
#https://manytools.org/hacker-tools/convert-images-to-ascii-art/go
#https://www.text-image.com/convert/ascii.html

f = open("Ascii.txt","r+")
ordered = []
x = f.readline() #reads in one line at a time
ordered.append(x.strip('\n')) #it reads in the newline character so needs to be striped
while x:
    x = f.readline() #reads in one line at a time
    ordered.append(x.strip('\n'))
f.close()

for i in ordered:
    print(i)

print("Here is your list:\n")
print(ordered)
