import serial
import time

serial = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
#f = open("data_humidity_temp.json", "w")
f = open("humidity_csv.csv","w")

while True:
  data = str (serial.readline())
  #data = data.encode("utf-8")
  f.write("{\"Date\":\"")
  f.write(time.strftime("%d/%m/%Y"))
  f.write("\",")
  f.write("\"Time\":\"")
  f.write(time.strftime("%T"))
  f.write("\",")
  data = data.replace("b","")
  data = data.replace("  ",",")
  data = data.replace("\'","")
  data = data.replace("iu","\"")
  f.write(data)
  f.write("}\n")
  f.flush()
f.close()
