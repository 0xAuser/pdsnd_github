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

    city = input("Enter name of the city: ").lower()
    while city not in ["chicago", "new york city", "washington"]:
        city = input("choose one of the cities : chicago, new york city, washington: ").lower()

    month = input("Enter a month or type all to get all the months: ").lower()
    while month not in ["all", "january", "febraury", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]:
        month = input("enter month as january, febraury...: ").lower()

    day = input("Enter a day or type all: ").lower()

    return city,month,day


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
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name

    if month != "all":
        months = ["january", "febraury", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
        month = months.index(month) + 1
        df = df[df["month"] == month]

    if day != "all":
        df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["month"].mode()
    print("most common month: ", common_month)

    # TO DO: display the most common day of week
    common_day = df["day_of_week"].mode()
    print("most common day of the week: ", common_day)

    # TO DO: display the most common start hour
    common_start_hour = df["Start Time"].dt.hour.mode()
    print("the most common start hour: ", common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_station = df["Start Station"].mode()
    print("the most commonly used start station is: ", common_station)

    # TO DO: display most commonly used end station
    common_end_station = df["End Station"].mode()
    print("the most common end station: ", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df["freq_trip"] = df["Start Station"] + df["End Station"]
    freq_combination = df["freq_trip"].mode()
    print("the most frequent combination of start and end station: ", freq_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df["Trip Duration"].sum()
    print("total travel time: ", travel_time)

    # TO DO: display mean travel time
    average_time = df["Trip Duration"].mean()
    print("total average travel time: ", average_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("user types:", df["User Type"].value_counts())


    # TO DO: Display counts of gender

    try:
        print("Genders:", df["Gender"].value_counts())

    except KeyError:
        print("there's no Gender classification for this city")
    print("\n")


   # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("earliest birth:", df["Birth Year"].min())
        print("most recent year birth:", df["Birth Year"].max())
        print("most common year of birth:", df["Birth Year"].mode())

    except KeyError:
        print("Birth Year classification is not available for this city")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Display raw data of first 5 rows of data frame for each action until five times

def raw_data(df):

    print(df.head())
    x = 0

    while True:
        view_raw_data = input('\n Type yes or no to check 5 rows of raw data.\n')
        if view_raw_data.lower() != 'yes':
            return
        x = x + 5
        print(df.iloc[x:x+5])





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Good Bye!")
            break


if __name__ == "__main__":
	main()
