from flask import Flask, render_template, request
import urllib.request, json
import config

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        zipcode = request.form['zipcode']
        url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode}&appid={config.api_key['API_KEY']}"
        response = urllib.request.urlopen(url)
        data = response.read()
        adict = json.loads(data)
        city = adict['name']
        temperature = adict['main']['temp']
        temp_in_f = kelvin_in_fahrenheit(temperature)
        temp_in_c = kelvin_in_celcius(temperature)
        humidity = adict['main']['humidity']
        country = adict['sys']['country']
        cloud = adict['weather'][0]['main']
        return render_template('weather_form.html', zip=zipcode, tempf=temp_in_f, tempc=temp_in_c, city=city, humid=humidity, country=country, sky_status=cloud)
    return render_template('weather_form.html')

def kelvin_in_celcius(K):
    C = K - 273.15
    return round(C)

def kelvin_in_fahrenheit(K):
    F = 1.8 * (K - 273) + 32
    return round(F)

if __name__ == '__main__':
    app.run(debug=True, port=1080)
