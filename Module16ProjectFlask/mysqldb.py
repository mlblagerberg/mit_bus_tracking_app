import mysql.connector


def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
    host="localhost",
    port=5509,
    user="root",
    password="MyNewPass",
    database="MBTAdb"
    )

    mycursor = mydb.cursor()
    # complete the following line to add all the fields from the table
    sql = ("insert into mbta_buses (id, latitude, longitude, current_stop_sequence, direction_id, speed, revenue,"
           " current_status, updated_at)"
           "values (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
    for mbtaDict in mbtaList:
        # Skip records with null stop sequence
        if mbtaDict['current_stop_sequence'] is None:
            continue  # Skip records where current_stop_sequence is null
        # complete the following line to add all the fields from the table
        val = (mbtaDict['id'], mbtaDict['latitude'], mbtaDict['longitude'], mbtaDict['current_stop_sequence'],
               mbtaDict['direction_id'], mbtaDict['speed'], mbtaDict['revenue'], mbtaDict['current_status'],
               mbtaDict['updated_at'])
        mycursor.execute(sql, val)

    mydb.commit()
