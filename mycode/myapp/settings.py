class Config:

    debug = False
    test = False
    online = False

    SECRET_KEY = "nsjkfhsdjkfhsjkh893HUK"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DebugConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:liuda6015?@127.0.0.1:3306/fl50"


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:liuda6015?@127.0.0.1:3306/fl50"


config = {
    "debug": DebugConfig,
    "test": TestConfig
}