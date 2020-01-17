import os
# from pathlib import Path

f = open('websites.txt', mode='r')

file = f.readlines()

for website in file:


    print("PINGING: " + website)
    os.system("ping " + website + " -c 1")


# os.system("date")
