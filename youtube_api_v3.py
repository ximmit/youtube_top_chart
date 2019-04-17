import datetime
from apiclient.discovery import build
api_key="AIzaSyCzk1hhI8kg0HCL1fMHJTQQZf10bgkzDm8"
youtube=build('youtube','v3', developerKey=api_key)
type(youtube)
req=youtube.search().list(part="snippet",order="viewCount",type='video',maxResults=1,publishedAfter='2018-06-01T00:00:00Z')
res=req.execute()
print(res)