import zmq

Context = zmq.Context()

# request 
socket = Context.socket(zmq.REQ) 
socket.connect("tcp://localhost:5551")

while True:
	msg= raw_input("Please input your message:")
	socket.send(msg)
	ser_msg = socket.recv()
	print("Server said:{}".format(ser_msg))


