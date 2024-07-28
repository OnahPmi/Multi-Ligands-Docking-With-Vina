# Ligand Preparation from a Single File

This example demonstrates how to use the `obabel_prep_ligands.py` script to prepare ligands contained in a single SDF file named `raw_ligand.sdf` for docking using AutoDock Vina.

## Steps

1. **Setup:**
   - Ensure that the `obabel_prep_ligands.py` script and the `raw_ligand.sdf` file are in the same directory.
   - Ensure that Open babel (obabel) is installed and added to the system path variables.
   - Ensure you have a virtual environment with Python 3 and RDKit installed.

2. **Prepare the Environment:**
   - Navigate to the folder containing the `obabel_prep_ligands.py` script and the `raw_ligand.sdf` file.
   - Open your terminal in this directory.

3. **Run the Script:**
   - Activate the RDKit virtual environment.
   - Run the following command:
     ```bash
     python obabel_prep_ligands.py
     ```
   - When prompted:
     - For the question "Are your ligands contained in a single file [y/n]?", type `y` or `yes`.
     - For the prompt "Input name of ligands file," type the name of the ligand file. In this example `raw_ligands.sdf` and hit enter.

4. **Completion:**
   - Once the conversion is complete, a new folder named `prepared_ligands` will be created.
   - This folder will contain the prepared ligands in PDBQT format.

## Notes
- Make sure your virtual environment is activated before running the script.
- Verify that both `obabel_prep_ligands.py` and `raw_ligand.sdf` are in the same directory for the script to work correctly.