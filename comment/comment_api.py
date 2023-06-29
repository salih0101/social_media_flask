from flask import Blueprint
from database.postservice import get_all_posts_db, get_exact_post_db, delete_exact_post_db, add_comment_post_db

comment_bp = Blueprint('comment', __name__, url_prefix='/comment')


# Получить комментарии определенного пользователя

@comment_bp.route('/<int:post_id>', methods=['GET'])
def get_exact_post_comments(post_id: int):
    exact_comment = get_exact_post_db(post_id)

    if exact_comment:
        return {'status': 1, 'message': 'Exact comment'}
    return {'status': 0, 'message': 'Not found'}


# Публикация комментарий

@comment_bp.route('/<int:post_id>/<int:comment_user_id>', methods=['POST'])
def publish_comment(post_id: int, comment_user_id: int, comment_text: str):
    publish_commentt = add_comment_post_db(comment_user_id, post_id, comment_text)

    if publish_commentt:
        return {'status': 1, 'message': 'Publish comment'}
    return {'status': 0, 'message': 'Not found'}



# Изменить комментарий отправленный

@comment_bp.route('/<int:comment_id>/<int:comment_user_id>', methods=['POST'])
def change_comment(comment_user_id: int, comment_id: int):
    pass


# Удаления определенное фото пользователя

@comment_bp.route('/<int:comment_id>/<int:comment_user_id>', methods=['DELETE'])
def delete_comment(user_id: int, photo_id: int, comment_user_id: int):
    pass
