import serial

class serialstream:
	def __init__(self,port = '/dev/ttyS0',baudrate = 9600):
		self.port = port
		self.baudrate = baudrate
		self.c = serial.Serial(self.port,baudrate = self.baudrate)
		self.c.flush()
		#while True:
		#	if self.c.in_waiting>0:print(self.c.readline())


	def serialread(self):
		try:
			if self.c.in_waiting>0:
				return self.c.readline()
		except: #if any error

			try:
				self.c.flush()
				self.c.close()
				c = serial.Serial(self.port,baudrate = self.baudrate)
			except:
				self.c.flush()
				self.c.close()
				self.c = serial.Serial(self.port,baudrate = self.baudrate)


#if __name__ =='__main__':
#	S = serialstream()
#	while True:
#		data = S.serialread()
#		if data is not None:
#			print(data)
