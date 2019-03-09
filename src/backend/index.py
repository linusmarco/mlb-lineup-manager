def getRoster(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'isBase64Encoded': False,
        'body': 'Hello, World'
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
