import raw_to_value
import gsm
import emgcon
import gps
import buzzer
import emg
detect= False
def check():
	a=15.0
	b=-15.0
	while(not detect):
		l2= list(raw_to_value(detect))
		if(l2[0]>=a or l2[0]<=b or l2[1]>=a or l2[1]<=b or l2[2]>=a or l2[2]<=b):
			detect=True	#Accident Detected
	gpsdata=list(get_gps())
	message="Accident Occure At Latitude= "+gpsdata[0]+" ,Longitude= "+gpsdata[1]+"\n"+map_link+"\n Please Report Urgently"
	for conn in llist:
		sendsms(message,str(conn))
	loop()	#Turning on Buzzer
	sendsms(message)
	while(True):
		add_contact()
		loop()
		add_contact()










