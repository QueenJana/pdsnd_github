import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():

    print('Hello! Do you want to explore Bikeshare data?')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please choose a city: Chicago, New York City or Washington: ').lower()
        if city not in CITY_DATA:
            print('please choose one of the three cities')
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please choose a month between january and june or all of them (by typing all)\n').lower()
    while True:
        if month in MONTHS:
            print(month)
            break
        elif month == 'all':
            print(month)
            break
        else:
            print('\n invalid month \n')
            month = input('Please choose a month between january and june or all of them (by typing all)\n').lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('choose a day from monday to sunday or the whole week').lower()
    while True:
        if day in DAYS:
            print(day)
            break
        elif day == 'all':
            print(day)
            break
        else:
            print('\n invalid month \n')
            day = input('Please choose a month between january and june or all of them (by typing all)\n').lower()

    print(city, month, day)
    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        month = MONTHS.index(month) +1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    common_month = df['month'].mode()[0]
    print('Most common Month: ', months[common_month-1])

    common_weekday = df['day_of_week'].mode()[0]
    print('Most common Day of the week is: ', days[common_weekday-1])

    df['start_hour'] = df['Start Time'].dt.hour
    common_hour = df['start_hour'].mode()[0]
    print('Most common hour: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most common Start station: ', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most common End station: ', end_station)


    # display most frequent combination of start station and end station trip
    combined_station = (df['Start Station'] + ' - ' + df['End Station']).value_counts().idxmax()
    print('Most frequent combined stations: ', combined_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_travel_time = df['Trip Duration'].sum()
    print('the total travel time:', total_travel_time, 'in seconds')

    # display mean travel time
    mean_travel_time=total_travel_time/count(df)
    print('the average travel time:', mean_travel_time, 'in seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts per each User Type:\n', user_types)

    # Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('Counts of each Gender Type:\n', gender)
    else:
        print('There is no Gender information in this city')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("earliest year of birth:", df['Birth Year'].min())
        print("latest year of birth:", df['Birth Year'].max())
        comon_birth_year = df['Birth Year'].value_counts().idxmax()
        print("most comon year of birth:", comon_birth_year)
    else:
        print('There is no Birthyear information in this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#display 5 lines of code if asked.

def data(df):
    raw_data = 0
    while True:
        show_data = input('Do you want to see the first 5 Lines of code? please type "yes" or "no"').lower()
        if show_data not in ['yes', 'no']:
            print('Your input is invalid: Please type "yes" or "no"')
        elif show_data == 'yes':
            raw_data += 5
            print(df.iloc[raw_data: raw_data + 5])
            more_data = input('Do you want to see more data? "yes" or "no"').lower()
            if more_data == 'no':
                break
            elif show_data == 'no':
                return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
