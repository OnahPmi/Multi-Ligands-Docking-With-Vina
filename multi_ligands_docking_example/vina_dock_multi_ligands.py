# Note: Before using this script ensure the following:
# 1. The receptor name, binding pocket coordinates and sizes, exhaustiveness, etc. are contained in the config.txt file
# 2. The prepared receptor and config.txt file are contained in the same folder
# 3. AutoDock vina is added to your system path pariables
# 4. Run the script from the folder containing the receptor and config.txt file

# To run the script: open the terminal in the appropriate folder and run the command:
# python vina_dock_multi_ligands.py

import os
import subprocess

ligands_dir = input("Input path to ligands directory: ") 

output_dir = "docking_results"
# os.makedirs(output_dir, exist_ok=True)

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# Function to run AutoDock Vina
def run_vina(ligand, output, log):
    command = ["vina", 
               "--config", "config.txt", 
               "--ligand", ligand, 
               "--out", output, 
               "--log", log]
    subprocess.run(command)

# Iterate over ligand files and run docking
for ligand_file in os.listdir(ligands_dir):
    if ligand_file.endswith(".pdbqt"):
        ligand_path = os.path.join(ligands_dir, ligand_file)
        output_file = os.path.join(output_dir, os.path.splitext(ligand_file)[0] + "_out.pdbqt")
        log_file = os.path.join(output_dir, os.path.splitext(ligand_file)[0] + "_log.txt")
        run_vina(ligand_path, output_file, log_file)

        print(f"Docking completed for {ligand_file} \n")

print("Docking completed for all ligands.")


# import os
# import subprocess

# ligands_dir = input("Input path to ligands directory: ") 

# output_dir = "docking_results"

# if not os.path.exists(output_dir):
#     os.mkdir(output_dir)

# for ligand_file in os.listdir(ligands_dir):
#     if ligand_file.endswith(".pdbqt"):
#         ligand_path = os.path.join(ligands_dir, ligand_file)
#         output_file = os.path.join(output_dir, os.path.splitext(ligand_file)[0] + "_out.pdbqt")
#         log_file = os.path.join(output_dir, os.path.splitext(ligand_file)[0] + "_log.txt")
#         command = ["vina", "--config", "config.txt", "--ligand", ligand_path, "--out", output_file, "--log", log_file]
#         subprocess.run(command)

#         print(f"Docking completed for {ligand_file} \n")

# print("Docking completed for all ligands.")