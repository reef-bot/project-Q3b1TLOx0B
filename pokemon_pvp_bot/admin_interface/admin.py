from flask import Flask

app = Flask(__name__)

@app.route('/admin')
def admin_panel():
    return 'Welcome to the admin panel'

if __name__ == '__main__':
    app.run()