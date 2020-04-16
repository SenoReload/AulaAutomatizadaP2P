import ipfsClient
apiServer = "/ip4/127.0.0.1/tcp/5001"
Client = ipfsClient.ipfsPubSub(apiServer)
Client.testConn()
