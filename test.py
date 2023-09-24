from scapy.all import *
import time

# Modbus ADU
class ModbusTCP(Packet):
    name = "Modbus/TCP"
    fields_desc = [
        ShortField("Transaction_Identifier", 1),
        ShortField("Protocol_Identifier", 0),
        ShortField("Length", 6),
        XByteField("Unit_Identifier", 1),
    ]

# Modbus PDU
class Modbus(Packet):
    name = "Modbus"
    fields_desc = [
        XByteField("Function_Code", 3),  
        ShortField("Reference_Number", 0),
        ShortField("Word_Count", 63),
    ]


s = socket.socket()
s.connect(("192.168.50.197", 502))
ss = StreamSocket(s, Raw)

try:
    response = ss.sr1(Raw(ModbusTCP()/Modbus()))
    if response:
        response_hexdump = hexdump(response, dump=True)
        print(response_hexdump)

        time.sleep(1)
except KeyboardInterrupt:
    pass