# add your code here
import pandas as pd
reviews=pd.read_csv('data/winemag-data-130k-v2.csv.zip', compression='zip',index_col=0)
data=reviews.groupby('country').agg(count=('description','size'),average_points=('points','mean')).reset_index()
data['average_points']=data['average_points'].round(1)
newdata=data.sort_values(by='count', ascending=False)
print(newdata)
newdata.to_csv('reviews-per-country.csv',index='false')

