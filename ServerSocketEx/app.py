__author__ = 'lk'

import Malm as malm


host = ''
port = 56789

ms = malm.MalmServer(host, port)

ms.open()
ms.start()
