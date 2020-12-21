'''
Explore US Bikeshare Data. The user can explore the US Bikeshare Data
set by choosing the State, the Month, the Day and how detailed he want
to see the query

Sources used 
https://docs.python.org/3/
https://stackoverflow.com/questions
https://www.youtube.com/channel/UCrEpGdiRBgj6-ru1Q7WKIBw
https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g
'''

import time
import pandas as pd
import numpy as np
import datetime as dt

# Dictionary with city Data
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
    
def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.
    And how extensive the Output should be

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        (bool) extended - boolean for extended option
    """
    
    # get user input for city (chicago, new york city, washington).
    city = ' '
    city_num = ('1', '2', '3')
    print('################################################')
    print('Bikeshare Statistics. Please choose your city:  ')
    print('################################################')
    print("\nAvailable Data for \n1 Chicago, 2 New York City, 3 Washington")
    # loop to get the right input, acknowledged input is city or city number
    while city not in CITY_DATA.keys() and city not in city_num:
        # get user input for city (chicago, new york city, washington).
        city = input('Please choose by number or City Name: ')
        city = city.lower()
        # ask user to repeat the input
        if city not in CITY_DATA.keys() and city not in city_num:
            print('Wrong Input! Please choose from Chicago, New York City or Washington')
                    
    if city == '1':
            city = 'chicago'
    elif city == '2': 
            city = 'new york city'
    elif city == '3':  
            city = 'washington'
    print('Your Input: ', city.title())
    print('-'*60)
        
               
    # get user input for month (all, january, february, ... , june)
    month = ''
    month_controll = ('january', 'february', 'march', 
                      'april', 'may', 'june', 'all')
    month_controll_num = ('1', '2', '3',
                          '4', '5', '6')
    print("Available Data from January to June")
    # loop to get the right input, acknowledged input is month or month number
    while month not in month_controll and month not in month_controll_num:
        # get user input for month 
        month = input('Please type your favourite month or type all if you want to see them all: ')
        month = month.lower()
        # ask user to repeat the input
        if month not in month_controll and month not in month_controll_num:
            print('Wrong Input! Please type in the Name of the month or the Number or all: ')
    if month == '1':
            month = 'january'
    elif month == '2': 
            month = 'february'
    elif month == '3':  
            month = 'march'   
    elif month == '4': 
            month = 'april'
    elif month == '5':  
            month = 'may' 
    elif month == '6':  
            month = 'june'        
    print("Your Input: ", month.title())
    print('-'*60)
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ' '
    day_controll = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all')
    # loop to get the right input, acknowledged input is day name
    while day not in day_controll:
        # get user input for day 
        day = input('Please type your favourite day or type all if you want to see them all: ')
        day = day.lower()
        # ask user to repeat the input
        if day not in day_controll:
            print('Wrong Input! Please type in the Name of the day or all: ')
    print('Your Input: ', day.title())
    
    # get user input for extendet statistiks
    extended = ' '
    extended_controll = ('regular', 'extended')
    # loop to get the right input, acknowledged input is extended or regular
    while extended not in extended_controll:
        # get user input for extended option 
        extended = input('Would you like to see regular or extended Statistics: ')
        extended = extended.lower()
        # ask user to repeat the input
        if extended not in extended_controll:
            print('Wrong Input! Please choose between regular or extended: ')    
        else:
            print('Your Input: ', extended)
    # change string to bloolean
    if extended == 'extended': 
        extended = bool(True)
    else:
        extended = bool(False)
        
    print()
    print('Loading your Data for') 
    print('City: ', city.title())
    print('Month: ', month.title())
    print('Day: ', day.title())
    print('...')
    print('-'*80)
    time.sleep(2) # slow down for better view
    return city, month, day, extended
    
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    # convert Start time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # get month and day
    df['month'] = df['Start Time'].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df, month, day, extended):
    """
    Displays statistics on the most frequent times of travel.
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month if all were choosen 
    if month == 'all':
        months = ('january', 'february', 'march', 'april', 'may', 'june')
        popular_month = df["month"].mode()[0]
        print('Most Popular Month:', df["month"].mode()[0], "=",
              months[popular_month-1].title())
         # extended output if option were choosen 
        if extended:
            # counts the same entries for months
            popular_months  = df["month"].value_counts()  # zählt alle gleichen einträge
            print("Printing the frequency", "\n", popular_months ) 
     # display the most common day if all were choosen
    if day == 'all':      
        # display the most common day of week
        print('Most common start day:' , df["day_of_week"].mode()[0])
         # extended output if option were choosen 
        if extended:
            # counts the same entries for day names
            popular_day = df["day_of_week"].value_counts()  # zählt alle gleichen einträge
            print('Printing the frequency', '\n', popular_day) 
        
    # display the most common start hour
    # get hour out of start time
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\nMost Popular Start Hour:', popular_hour)
    # extended output if option were choosen 
    if extended:
        # counts the same entries for hours
        popular_hours  = df["hour"].value_counts()
        print("Printing the frequency", "\n", popular_hours)
     
    print("\nThis took %s seconds." % (time.time() - start_time))
    time.sleep(2) # slow down for better view
    print('-'*80)

