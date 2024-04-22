# pip install pandas CLI
import requests
import pandas as pd

# Function to fetch data from the API
def fetch_data():
    url = "https://api.balldontlie.io/v1/stats"
    response = requests.get(url)
    data = response.json()  # Parse the JSON from the response
    return data

# Function to process and display data
def display_data(data):
    # Extract the 'data' part of the JSON
    stats = data['data']
    
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(stats)
    
    # To display more information, expand the DataFrame to include nested 'player' details
    # Flatten the 'player' dictionary into the main DataFrame, prefixing columns with 'player_'
    df = df.join(pd.json_normalize(df['player']).add_prefix('player_'))
    
    # Similarly, you might want to expand the 'team' and 'game' details
    df = df.join(pd.json_normalize(df['team']).add_prefix('team_'))
    df = df.join(pd.json_normalize(df['game']).add_prefix('game_'))
    
    # Drop the original nested columns if no longer needed
    df.drop(columns=['player', 'team', 'game'], inplace=True)
    
    # Display the DataFrame
    print(df.head())  # Shows the first few rows of the DataFrame

def main():
    # Fetch the data
    data = fetch_data()
    
    # Display the data
    display_data(data)

if __name__ == "__main__":
    main()
