import pymysql as pymysql

class MlbStatsDataAccessor:
    def get_roster(self):
        
        connection_info, cursor = self.get_connection_info()
        # execute SQL query using execute() method.
        cursor.execute("SELECT VERSION()")

        # Fetch a single row using fetchone() method.
        data = cursor.fetchone()

        cursor.close()
        connection_info.close()
        return data

 
    def get_connection_info(self):
        connection = pymysql.connect("hackday.cb8dv80mifqg.us-east-1.rds.amazonaws.com","mookie","baseball","lineup")
        cursor = connection.cursor()
        return connection, cursor

