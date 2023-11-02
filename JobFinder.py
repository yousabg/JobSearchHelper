import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt


def add_internship(df, company):
    title = input("Enter the title of the position: ")
    date = datetime.now().strftime('%Y-%m-%d')
    status = 'Applied'

    new_row = {'Company': company, 'Title': title, 'Date': date, 'Status': status}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv('jobs.csv', index=False)
    print("Internship details added successfully!")


def remove_internship(df, company):
    company_df = df[df['Company'] == company]
    if len(company_df) > 1:
        print("You applied for the following positions at " + company + ":")
        for title in company_df['Title']:
            print(title)
        title = input("Which one would you like to remove?")
        df = df[~((df['Company'] == company) & (df['Title'] == title))]
        df.to_csv('jobs.csv', index=False)
    else:
        df = df[~(df['Company'] == company)]
        df.to_csv('jobs.csv', index=False)


def update_internship(df, company):
    company_df = df[df['Company'] == company]
    if len(company_df) > 1:
        print("You applied for the following positions at " + company + ":")
        for title in company_df['Title']:
            print(title)
        title = input("Which one would you like to update?")
        new_status = input("What is the new status of " + title + "? (It is recommended to use the same terms)")
        df.loc[(df['Company'] == company) & (df['Title'] == title), 'Status'] = new_status
        df.to_csv('jobs.csv', index=False)
    else:
        title = df.loc[0, 'Title']
        new_status = input("What is the new status of " + title + "?")
        df.loc[(df['Company'] == company) & (df['Title'] == title), 'Status'] = new_status
        df.to_csv('jobs.csv', index=False)


def graph_results(df):
    plt.figure(figsize=(10, 8))
    plt.hist(df['Status'])

def track_status(df, company):
    company_df = df[df['Company'] == company]
    print("You applied for the following positions at " + company + ":")
    for title, status in zip(company_df['Title'], company_df['Status']):
        print(title)
        print("Status: " + status)


if __name__ == '__main__':
    if not os.path.isfile('jobs.csv'):
        df = pd.DataFrame(columns=['Company', 'Title', 'Date', 'Status'])
        df.to_csv('jobs.csv', index=False)
    df = pd.read_csv('jobs.csv')
    menu = """
    Options:
    0 - Add a new position
    1 - Delete a position
    2 - Update the status of a position
    3 - Graph the status of your applications
    4 - Track the status of your applications
    5 - Check how many jobs you've applied to
    """
    print(menu)
    response = input("Please enter the number of what you would like to do: ")

    if response == "0":
        company = input("What company do you want to add a position for?")
        add_internship(df, company)
    elif response == "1":
        company = input("What company do you want to remove a position for?")
        remove_internship(df, company)
    elif response == "2":
        company = input("What company do you want to update a position for?")
        update_internship(df, company)
    elif response == "3":
        graph_results(df)
        plt.show()
    elif response == "4":
        company = input("What company do you want to track an application for?")
        track_status(df, company)
    elif response == "5":
        print (len(df))
