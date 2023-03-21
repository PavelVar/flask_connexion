import connexion
from flask import render_template

app = connexion.App(__name__, specification_dir="../")

app.add_api("swagger.yml")


@app.route("/")
def home() -> str:
    data = {'swagger': 'http://127.0.0.1:5000/api/v1/ui', 'json': 'http://127.0.0.1:5000/api/v1/prods'}
    return render_template("home.html", data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
