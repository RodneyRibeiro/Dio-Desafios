import pandas as pnd

url = 'https://community.alteryx.com/pvsmt99345/attachments/pvsmt99345/weeklychallenge/109208/2/words.csv'
sf = pnd.read_csv(url)
sf.head()
print(f'{sf}\n')
print(sf.head())