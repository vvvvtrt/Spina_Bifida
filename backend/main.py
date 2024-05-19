from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

@app.route('/html/<path:filename>')
def get_file(filename):
    directory = 'C:/Users/sleim/PycharmProjects/SpinaBifida/frontend/' # Укажите путь к вашему каталогу здесь

    print(filename)

    if os.path.isfile(os.path.join(directory, filename)):
        return send_from_directory(directory, filename)
    else:
        return 'File not found', 404

if __name__ == '__main__':
    app.run(port=8001)
