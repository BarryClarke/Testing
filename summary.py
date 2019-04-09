# Code to summarise Fisher's Iris data set
# Barry Clarke
# Rev1 - 6th Apr 2019

import numpy as np
import pandas as pd 
import matplotlib.pyplot as pyplot 
import pylab 

# Read data file into array
data = np.genfromtxt('Data/iris.csv', delimiter=',')

# Reviewing each attribute of each specie
# Inputting a global title
fig = pyplot.figure()                   # https://stackoverflow.com/questions/7526625/matplotlib-global-legend-and-title-aside-subplots
st = fig.suptitle("Comparison of Iris species for individual attributes", fontsize="x-large", fontweight="bold")

# Analysing the data for sepal length
setseplen = data[0:50,0]                # setseplen = Selecting the data for Setosa Sepal Length
verseplen = data[50:100,0]              # verseplen = Selecting the data for Versicolor Sepal Length
virseplen = data[100:150,0]             # virseplen = Selecting the data for Virginica Sepal Length

# Plot the sepal length data for all 3 species on the same graph
pyplot.subplot(2,2,1)                   # Ref https://matplotlib.org/gallery/subplots_axes_and_figures/subplot.html for plotting many plots
#pyplot.plot(setseplen, 'ro', label='Setosa', verseplen, 'bo', label='Versicolor', virseplen, 'go', label='Virginica') # Ref https://matplotlib.org/users/pyplot_tutorial.html
pyplot.plot(setseplen, 'ro', label='Setosa') 
pyplot.plot(verseplen, 'bo', label='Versicolor') 
pyplot.plot(virseplen, 'go', label='Virginica') 
pyplot.title('Sepal Length', fontweight='bold')
pyplot.ylabel('Centimeter')
#fig.subplots_adjust(left=None, bottom=None, right=None, top=0.9)
#fig.legend(loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=3)
pyplot.axis([0,50, 0, 8])

# Analysing the data for sepal width
setsepwid = data[0:50,1]                # setseplen = Selecting the data for Setosa Sepal Width
versepwid = data[50:100,1]              # verseplen = Selecting the data for Versicolor Sepal Width
virsepwid = data[100:150,1]             # virseplen = Selecting the data for Virginica Sepal Width

# Plot the sepal width data for all 3 species on the same graph
pyplot.subplot(2,2,3)
pyplot.plot(setsepwid, 'ro', versepwid, 'bo', virsepwid, 'go')
pyplot.title('Sepal Width', fontweight='bold')
pyplot.xlabel('sample number')
pyplot.ylabel('Centimeter')
pyplot.axis([0,50, 0, 8])

# Analysing the data for petal length
setpetlen = data[0:50,2]                # setseplen = Selecting the data for Setosa Petal Length
verpetlen = data[50:100,2]              # verseplen = Selecting the data for Versicolor Petal Length
virpetlen = data[100:150,2]             # virseplen = Selecting the data for Virginica Petal Length

# Plot the petal length data for all 3 species on the same graph
pyplot.subplot(2,2,2)
pyplot.plot(setpetlen, 'ro', verpetlen, 'bo', virpetlen, 'go')
pyplot.title('Petal Length', fontweight='bold')
pyplot.ylabel('Centimeter')
pyplot.axis([0,50, 0, 8])

# Analysing the data for petal width
setpetwid = data[0:50,3]                # setseplen = Selecting the data for Setosa Petal Width
verpetwid = data[50:100,3]              # verseplen = Selecting the data for Versicolor Petal Width
virpetwid = data[100:150,3]             # virseplen = Selecting the data for Virginica Petal Width

# Plot the petal width data for all 3 species on the same graph
pyplot.subplot(2,2,4)
pyplot.plot(setpetwid, 'ro', verpetwid, 'bo', virpetwid, 'go')
pyplot.title('Petal Width', fontweight='bold')
pyplot.xlabel('sample number')
pyplot.ylabel('Centimeter')
pyplot.axis([0,50, 0, 8])

