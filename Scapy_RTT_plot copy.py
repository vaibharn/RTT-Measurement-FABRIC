import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Scapy_TCP_RTT.csv')
print(df)

df.plot(x='SITES', y='RTT(ms)', kind='barh', legend=False)

# Adding labels and title
plt.xlabel('SITES')
plt.ylabel('RTT(ms)')
plt.title('Scapy TCP RTT')

# Display the plot
plt.show()

print(df['RTT(ms)'])

