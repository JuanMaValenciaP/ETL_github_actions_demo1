# import requests
# import pandas as pd
# import datetime as dt

# def download_data():
#     url = "https://jsonplaceholder.typicode.com/posts"
#     response = requests.get(url)
#     data = response.json()
#     df = pd.DataFrame(data)
#     return df

# def save_data(df, filename="data", format='.csv'):
#     saving_date = dt.datetime.now().strftime('%Y%m%d-%H%M%S')
#     df.to_csv(filename, index=False)

# def main():
#     data = download_data()
#     # save_data(data, 'data_from_api.csv')

# if __name__ == "__main__":
#     main()
#     ##afkjaskdas

print ('saludos desde github actions JMVP')