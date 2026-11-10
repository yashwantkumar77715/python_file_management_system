
from pathlib import Path

def createfile():
    try:
        name = input("name of the file you want to create : ")
        path= Path(name)
        if not path.exists():
            with open(path, "w") as fs:
                data=input("what do you want to write :- ")
                fs.write(data)
            print("file created successfully")
        else:
            print(" file already exists")
    except Exception as err:
        print(f"an error occured as {err}")


def readfile():
    try:
        name= input("Enter the file name you want to read : -")
        path=Path(name)
        if path.exists():
            with open(path, "r") as fs:
               content=fs.read()
               print(f"your file content is \n {content}")
        else:
            print("No such file exists")
    except Exception as err:
        print(f"an error occured as {err}")        


def updatefile():
    try:
        name = input("tell me file name which you want to update : ")
        path=Path(name)
        if path.exists():
            print("Operations ")
            print("1 . Renaming the file")
            print("2 . Appending the file")
            print("3 . Overwriting the file")
            user_command= int(input("enter the operation number you want to perform : "))
            if user_command == 1:
                new_name = input("tell new file name : ")
                new_path =Path(new_name)
                if not new_path.exists():
                    path.rename(new_path)
                    print("file renamed successfully")
                else:
                    print("file already exixts")
            elif user_command == 2:
                with open(path,"a") as fs:
                    data = input("what do you want append : ")
                    fs.write("\n "+data)
                print("successfully appended")
            elif user_command == 3:
                with open(path , "w") as fs:
                    data=input("enter the data you want to overwrite in the file : ")
                    fs.write("\n "+data)
                print("sucessfully overwrite")
        else :
            print("the file name you have entered not exixts in your system")
    except Exception as err:
        print(f"An error occured as {err}")



def deletefile():
    try:
        name = input("Enter the file name you want to delete : ")
        path = Path(name)
        if path.exists() and path.is_file():
            confirm = input("Are you sure you want to delete this file? (yes/no) : ")
            if confirm.lower() == "yes":
                path.unlink()
                print("file deleted successfully")
            else:
                print("Deletion Cancelled")
        else:
            print("File does not exist")
    except Exception as err:
        print("An error occured: {err}")
            


print("Type 1 to create file")
print("Type 2 to read file")
print("Type 3 to update file")
print("Type 4 to delete file")

user_command = int(input("please select which action do you want perform : "))

if user_command == 1:
    createfile()
elif user_command == 2:
    readfile()
elif user_command == 3:
    updatefile()
elif user_command == 4:
    deletefile()
else:
    print("Invalid command kindly chhose option correctly ")