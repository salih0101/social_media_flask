from flask import Blueprint

post_bp = Blueprint('user_post', __name__, url_prefix='/post')


# Получить все фото всех пользователей

@post_bp.route('/', methods=['GET'])
def get_all_photo():
    pass


# Получить все посты

@post_bp.route('/', methods=['GET'])
def get_all_users_post():
    pass


# Получить определенное пост

@post_bp.route('/<int:post_id>', methods=['GET'])
def get_exact_post(post_id: int):
    pass


# Изменить определенное пост пользователя

@post_bp.route('/<int:post_id>/<int:user_id>', methods=['PUT'])
def change_user_post(post_id: int):
    pass


# Удаления определенное фото пользователя

@post_bp.route('/<int:user_id>/<int:post_id>', methods=['POST'])
def delete_user_post(user_id: int, post_id: int):
    pass

# Опубликовать пост

@post_bp.route('/upload_post', methods=['DELETE'])
def create_post(post_text: str, post_photo: str, hashtags: list, user_id: int):
    pass