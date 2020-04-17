#!/usr/bin/env python3
import ipfsClient
import base64 as b64
from tinydb import TinyDB,Query
from time import sleep
from datetime import datetime as dt

db = TinyDB("lista.json")
query = Query()

apiServer = "/ip4/127.0.0.1/tcp/5001/http"
Client = ipfsClient.ipfsPubSub(apiServer)

while True:
	with Client.sub("RFIDID", True) as A, Client.sub("RFIDName", True) as B:
		for msg in A:
			for val in msg.values():
				if not isinstance(val, list):
					print(b64decode(val))
			break
		for msg in B:
			for val in msg.values():
				if not isinstance(val, list):
					print(b64decode(val))
			break
