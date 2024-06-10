import time
import serial 
import mysql.connector;
from datetime import datetime
import board
import adafruit_dht

Maria = mysql.connector.connect(host="localhost", user="juno", passwd="wnsgh0924", database="temp");
Cursor = Maria.cursor();

def main():
	port = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=None)
	while True:
		line = port.readline()
		arr = line.split() 
		if len(arr) < 6: 
			continue 
		
		#print(line)
		
		dataType = (arr[0])
		data1 = float(arr[1]) 	
		data2 = float(arr[4])		
		
		print("Temperature: %.1f C" %data1)
		
		print("Humiditiy: %.1f %%" %data2)
			
		time.sleep(0.01)
		
		d = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
		Query = "insert into DHT22 values(%s,%s,%s)";
		Values= [(d,data1,data2)];
		Cursor.executemany(Query, Values)
		Maria.commit()
	
if __name__ == "__main__":
	main()
