# Regular Expression Auxiliary Library

import re

'''

Usage Example:

from reAuxLib import stringContainsExpr, removeExtraSpaces

removeExtraSpaces("   this is some    string   ")

'''

'''

returns a string that is just 'inputStr' with multi-spaces casted into single
spaces, and all whitespace before the first non-whitespace character removed,
as well as all whitespace after the last non-whitespace character removed

'''
def removeExtraSpaces(inputStr):
   tokens = inputStr.upper().split()
   returnStr = ""
   for i in range(0, len(tokens)):
      returnStr += tokens[i]
      if (i != (len(tokens) - 1)):
         returnStr += " "
   return returnStr

'''

returns true if the street 'street' is contained in the string 'names'

'''
def stringContainsExpr(expr, inputStr):
   if re.search(expr, inputStr):
      return True
   return False

'''

concatenates an array of tokens into a string of the tokens with spaces between them,
without adding a space before the first token or adding a space after the last token

'''
def createStringFromTokens(tokens):
   outputStr = ""

   for i in range(0, len(tokens)):
      outputStr += tokens[i]
      if (i != (len(tokens) - 1)):
         outputStr += " "

   return outputStr
