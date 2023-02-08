#coding=utf-8
import os
from alive_progress import alive_bar
import time
#так как переодически библиотеки отваливаются на каждом старте скрипта будет проверка
os.system("pip install -r requirements.txt --quiet")
import youtube_dl
#поиск и выдача 5 результатов с последующей их записью в base.txt
from youtubesearchpython import VideosSearch
name = input("What are you want? >> ")
videosSearch = VideosSearch(name, limit=5)
for i in range(5):
    a = (videosSearch.result(1)["result"][i]["title"])
    print (a)
    b = (videosSearch.result(1)["result"][i]["link"])
    print (b)
    enter = open("base.txt", "a")
    enter.write('\n' + str(b))
    enter.close()
    c = (videosSearch.result(1)["result"][i]["viewCount"])
    print (c)
#выбор одного из 5 вариантов
num = int(input("Choose:"))
#print(z)
with open("base.txt", "r") as f:
    text = f.readlines()
    global_link = (text[num])
#скачивание выбранного варианта
def run():
    video_url = (global_link)
    video_info = youtube_dl.YoutubeDL().extract_info(url=video_url,
                                                     download=False)
    os.system('rm base.txt')

filename = f"{video_info['title']}.mp3"
options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
   
    print("Скачал...обрабатываю {}")
    time.sleep(1)
    
    mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    with alive_bar(len(mylist)) as bar:
      for i in mylist:
        bar()
        time.sleep(1)
    os.system ('mv *.mp3 ~/*/music/')
    print("Готово! {}".format(filename))
if __name__ == '__main__':
    run()


print("╔╗╔╗╔══╗╔══╗╔╗╔══╗╔═══╗╔══╗───╔══╗─╔╗╔╗")
print("║║║║║╔╗║║╔═╝║║║╔═╝║╔══╝║╔╗╚╗──║╔╗║─║║║║")
print("║╚╝║║╚╝║║║──║╚╝║──║╚══╗║║╚╗║──║╚╝╚╗║╚╝║")
print("║╔╗║║╔╗║║║──║╔╗║──║╔══╝║║─║║──║╔═╗║╚═╗║")
print("║║║║║║║║║╚═╗║║║╚═╗║╚══╗║╚═╝║──║╚═╝║─╔╝║")
print("╚╝╚╝╚╝╚╝╚══╝╚╝╚══╝╚═══╝╚═══╝──╚═══╝─╚═╝")
print("╔═══╗╔════╗╔╗╔╗╔═══╗╔═══╗")
print("║╔═╗║╚═╗╔═╝║║║║║╔═╗║║╔══╝")
print("║╚═╝║──║║──║╚╝║║╚═╝║║╚══╗")
print("║╔══╝──║║──╚═╗║║╔══╝║╔══╝")
print("║║─────║║───╔╝║║║───║╚══╗")
print("╚╝─────╚╝───╚═╝╚╝───╚═══╝")
print("╔╗╔╗╔╗╔══╗╔════╗╔╗╔╗──╔╗──╔══╗╔╗╔╗╔═══╗")
print("║║║║║║╚╗╔╝╚═╗╔═╝║║║║──║║──║╔╗║║║║║║╔══╝")
print("║║║║║║─║║───║║──║╚╝║──║║──║║║║║║║║║╚══╗")
print("║║║║║║─║║───║║──║╔╗║──║║──║║║║║╚╝║║╔══╝")
print("║╚╝╚╝║╔╝╚╗──║║──║║║║──║╚═╗║╚╝║╚╗╔╝║╚══╗")
print("╚═╝╚═╝╚══╝──╚╝──╚╝╚╝──╚══╝╚══╝─╚╝─╚═══╝")
