#!/usr/bin/python2
#Katarzyna Banachowicz gr. 1

import sys, re

def is_number(n):
	try:
		if n[0] is not '-' and n[0] is not '+':
			float(n)
			return True
		else:
			return False
	except ValueError:
		return False

def checkNumber(grade):

	if is_number(grade):
		grade = float(grade)
		#print 'grade: {}'.format(grade)
		return grade	
	else:
		if grade[0] == '-':
			grade = float(grade[1])
			grade = grade - 0.25
			return grade
		elif grade[-1] == '-':
			grade = float(grade[0])
			grade = grade - 0.25
			return grade
		elif grade[0] == '+':
			grade = float(grade[1])
			grade = grade + 0.25
			return grade
		elif grade[-1] == '+':
			grade = float(grade[0])
			grade = grade + 0.25
			return grade
		else:
			#print 'some number is no number, neither + or - thing: {}'.format(grade)
			return grade