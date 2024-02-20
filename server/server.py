from flask import Flask, jsonify, request, blueprints
from flask_cors import CORS
from modules.tables import db

def create_app():
    # Flaskのインスタンスを作成
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample.db'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/dbname'
    # username、password、localhost、dbnameはそれぞれMySQLのユーザー名、パスワード、ホスト名、データベース名に置き換える

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # modules下のブループリントを呼び出す
    from modules.user_handler import user_handle_app
    from modules.timer_handler import timer_handle_app
    app.register_blueprint(user_handle_app)
    app.register_blueprint(timer_handle_app)

    return app

app = create_app()

# 単にHello, World!を返却する
# 引数:なし　返却値:'message': 'Hello, World
@app.route('/api/home', methods=['GET'])
def return_home():
    return jsonify({'message': 'Hello, World!'})

# サーバーの起動
if __name__ == '__main__':
    app.run(debug=True, port=8080)
