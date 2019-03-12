import os
import shutil

def cataloger(src):
    dest = "/media/minrax/LinuxData/python/backup"
    for i in os.listdir(src):
        extension = os.path.splitext(i)[1][1:]
        if (extension == "db"):
            shutil.move(src+i, dest+"/"+extension)
        elif (extension == "txt"):
            shutil.move(src+i, dest+"/"+extension)
        elif (extension == "md"):
            shutil.move(src+i, dest+"/"+extension)
        elif (extension == "lock"):
            shutil.move(src+i, dest+"/"+extension)
        else:
            shutil.move(src+i, dest+"/other")

cataloger("/media/minrax/LinuxData/python/test/")
