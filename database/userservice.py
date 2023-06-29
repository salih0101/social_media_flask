from database.models import User, Password, db


# Регистрация пользователя

def register_user_db(**user_data):
    new_user = User(**user_data)

    db.session.add(new_user)
    db.session.commit()


# Проверка пользователя

def check_user_db(email):
    user = User.query.filter_by(email=email).first()
    return user is not None


# Проверка пароля пользователя

def check_user_password_db(email, password):
    user = User.query.filber_by(email=email).first()

    if user is not None:
        user_password = Password.query.filter_by(user_id=user.user_id).first()
        if user_password is not None:
            return user_password.password == password

    return False


def get_all_users_db():
    user = User.query.all()

    return user


def get_exact_user_db(user_id):
    exact_user = User.query.filter_by(user_id=user_id).first()

    return exact_user


def delete_user_db(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if user:
        db.session.delete(user)
        db.session.commit()

        return True

    return False










