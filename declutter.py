import os
import shutil
import datetime
folderPath=input("Enter Path Of Folder You Want To Declutter:\nPress d to have the default download directory on windows.\n")
if folderPath.lower()=="d":
    from pathlib import Path
    folderPath=os.path.join(Path.home(), "Downloads")
os.chdir(folderPath)
_allfiles=os.listdir()
allfiles=[]
now=datetime.datetime.now()
for i in _allfiles:
    mtime=datetime.datetime.fromtimestamp(os.path.getmtime(i))
    if (now-mtime).days<5:
        continue
    else:
        allfiles.append(i)

print("""

           88                                   88
           88                                   ""
           88
 ,adPPYba, 88  ,adPPYba, ,adPPYYba, 8b,dPPYba,  88 8b,dPPYba,   ,adPPYb,d8
a8"     "" 88 a8P_____88 ""     `Y8 88P'   `"8a 88 88P'   `"8a a8"    `Y88
8b         88 8PP\"\"\"\"\"\"\" ,adPPPPP88 88       88 88 88       88 8b       88
"8a,   ,aa 88 "8b,   ,aa 88,    ,88 88       88 88 88       88 "8a,   ,d88
 `"Ybbd8"' 88  `"Ybbd8"' `"8bbdP"Y8 88       88 88 88       88  `"YbbdP"Y8
                                                                aa,    ,88
                                                                 "Y8bbdP"
""")

applications=["msi","exe","iso"]
archives=["zip","7z","rar","tar","gz"]
music=["mp3","wav","ogg"]
videos=["mp4","avi","mkv","m4v","webm"]
projects=["psd",]
documents=["pdf","doc","docx","epub","odt"]
pictures=["jpeg","jpg","png","gif","svg"]
html=["webp","html","htm"]
sheetandppt=["csv","xlsx","pptx","ppt","tsv","ods","odp"]
code=["py","c","cpp","ipynb","json","m","s","v","brd"]
text=["txt","md",]
filetypes=applications+archives+music+videos+projects+documents+pictures+html+sheetandppt+text+code


if not os.path.exists("Applications"):
    os.mkdir("Applications")
if not os.path.exists("Archives"):
    os.mkdir("Archives")
if not os.path.exists("Music"):
    os.mkdir("Music")
if not os.path.exists("Videos"):
    os.mkdir("Videos")
if not os.path.exists("Projects"):
    os.mkdir("Projects")
if not os.path.exists("Documents"):
    os.mkdir("Documents")
if not os.path.exists("Pictures"):
    os.mkdir("Pictures")
if not os.path.exists("Html"):
    os.mkdir("Html")
if not os.path.exists("Sheetandppt"):
    os.mkdir("Sheetandppt")
if not os.path.exists("Codes"):
    os.mkdir("Codes")
if not os.path.exists("Texts"):
    os.mkdir("Texts")

total=len(allfiles)
done=0
percentages=[1,2,3,4,5,6,7,8,9,]

for i in allfiles:
    try:
        ext=i.split(".")[-1].lower()
        if ext not in filetypes:
            continue
        else:
            if ext in applications:
                    shutil.move(i,"Applications")
            if ext in archives:
                    shutil.move(i,"Archives")
            if ext in music:
                    shutil.move(i,"Music")
            if ext in videos:
                    shutil.move(i,"Videos")
            if ext in projects:
                    shutil.move(i,"Projects")
            if ext in documents:
                    shutil.move(i,"Documents")
            if ext in pictures:
                    shutil.move(i,"Pictures")
            if ext in html:
                    shutil.move(i,"Html")
            if ext in sheetandppt:
                    shutil.move(i,"Sheetandppt")
            if ext in code:
                    shutil.move(i,"Codes")
            if ext in text:
                    shutil.move(i,"Texts")

        done+=1
    except:
        continue
    percent=(done*10)//total
    if percent in percentages:
        print("\r{}% Done.".format(percent*10))
        percentages.remove(percent)
print(f"ALl your files older than 5 days in {folderPath} has been decluttered successfully. Enjoy!🥳")
print("{} files moved out of {} files.".format(done,total))
