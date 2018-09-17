#Jacob Brunson & Carlos Ortiz

#This file contains methods to load data from .dat files and to print a decision tree

import re

#This method loads data from a given file name
def load_data(name):
	examples = [] #Training instances found in file
	attrs = [] #Attributes found in file

	f = open(name, "r")
	i = 0
	for line in f:
		#Skip lines that don't contain non-whitespace characters
		if not re.search('[^\t\r\n ]', line):
			continue

		#Split data along tab separator
		data = line.split("\t")

		#If first line (i.e. contains attributes) set attrs
		#Else create example dict. Key = attr name, Value = attr value
		if i == 0:
			attrs = data[:-1]
		else:
			ex = {}
			for j, attr in enumerate(attrs):
				ex[attr] = int(data[j])
			ex['class'] = int(data[-1])
			examples.append(ex)

		i += 1

	f.close()
	return (examples, attrs)

#Print a decision tree
#n = tree, d = 0 for left d = 1 for right, level = indentation level
def printTree(n, d, level=0):
	s = "%s = %d :"
	if n.classification == -1:
		print ("| " * level) + s % (n.parent.splitOn, d)
		printTree(n.leftNode, 0, level+1)
		printTree(n.rightNode, 1, level+1)
	else:
		s += "  %d"
		print ("| " * level) + s % (n.parent.splitOn, d, n.majorityClass())