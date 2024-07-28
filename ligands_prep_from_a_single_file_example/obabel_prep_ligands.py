import os
import subprocess
from rdkit import Chem

# Note: Before using this script ensure the following:
#   1. The ligands file or folder and this script are contained in the same folder
#   2. The ligand folder contains only the ligand files
#   3. obabel (Open babel) is added to your system path pariables
#   4. Have a virtual env where python3 and rdkit installed

# To run the script: 
#   1. open the terminal in the appropriate folder
#   2. Activate your rdkit env
#   3. run the command: python obabel_prep_ligands.py

user_response = input("Are your ligands contained in a single file[y/n]: ")

# Define the output directory
output_dir = "prepared_ligands"

def obabelPrepLigandsFromSingleFile():

    # Get the ligands file name from user input
    ligands_file = input("Input name of ligands file: ")

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # Read the SDF file using RDKit
    supplier = Chem.SDMolSupplier(ligands_file)                     

    # Iterate over each molecule in the SDF file
    for i, mol in enumerate(supplier):
        if mol is None:
            continue  # Skip molecules that RDKit can't parse
        # Extract the ligand name (assuming the molecule has a title)
        ligand_name = mol.GetProp('_Name') if mol.HasProp('_Name') else f'ligand_{i+1}'
        
        # Define the output file path
        output_file = os.path.join(output_dir, f'{ligand_name}.pdbqt')
        
        # Write the molecule to a temporary SDF file
        tmp_sdf_file = os.path.join(output_dir, f'tmp_{i}.sdf')
        writer = Chem.SDWriter(tmp_sdf_file)
        writer.write(mol)
        writer.close()
        
        # Convert the temporary SDF file to PDBQT using Open Babel
        subprocess.run([
            'obabel', tmp_sdf_file, '-O', output_file,
            '--add-hydrogens', '--partialcharge', 'gasteiger'
        ])
        
        # Remove the temporary SDF file
        os.remove(tmp_sdf_file)

    print("Conversion complete.") 

def obabelPrepLigandsFromMultiFiles():

    ligands_dir = input("Input path to ligands folder: ") 

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for ligand_file in os.listdir(ligands_dir):
        input_file = os.path.join(ligands_dir, ligand_file)
        input_file_extension = os.path.splitext(input_file)[1]
        output_file = os.path.join(output_dir, ligand_file.replace(input_file_extension, '.pdbqt'))
        subprocess.run(['obabel', input_file, '-O', output_file, '--add-hydrogens', '--partialcharge', 'gasteiger'])

if user_response in {"Yes", "yes", "Y", "y"}:
    obabelPrepLigandsFromSingleFile()
elif user_response in {"No", "no", "N", "n"}:
    obabelPrepLigandsFromMultiFiles()
else:
    print("Invalid respone")