import os
import random
#creates a secret message to decode




def rename_files():
    # get filenames from a folder
    file_list = os.listdir(r"C:\Users\EQHinson\Documents\Python\udacity\alphabet")
    
    print file_list
    saved_path =os.getcwd()
    print saved_path
    os.chdir(r"C:\Users\EQHinson\Documents\Python\udacity\alphabet")

    # for each file, rename filename
    for file_name in file_list:
              
        os.rename(file_name, (str(random.randint(1,99)) + file_name)) 
    
    print file_list
    
        
    os.chdir(saved_path)
rename_files()
