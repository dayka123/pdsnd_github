import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    print('\nWhich city do you want to explore?\n')

    while True:
        city = input('Please enter "Chicago", "New York City", "Washington"\n').lower()
        if city in ['chicago','new york city','washington']:
            print('\nLoading data for {}...'.format(city.title()))
            break
        print("\nData for {} is not available.\n".format(city))

    # get user input for month (all, january, february, ... , june)

    print('\nData from which month do you want to explore?\n')

    while True:
        month = input('Please enter a month from January to June. Type "All" for no filter.\n')
        if month.lower() in ['january','february','march','april','may','june','all']:
            print('\nLoading data for {}...'.format(month.title()))
            break
        elif month.lower() in ['july','august','september','october','november','december']:
            print('\nUnfortunately, data for {} is not available.\n'.format(month.title()))
            continue
        print("\nPlease enter month correctly.\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)

    print('\nData from which day of week do you want to explore?\n')

    while True:
        day = input('Please enter day of week. Type "All" for no filter.\n')
        if day.lower() in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']:
            print('\nLoading data for {}...'.format(day.title()))
            break
        print("\nPlease enter day of week correctly.\n")

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

    df = pd.read_csv(CITY_DATA.get(city.lower()))

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])


    if day != 'all':
        df = df[df['Start Time'].dt.dayofweek == DAYS.index(day)]

    if month != 'all':
        df = df[df['Start Time'].dt.month == MONTHS.index(month)+1]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # create 3 additional columns with month, day of week and hour.

    df['Month'] = df['Start Time'].dt.month

    df['Day of week'] = df['Start Time'].dt.dayofweek

    df['Hour'] = df['Start Time'].dt.hour

    # display the most common month
    print('asdfasdfsad {}'.format(df['Month'].mode()[0]))
    print('Most common month is {}'.format(MONTHS[df['Month'].mode()[0]-1].title()))
    # display the most common day of week
    print('Most common day is {}'.format(DAYS[df['Day of week'].mode()[0]].title()))

    # display the most common start hour
    print('Most common hour is {}'.format(df['Hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    df['Route'] = df['Start Station'] + " - " + df['End Station']
    # display most commonly used start station
    print('Most commonly used start station is {}.\n'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('Most commonly used end station is {}.\n'.format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    print('Most frequent combination of start station and end station trip is {}.\n'.format(df['Route'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time is {} seconds.'.format(df['Trip Duration'].sum()))

    # display mean travel time
    print('Mean travel time is {} seconds.'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())
    if 'Gender' in df.columns and 'Birth Year' in df.columns:
        # Display counts of gender
        print(df['Gender'].value_counts())

        # Display earliest, most recent, and most common year of birth
        print('Earliest year of birth is {}.'.format(df['Birth Year'].max()))
        print('Most recent year of birth is {}.'.format(df['Birth Year'].min()))
        print('Most common year of birth is {}.'.format(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_raw_data(df):
    df = df.drop(columns = ['Month', 'Day of week', 'Hour', 'Route'])
    pd.set_option('display.max_columns', 0)
    response = input('Do you want to see raw data? Type "yes" or "no".\n')
    while response == 'yes':
        print(df.sample(n=5))
        response = input('\nDo you want to see next sample? Type "yes" or "no".\n')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
