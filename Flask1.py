from flask import Flask, render_template, request, send_file
import pandas as pd
from googleapiclient.discovery import build
import re

app = Flask(__name__)

# YouTube API key
api_key = '#Your API Key' #Enter your API key
youtube = build('youtube', 'v3', developerKey=api_key)

# Channel name to ID mapping
channel_ids = {
    # Add channel IDs here...
}

# Course domains for URL extraction
course_domains = [
    #Add Domain URLs
]

# Function to get channel statistics (your existing function)
def get_channel_stats(youtube, channel_ids):
    alldata = []
    request = youtube.channels().list(
        part='snippet,contentDetails,statistics',
        id=','.join(channel_ids)
    )
    response = request.execute()

    for i in range(len(response['items'])):
        data = dict(
            Channel_name=response['items'][i]['snippet']['title'],
            Subscribers=response['items'][i]['statistics']['subscriberCount'],
            Views=response['items'][i]['statistics']['viewCount'],
            TotalVideos=response['items'][i]['statistics']['videoCount'],
            Playlist_id=response['items'][i]['contentDetails']['relatedPlaylists']['uploads']
        )
        alldata.append(data)
    return alldata

# Function to get video IDs from the playlist
def get_video_ids(youtube, playlist_id):
    video_ids = []
    request = youtube.playlistItems().list(
        part='contentDetails,snippet',
        playlistId=playlist_id,
        maxResults=50
    )
    response = request.execute()

    while 'items' in response:
        for item in response['items']:
            video_ids.append(item['contentDetails']['videoId'])

        if 'nextPageToken' in response:
            request = youtube.playlistItems().list(
                part='contentDetails,snippet',
                playlistId=playlist_id,
                maxResults=50,
                pageToken=response['nextPageToken']
            )
            response = request.execute()
        else:
            break

    return video_ids

# Function to get video details
def get_video_details(youtube, video_ids, course_domains):
    all_video_stats = []

    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part='snippet,statistics,contentDetails',
            id=','.join(video_ids[i:i + 50])
        )
        response = request.execute()

        for video in response['items']:
            video_stats = dict(
                Video_URL=f'https://www.youtube.com/watch?v={video["id"]}',
                Title=video['snippet']['title'],
                Description=video['snippet']['description'],
                Keywords=video['snippet'].get('tags', []),
                Published_date=video['snippet']['publishedAt'],
                Views=video['statistics']['viewCount'],
                Likes=video['statistics'].get('likeCount', 0),
                Favourites=video['statistics']['favoriteCount'],
                Comments=video['statistics'].get('commentCount', 0),
                Duration=video['contentDetails']['duration'],
                Course_URL=" "
            )

            # Extract duration format (e.g. PT15M33S -> 15m33s)
            duration = video_stats['Duration']
            duration = duration.replace('PT', '').lower()
            video_stats['Duration'] = duration

            # Extract course URLs from description
            pattern = r'(https?://\S+)'
            match = re.search(pattern, video_stats['Description'])
            if match:
                url = match.group(1)
                if any(domain in url for domain in course_domains):
                    video_stats['Course_URL'] = url

            all_video_stats.append(video_stats)

    return all_video_stats

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        channel_name = request.form['channel_name']
        if channel_name in channel_ids:
            channel_id = channel_ids[channel_name]

            # Get YouTube data for the requested channel
            channel_stats = get_channel_stats(youtube, [channel_id])
            playlist_id = channel_stats[0]['Playlist_id']
            video_ids = get_video_ids(youtube, playlist_id)
            video_details = get_video_details(youtube, video_ids, course_domains)

            # Save data to an Excel file
            excel_file = f"{channel_name}_data.xlsx"
            video_data = pd.DataFrame(video_details)
            video_data.to_excel(excel_file, index=False)

            # Send the file back as a downloadable response
            return send_file(excel_file, as_attachment=True)
        else:
            return "Channel not found. Please try again."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
