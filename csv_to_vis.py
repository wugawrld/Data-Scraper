import matplotlib.pyplot as plt
import pandas as pd
import locale

locale.setlocale(locale.LC_ALL, '')

df = pd.read_csv('music.csv') # Creating variable to read CSV 

df.dropna(subset=['Daily Streams'], inplace=True) # Appending additonal function to variable to drop rows (ignore essentially) that are missing integer values 

# Ensuring the conversion of Overall & Daily Streams to numeric types

df['Overall Streams'] = df['Overall Streams'].str.replace(',', '').astype(int)
df['Daily Streams'] = df['Daily Streams'].str.replace(',', '').astype(int)

# Predetermining amount of songs selected
df_subset = df.head(15)

song_title = df_subset['Song Title']
overall_streams = df_subset['Overall Streams']
daily_streams = df_subset['Daily Streams']

# Sort the overall streams data in descending order and reset index
sorted_overall_streams = overall_streams.sort_values(ascending=False).reset_index(drop=True)

plt.figure(figsize=(15, 8))  # Setting custom size of figure

# Plot the scatter plot using sorted indices
plt.scatter(range(len(sorted_overall_streams)), sorted_overall_streams, color='b', label='Overall Streams')
plt.scatter(range(len(sorted_overall_streams)), daily_streams, color='r', label='Daily Streams')

plt.xlabel('Songs', fontweight='bold', fontsize=10)
plt.ylabel('Streams', fontweight='bold', fontsize=10)

# Defining tick labels
sorted_song_title = song_title[overall_streams.argsort()][::-1]  # Reorder song titles based on sorted indices
plt.xticks(range(len(sorted_overall_streams)), sorted_song_title, rotation=90, fontsize=5)

# Assigning the numerical value to each plot [Annotation]
for i in range(len(song_title)):
    overall_y = sorted_overall_streams[i]
    daily_y = daily_streams.iloc[i]

    # Determining the neighboring height of annotations
    avg_height = (overall_y + daily_y) / 2 

    # Offsetting the annotations to prevent overlap
    offset = 15 if daily_y > overall_y else -15

    # Format the presentation of numbers (show place value commas)
    overall_streams_label = locale.format_string("%d", overall_streams.iloc[i], grouping=True)
    daily_streams_label = locale.format_string("%d", daily_streams.iloc[i], grouping=True)

    plt.text(i, sorted_overall_streams[i], overall_streams_label, fontsize=8, ha='center', va='bottom', color='blue', fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', pad=1))
    plt.text(i, daily_streams.iloc[i], daily_streams_label, fontsize=8, ha='center', va='bottom', color='red', fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', pad=1))


# Legend Adjustment
plt.legend(loc='upper right', bbox_to_anchor=(1.25, 1))

plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)  # Adjust the margins

plt.show()
