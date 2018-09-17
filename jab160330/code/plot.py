#This code is for generating the graphs
#This should not be evaluated by the grader, but is here for completeness

import matplotlib.pyplot as plt

x = range(1, max_instances)

y_training = []
y_testing = []
for i in x:
	n = Node(training_data[:i])
	learn.learn(n, attributes)
	y_training.append(learn.test(n, training_data))
	y_testing.append(learn.test(n, testing_data))

fig, ax = plt.subplots()
ax.plot(x, y_training, label="Training Data")
ax.plot(x, y_testing, label="Testing Data")

plt.xlabel('Number of Instances')
plt.ylabel('Accuracy')
ax.legend()

plt.title('Learning Curve')

plt.show()