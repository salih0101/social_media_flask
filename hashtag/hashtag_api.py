from flask import Blueprint
from database.postservice import get_exact_hashtag_db, get_all_hashtag_db

hashtag_bp = Blueprint('hashtag', __name__, url_prefix='/hashtag')


# Получить комментарии по количеству

@hashtag_bp.route('/', methods=['POST'])
def get_hashtags(size: int):
    get_hash = get_all_hashtag_db(size)

    if get_hash:
        return {'status': 1, 'message': get_hash}

    return {'status': 0, 'message': 'Not_found'}


# Получить хештег по названию

@hashtag_bp.route('/<string:hashtag_name>/<int:comment_user_id>', methods=['GET'])
def get_exact_hashtag(hashtag_name: str):
    get_exact_hash = get_exact_hashtag_db(hashtag_name)

    if get_exact_hash:
        return {'status': 1, 'message': get_exact_hash}

    return {'status': 0, 'message': 'Not_found'}


