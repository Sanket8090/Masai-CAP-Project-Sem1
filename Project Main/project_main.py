from pytube import YouTube
import instaloader
def instagram(db):
    ig=instaloader.Instaloader()
    
    ig.download_profile(db,profile_pic_only=True)



def Download(link):
    youtubeObject=YouTube(link)
    stream = youtubeObject.streams.get_highest_resolution()
    try:
        stream.download()
    except:
        print("An error has occurred")
    print("Download is completed succesfully")
link= input("Enter Link: ")
Download(link)

choose=input("Enter 1 for instagram operators and 2 for youtube :")
if choose=="1":
    db=input("Enter the instagram id:")
    instagram(db)
else:
    link= input ("Enter Link")
    Download(link)
