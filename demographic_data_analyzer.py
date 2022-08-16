import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    df["index"]=1
    df=df.filter(items=["race","index"])
    df=df.groupby("race").sum()
    df=df.to_dict()
    race_count=[]
    for i in df.values():
      for j in i.values():
        race_count.append(j)
    race_count.sort(reverse=True)
    df = pd.read_csv("adult.data.csv")
    # What is the average age of men?
    df=df.filter(items=["sex","age"]) 
    df=df.groupby("sex").mean()
    a=df["age"]["Male"]
    a=str(a)
    aa=a[:4]
    average_age_men = float(aa)

    # What is the percentage of people who have a Bachelor's degree?
    df = pd.read_csv("adult.data.csv")
    size=len((df))
    df["index"]=1
    df=df.filter(items=["education","index"])
    df=df.groupby("education").sum()
    b=(df["index"]["Bachelors"]/size)*100
    b=str(b)
    bb=b[:4]
    percentage_bachelors =float(bb) 

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    df=pd.read_csv("adult.data.csv",index_col="salary")
    df2=pd.read_csv("adult.data.csv",index_col="salary")
    df["index"]=1
    df=df.filter(items=["salary","education","index"])
    df=df.groupby("education").sum()
    size2=df["index"]["Bachelors"] + df["index"]["Masters"] + df["index"]["Doctorate"]
    df2["index"]=1
    df2=df2.filter(items=["salary","education","index"])
    df2=df2.drop(index="<=50K")
    df2=df2.groupby("education").sum()
    higher_education=(df2["index"]["Bachelors"] + df2["index"]["Masters"] + df2["index"]["Doctorate"])

    
    # What percentage of people without advanced education make more than 50K?
    df3=pd.read_csv("adult.data.csv",index_col="salary")
    df4=pd.read_csv("adult.data.csv",index_col="salary")
    df3["index"]=1
    df3=df3.filter(items=["salary","education","index"])
    df3=df3.groupby("education").sum()
    df4["index"]=1
    df4=df4.filter(items=["salary","education","index"])
    df4=df4.drop(index="<=50K")
    df4=df4.groupby("education").sum()
    df4=df4.drop(index=["Bachelors","Doctorate","Masters"])
    df3=df3.drop(index=["Bachelors","Doctorate","Masters"])
    df3=df3.sum()
    df4=df4.sum()
    df3.to_dict()
    df4.to_dict()
    c=(df4['index']/df3['index'])*100
    # c=str(c)
    # cc=c[:4]
    lower_education_rich =float("{:.1f}".format(c))
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # percentage with salary >50K
    d=((df2["index"]["Bachelors"] + df2["index"]["Masters"] + df2["index"]["Doctorate"])/size2)*100
    d=str(d)
    dd=d[:4]
    higher_education_rich =float(dd)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    df=pd.read_csv("adult.data.csv")
    df=df.filter(items=["hours-per-week"])
    df=df.min()
    df=df.to_dict()
    min_work_hours = df["hours-per-week"]

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df=pd.read_csv("adult.data.csv",index_col="salary")
    df=df.filter(items=["hours-per-week"])
    df=df.drop(index='<=50K')
    df=df.set_index('hours-per-week')
    df=pd.read_csv("adult.data.csv",index_col="salary")
    df2=pd.read_csv("adult.data.csv",index_col="salary")
    df=df.filter(items=["hours-per-week"])
    df2=df2.filter(items=["hours-per-week"])
    df=df.drop(index='<=50K')
    df2=df2.set_index('hours-per-week')
    df2=df2.loc[min_work_hours]
    df=df.set_index('hours-per-week')
    df=df.loc[min_work_hours]
    num_min_workers = None

    rich_percentage = (len(df)/len(df2))*100

    # What country has the highest percentage of people that earn >50K?
    df = pd.read_csv("adult.data.csv",index_col="salary")
    df2=pd.read_csv("adult.data.csv",index_col="salary")
    df=df.filter(items=["native-country","salary"])
    df2=df2.filter(items=["native-country"])
    df["index"]=1
    df2["index"]=1
    df=df.drop(index="<=50K")
    df=df.groupby("native-country").sum()
    df2=df2.groupby("native-country").sum()
    df=(df/df2)*100
    df=df.sort_values('index',ascending=False)
    df=df.to_dict()
    for i in df.values():
        for j in i:
            highest_earning_country=j
            break
    
    e=df['index'][highest_earning_country]
    # e=str(e)
    # ee=e[:6]
    highest_earning_country_percentage = float("{:.1f}".format(e))

    # Identify the most popular occupation for those who earn >50K in India.
    df=pd.read_csv("adult.data.csv",index_col="salary")
    df=df.filter(items=["occupation","native-country","salary"])
    df=df.drop(index="<=50K")
    df=df.set_index(['native-country'])
    df=df.loc["India"]
    df["index"]=1
    df=df.set_index(['occupation'])
    df=df.groupby("occupation").sum()
    df=df.sort_values('index',ascending=False)
    df=df.to_dict()
    for i in df.values():
      for j in i:
        top_IN_occupation=j
        break

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
