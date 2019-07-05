#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 12:21:25 2019

@author: prashantpk
"""
# API KEY: fpnfmdrthc


import requests
def user_menu():
    user_input = input("""Hi! What would you like to do.
        1. Enter 1 to check PNR Status.
        2. Enter 2 to check Route of the Train.
        3. Enter 3 to check the seat availabilty of train for a given date.
        4. Enter 4 to check Train Status.
        5. Enter 5 to find train between stations.
        6. Enter 6 to find trains at the station.
        7. Enter 7 to find cancelled trains for the day.
        8. Enter 8 to exit. \n""")
    if user_input == "1":
        pnr_status()
    elif user_input == "2":
        train_route()
    elif user_input == "3":
        seat_availability()
    elif user_input == "4":
        train_status()
    elif user_input == "5":
        find_train()
    elif user_input == "6":
        train_arrival()
    elif user_input == "7":
        cancelled_trains()
    else:
        print("BYE")


def pnr_status():
    """
        ===> Doc String of the FUNCTION: pnr_status "
        This Function is used to find the pnr status for a given PNR Number.
        Date: 21st June 2019
        Created By: Prashant Kumar
        Input: A valid PNR Number of a train from India
        Output: details related to the give PNR number.
        """
    # https://api.railwayapi.com/v2/pnr-status/pnr/<PNR No>/apikey/fpnfmdrthc/
    pnr_no = input("Enter the PNR number: ")
    pnr_url = "https://api.railwayapi.com/v2/pnr-status/pnr/{}/apikey/fpnfmdrthc/".format(pnr_no)
    pnr_response = requests.get(pnr_url)
    pnr_response = pnr_response.json()
    #print(pnr_response)
    print("Train Number:", pnr_response['train']['number'], "|" , "Train Name:", pnr_response['train']['name'])
    print("Date of Journey:", pnr_response['doj'], "|" , "Chart Prepared:", pnr_response['chart_prepared'], "|", "Total Passengers:", pnr_response['total_passengers'])
    print("From: ", pnr_response['from_station']['name'], "|", "Reservation Upto: ", pnr_response['reservation_upto']['name'])
    
    
def train_route():
    """
        ===> Doc String of the FUNCTION: train_route "
        This Function is used to find the route for a given train number.
        Date: 21st June 2019
        Created By: Prashant Kumar
        Input: A valid Train Number from India
        Output: Train Name, Number and details of the station that the train covers.
        """
    # https://api.railwayapi.com/v2/route/train/<train number>/apikey/fpnfmdrthc/
    train_no = input("Enter the Train Number: ")
    status_url = "https://api.railwayapi.com/v2/route/train/{}/apikey/fpnfmdrthc/".format(train_no)
    status_response = requests.get(status_url)
    status_response = status_response.json()
    #print(response)
    #for i in status_response['train']:
    print(status_response['train']['name'])
    for i in status_response['route']:
        print(i['station']['name'], "|", i['scharr'], "|", i['schdep'], "|", i['distance'], "|", i['halt'], " expected")
        print("-------------------------------------------------------")
 

def seat_availability():
    """
        ===> Doc String of the FUNCTION: seat_availability "
        This Function is used to find the number of seats available for a train on a given date between two stations.
        Date: 21st June 2019
        Created By: Prashant Kumar
        Input: A vaild Train Number.
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
    #https://api.railwayapi.com/v2/check-seat/train/<train number>/source/<stn code>/dest/<dest code>/date/<dd-mm-yyyy>/pref/<class code>/quota/<quota code>/apikey/fpnfmdrthc/
    train_no = input("Enter the Train Number: ")
    source_stn = input("Enter the Source Station Code: ")
    dest_stn = input("Enter the Destination Station Code: ")
    date = input("Enter the date of journey: ")
    class_code = input("Enter the class code: ")
    quota_code = input("Enter the Quota to book the ticket: ")
    url = "https://api.railwayapi.com/v2/check-seat/train/{}/source/{}/dest/{}/date/{}/pref/{}/quota/{}/apikey/fpnfmdrthc/".format(train_no, source_stn, dest_stn, date, class_code, quota_code)
    response = requests.get(url)
    response = response.json()
    print(response["\n",'train']['name'], "|", response['train']['number'])
    print(response['journey_class']['name'], "|", response['journey_class']['code'])
    print(response['from_station']['name'], "--->", response['to_station']['name'])
    print(response['availability'][0]['date'], "|", response['availability'][0]['status'])
       

