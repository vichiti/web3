from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    account_id = db.Column(db.String(50), primary_key=True)  # Hedera account ID
    email = db.Column(db.String(120), nullable=True)         # Optional off-chain data
    created_at = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return f'<User {self.account_id}>'