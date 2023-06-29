from flask_restx import Resource, Api, fields
from flask import Blueprint, request
from database.userservice import register_user_db, get_exact_user_db, get_all_users_db, delete_user_db

swagger_bp = Blueprint('swagger', __name__, url_prefix='/docs')
api = Api(swagger_bp)


model_user = api.model('Registration', {
    'username': fields.String(description='Enter username'),
    'first_name': fields.String(description='Enter firstname'),
    'last_name': fields.String(description='Enter lastname'),
    'birthday': fields.Date(description='Your birthday')
})

user_id_field = api.model('user_id', {'user_id': fields.Integer})


# Первый тестовый интерфейс для тестов

@api.route('/test-user')
class TestSwagger(Resource):
    # Методы http
    def get(self):
        all_users = get_all_users_db()

        return {'message': all_users}


@api.route('/')
class UserService(Resource):
    # Получить определенного пользователя
    @api.expect(user_id_field)
    def get(self):
        response = request.json
        user_id = response.get('user_id')
        exact_user = get_exact_user_db(user_id)

        return {'message': exact_user}

    @api.expect(user_id_field)
    def delete(self):
        response = request.json
        user_id = response.get('user_id')
        deleted_user = delete_user_db(user_id)

        return {'message': deleted_user}


# Регистрация
    @api.expect(model_user)
    def post(self):
        response = request.json
        new_user = register_user_db(**response)
        return {'status': 'Registered'}

