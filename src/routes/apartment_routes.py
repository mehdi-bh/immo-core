from flask import Blueprint, jsonify, request
from src.models.apartment import Apartment

apartment_routes = Blueprint('apartment_routes', __name__)

apartment_model = Apartment("Apartments")


@apartment_routes.route('/apartments', methods=['GET'])
def get_all_apartment():
    apartments = apartment_model.get_all_apartments()
    if apartments:
        return jsonify({'message': 'Apartments found', 'apartments': apartments}), 200
    return jsonify({'message': 'No apartments found'}), 404


@apartment_routes.route('/apartments', methods=['POST'])
def create_apartment():
    data = request.get_json()
    new_apartment = apartment_model.create_apartment(data['apartmentId'], data['address'], data['price'], data['size'], data['company'], data['details_link'], data['google_maps_link'])
    if new_apartment:
        return jsonify({"message": "Apartment created", "apartment": new_apartment}), 201
    return jsonify({"message": "Could not create apartment"}), 400


@apartment_routes.route('/apartments/<string:apartment_id>', methods=['GET'])
def get_apartment(apartment_id):
    apartment_data = apartment_model.get_apartment(apartment_id)
    if apartment_data:
        return jsonify({"message": "Apartment found", "apartment": apartment_data}), 200
    return jsonify({"message": "Apartment not found"}), 404
