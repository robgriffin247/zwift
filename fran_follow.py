#https://www.youtube.com/watch?v=sgscChKfGyg
import os
from dotenv import load_dotenv

load_dotenv()

# before starting:
# 1. install postman
# 2. make a get request 
# - to https://www.strava.com/api/v3/athlete
# - header; key = Authorization, value = Bearer <ACCESS_TOKEN>
# 3. Get the authorization code
# - navigate to (swapping in your CLIENT_ID):
# print(f"https://www.strava.com/oauth/authorize?client_id={os.getenv('CLIENT_ID')}&redirect_uri=http://localhost&response_type=code&scope=activity:read_all")
# - authorize
# - copy the code from the url between `code=` and `&scope` into .env AUTH_CODE
# 4. Exchange authorization code for access token and refresh token
# print(f"https://www.strava.com/oauth/token?client_id={os.getenv('CLIENT_ID')}&client_secret={os.getenv('CLIENT_SECRET')}&code={os.getenv('AUTH_CODE')}&grant_type=authorization_code")
# - copy the url into postman for a post request and make the request
# - copy the access token into .env
# 5. View activities using the access token
# - make a et request in postman to
# print(f"https://www.strava.com/api/v3/athlete/activities?access_token={os.getenv('ACCESS_TOKEN')}")
# 6. Use a refresh token
# print(f"https://www.strava.com/oauth/token?client_id={os.getenv('CLIENT_ID')}&client_secret={os.getenv('CLIENT_SECRET')}&refresh_token={os.getenv('REFRESH_TOKEN')}&grant_type=refresh_token")

