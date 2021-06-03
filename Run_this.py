import shutil
import xml.etree.ElementTree as ET
tree = ET.parse("/Users/federicoviviani/Desktop/task/configuration.xml")
root = tree.getroot()
for item in root.iter('config'):
    for file in item.iter("file"):
        name=file.attrib["file_name"]
        src=file.attrib["source_path"]
        dst=file.attrib["destination_path"]
        print ("Copying--->",file.attrib["file_name"])
        print("From:",file.attrib["source_path"])
        print ("To:",file.attrib["destination_path"])
        print("##############################################")
        string=[src,name]
        item="/".join(string)
        shutil.copy2(item,dst)
