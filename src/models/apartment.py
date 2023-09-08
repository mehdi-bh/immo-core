import boto3


class Apartment:
    def __init__(self, table_name):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(table_name)

    def get_all_apartments(self):
        response = self.table.scan()
        return response.get('Items', [])

    def create_apartment(self, apartment_id, address, price, size, company, details_link, google_maps_link):
        response = self.table.put_item(
            Item={
                'apartmentId': apartment_id,
                'address': address,
                'price': price,
                'size': size,
                'company': company,
                'detailsLink': details_link,
                'googleMapsLink': google_maps_link
            }
        )
        return response

    def get_apartment(self, apartment_id):
        response = self.table.get_item(
            Key={
                'apartmentId': apartment_id
            }
        )
        return response.get('Item')
