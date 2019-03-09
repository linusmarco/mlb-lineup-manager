import pymysql as pymysql
import pandas as pd
import os
import json

class MlbStatsDataAccessor:
    def get_roster(self):
        
        connection_info, cursor = self.get_connection_info()
        # execute SQL query using execute() method.
        cursor.execute("SELECT * from Player")

        player_data = self.read_records_from_cursor(cursor)

        cursor.close()
        connection_info.close()

        connection_info, cursor = self.get_connection_info()
        cursor.execute("SELECT * from Game")
        game_data = self.read_records_from_cursor(cursor)
        game_df = pd.DataFrame(data=game_data)

        player_data_Df = pd.DataFrame(data=player_data)
        game_grouped_df = game_df.groupby('PLAYER_ID')['AT_BAT_COUNT','DOUBLE_COUNT','HIT_COUNT','HOMERUN_COUNT','PLATE_APPEARANCE_COUNT','WALK_COUNT','TRIPLE_COUNT'].agg('sum')

        merge_df = pd.merge(player_data_Df,game_grouped_df,how="inner",left_on="PLAYER_ID",right_on="PLAYER_ID")
        connection_info.close()
        return merge_df.to_json(orient='records')
    
    def get_ranks(self):
        _file_path = os.path.dirname(os.path.realpath(__file__)) + '/ranks.json'
        try:
             with open(_file_path, 'r') as f:
                 data = json.load(f)
                 return data
        except Exception as error:
            raise error


 
    def get_connection_info(self):
        connection = pymysql.connect("hackday.cb8dv80mifqg.us-east-1.rds.amazonaws.com","mookie","baseball","lineup")
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
