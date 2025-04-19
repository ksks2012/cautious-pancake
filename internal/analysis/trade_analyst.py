import pandas as pd

players1 = "250411"
players2 = "250420"

def compare_trade_data():
    df1 = pd.read_csv(f'./var/trade_data_{players1}.csv', encoding='utf-8-sig')
    df2 = pd.read_csv(f'./var/trade_data_{players2}.csv', encoding='utf-8-sig')

    # Display the initial number of records
    print(f"Number of records in the first dataset: {len(df1)}")
    print(f"Number of records in the second dataset: {len(df2)}")

    # Define the columns used to identify duplicate players
    # Assume that "Name" and "Height" uniquely identify a player
    unique_columns = ['Name', 'Salary']

    merge_trade_data(df1, df2, unique_columns)
    filter_trade_data(df1, df2, unique_columns)

def merge_trade_data(df1, df2, unique_columns):
    # Combine the two DataFrames
    combined_df = pd.concat([df1, df2], ignore_index=True)

    # Check the total number of records after combining
    print(f"Total number of records after combining: {len(combined_df)}")

    # Remove duplicate players
    # keep='first' means keeping the first occurrence; you can change it to 'last' or other logic
    deduplicated_df = combined_df.drop_duplicates(subset=unique_columns, keep='first')

    # Check the number of records after deduplication
    print(f"Number of records after deduplication: {len(deduplicated_df)}")

    # If you need to check which players are duplicates
    duplicates = combined_df[combined_df.duplicated(subset=unique_columns, keep=False)]
    if not duplicates.empty:
        print("\nDetected duplicate players:")
        print(duplicates[['Name', 'Team', 'Height', 'RT']])

    # Save the deduplicated results to a new CSV file
    deduplicated_df.to_csv('./var/trade_data_deduplicated_players.csv', index=False, encoding='utf-8-sig')


def filter_trade_data(df1, df2, unique_columns):
    # Convert the unique identifier columns of df1 to a set for faster lookup
    df1_keys = set(df1[unique_columns].apply(tuple, axis=1))

    # Filter df2 to keep players not present in df1
    filtered_df2 = df2[~df2[unique_columns].apply(tuple, axis=1).isin(df1_keys)]

    # Check the number of records after filtering
    print(f"Number of records in players2.csv after filtering: {len(filtered_df2)}")

    # If you need to check the players that were removed
    removed_players = df2[df2[unique_columns].apply(tuple, axis=1).isin(df1_keys)]
    if not removed_players.empty:
        print("\nPlayers removed from players2.csv (found in players1.csv):")
        print(removed_players[['Name', 'Team', 'Height', 'RT']])

    # Save the filtered results to a new CSV file
    filtered_df2.to_csv('./var/trade_data_filtered_players2.csv', index=False, encoding='utf-8-sig')

if __name__ == "__main__":
    compare_trade_data()