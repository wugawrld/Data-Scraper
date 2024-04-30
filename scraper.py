from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://kworb.net/spotify/artist/15iVAtD3s3FsQR4w1v6M0P_songs.html').text

soup = BeautifulSoup(source, 'html.parser')

table = soup.find_all('table')[1]
table_row = table.find_all('tr')

filename = 'music.csv'
f = open(filename, 'w', newline= '')
music = csv.writer(f)

music.writerow(['Song Title', 'Overall Streams', 'Daily Streams'])

for tr in table_row:
    td = tr.find_all('td')
    row = ([tr.text.strip() for tr in td])
    if row == []:
        continue
    if td:
            song_title = td[0].text.strip()
            overall_streams = td[1].text.strip()
            daily_streams = td[2].text.strip()
            music.writerow([song_title, overall_streams, daily_streams])
    print(row)

    print()

f.close()
