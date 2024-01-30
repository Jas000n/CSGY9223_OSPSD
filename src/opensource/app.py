from flask import Flask

app = Flask("TestServer")


@app.route("/")
def hello_world():
    print("Test Server received!")
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