def train_status():
    """
        ===> Doc String of the FUNCTION: pnr_status "
        This Function is used to find the Live Train status for a given Train Number, Station and Date.
        Date: 21st June 2019
        Created By: Prashant Kumar
        Input: A valid Train Number
               Station Code
               Date for which the user wants to check
        Output: Train Number
                Train Name
                Curreent Position of the Train
        """
    # https://api.railwayapi.com/v2/live/train/<train-number>/station/<station-code>/date/<dd-mm-yyyy>/apikey/fpnfmdrthc/
    train_no = input("Enter the train number: ")
    station = input("Enter the station code: ")
    date = input("Enter the date:")
    url = "https://api.railwayapi.com/v2/live/train/{}/station/{}/date/{}/apikey/fpnfmdrthc/".format(train_no, station, date)
    response = requests.get(url)
    response = response.json()
    #print(response)
    print(response['train']['number'], "|", response['train']['name'])
    print(response['position'])


def find_train():
    """
        ===> Doc String of the FUNCTION: find_train "
        This Function is used to find the train between stations for a given date.
        Date: 21st June 2019
        Created By: Prashant Kumar
        Input: Source Station Code
               Destination Station Code
               Date for which the user wants to check
        Output: Train Number, Train Name
                From Station (from the station where the train starts), To Station (to the station where train goes.)
                Source Departure Time, Destination Arrival Time
        """
    #https://api.railwayapi.com/v2/between/source/<stn code>/dest/<stn code>/date/<dd-mm-yyyy>/apikey/fpnfmdrthc/
    source_station = input("Enter the source station: ")
    dest_station = input("Enter the destination station: ")
    date = input("Enter the date of journey: ")
    find_train_url = "https://api.railwayapi.com/v2/between/source/{}/dest/{}/date/{}/apikey/fpnfmdrthc/".format(source_station, dest_station, date)
    response = requests.get(find_train_url)
    response = response.json()
    #print(find_train_response)
    for i in response['trains']:
        print(i['number'], "|", i['name'], "|", i['travel_time'])
        print(i['from_station']['name'], "--->", i['to_station']['name'])
        print(i['src_departure_time'], "--->", i['dest_arrival_time'], "\n")


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
    #https://api.railwayapi.com/v2/arrivals/station/<stn code>/hours/<window period in hours>/apikey/fpnfmdrthc/
    station = input("Enter the station for which you want to check: ")
    window_period = input("Enter the amount of time for which you want to check: ")
    url = "https://api.railwayapi.com/v2/arrivals/station/{}/hours/{}/apikey/fpnfmdrthc/".format(station, window_period)
    response = requests.get(url)
    response = response.json()
    for i in response['trains']:
        print(i['number'], "|", i['name'])
        print(i['scharr'], "|", i['actarr'], "|", i['delayarr'])
        print(i['schdep'], "|", i['actdep'], "|", i['delaydep'], "\n")
  

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
    #https://api.railwayapi.com/v2/cancelled/date/<dd-mm-yyyy>/apikey/fpnfmdrthc/
    date = input("Enter the date for which you want to find cancelled train: ")
    url = "https://api.railwayapi.com/v2/cancelled/date/{}/apikey/fpnfmdrthc/".format(date)
    response = requests.get(url)
    response = response.json()
    for i in response['trains']:
        print(i['number'], "|", i['name'])
        print(i['source']['name'], "--->", i['dest']['name'], "\n")


      
        
user_menu()