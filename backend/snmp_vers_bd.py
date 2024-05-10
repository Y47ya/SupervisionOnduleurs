from pysnmp.hlapi import *
from dictionaries import oids
from connection import get_connection
import time
from datetime import datetime

mydb = get_connection()
cursor = mydb.cursor()
query = "insert into consomation (consomation, date_de_consomation, intervalle) values (%s, %s, %s)"
delete_query = "delete from consomation where intervalle = %s"


def snmp_get():
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData('public', mpModel=0),
               UdpTransportTarget(('192.168.12.113', 161)),
               ContextData(),
               ObjectType(ObjectIdentity(oids.get("outputWatt"))))
    )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            return varBind[1].prettyPrint()


def insert_consumption():
    while True:
        consumption = float(snmp_get()) * (5 / 60)
        current_datetime = datetime.now()
        cursor.execute(query, (consumption, current_datetime, "5min"))
        mydb.commit()
        time.sleep(300)
        print("added succefully")


def insert_hour_consumption():
    while True:
        cursor.execute("select consomation from consomation where intervalle = '5min' ")
        total_consumption = 0
        result = cursor.fetchall()
        for consumption in result:
            total_consumption += consumption[0]

        current_datetime = datetime.now()
        cursor.execute(query, (total_consumption, current_datetime, "1h"))
        mydb.commit()
        cursor.execute(delete_query, ("5min",))
        mydb.commit()
        time.sleep(3600)














