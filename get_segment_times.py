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
print('\n' + ('-'*80) + '\nRequesting Access Token...\n')
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']


# Get Segment Times
header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}

test_log = pd.read_csv('data/test_log.csv')
focal_activities = list(test_log['activity'])


if os.path.exists('data/segment_times.csv'):
    segment_times = pd.read_csv('data/segment_times.csv')
    print(f"Data already present for {len(set(segment_times['activity']))} activities.\n")
else:
    segment_times = pd.DataFrame({'activity':[], 'segment':[], 'time':[], 'distance':[]})


n_activities = len(test_log.index)
request_count = 0
for activity in focal_activities:
    if activity not in set(segment_times['activity']):
        request_count += 1
        print(f'> Requesting activity {request_count} of {n_activities} (#{activity})')
        activity_data = requests.get(f'https://www.strava.com/api/v3/activities/{activity}', headers=header, params=param).json()
        segment_data = activity_data['segment_efforts']
        for segment in segment_data:
            segment_times.loc[len(segment_times.index)] = [activity, segment['name'], segment['elapsed_time'], segment['distance']]
    
if request_count==0:
    print('No new activities to collect!')

segment_times.to_csv('data/segment_times.csv', index=False)

print(f"\nData for {len(set(segment_times['activity']))} activities output to data/segment_times.csv\n" + ("-"*80) + '\n')