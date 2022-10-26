"""This class is to handle the log.txt file"""
from Modules import DatetimeReturn

class loggings():

  ## Text_Writer handles the data from default settings model
  ## the one that is edited for the performance of the system by the developer
  def Text_writer(self,ques, ans):
    try:
      f = open("files/Logs.txt","a",encoding="utf-8")
    except:
      return "Logs not added, No file of such name found"
    d = DatetimeReturn()
    f.write(f"{d} :")
    f.write("\nHuman: " + ques)
    f.write("\nBot: " + ans)
    f.write("\n=========================================\n")

    return f"Logs added at {d}"

  ## Text_writer2 handles the data recieved from Custom entries html file.
  def Text_writer2(self,ans,ques):
    try:
      f = open("files/Logs2.txt","a",encoding="utf-8")
    except:
      return "Logs not added, No file of such name found"
    f.write(f"{DatetimeReturn()} :")
    f.write("\n"+ques+" "+ans)
    f.write("\n============================================\n")
    
    return f"Logs added at {DatetimeReturn()}"


  ## Text_reader and Clearer are for the admin page to use. In case the person with the credentials wants to access logs or clear them through HTML link instead of accessing the server and do it manually

  def Text_reader(self):
    try:
      f = open("files/Logs.txt","r+")
    except:
      return "Logs not cleared, No file of such name found" 
    logs = f.read()
    return logs

  def Clearer(self):
    try:
      f = open("files/Logs.txt","w+")
    except:
      return "Logs not cleared, No file of such name found"
    f.truncate(0) 
    return "Logs Cleared"