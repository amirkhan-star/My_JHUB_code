import os
import pandas as pd 
import xml.etree.ElementTree as ET
local_dir = '/home/ubuntu/xml_file_paths/valid_excel_files'

bucket_names='newbucket'
MINIO_user_name='AMIRKHAN'
MINIO_password ='amirkhan13'

def xml_to_excel(xml_path, excel_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    data = []
    for item in root.findall('.//item'): 
        row = {child.tag: child.text for child in item}
        data.append(row)
    df = pd.DataFrame(data)
    df.to_excel(excel_path, index=False)
    
def convert_all_xml_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.xml'):
            xml_path = os.path.join(directory_path, filename)
            excel_path = os.path.join(directory_path, filename.replace('.xml', '.xlsx'))
            xml_to_excel(xml_path, excel_path)
            os.remove(xml_path)

convert_all_xml_in_directory(local_dir)
