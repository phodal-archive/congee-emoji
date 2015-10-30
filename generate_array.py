import glob, os
os.chdir("./images")
filesname = ""
for file in glob.glob("*.png"):
    filesname += '"' + str(file) + '",' 
print filesname    