import pandas as pd

test_log = pd.read_csv('data/test_log.csv')
segment_times = pd.read_csv('data/segment_times.csv')

main = test_log.merge(segment_times, on='activity')

main['ms'] = main['distance'] / main['time']

main['kmh'] = 3600 * main['ms'] / 1000

print(main.groupby(['frame', 'wheels', 'watts', 'weight', 'height', 'cadence', 'segment']).mean(['kmh', 'time']))
