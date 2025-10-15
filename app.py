from flask import Flask, render_template

# Создаем экземпляр приложения
app = Flask(__name__)

# Создаем маршрут для главной страницы
@app.route('/')
def index():
    # Передаем переменную в шаблон
    title = "PowerTest"
    return render_template('index.html', title=title)

# Запускаем сервер в режиме отладки
if __name__ == '__main__':
    app.run(debug=True)