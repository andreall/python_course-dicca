#!/usr/bin/env python
# coding: utf-8

# # Introduction to Matplotlib

# The **Matplotlib** package can be used to make scientific-grade plots. You can import it with:

# In[1]:


import matplotlib.pyplot as plt


# If you are using IPython and you want to make interactive plots, you can start up IPython with:
# 
#     ipython --matplotlib
# 
# If you now type a plotting command, an interactive plot will pop up.
# 
# If you use the IPython notebook, add a cell containing:

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# and the plots will appear inside the notebook.

# ## Basic plotting

# The main plotting function is called ``plot``:

# In[3]:


plt.plot([1,2,3,6,4,2,3,4])


# In the above example, we only gave a single list, so it will assume the x values are the indices of the list/array.

# However, we can instead specify the x values:

# In[4]:


plt.plot([3.3, 4.4, 4.5, 6.5], [3., 5., 6., 7.])


# Matplotlib can take Numpy arrays, so we can do for example:

# In[5]:


import numpy as np
x = np.linspace(0., 10., 50)
y = np.sin(x)
plt.plot(x, y)


# The ``plot`` function is actually quite complex, and for example can take arguments specifying the type of point, the color of the line, and the width of the line:

# In[6]:


plt.plot(x, y, marker='o', color='green', linewidth=2)


# The line can be hidden with:

# In[7]:


plt.plot(x, y, marker='o', color='green', linewidth=0)


# If you are interested, you can specify some of these attributes with a special syntax, which you can read up more about in the Matplotlib documentation:

# In[8]:


plt.plot(x, y, 'go')  # means green and circles


# In[9]:


X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C)
plt.plot(X, S)


# ## Exercise

# We start off by loading the ``data/SIMAR_gaps.txt`` file which we encountered in the Numpy lecture:

# In[10]:


# The following code reads in the file and removes bad values
import numpy as np
data = np.loadtxt('data/SIMAR_gaps.txt', skiprows=1)
Hm0 = data[:, 4]
keep = Hm0 > -99.9
data = data[keep]


# Now that the data has been read in, plot the Hm0:

# In[11]:


# your solution here


# ## Customizing plots

# In[12]:


# Create a figure of size 8x6 inches, 80 dots per inch
plt.figure(figsize=(8, 6), dpi=80)

# Create a new subplot from a grid of 1x1
plt.subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)

# Plot cosine with a blue continuous line of width 1 (pixels)
plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# Plot sine with a green continuous line of width 1 (pixels)
plt.plot(X, S, color="green", linewidth=1.0, linestyle="-")

# Set x limits
plt.xlim(-4.0, 4.0)

# Set x ticks
plt.xticks(np.linspace(-4, 4, 9))

# Set y limits
plt.ylim(-1.0, 1.0)

# Set y ticks
plt.yticks(np.linspace(-1, 1, 5))


plt.xlabel('x values')
plt.ylabel('y values')


# In[13]:


plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sine")

plt.legend(loc='upper left')


# ## Other types of plots

# <center> <img src="img/matplotlib_ex.png" width="1600"/> </center>

# ### Scatter plots

# While the ``plot`` function can be used to show scatter plots, it is mainly used for line plots, and the ``scatter`` function is more often used for scatter plots, because it allows more fine control of the markers:

# In[14]:


x = np.random.random(100)
y = np.random.random(100)
plt.scatter(x, y)


# ### Errorbar

# In[15]:


###  generate some random data
xdata2 = np.arange(15)
ydata2 = np.random.randn(15)
yerrors = np.random.randn(15)

###  initialize the figure
fig, ax = plt.subplots()

ax.errorbar(xdata2, ydata2, yerr=yerrors)


# In[16]:


plt.errorbar(xdata2, ydata2, yerr=yerrors, ls='',         # no lines connecting points
                                               marker='*',    # circular plot symbols
                                               ms=20,         # marker size
                                               mfc='r',       # marker face color
                                               mew=2,         # marker edge width
                                               mec='k',       # marker edge color
                                               elinewidth=2,  # error line width
                                               ecolor='gray', # error color
                                               capsize=6)     # error hat sizex


# ### Histograms

# Histograms are easy to plot using the ``hist`` function:

# In[17]:


v = np.random.uniform(0., 10., 100)
h = plt.hist(v)  # we do h= to capture the output of the function, but we don't use it


# In[18]:


h = plt.hist(v, range=[-5., 15.], bins=100)


# In[19]:


h = plt.hist(v, orientation='horizontal')


# ### Images

# You can also show two-dimensional arrays with the ``imshow`` function:

# In[20]:


array = np.random.random((64, 64))
plt.imshow(array)


# And the colormap can be changed:

# In[21]:


plt.imshow(array, cmap=plt.cm.gist_heat)


# ### Contour

# In[22]:


def f(x,y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X,Y = np.meshgrid(x, y)

plt.axes([0.025, 0.025, 0.95, 0.95])

plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
plt.clabel(C, inline=1, fontsize=10)

plt.xticks([])
plt.yticks([])
plt.show()


# ### Polar plots

# In[23]:


ax = plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)

N = 20
theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / N)
radii = 10 * np.random.rand(N)
width = np.pi / 4* np.random.rand(N)
bars = plt.bar(theta, radii, width=width, bottom=0.0)

for r,bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.jet(r/10.))
    bar.set_alpha(0.5)

ax.set_xticklabels([])
ax.set_yticklabels([])
plt.show()


# ### Multiplots

# In[24]:


# First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# Create just a figure and only one subplot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple plot')


# In[25]:


# Create two subplots and unpack the output array immediately
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)


# In[26]:


# Create four polar axes and access them through the returned array
fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
axs[0, 0].plot(x, y)
axs[1, 1].scatter(x, y)


# In[27]:


# Share a X axis with each column of subplots
plt.subplots(2, 2, sharex='col')

# Share a Y axis with each row of subplots
plt.subplots(2, 2, sharey='row')

# Share both X and Y axes with all subplots
plt.subplots(2, 2, sharex='all', sharey='all')

# Note that this is the same as
plt.subplots(2, 2, sharex=True, sharey=True)


# ## Saving plots to files

# To save a plot to a file, you can do for example:

# In[28]:


plt.savefig('my_plot.png')


# and you can then view the resulting file like you would iew a normal image. On Linux, you can also do:
# 
#     $ xv my_plot.png
# 
# in the terminal.

# ## Learning more

# The easiest way to find out more about a function and available options is to use the ``?`` help in IPython:
# 
#         In [11]: plt.hist?
# 
#     Definition: plt.hist(x, bins=10, range=None, normed=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, hold=None, **kwargs)
#     Docstring:
#     Plot a histogram.
# 
#     Call signature::
# 
#       hist(x, bins=10, range=None, normed=False, weights=None,
#              cumulative=False, bottom=None, histtype='bar', align='mid',
#              orientation='vertical', rwidth=None, log=False,
#              color=None, label=None, stacked=False,
#              **kwargs)
# 
#     Compute and draw the histogram of *x*. The return value is a
#     tuple (*n*, *bins*, *patches*) or ([*n0*, *n1*, ...], *bins*,
#     [*patches0*, *patches1*,...]) if the input contains multiple
#     data.
# 
#     etc.
# 
# But sometimes you don't even know how to make a specific type of plot, in which case you can look at the [Matplotlib Gallery](http://matplotlib.org/gallery.html) for example plots and scripts.
# 

# ## Exercise

# Use Numpy to make the histogram of Hm0 and make a histogram. Try changing the number of bins and try plotting the CDF on top of it.

# In[29]:



# your solution here

