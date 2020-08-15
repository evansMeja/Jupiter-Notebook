import glob
import json
import xml.etree.cElementTree as ET 
import os
base="31092306/"
txtfiles = []
for file in glob.glob("31092306/*.txt"):
    txtfiles.append(file)

for i in range(len(txtfiles)):
    with open(txtfiles[i]) as json_file:
        data = json.load(json_file)
        root = ET.Element("root")
        for p in data['data']:
            doc = ET.SubElement(root, "doc")
            ET.SubElement(doc, "id", name=p['id']).text = p['id']
            ET.SubElement(doc, "text", name="text").text = p['text']
            ET.SubElement(doc, "created_at", name="tweets").text = p['created_at']
        tree = ET.ElementTree(root)
        filenames = txtfiles[i].split("/")
        getExt = filenames[1].split(".")
        tree.write("output/"+getExt[0]+".xml")

  
  
  


