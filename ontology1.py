#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:59:34 2018

@author: Mahmoud Zeydabadinezhad
email: mzeydab@emory.edu
"""
import pandas as pd
import sys

def ontology1(File1, File2):
    """
    Inputs: 
        - File1: Path to the 2018_I10gem.txt
        - File2 Path to the 2018_I9em.txt
    
    Outputs: 
        - Prints out the number of one-to-one, one-to-many, and terms with no mapping.
    """
#ile1 = '/home/mahmoud/Desktop/BMI500/Ontology/2018-ICD-10-CM-GEM/2018_I10gem.txt'
    ICD10To9 = pd.read_fwf(File1,header=None, converters={0:str, 1:str, 2:str})
#ile2 = '/home/mahmoud/Desktop/BMI500/Ontology/2018-ICD-10-CM-GEM/2018_I9gem.txt'
    ICD9To10 = pd.read_fwf(File2,header=None, converters={0:str, 1:str, 2:str})
    flag1 = ICD10To9.iloc[:,-1] # The 3rd column in ICD10-9 is the flags column.

# To find all one-to-one mappings we look for flags that have 0 in combination (3rd) and No map (2nd) location.
    print("Number of one-to-one mappings in ICD10-9 is:",flag1.str[::].value_counts()[0] + flag1.str[::].value_counts()[3])

# To find all one-to-many mappings we look for flag1s that have 1 in combination (3rd) and 0 in No map (2nd) location.
    print("Number of one-to-many mappings in ICD10-9 is:",len(flag1) - flag1.str[::].value_counts()[0] - flag1.str[::].value_counts()[3] - flag1.str[::].value_counts()[4])

# To find all terms with no mappings we look for flags that have 1 No map (2nd) location.
    print("Number of terms with no mappings in ICD10-9 is:", flag1.str[::].value_counts()[4])

    flag2 = ICD9To10.iloc[:,-1] # The 3rd column in ICD9-10 is the flags column.

# To find all one-to-one mappings we look for flags that have 0 in combination (3rd) and No map (2nd) location.
    print("Number of one-to-one mappings in ICD9-10 is:",flag2.str[::].value_counts()[0] + flag2.str[::].value_counts()[3])

# To find all one-to-many mappings we look for flags that have 1 in combination (3rd) and 0 in No map (2nd) location.
    print("Number of one-to-many mappings in ICD9-10 is:",len(flag2) - flag2.str[::].value_counts()[0] - flag2.str[::].value_counts()[3] - flag2.str[::].value_counts()[4])

# To find all terms with no mappings we look for flags that have 1 No map (2nd) location.
    print("Number of terms with no mappings in ICD9-10 is:", flag2.str[::].value_counts()[4])


if __name__== "__main__":
    if len(sys.argv) == 3:
        ontology1(sys.argv[1],sys.argv[2])
    else:
        sys.exit("\nUsage: ontology1 path_to_2018_I10gem.txt path_to_2018_I9gem.txt\n\n\n\n")
        