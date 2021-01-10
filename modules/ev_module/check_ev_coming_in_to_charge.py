import random
from random import randrange
from datetime import time, datetime


def check_ev_coming_in_to_charge(ev_start_time):
    ev_start_time_hour = ev_start_time.hour
    # user inputs: number of chargers, 
    # ASSUMING ONE CHARGER RN
    chance_ev_wants_charge = random.uniform(0, 1)
    # this the chance that ev comes in and wants to charge

    if ev_start_time_hour >= 0 and ev_start_time_hour < 7: # 12am - 6am
        probability_of_ev_entered = 0.95
        probability_of_ev_charging = 0.85
        if (chance_ev_wants_charge <= probability_of_ev_charging*probability_of_ev_entered):     
            ev_wanting_charge = True
            ev_battery_start_percentage = random.randrange(0,40,1) # NEED TO CHANGE FOR BETTER ACCURACY
            print('ev wants it b/t 12am - 6am')
            return ev_wanting_charge, ev_battery_start_percentage

        else:
            ev_wanting_charge = False
            print('ev dont wants it b/t 12am - 6am')
            return ev_wanting_charge, None

    elif ev_start_time_hour >= 7 and ev_start_time_hour < 13: # 7a, - 12pm
        probability_of_ev_entered = 0.4
        probability_of_ev_charging = 0.85
        if (chance_ev_wants_charge <= probability_of_ev_charging*probability_of_ev_entered):     
            ev_wanting_charge = True
            ev_battery_start_percentage = random.randrange(0,40,1) # NEED TO CHANGE FOR BETTER ACCURACY
            print('ev wants it b/t 7am - 12pm')
            return ev_wanting_charge, ev_battery_start_percentage

        else:
            ev_wanting_charge = False
            print('ev dont wants it b/t 7am - 12pm')
            return ev_wanting_charge, None
    elif ev_start_time_hour >= 13 and ev_start_time_hour < 20: # 1pm - 7 pm
        probability_of_ev_entered = 0.7
        probability_of_ev_charging = 0.85
        if (chance_ev_wants_charge <= probability_of_ev_charging*probability_of_ev_entered):     
            ev_wanting_charge = True
            ev_battery_start_percentage = random.randrange(0,40,1) # NEED TO CHANGE FOR BETTER ACCURACY
            print('ev wants it b/t 1pm - 7pm')
            return ev_wanting_charge, ev_battery_start_percentage

        else:
            ev_wanting_charge = False
            print('ev dont wants it b/t 1pm - 7pm')
            return ev_wanting_charge, None
    else:
        probability_of_ev_entered = 0.87
        probability_of_ev_charging = 0.85
        if (chance_ev_wants_charge <= probability_of_ev_charging*probability_of_ev_entered):     
            ev_wanting_charge = True
            ev_battery_start_percentage = random.randrange(0,40,1) # NEED TO CHANGE FOR BETTER ACCURACY
            print('ev wants it b/t 8pm - 12am')
            return ev_wanting_charge, ev_battery_start_percentage

        else:
            ev_wanting_charge = False
            print('ev dont wants it b/t 8pm - 12am')
            return ev_wanting_charge, None