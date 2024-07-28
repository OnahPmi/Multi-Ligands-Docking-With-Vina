# Multi ligands docking (virtual screening) with AutoDock vina

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