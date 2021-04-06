#! python3
# Program that sorts files into folders based on filetype
import os, shutil

# Ask user what folder needs to get sorted
unsortedFolder = input("What folder do you want to have sorted? \n")


# Variable for absolute path
absolutePath = os.path.abspath("../" + unsortedFolder)
print(absolutePath)

# Change folder to the one that needs to be sorted
changeFolder = os.chdir(absolutePath)

# List files in the folder and print it (for debugging)
print("Current working directory:\n" + os.getcwd() + "\n")
print("These are the files in the current folder:\n" + str(os.listdir(os.getcwd()))) # Print the files + convert the list to string

# Variable for the list of files
listFiles = os.listdir(os.getcwd())

# For each file split into two variables - Filename and file_ext
for file in listFiles:
    fileName, fileExtension = os.path.splitext(file)
      # if filetype is a photo -> move file to pictures
    if fileExtension == ".png" or fileExtension == ".jpg" or fileExtension == ".HEIC" or fileExtension == ".jpeg": # if the filetype is a picture
        print(fileName) # print filename 
        picturesFolder = "Pictures"
        destFolder = os.path.abspath("../" + picturesFolder) # set destination folder to Pictures
        shutil.move(file, destFolder)
    elif fileExtension == ".pdf" or fileExtension == ".csv" or fileExtension == ".rtf":
         # if the filetype is a document
        print(fileName) # print filename 
        documentsFolder = "Documents"
        destFolder = os.path.abspath("../" + documentsFolder) # set destination folder to Pictures
        shutil.move(file, destFolder)







# path = os.path.abspath("../")
# folder = "Downloads"
# finalFolder = path + "/" + folder
# print(path)
# print(os.listdir(path))
# os.chdir(path + "/" + folder)
# print(os.path.abspath(folder))

# print(os.listdir(os.getcwd()))

# filename, file_extension = os.path.splitext(finalFolder + "/" + "IMG_3317.jpg")
# print(filename)
# print(file_extension)