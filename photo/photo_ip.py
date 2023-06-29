from flask import Blueprint, request
from database.postservice import get_all_posts_db, delete_exact_post_db, get_all_photo_db


photo_bp = Blueprint('photo', __name__, url_prefix='/photo')


# Получить все фото всех пользователей

@photo_bp.route('/', methods=['GET'])
def get_all_photo():
    all_photos = get_all_photo_db()

    if all_photos:
        return {'status': 1, 'message': all_photos}
    return {'status': 0, 'message': 'Not found'}


# Публикация фотографии

@photo_bp.route('/', methods=['POST'])
def save_user_photo():

    # Получить фото из фронта части
    file = request.files.get('image', '')
    file.save("user_images/" + file.filename)

    print(file)
    return 'Hello'


# Получить все фото определенного пользователя

@photo_bp.route('/<int:user_id>', methods=['GET'])
def get_exact_user_photo(user_id: int):
    pass


# Получить определенное фото

@photo_bp.route('/<int:photo_id>', methods=['GET'])
def get_exact_photo(photo_id: int):
    pass


# Изменить определенное фото пользователя

@photo_bp.route('/<int:user_id>/<int:photo_id>', methods=['POST'])
def change_user_photo(user_id: int, photo_id: int):
    pass


# Удаления определенное фото пользователя

@photo_bp.route('/<int:user_id>/<int:photo_id>', methods=['POST'])
def delete_user_photo(user_id: int, photo_id: int):
    pass



