import os

for dir_path, directories, files in os.walk(os.getcwd()):
    for i in files:
        file_path = os.path.join(dir_path, i)
        with open(file_path, "r") as missing_package:
            temp = missing_package.read()
        with open(file_path, 'w') as to_be_packaged:
            to_be_packaged.write("package " + os.path.basename(dir_path) + ";" + "\n\n" + temp)
        to_be_packaged.close()
