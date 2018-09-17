#Jacob Brunson & Carlos Ortiz

#This file contains the definition of the Node class along with the various math functions utlized by the ID3 algorithm

from __future__ import division
import math

#Special log function where log(0) = 0
def log2(x):
	if (x == 0):
		return 0
	return math.log(x, 2)

#Each node of a decision tree is represented by this
class Node:
	examples = [] #All training instances for thid node 
	classification = -1 #Leaf = -1, Class 0 = 0, Class 1 = 1
	leftNode = None #Reference to Node instance for left child
	rightNode = None #Reference to Node instance for right child
	splitOn = None #Attribute which this node will split on
	parent = None #Reference to Node instance for parent
	root = None #Reference to Node instance for root

	#Constructor: Populate training instances, set root and parent
	def __init__(self, examples, parent=None):
		self.examples = examples
		self.parent = parent
		self.root = self
		if parent is not None:
			self.root = parent.root

	#Calculate entropy of this Node
	def entropy(self):
		H = 0
		total = len(self.examples)

		#If there are no examples, entropy is 0
		if total == 0:
			return 0

		#This will populate counts with the number of instances of each class.
		#Counts[i] == # of instances of class i
		counts = [0, 0]
		for e in self.examples:
			counts[e['class']] += 1
		
		#Summation formula from slides
		for count in counts:
			p = count / total
			H -= p * log2(p)

		return H

	#Calculate information gain from splitting into node0 and node1
	def informationGain(self, node0, node1):
		#Get entropy of each node
		H = self.entropy()
		Hl = node0.entropy()
		Hr = node1.entropy()

		#Get proportions for each class
		Pl = len(node0.examples)/len(self.examples)
		Pr = len(node1.examples)/len(self.examples)

		#Compute IG using formula from slides
		IG = H - ((Hl)*(Pl) + (Hr)*(Pr))

		return IG

	#Return pair of nodes that result from splitting this node 
	def split(self, attr):
		leftExamples = [] #Examples for attr = 0
		rightExamples = [] #Examples for attr = 1

		#Add examples to respective list
		for e in self.examples:
			if(e[attr] == 0):
				leftExamples.append(e)
			if(e[attr] == 1):
				rightExamples.append(e)

		#Create node objects using example lists
		left = Node(leftExamples, self)
		right = Node(rightExamples, self)

		return (left, right)

	#Returns true of examples in node are all of the same class
	def isPure(self):
		c = self.examples[0]['class'] #Class of first example

		#Check if every example matches first example
		for e in self.examples:
			if e['class'] != c:
				return False

		return True

	#Returns the class that has the most examples in this node
	#If evenly split, will choose the most frequent class of all data
	def majorityClass(self):
		#Usually the split method is for attributes
		#but we if we split on class then we can easily count the number of examples for each class
		s = self.split('class')

		if len(s[0].examples) > len(s[1].examples):
			return 0
		elif len(s[0].examples) < len(s[1].examples):
			return 1 
		else:
			#If the classes are evenly split for the entire distribution (i.e. root) then return 0
			if self.root == self:
				return 0
			else:
				return self.root.majorityClass()