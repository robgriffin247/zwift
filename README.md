# Zwift Material

This repository contains material related to Zwift including race notes, dropshop data and testing data from tests using a bot.

### Race Notes

I am gradually building a set of race notes for various routes in Zwift. The aim is to keep them concise enough to scan during a race, while getting across the key features of a route and important things to focus on during a race.

### Speed Testing 

Speed tests are performed to test different equipment (frames and wheels from the in game dropshop), rider profiles (height, weight) and ride parameters (power, cadence etc.). Data is uploaded from Zwift to Strava. Tests are logged in `data/test_log.csv` with the id coming from the strava activity url. A python script (`get_segment_times.py`) collects the segment times for the activities logged in `data/test_log.csv` and outputs them to `data/segment_times.csv`. Test log data and segment times are combined into `data/test_times.csv`.