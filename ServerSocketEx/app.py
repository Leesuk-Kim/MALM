__author__ = 'lk'

import Malm as malm


host = ''
port = 56789

bms = malm.BaseMalmServer(host, port)

malm.decoder_powerstrip('abcd')

# bms.open()
# bms.start()
