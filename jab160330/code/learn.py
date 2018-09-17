#Jacob Brunson & Carlos Ortiz

#This file contains the ID3 algorithm and 2 small methods for clasifying and testing instances

from __future__ import division

#This method is an implementation of the ID3 algorithm
def learn(n, attrs):
	#Make leaf if node is pure
	if n.isPure():
		n.classification = n.examples[0]['class']
		return

	#Make leaf w/ majority class if we already split on every attribute
	if len(attrs) == 0:
		n.classification = n.majorityClass()
		return

	#This loop will set Same to False if every example isn't identical
	Same = True
	for a in attrs:
		value = n.examples[0][a]
		for e in n.examples:
			if e[a] != value:
				Same = False
				break
		if not Same:
			break
	#If every example is identical then make leaf w/ majority
	if Same:
		n.classification = n.majorityClass()
		return

	maxIG = -1 #This will store max information gain
	maxAttr = None #This will be the attribute that will give us the most IG
	minAttrIndex = len(attrs) #This keeps track of the attribute index (needed for tiebreaking)
	maxNodes = (None, None) #This will be a pair of nodes that result from splitting on maxAttr

	#This loop calculates the 4 variables described above
	for i, a in enumerate(attrs):
		nodes = n.split(a) #Split on attribute a
		tempIG = n.informationGain(nodes[0], nodes[1]) #Calculate IG from that split
		if(tempIG > maxIG or (tempIG == maxIG and i < minAttrIndex)): #check if this IG is the highest we've seen
			maxIG = tempIG 
			maxAttr = a
			minAttrIndex = i
			maxNodes = nodes

	#Save which attribute we are splitting on
	n.splitOn = maxAttr

	#Set the children of current node
	n.leftNode = maxNodes[0]
	n.rightNode = maxNodes[1]

	#Remove attribute from list (so we don't consider it again)
	attrs = [x for x in attrs if x != maxAttr]

	#Repeat for children
	learn(n.leftNode, attrs)
	learn(n.rightNode, attrs)


#This method classifies an example given a decision tree n
def classify(n, example):
	if n.classification != -1:
		return n.classification
	if example[n.splitOn] == 0:
		return classify(n.leftNode, example)
	else:
		return classify(n.rightNode, example)

#This method calculates an accuracy given a decision tree and a list of examples
def test(tree, examples):
	correct = 0
	total = 0
	for e in examples:
		total += 1
		prediction = classify(tree, e)
		actual = e['class']
		if prediction == actual:
			correct += 1
	return correct / total