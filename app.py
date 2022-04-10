thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]


tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

newList = [x if x != "banana" else "orange" for x in thislist]

print(newList)