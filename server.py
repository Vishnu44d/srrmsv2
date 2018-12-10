from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from SRRMSv2.models import db
from SRRMSv2.api import statusBP, bookBP, userBP
from SRRMSv2.config import *
from SRRMSv2 import create_db_engine, create_db_sessionFactory

config_name = 'dev'


engine = create_db_engine(DevelopmentConfig)
SessionFactory = create_db_sessionFactory(engine)
SQLSession = create_db_sessionFactory(engine)




app = Flask(__name__)
Migrate(app, db)
app.config.from_object(config_by_name[config_name])
with app.app_context():
    db.init_app(app)

app.register_blueprint(statusBP, url_prefix='/status')
app.register_blueprint(bookBP, url_prefix='/book')
app.register_blueprint(userBP, url_prefix='/user')

if __name__ == "__main__":
    app.run(debug=True)
