mylist = []
count = 0
with open ('Ocean-City.txt','r') as f:
    for line in f:
        if (count == 0):
            mylist.append(line.rstrip())
        if (count == 1):
            mylist.append(float(line))
        if (count == 2):
            mylist.append(line.rstrip())
        if (count == 3):
            mylist.append("AutoGenerated")
            mylist.append(line.rstrip())
        if (count == 4):
            mylist.append(line.rstrip())
        if (count == 5):
            mylist.append(float(line))
        if (count == 6):
            mylist.append(float(line))
        count = count + 1
        if (count >= 7):
            print(mylist)
            mylist = []
            count = 0
        

        