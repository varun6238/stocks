from flask import Flask

app = Flask(__name__)

@app.route('/')
def admin():
    return "CM{D4MN_Y0U_DN$}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
