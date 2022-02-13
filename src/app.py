from flask import Flask, render_template, request
from handler import Handler
from datetime import date
import pygal
from pygal.style import Style
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
    custom_style = Style(
        font_family='googlefont:Roboto',
        legend_font_size=20,
        title_font_size=20,
        value_font_size=20,
        value_label_font_size=20,
        plot_background = 'transparent',
        background = 'transparent',
        foreground_strong = 'white',
        foreground_subtle = 'white',
        foreground='white',
        opacity_hover='0.2'
    )

    circuit = request.form.get("circuit")
    season = request.form.get("season")
    
    # * Accidents Graph
    accidents = handler.showAccidents(circuit, season)
    pieChart = pygal.Pie(style=custom_style)
    pieChart.title = 'Types of accidents'
    accidentCounter = []
    smallerCounter = Counter()
    for accident in accidents:
        # * Filtering through array
        accident.pop(0) 
        accidentCounter.append(*accident)
        smallerCounter = Counter(accidentCounter)
    for onlyProblems in smallerCounter.most_common():
        pieChart.add(onlyProblems[0], onlyProblems[1])
    pieChart.render()
    # * Rendering graph for web
    accidents = pieChart.render_data_uri()

    # * Drivers Graph
    drivers = handler.showDrivers(circuit, season)
    pieChart2 = pygal.Pie(style=custom_style)
    pieChart2.title = 'Most drivers in accidents'
    count = Counter()
    driverId = []
    for driver in drivers:
        # * Filtering through array
        driver = driver.split(",")
        driverId.append(driver[1])
    count = Counter(driverId)
    for common in count.most_common():
        pieChart2.add(common[0], common[1]) 
    pieChart2.render()
    # * Rendering graph for web
    drivers = pieChart2.render_data_uri()

    # * Constructors Graph
    constructors = handler.showConstructors(circuit, season)
    pieChart3 = pygal.Pie(style=custom_style)
    pieChart3.title = 'Most constructors in accidents'
    count = Counter()
    constructorId = []
    for constructor in constructors:
        # * Filtering through array
        constructor = constructor.split(",")
        constructorId.append(constructor[1])
    count = Counter(constructorId)
    for common in count.most_common():
        pieChart3.add(common[0], common[1]) 
    pieChart3.render()
    # * Rendering graph for web
    constructors = pieChart3.render_data_uri()

    return render_template("graphs.html", typeOfAccidents=accidents, driversInAccidents=drivers, constructorsOfAccidents=constructors)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=3000)