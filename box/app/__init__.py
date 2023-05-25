from flask import Flask
app=Flask(__name__)
# DO NOT EDIT ABOVE

@app.route("/")
def hello():
        return "Hello World"

# DO NOT EDIT BELOW
if __name__ == "__main__":
        app.run()