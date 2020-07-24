import os
from shutil import copyfile

"""
This python script will copy all of the PDF submissions from a Snappy download 
(unzipped) from Gauchospace into the GRADED_FOLDER. It will also rename them as
"lastname-firstname_exp<EXP_NUM>_graded.pdf".
"""

# VARIABLES (EDIT ME!)
REPORT_FOLDER='./test_reports'  # this is the name of the root folder that contains all submission folders
GRADED_FOLDER='./graded/'       # change this if you want to specify a different output folder
EXP_NUM = '15'                  # change this to the current experiment number

# Function definitions

def parse_name(folder_name):
    name = folder_name.split('_')[0].split(' ')[::-1]
    return "-".join([x.lower() for x in name])

def get_reports(folder_list):
    reports = []
    for f in folder_list:
        reports.append(os.listdir(f'{REPORT_FOLDER}/{f}'))
    return list(map(''.join, reports))

def generate_report_paths(folder_list, report_list):
    paths = []
    for i in range(0, len(report_list)):
        paths.append(f'{REPORT_FOLDER}/{folder_list[i]}/{report_list[i]}')
    return paths

def generate_name_report_dict(names, reports):
    return dict(zip(names, reports))

def save_graded_report(report_dict):
    for report in report_dict:
        output_path = GRADED_FOLDER + str(report) + '_exp' + f'{EXP_NUM}_graded.pdf'
        print(f"Writing {output_path}...")
        try:
            copyfile(report_dict[report], output_path)
        except Exception as e:
            print(f'{e}')
            break
        print('Success!')

# Executed code

# get a list of all the subfolders from the root folder
folder_list = os.listdir(REPORT_FOLDER)

# parse the students' names from the folder list
student_names = [parse_name(name) for name in folder_list]

# make a list of the relative paths to the PDF files
report_paths = generate_report_paths(folder_list, get_reports(folder_list))

# create a dictionary to corrolate names with PDF paths
name_report_dictionary = generate_name_report_dict(student_names, report_paths)

# create the GRADED_FOLDER if it doesn't already exist
if not os.path.exists(GRADED_FOLDER):
    os.makedirs(GRADED_FOLDER)

# copy and rename all PDFs into the GRADED_FOLDER
save_graded_report(name_report_dictionary)