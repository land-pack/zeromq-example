import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)

socket.bind("tcp://*:5551")


while True:
	print 'wait message in...'
	msg = socket.recv()
	print('msg:{}'.format(msg))
	socket.send('world')
