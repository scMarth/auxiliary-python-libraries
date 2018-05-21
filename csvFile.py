import sys

class csvFile(object):
   """
   A class to represent a csv file
   """

   # private variables
   __buffer = ""
   __waitingForEndQuote = False
   __maxBufferLen = 1000
   __numColumns = None
   __bufferIndex = 0

   # public variable
   csvArray = None

   # Create a new set of records
   #
   # Records is an array of arrays of strings, e.g.:
   #
   # [
   #    ["this", "is", "an"],
   #    ["example", "of", "records"],
   # ]
   def __createNewRecords(self):
      self.csvArray = []
      self.csvArray.append([])
      return

   # Process a byte
   def __processByte(self, byte):
      if (byte == ','):
         if (self.__waitingForEndQuote != True):
               self.__addBufferAsValue()
         else:
               self.__addByteToBuffer(byte)
      elif (byte == '"'):
         if (self.__waitingForEndQuote):
               self.__waitingForEndQuote = False
         else:
               self.__waitingForEndQuote = True
      elif (byte == '\r'):
         return
      elif (byte == '\n'):
         if (self.__waitingForEndQuote):
               self.__addByteToBuffer(byte)
         else:
               self.__addBufferAsValue()
      else:
         self.__addByteToBuffer(byte)
      return

   # Add the byte to the buffer
   def __addByteToBuffer(self, byte):
      if (len(self.__buffer) == (self.__maxBufferLen - 1)):
         self.__bufferLimitExceededExit()
      self.__buffer += str(byte)
      return

   # This function is called when the buffer length exceeds maxBufferLen.
   # This function prints an error and then terminates execution
   def __bufferLimitExceededExit(self):
      sys.stderr.write('Buffer limit of ' + str(self.__maxBufferLen) + " exceeded\n")
      sys.stderr.write('Buffer contents:\n\n' + self.__buffer + "\n")
      sys.exit()

   def __clearBuffer(self):
      self.__buffer = ""
      return

   def __addBufferAsValue(self):
      currInd = len(self.csvArray) - 1
      lastValueInd = len(self.csvArray[currInd])
      if (lastValueInd == self.__numColumns):
         self.csvArray.append([])
         currInd += 1
      self.csvArray[currInd].append(self.__buffer) # append to records
      self.__clearBuffer() # clear the buffer
      return

   def __readCsvIntoArray(self, csvPath):
      # Process the bytes in the file
      with open(csvPath) as file:
         while True:
            byte = file.read(1)
            if not byte:
                  # ignore newlines at the end of the file
                  if (len(self.csvArray[len(self.csvArray) - 1]) == (self.__numColumns - 1)):
                        self.__addBufferAsValue()
                  break
            else:
                  self.__processByte(byte)

   def __init__(self, csvPath, numColumns):
      # initialize the csvArray
      self.__createNewRecords()
      self.__numColumns = numColumns
      self.__readCsvIntoArray(csvPath)
      
   def validateRecords(self):
      errorsFound = False
       
      # (first line is header)
      print(str(len(self.csvArray)) + " lines found ; " + str(len(self.csvArray) - 1) + " records found")

      for i in range(0, len(self.csvArray)):
         if (len(self.csvArray[i]) != self.__numColumns):
               print("validateRecords: Error found: len(records[" + str(i) + "]) = " + str(len(self.csvArray[i])))
               errorsFound = True

      if not errorsFound:
         print("All records have the correct number of columns")
      return



