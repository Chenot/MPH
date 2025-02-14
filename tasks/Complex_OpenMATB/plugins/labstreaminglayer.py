# Copyright 2023-2024, by Julien Cegarra & Benoît Valéry. All rights reserved.
# Institut National Universitaire Champollion (Albi, France).
# License : CeCILL, version 2.1 (see the LICENSE file)

from plugins import Instructions
from core import validation
import socket
import json
import threading
from pylsl import local_clock

try:
    import pylsl
except:
    print("unable to import pylsl")

class Labstreaminglayer(Instructions):
    def __init__(self):
        super().__init__()

        self.validation_dict =  {
            'marker': validation.is_string,
            'MPH_send_markers': validation.is_string,
            'streamsession': validation.is_boolean,
            'pauseatstart': validation.is_boolean, 'state': validation.is_string}

        self.parameters.update({'marker':'', 'MPH_send_markers': '', 'streamsession':False,
                                'pauseatstart':False})

        self.stream_info = None
        self.stream_outlet = None
        self.stop_on_end = False

        self.lsl_wait_msg = _("Please enable the OpenMATB stream into your LabRecorder.")


    def start(self):
        # If we get there it's because the plugin is used.
        # If pylsl is not available this part should fail.
        # Create a LSL marker outlet.
        super().start()
        #self.stream_info = pylsl.StreamInfo('OpenMATB', type='Markers', channel_count=1,
        #                                     nominal_srate=0, channel_format='string',
        #                                     source_id='myuidw435368')
        self.stream_info = pylsl.StreamInfo(name='ExperimentMarkers', type='Markers', channel_count=1,
                                   nominal_srate=0, channel_format='string',
                                   source_id='experiment_marker_stream')

        self.stream_outlet = pylsl.StreamOutlet(self.stream_info)

        if self.parameters['pauseatstart'] is True:
            self.slides = [self.get_msg_slide_content(self.lsl_wait_msg)]


    def update(self, dt):
        super().update(dt)

        if self.parameters['streamsession'] is True and self.logger.lsl is None:
            self.logger.lsl = self
        elif self.parameters['streamsession'] is False and self.logger.lsl is not None:
            self.logger.lsl = None

        # Check if a marker is set and push it to the LSL stream
        if self.parameters['marker'] != '':
            self.push(self.parameters['marker'])
            self.parameters['marker'] = ''  # Reset marker after pushing
    
        # Check if MPH_send_markers is set and send the marker via socket
        if self.parameters['MPH_send_markers'] != '':
            self.MPH_send_markers(self.parameters['MPH_send_markers'])
            self.parameters['MPH_send_markers'] = ''  # Reset after sending


    def push(self, message):
        if self.stream_outlet is None:
            return
        self.stream_outlet.push_sample([message])
        print(message)

    def stop(self):
        super().stop()
        self.stream_info = None
        self.stream_outlet = None


    def get_msg_slide_content(self, str_msg):
        return f"<title>Lab streaming layer\n{self.lsl_wait_msg}"

    # Custom function to send markers via a socket (MPH_send_markers)
    def MPH_send_markers(self, marker):
        event = {
            'marker': marker,
            'timestamp': local_clock()
        }
        message = json.dumps(event)

        def send():
            try:
                # Connect to the socket server and send the marker with a timeout
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.settimeout(0.1)  # Set timeout to 100 milliseconds
                client_socket.connect(('localhost', 5000))  # Assuming the server is on localhost:5000
                client_socket.sendall(message.encode('utf-8'))
                client_socket.close()
            except (ConnectionRefusedError, socket.timeout):
                print("LSL server is not running or connection timed out. Continuing without sending marker.")

        # Create and start a thread to send the marker
        send_thread = threading.Thread(target=send)
        send_thread.start()
        