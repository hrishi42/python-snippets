#!/usr/bin/python
userstring=raw_input("Enter the text: ")
print "Text entered by you is: ",userstring
userstring=userstring.lower()

focuslist=list(userstring)

finallist=[]
for item in focuslist:
	if item == 'a':
		item='c'
		finallist.append(item)
	elif item == 'b':
		item='d'
		finallist.append(item)
	elif item == 'c':
		item='e'
		finallist.append(item)
	elif item == 'd':
		item='f'
		finallist.append(item)
	elif item == 'e':
		item='g'
		finallist.append(item)
	elif item == 'f':
		item='h'
		finallist.append(item)
	elif item == 'g':
		item='i'
		finallist.append(item)
	elif item == 'h':
		item='j'
		finallist.append(item)
	elif item == 'i':
		item='k'
		finallist.append(item)
	elif item == 'j':
		item='l'
		finallist.append(item)
	elif item == 'k':
		item='m'
		finallist.append(item)
	elif item == 'l':
		item='n'
		finallist.append(item)
	elif item == 'm':
		item='o'
		finallist.append(item)
	elif item == 'n':
		item='p'
		finallist.append(item)
	elif item == 'o':
		item='q'
		finallist.append(item)
	elif item == 'p':
		item='r'
		finallist.append(item)
	elif item == 'q':
		item='s'
		finallist.append(item)
	elif item == 'r':
		item='t'
		finallist.append(item)
	elif item == 's':
		item='u'
		finallist.append(item)
	elif item == 't':
		item='v'
		finallist.append(item)
	elif item == 'u':
		item='w'
		finallist.append(item)
	elif item == 'v':
		item='x'
		finallist.append(item)
	elif item == 'w':
		item='y'
		finallist.append(item)
	elif item == 'x':
		item='z'
		finallist.append(item)
	elif item == 'y':
		item='a'
		finallist.append(item)
	elif item == 'z':
		item='b'
		finallist.append(item)
	elif item == ' ':
		item=' '
		finallist.append(item)
final_answer=''.join(finallist)
print "Final text is (after decryption): ",final_answer
