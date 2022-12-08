#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    for args in sys.argv[1:]:
        sum += int(args)
    print(sum)    
