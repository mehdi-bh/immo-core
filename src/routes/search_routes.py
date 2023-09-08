from flask import Blueprint, jsonify, request
from src.models.search import Search

search_routes = Blueprint('search_routes', __name__)

search_model = Search("Searches")


@search_routes.route('/searches', methods=['GET'])
def get_all_searches():
    searches = search_model.get_all_searches()
    if searches:
        return jsonify({'message': 'Searches found', 'searches': searches}), 200
    return jsonify({'message': 'No searches found'}), 404


@search_routes.route('/searches', methods=['POST'])
def create_search():
    data = request.get_json()
    new_search = search_model.create_search(data['searchId'], data['userId'], data['priceMin'], data['priceMax'], data['sizeMin'], data['sizeMax'], data['propertyType'], data['minRooms'], data['minBedrooms'], data['isActive'])
    if new_search:
        return jsonify({"message": "Search created", "search": new_search}), 201
    return jsonify({"message": "Could not create search"}), 400
