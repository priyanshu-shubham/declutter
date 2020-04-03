import os
import shutil
import datetime
downloadspath="C:\\Users\\Owner\\Downloads"
#downloadspath="sample"
os.chdir(downloadspath)
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
  ||
  ||
  ||
  ||
  ||
  ||
  ||     Here you go, sweep
  ||     that up..............
 /||\\
/||||\\
======         __|__
||||||        / ~@~ \
||||||       |-------|
||||||       |_______|
""")

applications=["msi","exe"]
archives=["zip","7z","rar"]
music=["mp3",]
videos=["mp4","avi"]
projects=["psd",]
documents=["pdf","doc","docx",]
pictures=["jpeg","jpg","png","gif"]
html=["webp","html"]
sheetandppt=["csv","xlsx","pptx"]
filetypes=applications+archives+music+videos+projects+documents+pictures+html+sheetandppt


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
    except:
        continue
    done+=1
    percent=(done*10)//total
    if percent in percentages:
        print("{}% Done.".format(percent*10))
        percentages.remove(percent)
print("{} files moved.".format(done))
print(total)
