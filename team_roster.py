from datetime import datetime
from datetime import timedelta
from pprint import pprint
import collections
from collections import OrderedDict

def date_creator(roster_start_date,year):
    # if the given roster start date is not a Monday
    if roster_start_date.isoweekday() != 1:
        # Find the previous Monday as the start of the roster
        roster_start_date = roster_start_date - timedelta(days=(roster_start_date.isoweekday()-1))

    roster_start_week_number = roster_start_date.isocalendar()[1]
    roster_last_week_number = 52
    number_of_weeks = roster_last_week_number - roster_start_week_number

    roster_end_date = roster_start_date + timedelta(days= number_of_weeks*7 + 7)
    return roster_start_date, roster_end_date

def team_roster_generator(roster_start_date,team_roster_end_date):

    team_roster_default_value = {
        "Helpdesk": {
            "name": ""
        },
        "GWAN_Helpdesk": {
            "name": ""
        },
        "Pager": {
            "name": "",
            "GWAN_Support_Weekend": False
        },
        "DC Check": {
            "HK": "",
            "SG": "",
            "SY": ""
        }
    }

    roster_start_week_number = roster_start_date.isocalendar()[1]
    roster_last_week_number = 52
    number_of_weeks = roster_last_week_number - roster_start_week_number

    team_roster_dict = OrderedDict({})

    for date in (roster_start_date + timedelta(n) for n in range(number_of_weeks * 7 + 7)):
        team_roster_dict.setdefault(date,team_roster_default_value)

    return team_roster_dict

def team_roster_update(team_roster, duty_roster, roster_type):
    if roster_type == "Pager":
        team_roster[datetime(2019, 2, 18, 0, 0)][roster_type]['name'] = "shit"
        # for date in duty_roster:
        #     team_roster[date][roster_type]['name'] = duty_roster[date]
        #     print(date, duty_roster[date],team_roster[date][roster_type]['name'])
    else:
        pass
    pprint("outside for loop")
    pprint(team_roster)
    return team_roster

def roster_generator(roster_pattern,roster_start_date,roster_pattern_offset,year,roster_cycle,weekend_required):

    roster_start_week_number = roster_start_date.isocalendar()[1]
    # roster_cycle = 0, it means to generate the roster for the whole year
    if roster_cycle == 0:
        roster_cycle = (52 - roster_start_week_number) // len(roster_pattern)
        roster_last_week_number = 52
    # roster_cycle > 0, it means to repeat the roster pattern for number of roster_cycle
    elif roster_cycle > 0:
        roster_last_week_number = roster_start_week_number + roster_cycle * len(roster_pattern)

    number_of_weeks = roster_last_week_number - roster_start_week_number

    # if the given roster start date is not a Monday
    if roster_start_date.isoweekday() != 1:
        # Find the previous Monday as the start of the roster
        roster_start_date = roster_start_date - timedelta(days=(roster_start_date.isoweekday()-1))

    # roster dictionary initialization
    roster_dict = {}

    next = 0 + roster_pattern_offset
    for date in (roster_start_date + timedelta(n) for n in range(number_of_weeks * 7 + 7)):
        # weekday
        if date.isoweekday() <= 5:
            roster_dict[date] = roster_pattern[next].name
        # weekend
        elif date.isoweekday() > 5:
            # if weekend support is required
            if weekend_required:
                roster_dict[date] = roster_pattern[next].name
            else:
                roster_dict[date] = ""
            # if it's Sunday, advance to next person for next monday
            if date.isoweekday() == 7 and next < len(roster_pattern)-1:
                next += 1
            elif date.isoweekday() == 7 and next >= len(roster_pattern)-1:
                next = 0
        #print(roster_dict[date])

    return roster_dict

