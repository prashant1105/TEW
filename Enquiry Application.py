#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 15:58:25 2019

@author: prashantpk
"""

# API KEY: 0299a321aad8b514e4873dff5b831681
# PRIVATE KEY: 5c7c66e8bfecdd1662bbaeafabfeb3ff
## Application ID: e7d78c18
## Application Key: 3b93ac98bf5e39f4e5a5dc09e9910c0a    

_app_id = "e7d78c18"
_app_key = "3b93ac98bf5e39f4e5a5dc09e9910c0a"
api_key = '0299a321aad8b514e4873dff5b831681'

import requests

class Enquiry:

#### The Constructor for the Class Enquiry...    
    def __init__(self):
        
        user_input = input("""Hi! What would you like to do.
            1. Enter 1 to search for flights.
            2. Enter 2 to check PNR Status.
            3. Enter 3 to check Route of the Train.
            4. Enter 4 to check the seat availabilty of train for a given date.
            5. Enter 5 to check Train Status.
            6. Enter 6 to find train between stations.
            7. Enter 7 to find trains at the station.
            8. Enter 8 to find cancelled trains for a given date.
            9. Enter 9 to find diverted trains for a given date.
            10. Enter 10 to check station location on map.
            11. Enter 11 to check Coach Position for a given train number.
            12. Enter 12 to exit. \n""")
        if user_input == "1":
            flight_search()        
        if user_input == "2":
            pnr_status()
        elif user_input == "3":
            train_route()
        elif user_input == "4":
            seat_availability()
        elif user_input == "5":
            train_status()
        elif user_input == "6":
            find_train()
        elif user_input == "7":
            train_arrival()
        elif user_input == "8":
            cancelled_trains()
        elif user_input == "9":
            diverted_trains()
        elif user_input == "10":
            station_location()
        elif user_input == "11":
            coach_position()
        else:
            print("BYE")

            
#######################################################################################################


#######################################################################################################         

    def flight_search():
        """
        ===> Doc String of the FUNCTION: flight_search "
        This Function is used to seach for flights between two places on a given date.
        Date: 09 2019
        Created By: Prashant Kumar
        Input: Origin Airport Code (from where the journey starts, should be a valid IATA Code)
               Destination Airport Code (upto where the journey has to end, should be a valid IATA Code)
               Departure Date: The date of Journey.
               Check: If One Way Flight: 0, otherwise if Return Flight is also considered: 1
               Arrival Date: If Return Flight is also considered then date of return.
               Seating Class: The type of Class in which user wants to travel, Business: B, or Economy : E
               Adult Pass: Number of Adult Passengers (At least one)
               Child Pass: Number of Children Passengers.
               Infant Pass: Number of Infant Passengers
               Counter: International: 0, Domestic: 100
        Output: Flight Detais as per the User Search.
        """

        source = input("Enter the Origin Airport code. \n(Should be a valid IATA code): ").upper()
        dest = input("Enter the Destination Airport code. \n(Should be a valid IATA code): ").upper()
        departure_date = input("Enter the Departure Date \n(for onward flights only). (Format (YYYYMMDD)): ")
        check = input("Do you wish to check for return flight to. \n(If yes enter 1 else enter 0): ")
        if check == '1':
            arrival_date = input("Enter the Arrival Date \n(for onward & return Flights). (Format (YYYYMMDD)): ")
        else:
            pass
        seating_class = input("Enter the Travel Class/ Cabin Type. \n(E(Economy) or B(Business)): ").upper()
        adult_pass = input("Enter the number of Adult Passengers. \n(Integer value between 1-9. Minimum of one adult is required.): ")
        child_pass = input("Enter the number of Children Passengers. \n(Integer value between 0-9.): ") 
        infant_pass = input("Enter the number of Infant Passengers. \n(Integer value between 0-9.): ")
        counter = input("Enter the Counter No. \n(100 for domestic, 0 for International): ")
        
        if check == '1':
            url = "http://developer.goibibo.com/api/search/?app_id={}&app_key={}&format=json&source={}&destination={}&dateofdeparture={}&dateofarrival={}&seatingclass={}&adults={}&children={}&infants={}&counter={}".format(_app_id, _app_key, source, dest, departure_date, arrival_date, seating_class, adult_pass, child_pass, infant_pass, counter)
            
        else:
            url = "http://developer.goibibo.com/api/search/?app_id={}&app_key={}&format=json&source={}&destination={}&dateofdeparture={}&seatingclass={}&adults={}&children={}&infants={}&counter={}".format(_app_id, _app_key, source, dest, departure_date, seating_class, adult_pass, child_pass, infant_pass, counter)
        
        response = requests.get(url)
        response = response.json()
        #print(response)
        
        if check == '0':
            for i in response['data']['onwardflights']:
                print("\n", i['airline'], "|", i['origin'], i['deptime'], "-->", i['duration'], "(", i['stops'], "Stop)", "-->", i['destination'], i['arrtime'], "|", i['seatingclass'], i['fare']['totalfare'])
                print("-------- FLIGHT INFORMATION --------")
                print(i['airline'], "(", i['carrierid'], "-", i['flightno'], ")", "(Aircraft:", i['aircraftType'], ")", i['origin'], i['deptime'], "-->", i['duration'], "(", i['stops'], "STOPS)", "-->", i['destination'], i['arrtime'])
                print("-------- FARE DETAILS --------")
                print("Base Fare (", adult_pass, "Adults,", child_pass, "Child,", infant_pass, "Infant) :", i['fare']['totalbasefare'])
                #print("Taxes and Fees (", adult_pass, "Adults,", child_pass, "Child,", infant_pass, "Infant) :", (i['fare']['adulttax'] + i['fare']['infanttaxes'] + i['fare']['childtaxes']))
                print("Total Fare (", adult_pass, "Adults,", child_pass, "Child,", infant_pass, "Infant) :", i['fare']['totalfare'])
                print("--------------------------------------------")
                
        else:
            for i, j in zip(response['data']['onwardflights'], response['data']['returnflights']):
                print("\n", i['airline'], "|", i['origin'], i['deptime'], "-->", i['duration'], "(", i['stops'], "Stop)", "-->", i['destination'], i['arrtime'], "|", i['seatingclass'], i['fare']['totalfare'], "|||", j['airline'], "|", j['origin'], j['deptime'], "-->", j['duration'], "(", j['stops'], "Stop)", "-->", j['destination'], j['arrtime'], "|", j['seatingclass'], j['fare']['totalfare'])
                print("-------- FLIGHT INFORMATION --------")
                print(i['airline'], "(", i['carrierid'], "-", i['flightno'], ")", "(Aircraft:", i['aircraftType'], ")", i['origin'], i['deptime'], "-->", i['duration'], "(", i['stops'], "STOPS)", "-->", i['destination'], i['arrtime'], "|||", j['airline'], "(", j['carrierid'], "-", j['flightno'], ")", "(Aircraft:", j['aircraftType'], ")", j['origin'], j['deptime'], "-->", j['duration'], "(", j['stops'], "STOPS)", "-->", j['destination'], j['arrtime'])
                print("-------- FARE DETAILS --------")
                print("Base Fare (", adult_pass, "Adults,", child_pass, "Child,", infant_pass, "Infant) :", i['fare']['totalbasefare'], "\n", "Total Fare (", adult_pass, "Adults,", child_pass, "Child,", infant_pass, "Infant) :", i['fare']['totalfare'], "\n", "Base Fare (", adult_pass, "Adults,", child_pass, "Child,", infant_pass, "Infant) :", j['fare']['totalbasefare'], "\n", "Total Fare (", adult_pass, "Adults,", child_pass, "Child,", infant_pass, "Infant) :", j['fare']['totalfare'], "\n")
                #print("Taxes and Fees (", adult_pass, "Adults,", child_pass, "Child,", infant_pass, "Infant) :", (i['fare']['adulttax'] + i['fare']['infanttaxes'] + i['fare']['childtaxes']))

           
#######################################################################################################
            
            
#######################################################################################################

    def pnr_status():
        """
        ===> Doc String of the FUNCTION: pnr_status "
        This Function is used to find the pnr status for a given PNR Number.
        Date: 21st June 2019
        Created By: Prashant Kumar
        Input: A valid PNR Number of a train from India.
        Output: Details related to the give PNR number.
        """
        # http://indianrailapi.com/api/v2/PNRCheck/apikey/<apikey>/PNRNumber/<pnrNumber>/Route/1/
        pnr_no = input("Enter the PNR number: ")
        pnr_url = "http://indianrailapi.com/api/v2/PNRCheck/apikey/{}/PNRNumber/{}/Route/1/".format(api_key, pnr_no)
        response = requests.get(pnr_url)
        response = response.json()
        #print(pnr_response)
        print("PNR No.: ", response['PnrNumber'])
        print("Train Number:", response['TrainNumber'], "|" , "Train Name:", response['TrainName'])
        print("Date of Journey:", response['JourneyDate'], "|" , "Chart Prepared:", response['ChatPrepared'], "|", "Journey Class:", response['JourneyClass'])
        print("From: ", response['From'], "---->", "Reservation Upto: ", response['To'])
        for i in response['Passangers']:
            print("Passenger Details: ", i['Passenger'])
            print("Booking Status:", i['BookingStatus'])
            print("Current Status: ", i['CurrentStatus'], "\n")            


#######################################################################################################
            

#######################################################################################################
        
    def train_route():
        """
        ===> Doc String of the FUNCTION: train_route "
        This Function is used to find the route for a given train number.
        Date: 21st June 2019
        Created By: Prashant Kumar
        Input: A valid Train Number from India Railway
        Output: Train Name, Number and Details of the station that the train covers.
        """
        # http://indianrailapi.com/api/v2/TrainSchedule/apikey/<apikey>/TrainNumber/<TrainNumber>/
        train_no = input("Enter the Train Number: ")
        status_url = "http://indianrailapi.com/api/v2/TrainSchedule/apikey/{}/TrainNumber/{}/".format(api_key, train_no)
        response = requests.get(status_url)
        response = response.json()
        #print(response)
        #for i in status_response['train']:
        #print(response['train']['name'])
        for i in response['Route']:
            print("Station No.:", i['SerialNo'], "|", "Station Name:", i['StationName'], "|", "Arrival Time:", i['ArrivalTime'], "|", "Departure Time:", i['DepartureTime'], "|", "Distance Covered:", i['Distance'], "\n")          


#######################################################################################################
            

#######################################################################################################
            
    def seat_availability():
        
        """
        ===> Doc String of the FUNCTION: seat_availability "
        This Function is used to find the number of seats available for a train on a given date between two stations.
        Date: 21st June 2019
        Created By: Prashant Kumar
        Input: A vaild Train Number
               Source Station Code
               Destination Station code
               Date of the journey
               Class Code of the Class in which user wants to find the seat.
               Quota Code of the quota in user wants to book a seat.
        Output: Train Name, Train Number 
                Journey Class which user has selected along with its Code
                From Station where user is starting the journey, Destination Station Name.
                Selected date and the Availabilty Status for the given date.
                """
        # Train Fare: http://indianrailapi.com/api/v2/TrainFare/apikey/<apikey>/TrainNumber/<trainNumber>/From/<stationFrom>/To/<stationTo>/Quota/<quota>
        # https://indianrailapi.com/api/v2/SeatAvailability/apikey/{apikey}/TrainNumber/{trainNumber}/From/{stationFrom}/To/{stationTo}/Date/{yyyyMMdd}/Quota/GN/Class/{classCode}
        train_no = input("Enter the Train Number: ")
        source_stn = input("Enter the Source Station Code: ").upper()
        dest_stn = input("Enter the Destination Station Code: ").upper()
        date = input("Enter the date of journey \n(in yyyymmdd format): ")
        class_code = input("Enter the class code: ").upper()
        quota_code = input("Enter the Quota to book the ticket(GN: General, CK: Tatkal): ").upper()
        url = "https://indianrailapi.com/api/v2/SeatAvailability/apikey/{}/TrainNumber/{}/From/{}/To/{}/Date/{}/Quota/GN/Class/{}".format(api_key, train_no, source_stn, dest_stn, date, class_code)
        fare_url = "http://indianrailapi.com/api/v2/TrainFare/apikey/{}/TrainNumber/{}/From/{}/To/{}/Quota/{}".format(api_key, train_no, source_stn, dest_stn, quota_code)
        response = requests.get(url)
        response = response.json()
        fare_response = requests.get(fare_url)
        fare_response = fare_response.json()
        print("Train Number:", response['TrainNo'], "|", "Train Name:", fare_response['TrainName'], "|" "From:", response['From'], "|", "To:", response['To'], "|", "Class Code:", response['ClassCode'], "|", "Quota:", response['Quota'])
            
        for k in fare_response['Fares']:
            if k['Code'] == class_code:
                for i in response['Availability']:
                    print("Date:", i['JourneyDate'], "|", i['Availability'], "|", "Confirm Percentage:", i['Confirm'], "|", "Fare:", k['Fare'], "\n")           


#######################################################################################################
            
            
#######################################################################################################

    def train_status():
        
        """
        ===> Doc String of the FUNCTION: train_status "
        This Function is used to find the Live Train status for a given Train Number, Station and Date.
        Date: 21st June 2019
        Created By: Prashant Kumar
        Input: A valid Train Number
               Date for which the user wants to check
        Output: Train Number
                Train Name
                Curreent Position of the Train
        """
        # http://indianrailapi.com/api/v2/livetrainstatus/apikey/<apikey>/trainnumber/<train_number>/date/<yyyymmdd>/
        train_no = input("Enter the train number: ")
        date = input("Enter the date \n(in yyyymmdd format):")
        url = "http://indianrailapi.com/api/v2/livetrainstatus/apikey/{}/trainnumber/{}/date/{}/".format(api_key, train_no, date)
        response = requests.get(url)
        response = response.json()
        #print(response)
        print(response['TrainNumber'], "|", response['StartDate'])
        print("Current Status:", response['CurrentStation']['StationName'], "|", "Schedule Arrival:", response['CurrentStation']['ScheduleArrival'], "|", "Actual Arrival:", response['CurrentStation']['ActualArrival'], "|", "Scheduled Departure:", response['CurrentStation']['ScheduleDeparture'], "|", "Actual Departure:", response['CurrentStation']['ActualDeparture'])
        print("Train is at:", response['CurrentStation']['StationName'], "|", "Train is delayed by:", response['CurrentStation']['DelayInDeparture'], "\n")            


#######################################################################################################


#######################################################################################################

    def find_train():
        """
        ===> Doc String of the FUNCTION: find_train "
        This Function is used to find the train between stations for a given date.
        Date: 21st June 2019
        Created By: Prashant Kumar
        Input: Source Station Code
               Destination Station Code
        Output: Train Number, Train Name
                From Station (from the station where the train starts), To Station (to the station where train goes.)
                Source Departure Time, Destination Arrival Time
        """
        # http://indianrailapi.com/api/v2/TrainBetweenStation/apikey/<apikey>/From/<From>/To/<To>
        source_station = input("Enter the source station: ").upper()
        dest_station = input("Enter the destination station: ").upper()
        #date = input("Enter the date of journey: ")
        find_train_url = "http://indianrailapi.com/api/v2/TrainBetweenStation/apikey/{}/From/{}/To/{}".format(api_key, source_station, dest_station)
        response = requests.get(find_train_url)
        response = response.json()
        print("Total Number of Trains Found:", response['TotalTrains'])
        for i in response['Trains']:
            print("Train Number:", i['TrainNo'], "|", "Train Name:", i['TrainName'])
            print("Source Station:", i['Source'], "--->", "Destination Station:", i['Destination'])
            print("Departure from Source:", i['DepartureTime'], "---->", "Arrival at Destination:", i['ArrivalTime'])
            print("Travel Time:", i['TravelTime'], "|", "Train Type:",  i['TrainType'], "\n")


#######################################################################################################


#######################################################################################################

    def train_arrival():
        """
        ===> Doc String of the FUNCTION: pnr_status "
        This Function is used to find the number of trains arriving at a station for a given period of time.
        Date: 21st June 2019
        Created By: Prashant Kumar
        Input: A valid Station Code
               Time period in hours for which user wants to check (such as 2, 4)
        Output: Train Number, Train Name
                Scheduled Arrival time, Actual Arrival Time, Arrival time of Train delayed by.
                Scheduled Departure time, Actual Departure Time, Departure time of Train delayed by.
        """
        # http://indianrailapi.com/api/v2/LiveStation/apikey/<apikey>/StationCode/<StationCode>/hours/<Hours>/
        station = input("Enter the station code for which you want to check: ").upper()
        window_period = input("Enter the amount of time for which you want to check: ")
        url = "http://indianrailapi.com/api/v2/LiveStation/apikey/{}/StationCode/{}/hours/{}/".format(api_key, station, window_period)
        response = requests.get(url)
        response = response.json()
        for i in response['Trains']:
            print(i['Number'], "|", i['Name'])
            print(i['Source'], "|", i['Destination'])
            print("Scheduled Arrival:", i['ScheduleArrival'], "|", "Expected Arrival:", i['ExpectedArrival'])
            print("Scheduled Departure:", i['ScheduleDeparture'], "|", "ExpectedDeparture:", i['ExpectedDeparture'])
            print("Delayed By:", i['DelayInDeparture'], "\n")
            

#######################################################################################################


#######################################################################################################

    def cancelled_trains():
        """
        ===> Doc String of the FUNCTION: find_train "
        This Function is used to find the trains that are cancelled for the given date.
        Date: 21st June 2019
        Created By: Prashant Kumar
        Input: Date for which the user wants to check              
        Output: Train Number, Train Name (of the trains that are cancelled.)
                Source Station name, destination Station Name
        """
        # https://indianrailapi.com/api/v2/CancelledTrains/apikey/<apikey>/Date/<yyyyMMdd>
        date = input("Enter the date for which you want to find cancelled train \n(in yyyymmdd format): ")
        url = "https://indianrailapi.com/api/v2/CancelledTrains/apikey/{}/Date/{}".format(api_key, date)
        response = requests.get(url)
        response = response.json()
        print("Total Number of Cancelled Trains: ", response['TotalTrain'], "\n")
        for i in response['Trains']:
            print(i['TrainNumber'], "|", i['TrainName'])
            print(i['StartDate'], "|", i['TrainType'])
            print(i['Source'], "--->", i['Destination'], "\n")
            

#######################################################################################################


#######################################################################################################

    def diverted_trains():
        """
        ===> Doc String of the FUNCTION: find_train "
        This Function is used to find the trains that are cancelled for the given date.
        Date: 21st June 2019
        Created By: Prashant Kumar
        Input: Date for which the user wants to check              
        Output: Train Number, Train Name (of the trains that are cancelled.)
                Source Station name, destination Station Name
        """
        # https://indianrailapi.com/api/v2/DivertedTrains/apikey/<apikey>/Date/<yyyyMMdd>
        date = input("Enter the date for which you want to find diverted train \n(in yyyymmdd format): ")
        url = "https://indianrailapi.com/api/v2/DivertedTrains/apikey/{}/Date/{}".format(api_key, date)
        response = requests.get(url)
        response = response.json()
        print("Total Number of Diverted Trains: ", response['TotalTrain'], "\n")
        for i in response['Trains']:
            print(i['TrainNumber'], "|", i['TrainName'])
            print(i['StartDate'], "|", i['TrainType'])
            print("Actual Route:", i['Source'], "--->", i['Destination'])
            print("Diverted Route:", i['DivertedFrom'], "---->", i['DivertedTo'], "\n")
            

#######################################################################################################            
        

#######################################################################################################

    def station_location():
        """
        ===> Doc String of the FUNCTION: station_location "
        This Function is used to find the location of the station on the map.
        Date: 21st June 2019
        Created By: Prashant Kumar
        Input: Station Code for which the user wants to check              
        Output: Station Name, Station Code
                URL of the Station Address.
        """
        # http://indianrailapi.com/api/v2/StationLocationOnMap/apikey/<apikey>/StationCode/<StationCode>
        station = input("Enter the station code for which you want to get the location URL: ").upper()
        url = "http://indianrailapi.com/api/v2/StationLocationOnMap/apikey/{}/StationCode/{}".format(api_key, station)
        response = requests.get(url)
        response = response.json()
        print(response['StationCode'], "|", response['StationName'])
        print("Station Map Location URL:", response['URL'], "\n")       

#######################################################################################################


#######################################################################################################

    def coach_position():
        """
        ===> Doc String of the FUNCTION: coach_position "
        This Function is used to find the position of coaches for a given train number.
        Date: 21st June 2019
        Created By: Prashant Kumar
        Input: Train Number for which the user wants to check              
        Output: Train Number
                Serial Number and Coach Name.
        """
        # http://indianrailapi.com/api/v2/CoachPosition/apikey/<apikey>/TrainNumber/<TrainNumber>
        train_no = input("Enter the train number for which you want to get the coach position: ")
        url = "http://indianrailapi.com/api/v2/CoachPosition/apikey/{}/TrainNumber/{}".format(api_key, train_no)
        response = requests.get(url)
        response = response.json()
        print(response['TrainNumber'])
        for i in response['Coaches']:
            print(i['SerialNo'], "|", i['Name'], "---->")

#######################################################################################################        


Enquiry()