from flask import Flask
from weather import weather_by_city

app=Flask(__name__)

@app.route("/")
def hello():
    weather = weather_by_city("Moscow,Russia")
    if weather:
        return f"Сейчас {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"
    else:
        return "Прогноз сейчас недоступен"
        

if __name__=="__main__":
    app.run(debug=True)    