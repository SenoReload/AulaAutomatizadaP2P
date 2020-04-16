import ipfshttpclient
from base64 import b64encode, b64decode
# Objeto para un cliente que corre continuamente
class ipfsPubsub:
	"""Clase para el cliente de Publisher-Subscriber"""
	def __init__(self):
		self._client = ipfshttpclient.connect("/ip4/127.0.0.1/tcp/5001")
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
def main():
	# Ejemplos
	# Instancia de clase
	with ipfsPubsub().client() as client:
		for item in client.id().items():
			print(item)
	# Instancia de cliente
	with ipfshttpclient.connect("/ip4/127.0.0.1/tcp/5001") as client:
		for item in client.id().items():
			print(item)
	# Instancia de PubSub
	client = ipfsPubsub()
	with client.sub("testing", True) as sub:
		client.pub("testing","hola")
		# Imprime diccionario de subcripciones
		print(client.peers("testing"))
		print(client.ls())
		for msg in sub:
			for val in msg.values():
				if not isinstance(val, list):
					print(b64decode(val))

if __name__ == '__main__':
	main()
