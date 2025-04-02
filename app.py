from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Данные для сайта
users = [
    {"id": 1, "name": "Alice", "role": "admin", "email": "alice@example.com", "last_active": "2023-05-15"},
    {"id": 2, "name": "Bob", "role": "user", "email": "bob@example.com", "last_active": "2023-05-14"},
    {"id": 3, "name": "Charlie", "role": "user", "email": "charlie@example.com", "last_active": "2023-05-10"},
    {"id": 4, "name": "Diana", "role": "moderator", "email": "diana@example.com", "last_active": "2023-05-12"},
]

products = [
    {"id": 1, "name": "MacBook Pro", "price": 1999.99, "in_stock": True, "category": "laptops", "rating": 4.8},
    {"id": 2, "name": "Wireless Mouse", "price": 49.99, "in_stock": False, "category": "accessories", "rating": 4.2},
    {"id": 3, "name": "Mechanical Keyboard", "price": 129.99, "in_stock": True, "category": "accessories",
     "rating": 4.6},
    {"id": 4, "name": "4K Monitor", "price": 599.99, "in_stock": True, "category": "monitors", "rating": 4.7},
]


@app.route('/')
def index():
    featured = [p for p in products if p['rating'] > 4.5][:3]
    return render_template('index.html',
                           title="Главная страница",
                           products=products,
                           featured=featured,
                           current_year=datetime.now().year)


@app.route('/about')
def about():
    return render_template('about.html',
                           title="О нас",
                           team_size=len(users),
                           current_year=datetime.now().year)


@app.route('/users')
def user_list():
    return render_template('users.html',
                           title="Пользователи",
                           users=sorted(users, key=lambda x: x['name']),
                           current_year=datetime.now().year)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        flash('Ваше сообщение отправлено! Мы свяжемся с вами в ближайшее время.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html',
                           title="Контакты",
                           current_year=datetime.now().year)


if __name__ == '__main__':
    app.run(debug=True)
