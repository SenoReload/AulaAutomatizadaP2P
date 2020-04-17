#!/usr/bin/env python3
import ipfsClient
from RFID import  ReadRFID, WriteRFID
from time import sleep
from lastSpaces import deleteSpaces

piClass = Agent()
while True:
    id, name = ReadRFID()
	piClass.pub("RFIDID", deleteSpaces(str(id)))
	piClass.pub("RFIDName", deleteSpaces(name))
