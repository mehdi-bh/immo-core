import boto3


class User:
    def __init__(self, table_name):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(table_name)

    def get_all_users(self):
        response = self.table.scan()
        return response.get('Items', [])

    def create_user(self, user_id, name, email):
        response = self.table.put_item(
            Item={
                'userId': user_id,
                'name': name,
                'email': email
            }
        )
        return response

    def get_user(self, user_id):
        response = self.table.get_item(
            Key={
                'userId': user_id
            }
        )
        return response.get('Item')

    def update_user(self, user_id, new_email):
        response = self.table.update_item(
            Key={
                'userId': user_id,
            },
            UpdateExpression='SET email = :val1',
            ExpressionAttributeValues={
                ':val1': new_email
            }
        )
        return response

    def delete_user(self, user_id):
        response = self.table.delete_item(
            Key={
                'userId': user_id
            }
        )
        return response
