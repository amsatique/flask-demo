# from winreg import REG_NOTIFY_CHANGE_SECURITY
from flask import Flask
from api.elastic_test import connect_elasticsearch

es = connect_elasticsearch()

app = Flask(__name__)


# from api.insert_data import *
from api.retrieve_data import *


if __name__ == '__main__':
    app.run(host='0.0.0.0')