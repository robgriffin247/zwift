# Zwift Material

This directory contains material related to Zwift such as dropshop data, speed testing data, associated code, figures and other outputs.

### Speed Testing 

Speed tests are performed to test different equipment (frames and wheels from the in game dropshop), rider profiles (height, weight) and ride parameters (power, cadence etc.). Data is uploaded from Zwift to Strava. Tests are logged in `data/test_log.csv` with the id coming from the strava activity url. A python script (`get_segment_times.py`) collects the segment times for the activities logged in `data/test_log.csv` and outputs them to `data/segment_times.csv`.