import zmq
from zmq.eventloop import ioloop
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5551")

loop = ioloop.IOLoop.instance()


def f(sock, event):
	msg = sock.recv()
	print('recv:{}'.format(msg))
	sock.send('your said:{}'.format(msg))

if __name__ == '__main__':
	loop.add_handler(socket, f, zmq.POLLIN)
	loop.start()


