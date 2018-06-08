import pandas as pd
df=pd.read_csv('test2.csv')
print('read done')
import googlemaps
gmaps_key = googlemaps.Client(key = 'AIzaSyDMbN1bnCr-rT1aFVqELvAfX97PA9kujrg')


df['LAT']=None
df['LON']=None

for i in range(0,len(df),1):
    geocode_result = gmaps_key.geocode(df.iat[i,2])
    try:
        lat=geocode_result[0]['geometry']['location']['lat']
        lon=geocode_result[0]['geometry']['location']['lng']
        df.iat[i,df.columns.get_loc('LAT')]=lat
        df.iat[i,df.columns.get_loc('LON')]=lon
    except:
        lat =None
        lon =None

print('coding down')
df.to_csv('finish1.csv')
print('all done')
