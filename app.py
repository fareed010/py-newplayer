thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]


tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

for i in thislist:
    if i == "melon":
        thislist.remove("melon")
    print(thislist)
