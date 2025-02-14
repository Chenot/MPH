import sys; sys.path.append('..') # help python find pylsl relative to this example program
#from pylsl import StreamInfo, StreamOutlet
import pylsl
import random
import time
import numpy as np

# first create a new stream info (here we set the name to MyMarkerStream, the content-type to Markers, 1 channel, irregular sampling rate, and string-valued data)
# The last value would be the locally unique identifier for the stream as far as available, e.g. program-scriptname-subjectnumber (you could also omit it but interrupted connections wouldn't auto-recover).
# The important part is that the content-type is set to 'Markers', because then other programs will know how to interpret the content
info = pylsl.stream_info("LSLMarkers","Markers",1,0,pylsl.cf_int32,'myID_123');

# next make an outlet
outlet = pylsl.stream_outlet(info)

print("now sending markers...")
#markernames = ['Test', 'Blah', 'Marker', 'XXX', 'Testtest', 'Test-1-2-3']
mrk1=10
while True:
	# pick a sample to send an wait for a bit
	outlet.push_sample([mrk1])
	time.sleep(random.random()*3)
