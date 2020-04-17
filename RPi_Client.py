#!/usr/bin/env python3
import ipfsClient
from  agent import Agent
from RFID import  ReadRFID, WriteRFID
from time import sleep

piClass = Agent()
while True:
    id, name = ReadRFID()
