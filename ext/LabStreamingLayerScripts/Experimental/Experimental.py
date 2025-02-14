from pylsl import StreamInfo, StreamOutlet, local_clock
import socket
import json
import threading

def start_lsl_server():
    # Create LSL stream outlet
    info = StreamInfo(name='ExperimentMarkers', type='Markers', channel_count=1, channel_format='string', source_id='experiment_marker_stream')
    outlet = StreamOutlet(info)
    
    # Setup socket server to receive events
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen(1)
    server_socket.settimeout(5)  # Set a timeout of 5 seconds for the accept call
    
    print("LSL server started, waiting for events...")
    
    while True:
        try:
            client_socket, addr = server_socket.accept()
            data = client_socket.recv(1024).decode('utf-8')
            event = json.loads(data)
            marker = event['marker']
            timestamp = event['timestamp']
            outlet.push_sample([marker], timestamp)
            client_socket.close()
        except socket.timeout:
            continue  # Just continue the loop if no connection is received within the timeout

def main():
    server_thread = threading.Thread(target=start_lsl_server)
    server_thread.start()

if __name__ == "__main__":
    main()
