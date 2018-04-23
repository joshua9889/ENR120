# Part 1
# 1
Myfile = open('myfile.txt', 'w')
Myfile.write("hello text file\n")
Myfile.write("goodbye text file\n")
Myfile.close()

# 2
Myfile = open('myfile.txt', 'w')
Myfile.write("hello world there is some text in my file\n")
Myfile.write("goodbye file it's been nice knowing you, text file\n")
Myfile.close()

# 4
open('myfile.txt').read()
print(open('myfile.txt').read())
for line in open('myfile.txt'):
    print line

# Part 2
# Open file
f = open('myList.txt', 'w')

print "Enter q to quit the program."

running = True
while running:
    userInput = str(raw_input(""))

    if userInput.strip().lower() == 'q':
        running = False
    else:
        f.write(userInput + '\n')

f.close()
