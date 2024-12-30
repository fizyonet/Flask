from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# PostgreSQL bağlantı dizesi
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:XStvtrZHbETTLQQWRnGuSbqvMmsMCMft@postgres.railway.internal:5432/railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/test-db')
def test_db():
    try:
        # Veritabanına basit bir sorgu gönderiyoruz
        db.session.execute('SELECT 1')
        return "PostgreSQL bağlantısı başarılı!"
    except Exception as e:
        return f"Bağlantı başarısız: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
