
# coding: utf-8

# In[1]:

import numpy
import matplotlib.pyplot
get_ipython().magic(u'matplotlib inline')


# In[2]:

data = numpy.loadtxt (fname = 'data/weather-01.csv', delimiter = ',')


# In[3]:

print data


# In[4]:

# WARNING: put the following all in the same cell!

# create a wide figure to hold the subplots
fig = matplotlib.pyplot.figure (figsize=(10.0,3.0))

# create placeholders

subplot1 = fig.add_subplot (1,3,1)
subplot2 = fig.add_subplot (1,3,2)
subplot3 = fig.add_subplot (1,3,3)

subplot1.set_ylabel('average')
subplot1.plot(numpy.mean(data, axis=0))

subplot2.set_ylabel('min')
subplot2.plot(numpy.min(data, axis=0))

subplot3.set_ylabel('max')
subplot3.plot(numpy.max(data, axis=0))

fig.tight_layout()
matplotlib.pyplot.show()


# # Loops

# In[5]:

# we can call the letters of a string one by one
word = 'notebook'
print (word[4])


# In[6]:

# we can loop across every letter:
# INDENTATION IS KEY IN PYTHON!!!

for char in word:
    print (char)
        
    
    


# # Get a list of all the filenames from disk

# In[7]:

import glob


# In[8]:

print (glob.glob('data/weather*.csv')) # * is the wildcard


# This above is a list of twelve strings, each string represents a file. We should now be able to produce a series of plots.
# 
# ## Putting it all together:
# 

# In[9]:

filenames = sorted(glob.glob('data/weather*.csv')) # sorted it's to make sure they are in order -it's not guaranteed otherwise-

filenames = filenames[0:3]  # variable overwriting, to avoid too much data here

for f in filenames:  # loops across the three filenames
    print (f)
    
    data = numpy.loadtxt(fname = f, delimiter =',')

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
    fig.tight_layout()
    matplotlib.pyplot.show()


# # Making decisions

# In[10]:

num = 37

if num > 100:
    print ('Greater')
else:
    print ('Not greater')
    
print 'Done'


# In[11]:

num = -3

if num > 0:
    print num, 'is positive'
elif num == 0:                 # double equal is used to test (! used to test if not equal)
    print num, 'is zero'
else:
    print num, 'is negative'


# # something more on the plots

# In[12]:

filenames = sorted(glob.glob('data/weather*.csv')) # sorted it's to make sure they are in order -it's not guaranteed otherwise-

# filenames = filenames[0:3]  # variable overwriting, to avoid too much data here while testing
                              # line commented out after verifying everything works

for f in filenames:  # loops across the three filenames
    print (f)
    
    data = numpy.loadtxt(fname = f, delimiter =',')

# TEST ON DATA:
    
    if numpy.max(data, axis = 0)[0] == 0 and numpy.max (data, axis=0)[20] == 20:
        print 'Suspicious looking maxima'
    elif numpy.sum(numpy.min(data, axis=0)) == 0:
        print 'Minima add up to zero'
    else: 'Data looks ok'
        
    
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
    fig.tight_layout()
    matplotlib.pyplot.show()


# # Functions

# Ways to create reusable chunks of code.

# In[19]:

def fahr_to_kelvin(temp):
    return ((temp - 32)*(5.0/9.0)+273.15)


# In[20]:

print 'Freezing point of water in Kelvin: ', fahr_to_kelvin(32)
print 'Boiling point of water in Kelvin: ', fahr_to_kelvin(200)


# # analysis function

# In[23]:

def analyse(filename):
    """ Some of our temperature files have problems, this function checks for these.
    
        Good code is 50% about good comments. 
    
    """
    
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
    fig.tight_layout()
    matplotlib.pyplot.show()
    


# In[16]:

def detect_problems (filename):
    data = numpy.loadtxt(fname=filename, delimiter = ',')
    
    
# TEST ON DATA:
    
    if numpy.max(data, axis = 0)[0] == 0 and numpy.max (data, axis=0)[20] == 20:
        print 'Suspicious looking maxima'
    elif numpy.sum(numpy.min(data, axis=0)) == 0:
        print 'Minima add up to zero'
    else: 'Data looks ok'
    
    # this is a rough test (if max has problems then min is not checked), but you can write a better one
    # for example by concatenating things with "and"
    


# In[17]:

for f in filenames [0:5]:
    print f
    analyse(f)
    detect_problems(f)


# # 19th of January 2017

# In[22]:

help(numpy.loadtxt)


# In[24]:

help (analyse)


# In[ ]:



