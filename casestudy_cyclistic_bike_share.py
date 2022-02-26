# -*- coding: utf-8 -*-
"""CaseStudy_Cyclistic-bike-share.ipynb"""

from google.colab import drive
drive.mount('/content/drive')

#Import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Importing the files
case_file_1 = pd.read_csv("/content/drive/MyDrive/data_case study/202007-divvy-tripdata.csv")
case_file_2 = pd.read_csv("/content/drive/MyDrive/data_case study/202008-divvy-tripdata.csv")
case_file_3 = pd.read_csv("/content/drive/MyDrive/data_case study/202009-divvy-tripdata.csv")
case_file_4 = pd.read_csv("/content/drive/MyDrive/data_case study/202010-divvy-tripdata.csv")
case_file_5 = pd.read_csv("/content/drive/MyDrive/data_case study/202011-divvy-tripdata.csv")
case_file_6 = pd.read_csv("/content/drive/MyDrive/data_case study/202012-divvy-tripdata.csv")
case_file_7 = pd.read_csv("/content/drive/MyDrive/data_case study/202101-divvy-tripdata.csv")
case_file_8 = pd.read_csv("/content/drive/MyDrive/data_case study/202102-divvy-tripdata.csv")
case_file_9 = pd.read_csv("/content/drive/MyDrive/data_case study/202103-divvy-tripdata.csv")
case_file_10 = pd.read_csv("/content/drive/MyDrive/data_case study/202104-divvy-tripdata.csv")
case_file_11 = pd.read_csv("/content/drive/MyDrive/data_case study/202105-divvy-tripdata.csv")
case_file_12 = pd.read_csv("/content/drive/MyDrive/data_case study/202106-divvy-tripdata.csv")

# Merging all the dataframes into a single dataframe.

all_dfs = [case_file_1, case_file_2, case_file_3, case_file_4, case_file_5, case_file_6, case_file_7, case_file_8, case_file_9, case_file_10, case_file_11, case_file_12]
case_file = pd.concat(all_dfs)
df = case_file

# Reading the merged file

case_file_5000 = df
case_file_5000

# To get information about the dataframe.
case_file_5000.info()

#To convert object data type of start_time and end_time columns into datetime data type
case_file_5000["start_time"] = pd.to_datetime(case_file_5000["started_at"])
case_file_5000["end_time"] = pd.to_datetime(case_file_5000["ended_at"])

#Adding new column - ride_length (ended_at - started_at) to calculate the time travelled
case_file_5000["ride_length"] = case_file_5000["end_time"] - case_file_5000["start_time"]
case_file_5000["ride_length"]

# To get the updated information about the changes made in the data type of dataframe.
case_file_5000.info()

# Splitting and extracting the date from "started_at" column
case_file_5000["start_date1"] = [i.split(" ")[0] for i in case_file_5000["started_at"]]
case_file_5000["start_date1"]

# Converting start_date1 into datetime data type
case_file_5000["start_date1"] = pd.to_datetime(case_file_5000["start_date1"])

# Finding the weekday of the date
case_file_5000['week_day'] = case_file_5000["start_date1"].apply(lambda x: x.weekday())
case_file_5000['week_day'].unique()

# Converting weekday values into weekday
dict1 = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
case_file_5000['week_day'] = case_file_5000['week_day'].apply(lambda y: dict1[y])
case_file_5000['week_day']

# To sort the dataframe by start date in ascending order
case_file_5000.sort_values(by=['started_at'], inplace=True, ascending=True)

# Drop all rows with any NaN values
case_file_5000_cleaned = case_file_5000.dropna()

# To save the cleaned file for further transformation of data
case_file_5000_cleaned.to_csv('cleaned.csv')

# To import the cleaned data file
cleaned_file = pd.read_csv("cleaned.csv")

# Print the cleaned dataframe
cleaned_file

# To calculate euclidean distance between start and end point.
cleaned_file["x"] = (cleaned_file["end_lat"] - cleaned_file["start_lat"])**2
cleaned_file["y"] = (cleaned_file["end_lng"] - cleaned_file["start_lng"])**2
cleaned_file["distance"] = (cleaned_file["x"] + cleaned_file["y"])**(1/2)
cleaned_file["distance"]

# To extract year and month from start date column
cleaned_file['year'] = pd.DatetimeIndex(cleaned_file["start_date1"]).year
cleaned_file['month'] = pd.DatetimeIndex(cleaned_file["start_date1"]).month

# To convert object datatype to timedelta
cleaned_file["ride_len"] = pd.to_timedelta(cleaned_file["ride_length"])

# Print the cleaned dataframe
cleaned_file

# To check if there are null values in dataframe
cleaned_file.isnull().sum()

# To check if there are any duplicate values in dataframe
cleaned_file.duplicated().any()

"""Analysis

"""

#To calculate mean of ride length of all types of users
mean_ride_length = cleaned_file["ride_len"].mean()
mean_ride_length

# Calculate the max ride_length of all types of users
max_ride_length = cleaned_file["ride_len"].max()
max_ride_length

# To calculate mean ride length for member
mean_ride_length_member = cleaned_file[cleaned_file["member_casual"] == "member"]
mean_ride_length_member = mean_ride_length_member["ride_len"].mean()
mean_ride_length_member

# To calculate mean ride length for casual riders
mean_ride_length_casual = cleaned_file[cleaned_file["member_casual"] == "casual"]
mean_ride_length_casual = mean_ride_length_casual["ride_len"].mean()
mean_ride_length_casual

# To calculate max ride length for member
max_ride_length_member = cleaned_file[cleaned_file["member_casual"] == "member"]
max_ride_length_member = max_ride_length_member["ride_len"].max()
max_ride_length_member