def gwan_weekend_roster_generator(roster_start_date,country,year):

    gwan_weekend_support_country = ["APAC", "UK", "US"]
    roster_start_week_number = roster_start_date.isocalendar()[1]
    roster_last_week_number = 52

    number_of_weeks = roster_last_week_number - roster_start_week_number

    # if the given roster start date is not a Monday
    if roster_start_date.isoweekday() != 1:
        # Find the previous Monday as the start of the roster
        roster_start_date = roster_start_date - timedelta(days=(roster_start_date.isoweekday()-1))

    # roster dictionary initialization
    roster_dict = {}

    next = 0
    for date in (roster_start_date + timedelta(n) for n in range(number_of_weeks * 7 + 7)):
        # weekday
        if date.isoweekday() <= 5:
            roster_dict[date] = ""
        # weekend
        elif date.isoweekday() > 5:
            roster_dict[date] = gwan_weekend_support_country[next % len(gwan_weekend_support_country)]

            # if it's Sunday, advance to next country for next monday
            if date.isoweekday() == 7:
                if next > len(gwan_weekend_support_country):
                    next = 0
                else:
                    next += 1

    return roster_dict

def main():

    Person = collections.namedtuple('Person','name, gender, location, duty, annual_leave travelable supportable business_trip')

    eric = Person(name='Eric', gender='M', location='hk', duty= {}, annual_leave={}, travelable= False, supportable= True, business_trip={})
    gary = Person(name='Gary', gender='M', location='hk', duty= {}, annual_leave={}, travelable= True, supportable= True, business_trip={})
    danny = Person(name='Danny', gender='M', location='hk', duty= {}, annual_leave={}, travelable= False, supportable= True, business_trip={})
    bill = Person(name='Bill', gender='M', location='hk', duty= {}, annual_leave={},travelable= False, supportable= True, business_trip={})
    chihang = Person(name='Chihang', gender='M', location='hk', duty= {}, annual_leave={},travelable= False, supportable= True, business_trip={})
    bell = Person(name='Bell', gender='M', location='hk', duty= {}, annual_leave={},travelable= False, supportable= True, business_trip={})
    jack = Person(name='Jack', gender='M', location='hk', duty= {}, annual_leave={},travelable= False, supportable= True, business_trip={})
    azral = Person(name='Azral', gender='M', location='sg', duty= {}, annual_leave={},travelable= True, supportable= True, business_trip={})
    ray = Person(name='Ray', gender='M', location='sg', duty= {}, annual_leave={},travelable= False, supportable= True, business_trip={})
    john = Person(name='John', gender='M', location='sg', duty= {}, annual_leave={},travelable= False, supportable= True, business_trip={})
    andrew = Person(name='Andrew', gender='M', location='sy', duty= {}, annual_leave={},travelable= False, supportable= True, business_trip={})

    team = [eric, gary, danny, bill, chihang, bell, jack, azral, ray, john, andrew]

    name_list = [x.name for x in team]

    roster_start_date = datetime(2019,2,18) # Roster starts on Monday (18-Feb-2019)
    apac_gwan_weekend_start_date = datetime(2019,2,18) # Roster starts on Monday (18-Feb-2019)

    roster_pattern = [eric, ray, bill, azral, chihang, john, andrew, bell, jack, danny, gary]

    weekend_required = True
    weekend_not_required = False

    pager_roster = roster_generator(roster_pattern,roster_start_date,0,2019,0,weekend_required)
    #pprint(pager_roster)
    helpdesk_roster = roster_generator(roster_pattern,roster_start_date,2,2019,0,weekend_not_required)
    #pprint(helpdesk_roster)
    gwan_helpdesk_roster = roster_generator(roster_pattern,roster_start_date,4,2019,0,weekend_not_required)
    #pprint(gwan_helpdesk_roster)

    apac_gwan_weekend_roster = gwan_weekend_roster_generator(apac_gwan_weekend_start_date,'APAC',2019)
    #pprint(apac_gwan_weekend_roster)

    team_roster_start_date, team_roster_end_date = date_creator(roster_start_date,2019)
    #print(team_roster_start_date, team_roster_end_date)

    team_roster = team_roster_generator(team_roster_start_date,team_roster_end_date)
    #pprint(team_roster)

    team_roster1 = team_roster_update(team_roster, pager_roster, "Pager")
    #pprint(team_roster1)

if __name__ == "__main__":
    main()