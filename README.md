# AulaAutomatizadaP2P
Se busca automatizar un aula de clases con actuadores y sensores, logrando la comunicación entre estos con un protocolo peer-to-peer. En esta ocasión se usará el protocolo de IPFS. Se monta un nodo de IPFS subcrito a ciertos temas. Habrá una comunicación entre nodos, de esta manerá lograrán realizar ciertas acciones con ciertos mensajes.

## Instalación

Usar el gesto de paquete de Python [pip](https://pip.pypa.io/en/stable/) para instalar el módulo:

```bash
$ pip install ipfshttpclient
```
Una vez descargada la distribución de IPFS [aquí](https://ipfs.io/ipns/dist.ipfs.io/#go-ipfs) procedemos a instalarla:

```bash
$ tar xvfz go-ipfs.tar.gz
$ cd go-ipfs
$ ./install.sh
```
Probamos la instalación:
```bash
$ ipfs help
USAGE:

    ipfs - Global p2p merkle-dag filesystem.
...
```
## Uso
Procedemos a montar nuestro nodo de IPFS habilitando la modalidad de Publisher-Subscriber:
```bash
$ ipfs daemon --enable-pubsub-experiment
```
Obtendremos una serie de direcciones en la cual la dirección del API server nos será útil para definir la conexión de nuestro objeto de nodo IPFS.
```python
>>> from ipfsClient import ipfsPubSub
>>> apiServer = "/ip4/127.0.0.1/tcp/5001"
>>> Client = ipfsPubSub(apiServer)
```
Ahora se puede trabajar con el objeto de PubSub.
```python
>>> import ipfsClient
>>> apiServer = "/ip4/127.0.0.1/tcp/5001"
>>> Client = ipfsClient.ipfsPubSub(apiServer)
>>> Client.testConn()
```
Obtendremos lo siguiente:
```
('ID', 'QmSxHYnrpbD5TTcV1c4RdnLZHRt1fNPxf5n4uVBFHRQd8u')
('PublicKey',
'CAASpgIwggEiMA0GCSqGSIb3DQEBAQUAA4
IBDwAwggEKAoIBAQDZaDLqmWr/pkwDiD02a
9xwzWSVHGHkaI/ljdTcocWRfteTGvB1KwXk
ca0+HRiixaJu/hUy1aYnx+gb7kD8whGaT8F
8zijQGNa6UV4MAlb2evMA0ekoMRW4zwfSjA
a4PkLj77SUKHHh5yQwkobfLTSFvnGbcOjk0
6UumpwmOeLjBw1ubMl0FOErOVSu42T+1h8x
8UzNjzsIfrYsPzVx/Tcxs+Qwws5Z1Pu0Ng/
DxTgp8Z6b9fjtvC1MuvKHVOAquG8WnHiIzp
md+HGQ2c52IdaFjusQyEe1yHe3JLyAKhOY5
1Ejrtj1gjNMIrbNH9F5bek90IaDlGKipB9V
XrerTAgMBAAE=')
('Addresses', [
'/ip4/127.0.0.1/tcp/4001/ipfs/QmSxHYnrpbD5TTcV1c4RdnLZHRt1fNPxf5n4uVBFHRQd8u',
'/ip4/192.168.0.5/tcp/4001/ipfs/QmSxHYnrpbD5TTcV1c4RdnLZHRt1fNPxf5n4uVBFHRQd8u',
'/ip4/172.18.0.1/tcp/4001/ipfs/QmSxHYnrpbD5TTcV1c4RdnLZHRt1fNPxf5n4uVBFHRQd8u',
'/ip4/172.19.0.1/tcp/4001/ipfs/QmSxHYnrpbD5TTcV1c4RdnLZHRt1fNPxf5n4uVBFHRQd8u',
'/ip4/172.17.0.1/tcp/4001/ipfs/QmSxHYnrpbD5TTcV1c4RdnLZHRt1fNPxf5n4uVBFHRQd8u',
'/ip6/::1/tcp/4001/ipfs/QmSxHYnrpbD5TTcV1c4RdnLZHRt1fNPxf5n4uVBFHRQd8u',
'/ip4/200.92.172.161/tcp/4001/ipfs/QmSxHYnrpbD5TTcV1c4RdnLZHRt1fNPxf5n4uVBFHRQd8u'])
('AgentVersion', 'go-ipfs/0.4.23/')
('ProtocolVersion', 'ipfs/0.1.0')

```
## License
[MIT](https://choosealicense.com/licenses/mit/)
