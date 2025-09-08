import numpy as np
import matplotlib.pyplot as plt

ages = np.random.randint(10,81,50)

plt.hist(ages,bins=range(10,85,5), color='lavender',edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Histogram of Random Ages')
plt.show()