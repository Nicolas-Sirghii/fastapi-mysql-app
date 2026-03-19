import mysql
def getConnection():
    connection = mysql.connector.connect(


        host="db",
        user="root",
        password="example",
        database="messages_db"


        #
        # host="srv1590.hstgr.io",
        # user="u529719289_cloud_master",
        # password="myDBpass1$",
        # database="u529719289_cloud_1"

    )
    return connection
