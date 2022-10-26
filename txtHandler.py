
from files.GenZtext2 import Gen2
from files.Castext2 import Cas2
from files.GenZtext import Gen
from files.Castext import Cas
from Modules import DatetimeReturn

## Returns the 'prompt' to generate the entered query text in a GEN-Z weird way of talking
# Prompt data 1 - Default
def GenZ():
    ## Needs engine as 'TEXT-DAVINCI-002'
    return Gen
# Prompt data 2 - Not Default
def GenZ2():
    ## Needs engine as 'TEXT-DAVINCI-002'
    return Gen2

## Returns the 'prompt' to generate the entered query text in a more casual way of talking
## Prompt data 1 - Default
def ToneChanger():
    ## Needs engine as 'CURIE-001'
    return Cas
## Prompt data 2 - Not Default
def ToneChanger2():
    ## Needs engine as 'CURIE-001'
    return Cas2


class ParametersForAPI:
  sets1 = {"temp" : 0.5,
          "top_p_val" : 0.3,
          "freq_pen" : 0.5,
          "pres_pen" : 0
        }
  sets2 = {"temp" : 0.5,
          "top_p_val" : 0.3,
          "freq_pen" : 0.5,
          "pres_pen" : 0
        }
  # Values set using these will reset to the ones shown in the variable if the program is restarted.
  # Need to make sure that it takes backup of every changed settings to a text file along with updating the variables.
  # Being done using different classes that handle all 'Class variable' that stores the data in itself and methods to edit the data
  # Maybe need to finally integrate a database to fetch latest values from and store the changes into.
  # Feature : remove a month old data from it. Check is done every 24 hours and the most old data is removed from it altogether.
  # Maybe have it stored in some other low spec space and use the current storage as a cache of sorts to keep up with the fresh data only.
  def getGenZSettings(self):
    return self.sets1

  def setGenZSettings(self,vals):
    self.sets1 = vals

  def getCasSettings(self):
    return self.sets2

  def setCasSettings(self,vals):
    self.sets2 = vals

## Call to save the current Settings 
## ALL THE SAVERS BELOW NEED TO BE CONVERTED INTO ONE GAWD DAMN THING

# The functions mentioned in below comments that actually do the work
class BackupWriter:

  def ValUpdater():
    return

  def WriteBack():
    b = open("files/Backups.txt","a") 
    b.write("/n========================================/n")
    b.write(f"{DatetimeReturn()} :")
    b.write("\nPrompt: " + ToneChanger())
    b.write("\nSettings: " + ParametersForAPI.getCasSettings())

## saves the current settings to the txt files and then overwrites the current values to update them using certain functions that actually do the working
def fileSaver(prompt, settings , Fil):
    return prompt, settings, Fil

#def Sarcastic():
 #   Tone = '''This is a chatbot that reluctantly answers questions with sarcastic responses: \n\nNormal Version: How many pounds are in a kilogram? \nCooler Version: This again? There are 2.2 pounds in a kilogram. Please make a note of this. \nNormal Version: What does HTML stand for? \nCooler Version: Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future. \nNormal Version: What is the factorial of 4? \nCooler Version: Oh come on, you must have failed maths class 24 times. \nNormal Version: When did the first airplane fly? \n Cooler Version: On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away. \nNormal Version: Why are humans so much like humans? \nCooler Version: Why would you ask a bot a question like that? \nNormal Version: '''
  #  return Tone

  





