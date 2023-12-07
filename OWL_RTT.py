import pandas as pd

node_names = ["STAR","MAX","MICH","MASS","UTAH","NCSA","UCSD","FIU","CLEM","CERN" ]

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('PTP_slice_All_202311182114.csv')

# Group the data by source and destination, then calculate mean and median time for each group
result = df.groupby(['Source', 'Destination']).agg({'Latency': ['mean', 'median', 'std']}).reset_index()

# Print the results
print(result)