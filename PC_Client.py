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
		for id in A:
			for val in id.values():
				if not isinstance(val, list):
					idToDB = b64decode(val)
			break
		for name in B:
			for val in name.values():
				if not isinstance(val, list):
					nameToDB = b64decode(val)
			break
	if id != None and name != None:
        atte = dt.timestamp(dt.now())
        db.insert({'ID': str(idToDB), 'Nombre': str(nameToDB), 'Fecha': str(atte)})
        db.search(User.Nombre == str(nameToDB))
