import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    df["index"]=1
    df=df.filter(items=["race","index"])
    df=df.groupby("race").sum()
 # dfvvtyvybuvtyv
   print(df)
    df.to_dict()
    
    race_count = None
    df = pd.read_csv("adult.data.csv")
    # What is the average age of men?
    df=df.filter(items=["sex","age"]) 
    df=df.groupby("sex").mean()
    df.to_dict()
    average_age_men = df["age"]["Male"]

    # What is the percentage of people who have a Bachelor's degree?
    df = pd.read_csv("adult.data.csv")
    percentage_bachelors = None

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    df = pd.read_csv("adult.data.csv")
    higher_education = None
    lower_education = None

    # percentage with salary >50K
    df = pd.read_csv("adult.data.csv")
    higher_education_rich = None
    lower_education_rich = None

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    df = pd.read_csv("adult.data.csv")
    min_work_hours = None

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df = pd.read_csv("adult.data.csv")
    num_min_workers = None

    rich_percentage = None

    # What country has the highest percentage of people that earn >50K?
    df = pd.read_csv("adult.data.csv")
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    df = pd.read_csv("adult.data.csv")
    top_IN_occupation = None

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
