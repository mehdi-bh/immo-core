import boto3


class Search:
    def __init__(self, table_name):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(table_name)

    def get_all_searches(self):
        response = self.table.scan()
        return response.get('Items', [])

    def create_search(self, search_id, user_id, price_min, price_max, size_min, size_max, property_type, nb_rooms, nb_bedrooms, is_active):
        response = self.table.put_item(
            Item={
                'searchId': search_id,
                'userId': user_id,
                'priceMin': price_min,
                'priceMax': price_max,
                'sizeMin': size_min,
                'sizeMax': size_max,
                'propertyType': property_type,
                'minRooms': nb_rooms,
                'minBedrooms': nb_bedrooms,
                'isActive': is_active
            }
        )
        return response

    def get_search(self, user_id, search_id):
        response = self.table.get_item(
            Key={
                'userId': user_id,
                'searchId': search_id
            }
        )
        return response.get('Item')

    def get_searches_from_user(self, user_id):
        response = self.table.get_item(
            Key={
                'userId': user_id
            }
        )
        return response.get('Item')
