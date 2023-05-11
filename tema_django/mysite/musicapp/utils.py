import requests

YOUTUBE_API_KEY = 'AIzaSyA55dfg7WEcPMiCTVf2J_egdI9oTb2o2_A'

def search_youtube(query):
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={query}&type=video&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data['items']:
        video_id = data['items'][0]['id']['videoId']
        return f"https://www.youtube.com/embed/{video_id}"
    else:
        return None