# To calculate max ride length for casual riders
max_ride_length_casual = cleaned_file[cleaned_file["member_casual"] == "casual"]
max_ride_length_casual = max_ride_length_casual["ride_len"].max()
max_ride_length_casual

# Calculate the mode of week_day for all types of users
mode_week_day = cleaned_file["week_day"].mode()
mode_week_day

# To calculate mode of week_day for member
mode_week_day_member = cleaned_file[cleaned_file["member_casual"] == "member"]
mode_week_day_member = mode_week_day_member["week_day"].mode()
mode_week_day_member

# To calculate mode of week_day for casual
mode_week_day_casual = cleaned_file[cleaned_file["member_casual"] == "casual"]
mode_week_day_casual = mode_week_day_casual["week_day"].mode()
mode_week_day_casual

# Calculate the number of rides for users by week_day by adding Count of ride_id to Values
dict1 = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday":5, "Saturday": 6}
cleaned_file['week_day'] = cleaned_file['week_day'].apply(lambda y: dict1[y])

count_users_week_day = cleaned_file.groupby('week_day')['ride_id'].count()
count_users_week_day = count_users_week_day.sort_index()
count_users_week_day

# Calculate the number of rides for member by week_day by adding Count of ride_id to Values
count_member_week_day = cleaned_file[cleaned_file["member_casual"] == "member"].groupby('week_day')['ride_id'].count()
count_member_week_day

# Calculate the number of rides for casual by week_day by adding Count of ride_id to Values
count_casual_week_day = cleaned_file[cleaned_file["member_casual"] == "casual"].groupby('week_day')['ride_id'].count()
count_casual_week_day

# To plot graph of Weekday Vs Number Of Rides
plt.figure(figsize = (8,6))
plt.plot(count_users_week_day.index, count_users_week_day.values)
plt.plot(count_member_week_day.index, count_member_week_day.values)
plt.plot(count_casual_week_day.index, count_casual_week_day.values)
plt.title("Calculate the number of rides for different users by week_day by adding Count of ride_id to Values")
plt.legend(["user", "member", "casual"])
labels = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
plt.xticks(count_casual_week_day.index, labels)
plt.show()

# Calculate the average ride_length for users by week_day
user_avg_ride_len_week_day = cleaned_file.groupby("week_day")['ride_len'].mean(numeric_only=False)
user_avg_ride_len_week_day

# Calculate the average ride_length for members by week_day
member_avg_ride_len_week_day = cleaned_file[cleaned_file["member_casual"] == "member"].groupby('week_day')['ride_len'].mean(numeric_only=False)
member_avg_ride_len_week_day

# Calculate the average ride_length for casual by week_day
casual_avg_ride_len_week_day = cleaned_file[cleaned_file["member_casual"] == "casual"].groupby('week_day')['ride_len'].mean(numeric_only=False)
casual_avg_ride_len_week_day

# To plot graph of Weekday Vs Average ride length
plt.plot(user_avg_ride_len_week_day/pd.Timedelta(minutes=1))
plt.plot(member_avg_ride_len_week_day/pd.Timedelta(minutes=1))
plt.plot(casual_avg_ride_len_week_day/pd.Timedelta(minutes=1))
plt.title("The average ride_length for different users by week_day")
plt.legend(["user", "member", "casual"])
labels = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
plt.xticks(user_avg_ride_len_week_day.index, labels)
plt.show()

cleaned_file

# To extract important features of the dataframe into a new dataframe
final_file = cleaned_file[["ride_id", "rideable_type", "ride_len", "week_day", "distance", "year", "month", "member_casual"]]

# To get the information of the dataframe
final_file.info()

"""data analysis

"""

# To check the number of users in each type over past 12 months
member_type = final_file["member_casual"].value_counts()
member_type

# To plot the count plot of users in each type
plt.title("count of users in each type")
plt.bar(member_type.index, member_type.values)
plt.show()

# To plot the pie chart of users in each type
plt.figure(figsize = (8,6))
plt.pie(member_type.values, labels = member_type.index, autopct='%1.1f%%')
plt.title("Percentage of users in each type")
plt.legend(member_type.index)
plt.show()

# To check the number of users over years
users_over_year = final_file.groupby('year')['member_casual'].value_counts()
users_over_year

# To segregate the number of users into member or casual riders over the years
list_year = []
list_x = []
list_y = list(users_over_year.values)
for i, j in users_over_year.index:
  list_x.append(j)
  list_year.append(str(i))

sns.barplot(list_x, list_y, hue = list_year)
plt.title("Count of Member and Casual Riders over the years")

# To check the number of users over months
users_over_month = final_file.groupby('month')['member_casual'].value_counts()
users_over_month

# To segregate the number of users into member or casual riders over the months
list_month = []
list_x = []
list_y = list(users_over_month.values)
for i, j in users_over_month.index:
  list_x.append(j)
  list_month.append(str(i))

# Plot count of Member and Casual Riders over the months
plt.figure(figsize = (18,8))
sns.barplot(list_x, list_y, hue = list_month)
plt.title("Count of Member and Casual Riders over the months")

# To check the number of users for a particulat rideable_type
ride_type = final_file.groupby("member_casual")["rideable_type"].value_counts()
ride_type

# To segregate the number of users into member or casual riders based on ride type
list_member = []
list_x = []
list_y = list(ride_type.values)
for i, j in ride_type.index:
  list_x.append(j)
  list_member.append(str(i))

# To plot number of users into member or casual riders based on ride type
plt.figure(figsize = (18,8))
sns.barplot(list_x, list_y, hue = list_member)
plt.title("Count of Member and Casual Riders over the months")
