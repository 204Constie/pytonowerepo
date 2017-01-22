#!/usr/bin/python2
#Katarzyna Banachowicz gr. 1

import sys, os.path

from smallpyton import checkNumber

for filename in sys.argv[1:]:
	try:
		with open(filename) as class_register:
			lines = class_register.readlines()
	except IOError:
		print >> stderr, 'incorrect line: {}'.format(lines)
	else:
		dictionary = dict()
		for line in lines:
			words = [w.strip() for w in line.split(' ') if w.strip() is not '']
			#print 'words: {}'.format(words)
			if len(words) is not 3:
				print >> stderr, 'incorrect line: {}'.format(lines)
				continue
			firstname = words[0].title()
			lastname = words[1].title()
			#print 'firstname: {}, lastname: {}'.format(firstname, lastname)

			grade = checkNumber(words[2])

			key = '%s %s' % (firstname, lastname)
			if key in dictionary:
				dictionary[key].append(grade)
			else:
				dictionary[key] = [grade]
		#print 'dictionary: {}'.format(dictionary)

		medians = []

		for key, value in sorted(dictionary.items()):
			a = 0
			for grade in dictionary[key]:
				a = a + grade
			b = a/len(dictionary[key])
			b = round(b, 2)
			medians.append(b)
			print '{} : {} : {}'.format(key, value, b)

		m = 0
		for value in medians:
			m = m + value
		print 'median for the whole class: {0:.2f}'.format(m/len(medians))
