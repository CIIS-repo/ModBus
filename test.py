import scapy.all as scapy
import scapy.contrib.modbus as mb

for pkt in scapy.PcapReader("write.pcapng"):
    if mb.ModbusADUResponse in pkt:
        pkt.show()
    if mb.ModbusPDU06WriteSingleRegisterResponse in pkt:
        pkt.show()