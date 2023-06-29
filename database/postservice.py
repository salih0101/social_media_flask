from models import HashTag, Post, PostPhoto, PostComment, db


# Получение всех постов
def get_all_posts_db():
    posts = Post.query.all()
    return posts

# Получение всех фотографий
def get_all_photo_db():
    photos = PostPhoto.query.all()
    return photos

# Получение конкретного поста по идентификатору
def get_exact_post_db(post_id):
    post = Post.query.filter_by(post_id=post_id).first()
    return post

# Удаление конкретного поста
def delete_exact_post_db(post_id):
    post = Post.query.filter_by(post_id=post_id).first()
    if post is not None:
        db.session.delete(post)
        db.session.commit()

# Изменение текста поста
def change_post_text_db(post_id, new_text):
    post = Post.query.filter_by(post_id=post_id).first()
    if post is not None:
        post.post_text = new_text
        db.session.commit()

# Добавление комментария к посту
def add_comment_post_db(post_id, comment_user_id, comment_text):
    post = Post.query.filter_by(post_id=post_id).first()
    if post is not None:
        new_comment = PostComment(post_id=post_id, user_id=comment_user_id, comment_text=comment_text)
        db.session.add(new_comment)
        db.session.commit()

def get_all_hashtag_db(size):
    get_hashtag = HashTag.query.all()

    return get_hashtag


def get_exact_hashtag_db(hashtag_name):
    get_exact_hash_db = HashTag.filter_by(hashtag_name=hashtag_name).first()

    return get_exact_hash_db

