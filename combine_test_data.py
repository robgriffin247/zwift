import pandas as pd

test_log = pd.read_csv('data/test_log.csv')
segment_times = pd.read_csv('data/segment_times.csv')

main = test_log.merge(segment_times, on='activity')

main['ms'] = main['distance'] / main['time']

main['kmh'] = 3600 * main['ms'] / 1000

segment_means = main.groupby(['frame', 'wheels', 'watts', 'weight', 'height', 'cadence', 'world', 'segment']).mean(['kmh']).reset_index().drop(columns=['activity', 'zwift_version', 'distance', 'ms'])

segment_means.to_csv('data/test_times.csv')

