#!/usr/bin/python3

import xml.etree.ElementTree as ET 
import pandas as pd

tree = ET.parse('data/menu.xml')

root = tree.getroot()

#print(root.tag)
#print(list(root[1]))
#print(root[1].attrib)
#print(root[0][0].text)
#print(root[0][2].tag)

for dish in root:
    for param in dish:
        print(dish.attrib['name'], param.tag, param.text)
    print()
    
#--------------------------------------------------------------

tree = ET.parse('data/menu.xml')
root = tree.getroot()

df_list = []
column_names = ['name', 'price', 'weight', 'class']

for dish in root:
    df_list.append([dish.attrib['name'], dish[0].text, dish[1].text, dish[2].text])
    df = pd.DataFrame(df_list, columns=column_names)
    
print(df)
        


