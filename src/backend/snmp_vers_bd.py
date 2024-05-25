from pysnmp.hlapi import *

from src.backend.connection import get_connection
from src.backend.dictionaries import oids

from datetime import datetime

mydb = get_connection()
cursor = mydb.cursor()
query = "insert into consomation (consomation, date_de_consomation, intervalle, id_onduleur) values (%s, %s, %s, %s)"
delete_query = "delete from consomation where intervalle = %s"


def snmp_get(ip_address):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData('public', mpModel=0),
               UdpTransportTarget((ip_address, 161)),
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


def insert_consumption(ip_address):
    consumption = float(snmp_get(ip_address)) * (5 / 60)
    current_datetime = datetime.now()
    cursor.execute(query, (consumption, current_datetime, "5min", ip_address))
    mydb.commit()


def insert_hour_consumption(ip_address):
    cursor.execute("select consomation from consomation where intervalle = '5min' and id_onduleur = %s", (ip_address,))
    total_consumption = 0
    result = cursor.fetchall()
    for consumption in result:
        total_consumption += consumption[0]
    current_datetime = datetime.now()
    cursor.execute(query, (total_consumption, current_datetime, "1h", ip_address))
    mydb.commit()
    cursor.execute(delete_query, ("5min",))
    mydb.commit()


def insert_day_consumption(ip_address):
    cursor.execute("select consomation from consomation where intervalle = '1h' and id_onduleur = %s", (ip_address, ))
    total_day_consumption = 0
    result = cursor.fetchall()
    for consumption in result:
        total_day_consumption += consumption[0]
    current_datetime = datetime.now()
    cursor.execute(query, (total_day_consumption, current_datetime, "24h", ip_address))
    mydb.commit()
    cursor.execute(delete_query, ("1h",))
    mydb.commit()


def insert_week_consumption(ip_address):
    cursor.execute("SELECT SUM(consomation), DAY(date_de_consomation) AS jour FROM consomation WHERE intervalle = '24h' AND WEEK(date_de_consomation, 1) = WEEK(CURDATE(), 1) and id_onduleur = %s GROUP BY DAY(date_de_consomation) ORDER BY date_de_consomation ASC;", (ip_address, ))
    result = cursor.fetchall()
    current_datetime = datetime.now()
    cursor.execute(query, (result[0][0], current_datetime, "week", ip_address))
    mydb.commit()


def insert_month_consumption(ip_address):
    current_datetime = datetime.now()
    cursor.execute("select SUM(consomation) from consomation where intervalle = 'week' and MONTH(date_de_consomation) = MONTH(CURDATE()) and id_onduleur = %s", (ip_address, ))
    result = cursor.fetchall()
    cursor.execute(query, (result[0][0], current_datetime, "month", ip_address))
    mydb.commit()















