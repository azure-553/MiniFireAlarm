from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def loginscedul():
    return render_template("home.html")

if __name__=="__main__":
    app.run(host="0.0.0.0")

