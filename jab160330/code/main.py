#Jacob Brunson & Carlos Ortiz
#main.py <training_file> <testing_file> <max_training_instances>
#Outputs decision tree built using ID3 algorithm on training_file
#Also outputs testing accuracy on training set and testing set

#This is the main entry point of the application
#It checks the command line parameters, loads the data, builds the tree, prints the output

import sys

from node import Node
import learn
import util

#Check argument count
if len(sys.argv) != 4:
	print "Invalid number of arguments"
	sys.exit()

#Set argument variables
training_file = sys.argv[1]
test_file = sys.argv[2]
max_instances = int(sys.argv[3])

#This will hold the list of attributes e.g. [wesley, romulan, poetry]
attributes = []

#These will hold all of the training / testing vectors
training_data = []
testing_data = []

#Load the data from file
(training_data, attributes) = util.load_data(training_file)
(testing_data, _) = util.load_data(test_file)

#Create the root node of our tree and start recursive learning
n = Node(training_data[:max_instances])
learn.learn(n, attributes)

#Print the resulting tree
util.printTree(n.leftNode, 0)
util.printTree(n.rightNode, 1)

#Print accuracy percentages
print "\nAccuracy on training set (%d instances): %.1f%%" % (len(training_data), learn.test(n, training_data)*100)
print "\nAccuracy on test set (%d instances): %.1f%%" % (len(testing_data), learn.test(n, testing_data)*100)