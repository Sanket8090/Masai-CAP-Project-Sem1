from pytube import YouTube
import instaloader
def instagram():
    ig=instaloader.Instaloader()
    db=input("Enter the instagram id:")
    ig.download_profile(db,profile_pic_only=True)



def Download(link):
    youtubeObject=YouTube(link)
    youtubeOBJECT=youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed succesfully")
link= input("https://instagram.com/virat.kohli")
Download(link)

choose=("Enter 1 for instagram operators and 2 for youtube :")
if choose=="1":
    instagram()
else:
    link= input ("https://youtu.be/T2wCuBre0oU")
    Download(link)