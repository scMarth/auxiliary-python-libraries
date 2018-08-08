import sys
import re

'''

A class to represent a csv file.

Usage Example:

   import csv_file

   example_csv_file = csv_file.CsvFile("./test_csv.csv", 50) # csv has 50 columns

When the above class is initialized, it automatically loads the contents of the CSV into a 2D array.
They are accessible via example_csv_file.csv_array[row_num][column_num]

A function validate_records:

   example_csv_file.validate_records()

can be called to validate the records by printing out how many lines were found, and find out if
every record in the csv has the correct number of columns

'''

class CsvFile(object):

   # private variables
   __buffer = ""
   __waiting_for_end_quote = False
   __MAX_BUFFER_LEN = 1000 # The length of the longest allowable value in the csv
   __num_columns = None
   __buffer_index = 0

   # public variable
   csv_array = None

   # Create a new set of records in csv_array
   #
   # csv_array is an array of arrays of strings, e.g.:
   #
   # [
   #    ["this", "is", "an"],
   #    ["example", "of", "csv_array"],
   # ]
   def __create_new_records(self):
      self.csv_array = []
      self.csv_array.append([])
      return

   # Process a byte
   def __process_byte(self, byte):
      if (byte == ','):
         if (self.__waiting_for_end_quote != True):
               self.__add_buffer_as_value()
         else:
               self.__add_byte_to_buffer(byte)
      elif (byte == '"'):
         if (self.__waiting_for_end_quote):
               self.__waiting_for_end_quote = False
         else:
               self.__waiting_for_end_quote = True
      elif (byte == '\r'):
         return
      elif (byte == '\n'):
         if (self.__waiting_for_end_quote):
               self.__add_byte_to_buffer(byte)
         else:
               self.__add_buffer_as_value()
      else:
         self.__add_byte_to_buffer(byte)
      return

   # Add the byte to the buffer
   def __add_byte_to_buffer(self, byte):
      if (len(self.__buffer) == (self.__MAX_BUFFER_LEN - 1)):
         self.__buffer_limit_exceeded_exit()
      self.__buffer += str(byte)
      return

   # This function is called when the buffer length exceeds maxBufferLen.
   # This function prints an error and then terminates execution
   def __buffer_limit_exceeded_exit(self):
      sys.stderr.write('Buffer limit of ' + str(self.__MAX_BUFFER_LEN) + " exceeded\n")
      sys.stderr.write('Buffer contents:\n\n' + self.__buffer + "\n")
      sys.exit()

   def __clear_buffer(self):
      self.__buffer = ""
      return

   def __add_buffer_as_value(self):
      curr_ind = len(self.csv_array) - 1
      last_value_ind = len(self.csv_array[curr_ind])
      if (last_value_ind == self.__num_columns):
         self.csv_array.append([])
         curr_ind += 1
      self.csv_array[curr_ind].append(self.__buffer) # append to records
      self.__clear_buffer() # clear the buffer
      return

   def __read_csv_into_array(self, csv_path):
      # Process the bytes in the file
      with open(csv_path) as file:
         while True:
            byte = file.read(1)
            if not byte:
                  # ignore newlines at the end of the file
                  if (len(self.csv_array[len(self.csv_array) - 1]) == (self.__num_columns - 1)):
                        self.__add_buffer_as_value()
                  break
            else:
                  self.__process_byte(byte)

   def __init__(self, csv_path, num_columns):
      # initialize the csv_array
      self.__create_new_records()
      self.__num_columns = num_columns
      self.__read_csv_into_array(csv_path)
      
   def validate_records(self):
      errors_found = False
       
      # (first line is header)
      print(str(len(self.csv_array)) + " lines found ; " + str(len(self.csv_array) - 1) + " records found")

      for i in range(0, len(self.csv_array)):
         if (len(self.csv_array[i]) != self.__num_columns):
               print("validate_records: Error found: len(records[" + str(i) + "]) = " + str(len(self.csv_array[i])))
               errors_found = True

      if not errors_found:
         print("All records have the correct number of columns")
      return

   def check_for_special_characters(self):
      commas = 0
      newlines = 0

      for i in range(0, len(self.csv_array)):
         for j in range(0, len(self.csv_array[i])):
            if re.search(",", self.csv_array[i][j]):
               commas += 1
            if re.search("\n", self.csv_array[i][j]):
               newlines += 1

      print("commas within fields: " + str(commas))
      print("newlines within fields: " + str(newlines))
      return


