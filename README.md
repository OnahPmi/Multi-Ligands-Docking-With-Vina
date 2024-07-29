# Multi Ligands Docking with AutoDock Vina
### This repository contain python scripts for preparing ligands and performing multi ligand docking (virtual screening) with AutoDock vina

### To use the scripts, (Download)[https://github.com/OnahPmi/Multi-Ligands-Docking-With-Vina-Python-Scripts/archive/refs/heads/main.zip] the `Multi-Ligands-Docking-With_Vina-Python_Script` and extract contents.

# Step 1: Ligand Preparation with Open babel

## Ligand Preparation from a Single File

This example demonstrates how to use the `obabel_prep_ligands.py` script to prepare ligands contained in a single SDF file named `raw_ligand.sdf` for docking using AutoDock Vina.

### Steps

1. **Setup:**
   - Ensure that the `obabel_prep_ligands.py` script and the `raw_ligand.sdf` file are in the same directory.
   - Ensure that Open babel (obabel) is installed and added to the system path variables.
   - Ensure you have a virtual environment with Python 3 and RDKit installed.

3. **Prepare the Environment:**
   - Navigate to the folder containing the `obabel_prep_ligands.py` script and the `raw_ligand.sdf` file.
   - Open your terminal in this directory.

4. **Run the Script:**
   - Activate the RDKit virtual environment.
   - Run the following command:
     ```bash
     python obabel_prep_ligands.py
     ```
   - When prompted:
     - For the question "Are your ligands contained in a single file [y/n]?", type `y` or `yes`.
     - For the prompt "Input name of ligands file," type the name of the ligand file. In this example `raw_ligands.sdf` and hit enter.

5. **Completion:**
   - Once the conversion is complete, a new folder named `prepared_ligands` will be created.
   - This folder will contain the prepared ligands in PDBQT format.

### Notes
- Make sure your virtual environment is activated before running the script.
- Verify that both `obabel_prep_ligands.py` and `raw_ligand.sdf` are in the same directory for the script to work correctly.

## Ligand Preparation from Multi Ligand Files

This example demonstrates how to use the `obabel_prep_ligands.py` script to prepare individual ligands files (mol2, pdb, sdf, etc.) contained in a folder called `raw_ligands` for docking using AutoDock Vina.

### Steps

1. **Setup:**
   - Ensure that the `obabel_prep_ligands.py` script and the `raw_ligands` folder are in the same directory.
   - Ensure that Open babel (obabel) is installed and added to the system path variables.
   - Ensure you have a virtual environment with Python 3 and RDKit installed.

2. **Prepare the Environment:**
   - Navigate to the folder containing the `obabel_prep_ligands.py` script and the `raw_ligands` folder.
   - Open your terminal in this directory.

3. **Run the Script:**
   - Activate the RDKit virtual environment.
   - Run the following command:
     ```bash
     python obabel_prep_ligands.py
     ```
   - When prompted:
     - For the question "Are your ligands contained in a single file [y/n]?", type `n` or `no`.
     - For the prompt "Input name of ligands file," type the name of the ligands folder. In this example `raw_ligands` and hit enter.

4. **Completion:**
   - Once the conversion is complete, a new folder named `prepared_ligands` will be created.
   - This folder will contain the prepared ligands in PDBQT format.

### Notes
- Make sure your virtual environment is activated before running the script.
- Verify that both `obabel_prep_ligands.py` and `raw_ligands` folder are in the same directory for the script to work correctly.

# Step 2: Multi ligands docking (virtual screening) with AutoDock vina

This example demonstrates how to use the `vina_dock_multi_ligands.py` script to perform docking of ligands contained in a folder called `prepared_ligands.`

## Steps

1. **Setup:**
   - Ensure that the `vina_dock_multi_ligands.py` script, the prepared protein (named `protein.pdbqt` in this example), `config.txt` file, and the `prepared_ligands` folder are in the same directory.
   - Ensure that the `receptor name`, `binding pocket coordinates and sizes`, `exhaustiveness`, etc. are contained in the `config.txt` file.
   - Ensure that AutoDock vina is installed and added to your system path pariables.
   - Ensure you have a virtual environment with Python 3 installed.

2. **Prepare the Environment:**
   - Navigate to the folder containing the `vina_dock_multi_ligands.py` script, prepared protein (`protein.pdbqt`), `config.txt` file, and the `prepared_ligands` folder.
   - Open your terminal in this directory.

3. **Run the Script:**
   - Activate the python 3 virtual environment.
   - Run the following command:
     ```bash
     vina_dock_multi_ligands.py
     ```
   - When prompted:
     - For the question "Input path to ligands directory:", type the name of the prepared ligands folder. In this example `prepared_ligands` and hit enter.

4. **Completion:**
   - Once the docking is complete, a new folder named `docking_results` will be created.
   - This folder will contain the docking results and the log files.

## Notes
- Make sure your python3 virtual environment is activated before running the script.
- Verify that `vina_dock_multi_ligands.py` script, prepared protein (`protein.pdbqt`), `config.txt` file, and the `prepared_ligands` folder are in the same directory for the script to work correctly.
