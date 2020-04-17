import ipfshttpclient
# Objeto para un cliente que corre continuamente
class ipfsPubSub:
	"""Clase para el cliente de Publisher-Subscriber"""
	def __init__(self, conn = "/ip4/127.0.0.1/tcp/5001"):
		self._client = ipfshttpclient.connect(conn)
		self._pubsub = self._client.pubsub
	def client(self):
		return self._client
	def pubsub(self):
		return self._pubsub
	# Subscribirse
	def sub(self, topic, discover = False, **kwargs):
		return self._pubsub.subscribe(topic, discover, **kwargs)
	# Publicar
	def pub(self, topic, toPub, **kwargs):
		self._pubsub.publish(topic,toPub, **kwargs)
	def ls(self, **kwargs):
		return self._pubsub.ls(**kwargs)
	def peers(self, topic = None, **kwargs):
		return self._pubsub.peers(topic,**kwargs)
	def testConn(self):
		for item in self._client.id().items():
			print(item)
	def close(self):
		self._client.close()
def main():
	from base64 import b64encode,b64decode
	# Ejemplos
	# Instancia de clase
	with ipfsPubSub().client() as client:
		for item in client.id().items():
			print(item)
	# Instancia de cliente
	with ipfshttpclient.connect("/ip4/127.0.0.1/tcp/5001/http") as client:
		for item in client.id().items():
			print(item)

	# Instancia de PubSub
	client = ipfsPubSub("/ip4/127.0.0.1/tcp/5001")
	# prueba
	client.testConn()
	with client.sub("testing", True) as sub:
		client.pub("testing","hola")
		client.pub("testing","adios")
		for msg in sub:
			for val in msg.values():
				if not isinstance(val, list):
					print(b64decode(val))
			break
		for msg in sub:
			for val in msg.values():
				if not isinstance(val, list):
					print(b64decode(val))
			break
		client.pub("testing","perro")
		client.pub("testing","loco")
	with client.sub("testing", True) as sub:
		for msg in sub:
			for val in msg.values():
				if not isinstance(val, list):
					print(b64decode(val))
	# Prueba de método de prueba
if __name__ == '__main__':
	main()
