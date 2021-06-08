from datetime import datetime, timedelta
import time
from plyer import notification

import requests

if __name__ == '__main__':

    age = 52
    pin_codes = ["493773"]
    num_days = 2

    print("Searching for vaccine!")

    actual = datetime.today()
    list_format = [actual + timedelta(days=0) for iterator in range(num_days)]
    actual_dates = [iterator.strftime("%d-%m-%Y") for iterator in list_format]

    while True:
        counter = 0

        for pincode in pin_codes:
            for given_date in actual_dates:

                URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(
                    pincode, given_date)
                header = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/56.0.2924.76 Safari/537.36'}

                result = requests.get(URL, headers=header)

                if result.ok:
                    response_json = result.json()
                    if response_json["centers"]:
                        for center in response_json["centers"]:
                            for session in center["sessions"]:
                                if session["min_age_limit"] <= age and session["available_capacity"] > 0:

                                    print('Pin code: ' + pincode)
                                    print("Available on: {}".format(given_date))
                                    print("\t", center["block_name"])
                                    print("\t", center["name"])
                                    print("\t Price: ", center["fee_type"])
                                    print("\t Availability : ", session["available_capacity"])

                                    if session["vaccine"] != '':
                                        print("\t Vaccine type: ", session["vaccine"])
                                    print("\n")
                                    counter = counter + 1
                else:
                    print("No Vaccine Available!")

        break


