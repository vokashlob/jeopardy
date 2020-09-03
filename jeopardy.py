import pandas as pd

pd.set_option('display.max_colwidth', -1)

df = pd.read_csv('jeopardy.csv')
# print(df.head())
# print(df.columns)

new_col_names = []
for column_name in df.columns:
    new_col_names.append(column_name.strip())
df.columns = new_col_names


# print(df.columns)

def filter_data(data, words):
    filter = lambda x: all(word.lower() in x.lower() for word in words)
    return data[data["Question"].apply(filter)]


filtered = filter_data(df, ['King', 'England'])
# print(len(filtered))

#print(df['Value'].tail(20))

df['Float_Value'] = df['Value'].apply(lambda x: float(x[1:].replace(',', '') if x != 'None' else 0))

#print(df.head())

filtered = filter_data(df, ["King"])
print(filtered["Float_Value"].mean())