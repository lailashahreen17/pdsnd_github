import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

weekdays_list = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

choice = ['month','day','both']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    cities = CITY_DATA.keys()

    while True:
        city = input("\n Which city are you interested in to look at? new york city, chicago or washington?\n").lower()
        if city not in cities:
            print("Please enter the valid city name!")
            continue
        else:
            break


    # Get user input for month, day or both

    while True:
        filter_by = input("Do you want to filter by month, day or both?Please enter month or day or both.\n")
        if filter_by not in choice:
            print('please enter valid choice')
            continue
        else:
            break

    while True:
    # when user preference is month
        if filter_by == choice[0]:
            day = 'all'
            month = input('Which month are you interested in to look at? january, february, march, april, may, june or all?\n').lower()
            if month not in months_list:
                print('Oops!Something is wrong.Please enter the correct month')
                continue
            else:
                break
    # when user preference is day
        elif filter_by == choice[1]:
            month = 'all'
            day = input('If you are looking for a particular day please type the day as follows: sunday, monday, tuesday, wednesday, thursday, friday, saturday or all.\n').lower()
            if day not in weekdays_list:
                print('Oops!Something is wrong.Please enter the correct weekday')
                continue
            else:
                break
    # when user prefence is both

        elif filter_by == choice[2]:
            while True:
                month = input('Which month are you interested in to look at? january, february, march, april, may, june or all?\n').lower()
                if month not in months_list:
                    print('Oops!Something is wrong.Please enter the correct month')
                    continue
                else:
                    break
            while True:
                day = input('If you are looking for a particular day please type the day as follows: sunday, monday, tuesday, wednesday, thursday, friday, saturday or all .\n').lower()
                if day not in weekdays_list:
                    print('Oops!Something is wrong.Please enter the correct weekday')
                    continue
                else:
                    break
        break

    print('-'*50)
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
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Shows statistics on the most frequent times of travel by bike users."""

    print('\nCalculating the first statistics...\n')
    start_time = time.time()

    # Display the most common month
    most_common_month= df['month'].mode()[0]
    print('Most Common Month:', most_common_month)


    # Display the most common day of week
    most_common_weekday = df['day_of_week'].mode()[0]
    print('Most Common Day:', most_common_weekday)


    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('Most Common Hour:', most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating the next statistics...\n')
    start_time = time.time()

    # Display most commonly used start station
    most_popular_start_stations = df['Start Station'].mode()[0]
    print('Most used start station:',most_popular_start_stations)


    # Display most commonly used end station
    most_popular_end_stations = df['End Station'].mode()[0]
    print('Most used end station:',most_popular_end_stations)


    # Display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station'].str.cat(df['End Station'], sep = " to ")
    popular_route = df['routes'].mode()[0]
    print('Most frequent combination of start and end station trip:', popular_route)


    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*50)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating the next statistics...\n')
    start_time = time.time()

    # Display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])/86400
    print('Total travel time:', Total_Travel_Time, " Days")


    # Display mean travel time

    Mean_Travel_Time = df['Trip Duration'].mean()/60
    print('Mean travel time:', Mean_Travel_Time, " Minutes")



    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*50)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating the next statistics...\n')
    start_time = time.time()

    # Display counts of user types
    counts_user_types = df['User Type'].value_counts()
    print('Here are the counts of various user types:',counts_user_types)


    # Display counts of gender
    #Gender data is not available for Washington city,so we may need to be careful
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print('\nGender Types:\nData is missing for this month.')

    # Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = int(df['Birth Year'].min())
      print('Earliest Year:', Earliest_Year)
    except KeyError:
      print('Earliest Year:\nData is missing for this month.')

    try:
      Most_Recent_Year = int(df['Birth Year'].max())
      print('Most Recent Year:', Most_Recent_Year)
    except KeyError:
      print('Most Recent Year:\nData is missing for this month.')

    try:
      Most_Common_Year = int(df['Birth Year'].value_counts().idxmax())
      print('Most Common Year:', Most_Common_Year)
    except KeyError:
      print('Most Common Year:\nData is missing for this month.')


    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*50)

def display_data(df):
    """
    Display contents of the CSV file to the display as requested by
    the user.
    """
    # Dispalying five random rows of the raw data

    interested_in_display = input('Do you want to see five lines of the raw data?Enter yes or no.\n').lower()

    while interested_in_display == 'yes':
        print('\nRaw Data Display:\n', df[df.columns[0:-4]].sample(5))
        terminate_display = input('\nDo you wish to continue?Enter yes or no.\n').lower()
        if terminate_display == 'no':
            break
        else:
            print("\nLet's print more raw data\n")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
