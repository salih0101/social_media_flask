from flask import Flask
from flask import render_template
from flask_restx import Api
from swagger.test_swagger import swagger_bp
from database.models import db
from comment.comment_api import comment_bp
from hashtag.hashtag_api import hashtag_bp
from photo.photo_ip import photo_bp
from posts.posts_api import post_bp
from user.user_api import user_bp

# Объект Swagger
api = Api()
# Объект Фласк
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///media.db'
db.init_app(app)
api.init_app(app)

@app.route('/')
def test_api():

    return render_template('test.html')


# app.register_blueprint(comment_bp)
# app.register_blueprint(hashtag_bp)
# app.register_blueprint(photo_bp)
# app.register_blueprint(user_bp)
# app.register_blueprint(post_bp)

app.register_blueprint(swagger_bp)

app.run(debug=True)
