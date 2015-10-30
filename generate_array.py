import glob, os
os.chdir("./imgs")
filesname = ""
for file in glob.glob("*.png"):
    filesname += '"' + str(file) + '",' 
print filesname    