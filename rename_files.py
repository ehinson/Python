import os



def rename_files():
    # get filenames from a folder
    file_list = os.listdir(r"C:\Users\EQHinson\Documents\Python\udacity\alphabet")
    #print file_list
    saved_path =os.getcwd()
    print saved_path
    os.chdir(r"C:\Users\EQHinson\Documents\Python\udacity\alphabet")

    # for each file, rename filename
    for file_name in file_list:
        print "Old file name is " + file_name
        print "New file name is " + file_name.translate(None, "01234567989")
        os.rename(file_name, file_name.translate(None, "01234567989"))
        
        
    os.chdir(saved_path)
rename_files()
