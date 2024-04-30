from bs4 import BeautifulSoup
import requests
import csv

# Create a variable that sends HTTP requests to acquire data from designated site.
source = requests.get('https://kworb.net/spotify/artist/15iVAtD3s3FsQR4w1v6M0P_songs.html').text

# Create variable that uses BeautifulSoup function to pull data with preferred parser.
soup = BeautifulSoup(source, 'html.parser')

# Define variable "table"; this will use the previously established soup varible and the find_all function to find all the tables on a webpage.
    # * NOTE * = we set the index for our table to 1, as we are targeting a specific table on our webpage.

table = soup.find_all('table')[1]

# Define variable "table_row"; this will find all "tr" (a specific html tag) within the table selected.

table_row = table.find_all('tr')

# Create a CSV writer; filename sets the files name.
filename = 'music.csv'
# Create variable f; this variable will open the targeted file and write onto it (as designated by the 'w').
f = open(filename, 'w', newline= '')
# Create variable music; we will use this variable to write/format what we wish onto the file.
music = csv.writer(f)
# Here using the function writerow, we are creating three distinct columns. 
music.writerow(['Song Title', 'Overall Streams', 'Daily Streams'])
# Create a for loop; this will allow us to iterate through the table_row, aiming to find all td (a specific html tag) for every tr that is present within the table_row in the targeted table. 
for tr in table_row:
    td = tr.find_all('td')
    row = ([tr.text.strip() for tr in td])
    # if the row is blank, we wish to go over it, thus delineate this as if the row is empty to skip past it.
    if row == []:
        continue
        # Assign the extracted td to the specified columns; use the text.strip function to remove excess information. Moreover, we use the previously established music variable and writerow to write this onto the CSV in its designated column.
    if td:
            song_title = td[0].text.strip()
            overall_streams = td[1].text.strip()
            daily_streams = td[2].text.strip()
            music.writerow([song_title, overall_streams, daily_streams])
    print(row)

    print()
# Ensure you close the targeted file once the writing process is completed.
f.close()
