import sys
import xml.etree.ElementTree as ET
import pandas as pd
import os

# Parse XML FILES
def parse_xml(entry_dir, filename, save_dir):
    table = []
    tags = []
    tree = ET.parse(f"{entry_dir}\\{filename}")
    root = tree.getroot()
    for element in root[0]:
        tags.append(element.tag)

    for element in root:
        row = []
        for child in element:
            row.append(child.text)
        table.append(row)

    df = pd.DataFrame(table, columns=tags)
    basename = filename.rsplit(".", 1)[0]
    df.to_excel(f"{save_dir}\\{basename}.xlsx", index=False)

def parse_folder(entry_dir, save_dir):
    file_list = os.listdir(entry_dir)
    for file in file_list:
        if file.endswith(".xml"):
            parse_xml(entry_dir, file, save_dir)

entry_dir = sys.argv[1]
save_dir = sys.argv[2]

parse_folder(entry_dir, save_dir)