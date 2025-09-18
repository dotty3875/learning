import os, shutil  # shutil is shell utility
from os import path
from zipfile import ZipFile

if path.exists("sampleFile.txt"): # if the path exists to specified file
    src = path.realpath("sampleFile.txt") # file path of the file
    dst = src + ".bak" # destination includes the filepath + any additional stuff, in this case ".bak" on the end of it when its copied
    shutil.copy(src, dst) # copies a file and its content, not its metadata

    # os.rename("sampleFile.txt", "newFile.txt") # renames the first specified file to the specified second name

    root_dir, tail = path.split(src) # splits the path (file path & src file split) - root_dir becomes the filepath, tail = the src file itself

    shutil.make_archive("archive", "zip", root_dir) # makes an archive. first parameter is the name of the archive, 2nd parameter is the type of archive, 3rd parameter is where to make it

with ZipFile("testZip.zip", "w") as newzip: # opens a zip file called "testZip.zip" using ZipFile module, opens to write
    newzip.write("sampleFile.txt") # writes this specific file to that archive
    newzip.write("sampleFile.txt.bak")

