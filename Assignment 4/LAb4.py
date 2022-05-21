# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 18:09:38 2022

@author: sshaid2
"""



with open("RawData_TabDelimitted.txt") as dataTabDelim:
    content = dataTabDelim.readlines()
    
with open("exported_parsed_data.csv",'w') as outputfile:
    outputfile.write("test")
    for strLine in content:
        lineData = strLine.split("\t")
        
        campusDeptUnit = lineData[0].split("|")
        
        campus = campusDeptUnit[0].strip()
        
        if (len(campusDeptUnit) == 2):
            department = campusDeptUnit[1].strip()
            unit = ""
        elif (len(campusDeptUnit)==1):
            department=""
            unit=""
        else:
            department = campusDeptUnit[1].strip()
            unit = campusDeptUnit[2].strip()
            
        outputfile.write("{},{},{}\n".format(campus,department,unit))
            
             
                
        