from flask import Flask, jsonify, request, render_template, Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ("index.html")

@app.route('/google-charts/pie-chart')
def google_pie_chart():
    data = {'Task' : 'Hours per Day', 'Data programing': 11, 'Math': 2, 'Data Manipulation': 2, 'Data System': 2, 'Encoding': 7}
    return render_template("pie-chart.html", data=data)

if __name__ == "__main__":
    app.run()  