# Note: Before using this script ensure the following:
# 1. The ligands folder and this script are contained in the same folder
# 2. The ligand folder contains only the ligand files
# 3. obabel (Open babel) is added to your system path pariables

# To run the script: open the terminal in the appropriate folder and run the command:
# python obabel_prep_ligands_multi_files.py

import os
import subprocess

ligands_dir = input("Input path to ligands folder: ") 

output_dir = "prepared_ligands"

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

for ligand_file in os.listdir(ligands_dir):
    input_file = os.path.join(ligands_dir, ligand_file)
    input_file_extension = os.path.splitext(input_file)[1]
    output_file = os.path.join(output_dir, ligand_file.replace(input_file_extension, '.pdbqt'))
    subprocess.run(['obabel', input_file, '-O', output_file, '--add-hydrogens', '--partialcharge', 'gasteiger'])