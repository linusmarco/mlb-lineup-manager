import pymysql as pymysql


class MlbStatsDataAccessor:
    def get_roster(self):
        
        connection_info, cursor = self.get_connection_info()
        # execute SQL query using execute() method.
        cursor.execute("SELECT * from Player")

        # Fetch a single row using fetchone() method.
        data = self.read_records_from_cursor(cursor)

        cursor.close()
        connection_info.close()
        return data

    def get_connection_info(self):
        connection = pymysql.connect(
            "hackday.cb8dv80mifqg.us-east-1.rds.amazonaws.com", "mookie",
            "baseball", "lineup")
        cursor = connection.cursor()
        return connection, cursor
    

    def read_records_from_cursor(self, cursor):
        rows = list(cursor.fetchall())
        records = []
        columns = [column[0] for column in cursor.description]
        for row in rows:
            if row:
                records.append(dict(zip(columns, row)))
        return records
