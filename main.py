import requests
from datetime import datetime
import smtplib
import time

my_email= "angelasmithapple35@gmail.com"
password ="Angelarules"
MY_LAT = 34.179750 # Your latitude
MY_LONG = -118.363570 # Your longitude
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude<= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True



def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)
    time_now = datetime.now()
    hour = time_now.hour
    print(hour)
    if hour <= sunrise and hour >= sunset:
        return True




#If the ISS is close to my current position
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="nellymlopez3@gmail.com",
                                msg= "Subject: Alert! \n\n Look up, the ISS is passing by!!!")

# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



