import adxl345

from adxl345 import ADXL345
adxl345 = ADXL345()

def raw_to_value(detect):
	accel = adxl345.ADXL345()
	axes = accel.getAxes(True)
	accel.setRange(adxl345.RANGE_16G)

	while(not detect):

		x=axes['x']
		y=axes['y']
		z=axes['z']
		l1= []
		l1.append(x)
		l1.append(y)
		l1.append(z)
		return l1

	