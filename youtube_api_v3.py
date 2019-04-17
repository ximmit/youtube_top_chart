api_key="AIzaSyCzk1hhI8kg0HCL1fMHJTQQZf10bgkzDm8"
from apiclient.discovery import build
youtube=build('youtube','v3', developerKey=api_key)
type(youtube)
req=youtube.search().list(part="snippet",order="viewCount",type='video')
res=req.execute()
res