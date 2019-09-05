import sys, os
sys.path.insert(0, os.path.dirname(__file__) + '/../../')

from street_suffix_abbreviations import cast_street_suffixes_to_abrs

print("John Street -> " + cast_street_suffixes_to_abrs("John Street"))
print("John Strt -> " + cast_street_suffixes_to_abrs("John Strt"))
print("John St -> " + cast_street_suffixes_to_abrs("John St"))
