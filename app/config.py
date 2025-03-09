import os

class Config:
    SECRET_KEY = 'your-secret-key-for-hedera'
    HEDERA_NETWORK = 'testnet'
    CONTRACT_ID = '0.0.123456'  # Replace with deployed contract ID
    HASHCONNECT_DATA = {
        "topic": "your-topic-id",
        "encryptionKey": "your-encryption-key"
    }
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), '../instance/app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False