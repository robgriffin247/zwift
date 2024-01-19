# https://towardsdatascience.com/using-the-strava-api-and-pandas-to-explore-your-activity-data-d94901d9bfde
# https://www.youtube.com/watch?v=sgscChKfGyg
# https://www.youtube.com/watch?v=lOZFHhEtc8E
import os
from dotenv import load_dotenv
import requests
import urllib3
import pandas as pd

load_dotenv()


auth_code = os.getenv('AUTH_CODE')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
refresh_token = os.getenv('REFRESH_TOKEN')


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': client_id,
    'client_secret': client_secret,
    'refresh_token': refresh_token,
    'grant_type': "refresh_token",
    'f': 'json'
}

# Get Access Token ============================================================
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']


# Get Segment Times
header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}

test_log = pd.read_csv('data/test_log.csv')
focal_activities = list(test_log['activity'])

segment_times = pd.DataFrame({'activity':[], 'segment':[], 'time':[]})

for activity in focal_activities:
    activity_data = requests.get(f'https://www.strava.com/api/v3/activities/{activity}', headers=header, params=param).json()
    segment_data = activity_data['segment_efforts']
    for segment in segment_data:
        segment_times.loc[len(segment_times.index)] = [activity, segment['name'],segment['elapsed_time']]

segment_times.to_csv('data/segment_times.csv', index=False)