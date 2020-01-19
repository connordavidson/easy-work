import os, time
#opens the file called websites.txt (assumed to be in the same folder as this script) in read mode and prepares the file to be read line by line
f = open('websites.txt', mode='r')
file = f.readlines()
#loop through every line in the file and ping the website on that line. Has to use [ :-1] because the last character of every line is a newline character (\n). This messes up the command variable and puts it onto 2 lines
drive_number = 1
for website in file:
    command = "ping %s -c 1" % website[ : -1]
    print("PINGING: " + website[ : -1] )
    os.system(command)
    #sleep for 3 seconds before running the command again
    time.sleep(3)
    os.system(command)
    drive_number += 1
