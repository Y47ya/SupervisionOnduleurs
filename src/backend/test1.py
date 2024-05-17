from pysnmp.hlapi import *

host_ip_address = '192.168.12.113'

oid = "1.3.6.1.2.1.33.1.2.2.0"

authentication = UsmUserData(
    userName= 'readuser',
    authKey= 'admin',
    authProtocol=usmHMACSHAAuthProtocol,
    privKey='admin',
    privProtocol=usmAesCfb256Protocol
)


iterator = getCmd(SnmpEngine(),
                  authentication,
                  UdpTransportTarget((host_ip_address, 161)),
                  ContextData(),
                  ObjectType(ObjectIdentity(oid)))

errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

if errorIndication:  # SNMP engine errors
    print(errorIndication)
else:
    if errorStatus:  # SNMP agent errors
        print('%s at %s' % (errorStatus.prettyPrint(), varBinds[int(errorIndex)-1] if errorIndex else '?'))
    else:
        for varBind in varBinds:  # SNMP response contents
            print(' = '.join([x.prettyPrint() for x in varBind]))
