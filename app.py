from flask import Flask, render_template, url_for, request
import serial, string, time
app = Flask(__name__)
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
import datetime
@app.route('/')

def home():
	now=datetime.datetime.now()
	timeString = now.strftime("%Y-%m-%d %H:%M")
	temp = str(ser.readline().decode('utf-8').rstrip())
	humi = str(ser.readline().decode('utf-8').rstrip())
	light = str(ser.readline().decode('utf-8').rstrip())
	noise = str(ser.readline().decode('utf-8').rstrip())
	templateData = {'time' : timeString, 'temp':temp, 'humi':humi, 'light':light, 'noise':noise}
	return render_template('home.html', **templateData)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
