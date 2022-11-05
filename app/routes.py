from app import app
from flask import render_template
from datetime import date
from app.getData import getAverageRainOnDate, getAverageRain, tenYearHistory

@app.route('/')
@app.route('/index')
def index():
    findDate = date.today()
    #String of date to display on slide 3
    showDate = findDate.strftime('%d %B')
    #Calculate rain history for slide 3
    averageRainToday = getAverageRainOnDate('app\static\data\weatherData.json',findDate)
    averageRain = getAverageRain('app\static\data\weatherData.json')
    rainHistory = tenYearHistory('app\static\data\weatherData.json',findDate)
    return render_template('index.html',showDate = showDate,averageRainToday = averageRainToday,averageRain=averageRain,rainHistory=rainHistory)