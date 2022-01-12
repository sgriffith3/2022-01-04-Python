from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
@app.route("/pets")
def show_pets():
    store_data = {"company_name": "Frufur Pet Emporium", "cats": ["fluffy", "snowball"], "dogs": ["spot", "fido"],
                  'hamsters': "pluto"}
    return render_template("pets.html", fluffy_data=store_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)