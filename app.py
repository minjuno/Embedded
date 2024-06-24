from flask import Flask, render_template, jsonify, request, Response
from datetime import datetime
import time
import cv2
import os
from database import connect_to_database, save_data_to_database, fetch_latest_data, fetch_all_data
from arduino import read_arduino_data, toggle_led, toggle_gas, toggle_window
from weather import get_weather
from camera import gen_frames

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    data_type, temperature, humidity = read_arduino_data()
    print(f"Temperature: {temperature:.1f} C")
    print(f"Humidity: {humidity:.1f} %")

    timestamp = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    save_data_to_database((timestamp, temperature, humidity))

    weather = None
    error_message = None
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
        if weather_data['cod'] == 200:
            description = weather_data['weather'][0]['description'].lower()
            weather = {
                'city': weather_data['name'],
                'temperature': weather_data['main']['temp'],
                'description': description,
                'humidity': weather_data['main']['humidity'],
                'wind_speed': weather_data['wind']['speed'],
                'icon': weather_data['weather'][0]['icon']
            }
        else:
            error_message = weather_data.get('message', 'City not found')
    videos = os.listdir(VIDEO_DIR)
   
    return render_template('index.html', weather=weather, error_message=error_message, videos=videos)

@app.route("/data", methods=['GET'])
def get_data():
    result = fetch_latest_data()
    return jsonify(result)

@app.route("/cdata", methods=['GET'])
def get_cdata():
    result = fetch_all_data()
    return jsonify(result)

@app.route("/toggle_led", methods=['POST'])
def toggle_led_route():
    toggle_led()
    return jsonify({'status': 'success'})

@app.route("/toggle_gas", methods=['POST'])
def toggle_gas_route():
    toggle_gas()
    return jsonify({'status': 'success'})
   
@app.route("/toggle_window", methods=['POST'])
def toggle_window_route():
	toggle_window()
	return jsonify({'status': 'success'})

@app.route("/video_feed")
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/video")
def video():
    return render_template('cctv.html')

if __name__ == "__main__":  
    app.run(debug=True)