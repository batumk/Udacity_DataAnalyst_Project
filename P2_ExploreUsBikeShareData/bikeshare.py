"""
Created on Thursday Apr  12

@author: Batu Mengkai
"""
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = (input('\nPlease type in which city you want to explore: (Chicago, New York City, Washington):\n ')).lower()
        except:
            print('Wrong input! Please type in the correct city name again!')
        else:
            if city in ['chicago', 'new york city', 'washington']:
                break
            else:
                print('Wrong input! Please type in the correct city name again!')

    # TO DO: get user input for which way to filter the data.
    while True:
        try:
            print('\nYou want to filter the data by month, day, both or not at all?\n Type none for no filter\n')
            time_filter = (input('Filter by:')).lower()
        except:
            print('Wrong input! Please type in month, weekday, both or none.')
        else:
            if time_filter in ['month','day','both','none']:
                break
            else:
                print('Wrong input! Please type in month, weekday, both or none.')
    # if fliter by month, get user input for month (all, january, february, ... , june)
    if time_filter == 'month':
        while True:
            try:
                month = int(input('\nWhich month? (Type in integer. e.g., 1 = January)\n'))
                day = None
            except:
                print('Wrong input! Please type month as an integer.')
            else:
                if month in [1,2,3,4,5,6,7,8,9,10,11,12]:
                    break
                else:
                    print('Wrong input! Please type month as an integer.')
    #if fliter by day of week, get user input for day of week (all, monday, tuesday, ... sunday)
    elif time_filter == 'day':
        while True:
            try:
                month = int(input('\nWhich day of the week? (Type in integer. e.g., 0=Monday; 6=Sunday)\n'))
                day = None
            except:
                print('Wrong input! Please type day as an integer.')
            else:
                if month in [0,1,2,3,4,5,6]:
                    break
                else:
                    print('Wrong input! Please type month as an integer.')
    # if fliter by month and day, get user input for month and week.
    elif time_filter == 'both':
        while True:
            try:
                month = int(input('\nWhich month? (Type in integer. e.g., 1 = January)\n'))
                day = int(input('\nWhich day of the week? (Type in integer. e.g., 0=Monday; 6=Sunday)\n'))
            except:
                print('Wrong input! Please type month and day as an integer.')
            else:
                if month in [1,2,3,4,5,6,7,8,9,10,11,12] and day in [0,1,2,3,4,5,6]:
                    break
                else:
                    print('Wrong input! Please type month and day as an integer.')
    #if no need to fliter
    else:
        month = None
        day = None

    print('-'*40)
    return city, month, day


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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour

    if month != None:
        df = df[ df['month'] == month ]
    if day != None:
        df = df[ df['day_of_week'] == day ]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    print('\nThe most common month is {}'.format(common_month))

    # TO DO: display the most common day of week
    common_dayweek = df['day_of_week'].value_counts().idxmax()
    print('Thr most common day of the week is {}'.format(common_dayweek))

    # TO DO: display the most common start hour
    common_hour = df['hour'].value_counts().idxmax()
    print('The most common start hour is {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('\nThe most commonly used start station is {}'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is {}'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    count_df = df.groupby(['Start Station','End Station']).size().reset_index(name='count')
    combination_index = count_df['count'].idxmax()
    combination_star = count_df['Start Station'][combination_index]
    combination_end = count_df['End Station'][combination_index]
    print('The most frequent combination of start station and end station trip is: from {} to {}'.format(combination_star,combination_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nThe total travel time is {}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_usertype = df['User Type'].value_counts().count()
    print('The counts of user types are {}'.format(count_of_usertype))

    # TO DO: Display counts of gender
    count_of_gender = df['Gender'].value_counts().count()
    print('The counts of gender is {}'.format(count_of_gender))
    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year = df['Birth Year'].max()
    most_recent_year = df['Birth Year'].min()
    most_common_year = df['Birth Year'].value_counts().idxmax()
    print('\nThe earliest year is {}'.format(earliest_year))
    print('The most recent year is {}'.format(most_recent_year))
    print('The most common year is {}'.format(most_common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)

        if city != 'washington': # there are no gender and birth day data in washington.csv
            user_stats(df)
        else:
            count_of_usertype = df['User Type'].value_counts().count()
            print('The counts of user types are {}'.format(count_of_usertype))

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
