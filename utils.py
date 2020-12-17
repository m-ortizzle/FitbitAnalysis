import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import requests
import json
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing

def create_pie_chart(x, y, title, color_scheme):
    plt.pie(y, labels=x, autopct="%1.1f%%", colors=color_scheme)
    plt.title(title)
    plt.show()

def create_bar_chart(x, y, xlabel, ylabel, graph_color):
    plt.bar(x, y, color=graph_color)
    plt.xticks(rotation=45, horizontalalignment="right")
    plt.title("Average " + str(ylabel) + " by " + str(xlabel))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
def create_mean_series(grouped_df, column):
    mean_ser = pd.Series(dtype=float)
    for group_name, group_df in grouped_df:
        mean = group_df[column].mean()
        mean_ser[str(group_name)] = mean
    return mean_ser

def create_scatter_plot(x, y, xlabel, ylabel):
    plt.scatter(x, y)
    plt.xticks(rotation=45, horizontalalignment="right")
    plt.title(str(ylabel) + " by " + str(xlabel))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

def create_avg_ser(df):
    avg_ser = pd.Series(dtype=float)
    for column in df:
        mean = df[column].mean()
        avg_ser[column] = mean
    avg_ser.drop(labels=["Calories Burned", "Steps", "Distance", "Activity Calories", "Minutes Total Activity"], inplace=True)
    return avg_ser

def avg_activity(ser, days):
    avg_activity = 0 
    for day in days:
        avg_activity = avg_activity + ser[day]
    avg_activity = avg_activity / len(days)
    return avg_activity
    
def get_temps():
    api_key = "CvdJRosglIDZZ6I1LIIWXVP8V6cQMTnO"
    headers = {"x-api-key": api_key}
    spokane_id = "72785"
    url = "https://api.meteostat.net/v2/stations/daily"
    url += "?station=" + spokane_id 
    url += "&start=2020-08-01&end=2020-10-31"
    response = requests.get(url=url, headers=headers)
    json_object = json.loads(response.text)
    data_object = json_object["data"]
    max_temps = []
    for date_object in data_object:
        high_temp = date_object["tmax"] * (9 / 5) + 32 # convert C to F
        max_temps.append(high_temp)
    return max_temps
    
def convert_categoricals(df, column, labels):
    le = preprocessing.LabelEncoder()
    le.fit(labels)
    list(le.classes_)
    df[column] = le.transform(df[column])
    return df

def scale_split(x, y):
    scaler = MinMaxScaler()
    x = scaler.fit_transform(x)
    X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)
    return X_train, X_test, y_train, y_test

