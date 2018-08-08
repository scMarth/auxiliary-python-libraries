# Regular Expression Auxiliary Library

import re

'''

Usage Example:

   from re_aux_lib import string_contains_expr, remove_extra_spaces

   remove_extra_spaces("   this is some    string   ",True)

'''

'''

Returns a string that is just 'input_string' with multi-spaces casted into single
spaces, and all whitespace before the first non-whitespace character removed,
as well as all whitespace after the last non-whitespace character removed.
The second parameter 'capitalize' controls whether or not the result is
capitalized.

'''
def remove_extra_spaces(input_string,capitalize):
   tokens = tokens = input_string.upper().split() if capitalize else input_string.split()
   return_string = ""
   for i in range(0, len(tokens)):
      return_string += tokens[i]
      if (i != (len(tokens) - 1)):
         return_string += " "
   return return_string

'''

Returns true if the expression 'expr' is contained in the string 'input_string'.

'''
def string_contains_expr(expr, input_string):
   if re.search(expr, input_string):
      return True
   return False

'''

Concatenates an array of tokens into a string of the tokens with the string
'separator' between them, without adding 'separator' before the first token
or adding 'separator' after the last token.

'''
def create_string_from_tokens(tokens,separator):
   output_str = ""

   for i in range(0, len(tokens)):
      output_str += tokens[i]
      if (i != (len(tokens) - 1)):
         output_str += separator

   return output_str
