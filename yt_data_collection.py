import requests
import json
import pandas as pd

# API key and region
API_KEY = 'api_key'
REGION_CODE = 'IN'  
MAX_RESULTS = 50 

# Define the YouTube API endpoint and parameters
url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics,contentDetails&chart=mostPopular&regionCode={REGION_CODE}&maxResults={MAX_RESULTS}&key={API_KEY}"

# Make the request to the YouTube API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    trending_videos = response.json()

    yt_data = []
    
    # Print or save the trending video data
    for video in trending_videos['items']:
        id = video['id']
        title = video['snippet']['title']
        description = video['snippet']['description']
        tags = video['snippet'].get('tags', 'NA')
        viewCount = video['statistics']['viewCount']
        commentCount = video['statistics']['commentCount']
        likeCount = video['statistics'].get('likeCount', 0)
        categoryId = video['snippet']['categoryId']
        publishedAt = video['snippet']['publishedAt']
        channel_name = video['snippet']['channelTitle']
        duration = video['contentDetails']['duration']

        dict = {
            'id' : id,
            'title' : title,
            'view' : viewCount,
            'like' : likeCount,
            'comment' : commentCount,
            'category_id' : categoryId,
            'duration_ios' : duration,
            'channel_name' : channel_name,
            'description' : description,
            'tag' : tags,
            'published_at' : publishedAt
        }

        yt_data.append(dict)
    
else:
    print(f"Failed to fetch trending videos: {response.status_code}")


# export csv
df = pd.DataFrame(yt_data)
df.to_csv('yt_trending_data.csv')