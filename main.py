import pandas

# First, we will load all signals into Pandas DataFrames
pointA_received_signal = pandas.read_csv('data/pointA.txt', header=None)
pointB_received_signal = pandas.read_csv('data/pointB.txt', header=None)
sent_signal = pandas.read_csv('data/sent.txt', header=None)

# Time duration of each sample point in milliseconds
sample_duration = 0.001

# Allow pandas to display 1000 values while printing results
pandas.set_option('display.max_rows', 1000)

# Print a list of values in the signal received at Point A that match the sent signal
print(pointA_received_signal[pointA_received_signal[0].isin(sent_signal[0])])
