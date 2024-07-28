# Multi-Ligands-Docking-With-Vina
**This repository contain python scripts for performing multi ligand docking (virtual screening) with AutoDock vina**

# Instructions on how to use the scripts

## obabel_prep_ligands.py script
### Note: Before using this script ensure the following:
  1. The ligands file or folder and this script are contained in the same folder
  2. The ligand folder contains only the ligand files
  3. obabel (Open babel) is added to your system path pariables
  4. Have a virtual env where python3 and rdkit installed

### To run the script: 
  1. open the terminal in the appropriate folder
  2. Activate your rdkit env
  3. run the command: python obabel_prep_ligands.py

## vina_dock_multi_ligands.py
### Note: Before using this script ensure the following:
1. The receptor name, binding pocket coordinates and sizes, exhaustiveness, etc. are contained in the config.txt file
2. The prepared receptor and config.txt file are contained in the same folder
3. AutoDock vina is added to your system path pariables
4. Run the script from the folder containing the receptor and config.txt file

### To run the script: open the terminal in the appropriate folder and run the command:
- python vina_dock_multi_ligands.py