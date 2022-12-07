#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if(i == 8 & j == 9):
            print("{}{}".format(str(i),str(j)))
        elif(i < j):
            print("{}{}".format(str(i),str(j))+ ", ", end="")
