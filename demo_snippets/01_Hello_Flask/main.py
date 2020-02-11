from flask import Flask

app = Flask("Hello World")


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run(debug=True, port=5000)

# In der Anaconda Konsole kann nun main.py aufgerufen werden.
# > python main.py
# Im Browser kann dann auf http://localhost:5000/hello
# aufgerufen werden.