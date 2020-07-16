import os                                   # make sure file with extension is in the same folder 
for filename in os.listdir():
    if filename.endswith('.txt'):
      # os.unlink(filename)             # this line will delete the file

        print(filename)
                                        
