from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# PostgreSQL bağlantı dizesi
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:XStvtrZHbETTLQQWRnGuSbqvMmsMCMft@postgres.railway.internal:5432/railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Örnek bir model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route('/')
def home():
    return "PostgreSQL bağlantısı başarılı!"

if __name__ == "__main__":
    app.run(debug=True)