def station_stats(df, extended):
    """
    Displays statistics on the most popular stations and trip.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_st = df['Start Station'].mode()[0]
    print('\nMost Popular Start Station:', popular_start_st)
     # extended output if option were choosen 
    if extended:
        # counts the same entries for start station names
        popular_start_sts  = df["Start Station"].value_counts()
        print("Printing the frequency", "\n", popular_start_sts.head(3))
    
    # display most commonly used end station
    popular_end_st = df['End Station'].mode()[0]
    print('\nMost Popular End Station:', popular_end_st)
     # extended output if option were choosen 
    if extended:
        # counts the same entries for end station names
        popular_end_sts  = df["End Station"].value_counts()
        print("Printing the frequency", "\n", popular_end_sts.head(3))
    
    # display most frequent combination of start station and end station trip
    # combines start and end station to get the route
    df['tour'] = df['Start Station'] + ' --> ' + df['End Station']
    popular_tour = df['tour'].mode()[0]
    print('\nMost Popular Tour: ', popular_tour)
     # extended output if option were choosen 
    if extended:
        # counts the same entries for tours
        popular_tours  = df['tour'].value_counts()
        print("Printing the frequency", "\n", popular_tours.head(3))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    time.sleep(2) # slow down for better view
    print('-'*80)

def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    totrti = df['Trip Duration'].sum()
    print('Total Travel Time in hours:', int((totrti/60)/60))
    
    # display mean travel time
    avg_totrti = df['Trip Duration'].mean()
    print('Average Travel Time {} minutes'.format(int(avg_totrti/60)))
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    time.sleep(2) # slow down for better view
    print('-'*80)

def user_stats(df, city):
    """
    Displays statistics on bikeshare users.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Types", "\n", user_types)
    
    # Display counts of gender and handles missing data
    try:
        gender_count = df['Gender'].value_counts()
        print('\nGender count', '\n', gender_count)
    except:
        print("No Gender Data for ", city.title())
    
    # Display earliest, most recent, and most common year of birth
    # and handles missing data
    try:
        dinosaur = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        print('\nThe erlies Date of birth is: ', int(dinosaur))
        print('The most recent Date of Birth', int(recent_year))
        print('The most common Date of Birth', int(common_birth))        
    except:
        print('No Birth Data for ', city)
    print("\nThis took %s seconds." % (time.time() - start_time))
    
        
    time.sleep(2) # slow down for better view
    print('-'*80)

def main():
	'''
	main part to get the necessary user inputs, initiate output
	and print the requested data
	'''
    while True:
        # functions call
        city, month, day, extended = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day,extended)
        station_stats(df, extended)
        trip_duration_stats(df)
        user_stats(df, city)
        
        # display user data for Top Birth years
        # ask user to see the top 5
        view_data = input('\nWould you like to view the raw Data for your query? Enter yes or no\n')
        if view_data == 'yes':
            # set start index
            start_loc = 0
            repeat = 'yes'
            # repeat as long user choose yes
            while (repeat == 'yes'):
                # print 5 rows per run
                pd.set_option('display.max_columns', None)
                print(df.iloc[start_loc:start_loc+5])
                start_loc += 5
                # repeat until user choose no
                while True:        
                    repeat = input('Do you wish to see the next 5, (yes or no)?: ').lower()
                    print('Your Input', repeat)
                    if repeat == 'yes' or repeat == 'no':
                        break
        
        # ask user if he want to repeat the query 
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
