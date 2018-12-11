from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from SRRMSv2.api import statusBP, bookBP, userBP, cancelBP
from SRRMSv2.config import DevelopmentConfig, config_by_name
from SRRMSv2 import create_db_engine, create_db_sessionFactory
from SRRMSv2.models import createTables


config_name = 'dev'


engine = create_db_engine(DevelopmentConfig)
createTables(engine)
SessionFactory = create_db_sessionFactory(engine)
SQLSession = create_db_sessionFactory(engine)


app = Flask(__name__)
app.config.from_object(config_by_name[config_name])


app.register_blueprint(statusBP, url_prefix='/status')
app.register_blueprint(bookBP, url_prefix='/book')
app.register_blueprint(userBP, url_prefix='/user')
app.register_blueprint(cancelBP, url_prefix='/cancel')

if __name__ == "__main__":
    app.run(debug=True)
