code = input('Codes: ')
codeSplit = code.split(' ')
for i in codeSplit:
    result = int(i)
    print(chr(result))
