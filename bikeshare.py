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
    #  get user input for city (chicago, new york city, washington). Using a while loop to handle invalid inputs
    while True: 
        city = input('Salut! Enter your lovely city: ').lower()
        
        if city not in CITY_DATA :
            print("hmm! i guess it's not your lovely one,\n please enter your city")
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Now, Choose your lucky month: ').lower()
        mon = ['all', 'january', 'february', 'march','april','may' ,' june']
       
        if month not in mon :
            print("I belive you're lucky,\n please retype your month")
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Finally, Choose your nice day: ').lower()
        jour = ['all', 'monday', 'tuesday','Wednesday','Thursday','Friday','Saturday','sunday']
        
        if day not in jour:
            print("Have a nice day,\n and please reenter your day")
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day.

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #  display the most common month
    mois_commun = df['month'].mode()[0]
    print('alors, the most common month is: ', mois_commun)

    #  display the most common day of week
    jour_commun = df['day_of_week'].mode()[0]
    print('alors, the most commun day of the week is: ', jour_commun)
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print(' so! the most commonly used start station is: ',start_station)
    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print(' so! the most commonly used end station is: ',end_station)
    # display most frequent combination of start station and end station trip
   
    comb = df[['Start Station','End Station']].mode()
    print('well! the most frequent combination of start and end station is: ', comb)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

#    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total = df['Trip Duration'].sum()
    print('alors, the total travel time is: {} '.format(total)) 
    # display mean travel time
    mean = df['Trip Duration'].mean()
    print('so! the mean ravel time is: ', mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #  Display counts of user types
    user_types = df['User Type'].value_counts()
    print('well! for the typs, we have: ',user_types)
    #  Display counts of gender
    # Display earliest, most recent, and most common year of birth
    
  
    
    if 'Gender'and 'Birth Year' in df:
        ugender = df['Gender'].value_counts()
        print('well! for the gender, we have:   ', ugender)                                                           
        early = int(df['Birth Year'].min())
        print('so, for the earliest year of birth, we have: ', early)
        recent =int( df['Birth Year'].max())
        print('so, for the recent year of birth, we have: ', recent)
        commony = int(df['Birth Year'].mode()[0])
        print('so, for the common year of birth, we have: ', commony)
    else:
        print('oops! no gender for washington!')
                
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    r = 0
    shrow = input('Do you like displaying rows? yes/ no \n').lower()
    while True:
        if shrow.lower() == 'no':
            print('salut!')
            break
        elif shrow.lower() == 'yes':
            print(df.iloc[r:r+5])
            shrow = input('Do you like displaying rows? yes/ no \n').lower()
            r +=5
                  

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
