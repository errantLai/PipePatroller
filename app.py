from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
	return "Hello, World!"

@app.route('/input', methods=['GET'])
def input():

	def addToSensorData(a,b,c,d,e,f,g):

		return "INSERT INTO sensorData (deviceID, soilHumidity, soilTemperature, pipeSurfaceTemperature, gasPressure, ultrasoundDistance, batteryCharge) VALUES (" + a  + "," +  b + "," + c  + "," + d + "," + e + "," + f + "," + g +")"

	deviceID = request.args.get('deviceid')
	soilHumidity = request.args.get('soilhumidity')
	soilTemperature = request.args.get('soiltemperature')
	pipeSurfaceTemperature = request.args.get('pipetemperature')
	gasPressure = request.args.get('gaspressure')
	ultrasoundDistance = request.args.get('ultrasounddistance')
	batteryCharge = request.args.get('batterycharge')

	return  addToSensorData(deviceID, soilHumidity, soilTemperature, pipeSurfaceTemperature, gasPressure, ultrasoundDistance, batteryCharge)

#http://127.0.0.1:5000/input?deviceid=8&soilhumidity=483&soiltemperature=17&pipetemperature=11&gaspressure=83&ultrasounddistance=18&batterycharge=9