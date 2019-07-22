from datetime import datetime
import platform

class Logger(object):
  def __init__(self, _out_format = 'stdout'): 
    self.out_format = _out_format
    if(self.out_format != 'stdout'):
      if(platform.system() == 'Windows'):
        self.file_name = ".\logs\\"+ str(datetime.now().strftime('activity_checker_%Y%m%d_%H%M%S.log'))
      elif(platform.system() == 'Linux'):
        self.file_name = "./logs/"+ str(datetime.now().strftime('activity_checker_%Y%m%d_%H%M%S.log'))
      else:
        self.out_format =  'stdout'
        print("Unrecognized FileSystem, defaulting logs to stdout")
  
  def logNote(self, message):  
    if(self.out_format == 'stdout'):
      print("NOTE: " + str(message))
    else:
      with open(self.file_name, "a+") as log_file:
        log_file.write("NOTE: " + str(message) + "\n")

  def logWarning(self, message):  
    if(self.out_format == 'stdout'):
      print("WARNING: " + str(message))
    else:
      with open(self.file_name, "a+") as log_file:
        log_file.write("WARNING: " + str(message) + "\n")
    
  def logError(self, message):  
    if(self.out_format == 'stdout'):
      print("ERROR: " + str(message))
    else:
      with open(self.file_name, "a+") as log_file:
        log_file.write("ERROR: " + str(message) + "\n")
    
  def logFatalError(self, message):  
    if(self.out_format == 'stdout'):
      print("FATAL ERROR: " + str(message))
    else:
      with open(self.file_name, "a+") as log_file:
        log_file.write("FATAL ERROR: " + str(message) + "\n")
    