#!/usr/bin/python3

import xml.etree.ElementTree as ET 
import pandas as pd

new_root = ET.Element('menu')

dish1 = ET.SubElement(new_root, 'dish', name='Кура')
dish2 = ET.SubElement(new_root, 'dish', name='Греча')

price1 = ET.SubElement(dish1, "price").text = "40"
weight1 = ET.SubElement(dish1, "weight").text = "300"
class1 = ET.SubElement(dish1, "class").text = "Мясо"

price2 = ET.SubElement(dish2, "price").text = "20"
weight2 = ET.SubElement(dish2, "weight").text = "200"
class2 = ET.SubElement(dish2, "class").text = "Крупа"



new_root_string = ET.tostring(new_root)
#with open("new_menu.xml", "wb") as f:
#    f.write(new_root_string)
ET.ElementTree(new_root).write('new_menu_good.xml', encoding="utf-8")
