import sys

try:
    open_file = open("./rumi.txt",encoding="utf8")
    print("file opened successfully")

    count = 0
    for line in open_file:
        count = count + 1
        print(line)
        
except Exception as err:
    print("Error: %s" % str(err))

finally:
    print("final line")