# adjusting the size of the subplots to allow for room for the legend at the top of the subplots. 
fig.subplots_adjust(left=None, bottom=None, right=None, top=0.9)    #Ref: https://stackoverflow.com/questions/39164828/global-legend-for-all-subplots
fig.legend(loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=3)

pyplot.show()
#---------------------------------------------------------------------------------------------------------------------------------------------

# Main statistics for each specie
minsetseplen = np.min(data[0:50,0])      # Minimum Sepal length of a Setosa
maxsetseplen = np.max(data[0:50,0])      # Maximum Sepal length of a Setosa
meansetseplen = np.mean(data[0:50,0])    # Average Sepal length of a Setosa
scatsetseplen = np.max(data[0:50,0]) - np.min(data[0:50,0]) # The scatter of sepal length in the Setosa (ie Max length - Min length)

minverseplen = np.min(data[50:100,0])    # Average Sepal length of a Versicolor
maxverseplen = np.max(data[50:100,0])    # Average Sepal length of a Versicolor
meanverseplen = np.mean(data[50:100,0])  # Average Sepal length of a Versicolor
scatverseplen = np.max(data[50:100,0]) - np.min(data[50:100,0]) # The scatter of sepal length in the Versicolor

minvirseplen = np.min(data[100:150,0])  # Average Sepal length of a Virginica
maxvirseplen = np.max(data[100:150,0])  # Average Sepal length of a Virginica
meanvirseplen = np.mean(data[100:150,0])  # Average Sepal length of a Virginica
scatvirseplen = np.max(data[100:150,0]) - np.min(data[100:150,0]) # The scatter of sepal length in the Virginica

print("The data collected for Setosa sepal length is: \n", setseplen)
print("The minumum sepal length of a Setosa is: ", minsetseplen)
print("The maximum sepal length of a Setosa is: ", maxsetseplen)
print("The average sepal length of a Setosa is: ", format(meansetseplen, '.1f')) #ref https://docs.python.org/3/tutorial/floatingpoint.html for printing a number with limited decimal places 
print("The scatter of sepal length in the setosa is: ", format(scatsetseplen, '.1f'))
print()
print("The data collected for Versicolor sepal length is: \n", verseplen)
print("The minimum sepal length of a Versicolor is: ", minverseplen)
print("The maximum sepal length of a Versicolor is: ", maxverseplen)
print("The average sepal length of a Versicolor is: ", format(meanverseplen, '.1f'))
print("The scatter of sepal length in the Versicolor is: ", format(scatverseplen, '.1f'))
print()
print("The data collected for Virginica sepal length is: \n", virseplen)
print("The minimum sepal length of a Virginica is: ", minvirseplen)
print("The maximum sepal length of a Virginica is: ", maxvirseplen)
print("The average sepal length of a Virginica is: ", format(meanvirseplen, '.1f'))
print("The scatter of sepal length in the Virginica is: ", format(scatvirseplen, '.1f'))

#import numpy
#import matplotlib.pyplot as plot
#import pylab                        # Pylab allows the addition of a legend in a plot. Reference: https://stackoverflow.com/questions/19125722/adding-a-legend-to-pyplot-in-matplotlib-in-the-most-simple-manner-possible

# setup of the plot chart
#x = numpy.arange(0, 4.01, 0.1)


# setting up the plot title and axes labels
#pylab.title('Plot of x, $x^{2}$ and $2^{x}$ as a function of x', fontweight='bold')    # Superscripts in python plots. Reference: https://stackoverflow.com/questions/21226868/superscript-in-python-plots
#pylab.xlabel('x', fontweight='bold')
#pylab.ylabel('f(x)', fontweight='bold')
## Setting up each f(x), along with a legend
#pylab.plot(x, x, 'r-', label='x')
#pylab.plot(x, x**2, 'b-', label='$x^{2}$')
#pylab.plot(x, 2**x, 'g-', label='$2^{x}$')
#pylab.legend(loc='upper left')
# Setting up the axes limits
#pylab.axis([0, 5, 0, 18])

#pylab.show()


#sepal_length,sepal_width,petal_length,petal_width,species