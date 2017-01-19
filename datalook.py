
# coding: utf-8

import sys
import numpy
import matplotlib.pyplot
#get_ipython().magic(u'matplotlib inline')

data = numpy.loadtxt (fname = 'data/weather-01.csv', delimiter = ',')

 
# # Functions
 

def fahr_to_kelvin(temp):
    return ((temp - 32)*(5.0/9.0)+273.15)

 
def analyse(filename, outfile=None):
    data = numpy.loadtxt(fname=filename, delimiter = ',')
    
    # create a wide figure to hold the subplots
    fig = matplotlib.pyplot.figure (figsize=(10.0,3.0))
    
    # create placeholders
    subplot1 = fig.add_subplot (1,3,1)
    subplot2 = fig.add_subplot (1,3,2)
    subplot3 = fig.add_subplot (1,3,3)

    # plot average, min and max graphs
    subplot1.set_ylabel('average')
    subplot1.plot(numpy.mean(data, axis=0))

    subplot2.set_ylabel('min')
    subplot2.plot(numpy.min(data, axis=0))

    subplot3.set_ylabel('max')
    subplot3.plot(numpy.max(data, axis=0))

    #show the graphs with a bit of space between them
#    fig.tight_layout()
    if outfile is None:
        matplotlib.pyplot.show()
    else:
        matplotlib.pyplot.savefig(outfile)


def detect_problems (filename):
    """ Some of our temperature files have problems, this function checks for these.
    
        Good code is 50% about good comments. 
    
    """
    data = numpy.loadtxt(fname=filename, delimiter = ',')
     
# TEST ON DATA:
    
    if numpy.max(data, axis = 0)[0] == 0 and numpy.max (data, axis=0)[20] == 20:
        print 'Suspicious looking maxima'
    elif numpy.sum(numpy.min(data, axis=0)) == 0:
        print 'Minima add up to zero'
    else: 'Data looks ok'
    
if __name__== "__main__": # if I'm running in the command line do this:

    print "Running ", sys.argv[0]

# for f in sys.argv[1:]:
#    print f
#    analyse(f)
#    detect_problems(f)

    print sys.argv[1]
    analyse (sys.argv[1], outfile=sys.argv[2])
    detect_problems(sys.argv[1])

 


