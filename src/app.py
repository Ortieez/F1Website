from flask import Flask, render_template, request
from handler import Handler
from datetime import date
import pygal
from collections import Counter

app = Flask(__name__)
todays_date = date.today()
handler = Handler()
seasons = []

for year in range(1950,todays_date.year+1):
    seasons.append(year)

@app.route('/')
def select():
    return render_template('selection.html', circuits=handler.showCircuits(), seasons=seasons)

@app.route('/accidents', methods=['POST'])
def accidents():
    circuit = request.form.get("circuit")
    season = request.form.get("season")
    accidents = handler.showAccidents(circuit, season)
    pieChart = pygal.Pie()
    pieChart.title = 'Types of accidents on {}'.format(circuit)
    accidentCounter = []
    smallerCounter = Counter()
    for accident in accidents:
        accident.pop(0) 
        accidentCounter.append(*accident)
        smallerCounter = Counter(accidentCounter)
    for onlyProblems in smallerCounter.most_common():
        pieChart.add(onlyProblems[0], onlyProblems[1])
    pieChart.render()
    graph_data = pieChart.render_data_uri()
    return render_template("graphs.html", graph_data = graph_data)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=3000)