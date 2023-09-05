from flask import Blueprint, jsonify, request
from src.models.user import User

user_routes = Blueprint('user_routes', __name__)

user_model = User("Users")


@user_routes.route('/users', methods=['GET'])
def get_all_users():
    users = user_model.get_all_users()
    if users:
        return jsonify({'message': 'Users found', 'users': users}), 200
    return jsonify({'message': 'No users found'}), 404


@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = user_model.create_user(data['userId'], data['name'], data['email'])
    if new_user:
        return jsonify({"message": "User created", "user": new_user}), 201
    return jsonify({"message": "Could not create user"}), 400


@user_routes.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user_data = user_model.get_user(user_id)
    if user_data:
        return jsonify({"message": "User found", "user": user_data}), 200
    return jsonify({"message": "User not found"}), 404


@user_routes.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    updated_user = user_model.update_user(user_id, data)
    if updated_user:
        return jsonify({"message": "User updated", "user": updated_user}), 200
    return jsonify({"message": "Could not update user"}), 400


@user_routes.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    is_deleted = user_model.delete_user(user_id)
    if is_deleted:
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"message": "Could not delete user"}), 400
