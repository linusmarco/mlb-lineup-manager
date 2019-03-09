from dataaccessor.mlbstats_dataaccessor import MlbStatsDataAccessor

def getRoster(event, context):
    mlb_data_accessor = MlbStatsDataAccessor()
    data = mlb_data_accessor.get_roster()
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'isBase64Encoded': False,
        'body': data
    }


def get_ranks(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'isBase64Encoded': False,
        'body': 'Hello, World'
    }
