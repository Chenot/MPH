import sys; sys.path.append('..') # help python find pylsl relative to this example program
from pylsl import StreamInlet, resolve_stream
import matplotlib.pyplot as plt
from time import sleep, time
import numpy as np
import pdb

# first resolve an EEG stream on the lab network
print("looking for an ECG stream...")
streams= resolve_stream('type','ECG')
# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

fig, ax = plt.subplots(1, 1)
ax.set_aspect('equal')
ax.set_xlim(0, 1500)
ax.set_ylim(-500,500)
ax.hold(True)
x, y = 0,0

plt.show(False)
plt.draw()

background = fig.canvas.copy_from_bbox(ax.bbox)

line = ax.plot(x, y, '.')[0]
tic = time()
i=0
while True:
    # get a new sample (you can also omit the timestamp part if you're not interested in it)
    sample,timestamp = inlet.pull_sample()
    #print(timestamp, sample)

    x = np.concatenate((line.get_xdata(),[i]))
    y = np.concatenate((line.get_ydata(),[sample[0]]))
    line.set_data(x,y)
    
    plt.draw() 
    
    #~ points.set_data(x, y)
   
    # restore background
    #~ fig.canvas.restore_region(background)
#~ 
    #~ # redraw just the points
    #~ ax.draw_artist(points)
#~ 
    #~ # fill in the axes rectangle
    #~ fig.canvas.blit(ax.bbox)
    i+=1
