# 📂 Navigate and prepare folders
ls                       # List files/folders in the current directory
cd Lecturing             # Move into the "Lecturing" folder
mkdir SeptemberFolder    # Create a new folder named "SeptemberFolder"
cd SeptemberFolder       # Enter the new folder
cd ..                    # Go back one directory level
cd ../..                 # Go up two levels

# 🐍 Check Python and pip installations
python --version         # Show the default Python version
python3 --version        # Show the Python 3 version
pip list                 # Show installed Python packages

# 📦 Install a package
pip install matplotlib   # Install the Matplotlib plotting library

# ⚙️ Work with virtual environments
python -m venv venv      # Create a virtual environment named "venv"
source venv/bin/activate # Activate the virtual environment
pip list                 # Check installed packages inside the venv

# ⚙️ Work with virtual environments (Windows)
python -m venv venv      # Create a virtual environment named "venv"
venv\Scripts\activate    # Activate the virtual environment (Windows)
venv\Scripts\activate.ps1 # Activate the virtual environment (PowerShell Windows)
pip list                 # Check installed packages inside the venv

# Work with conda environments (if using Anaconda/Miniconda)
conda create --name myenv python=3.9  # Create a new conda environment with Python 3.9
conda activate myenv     # Activate the conda environment
conda deactivate         # Deactivate the current conda environment

# ❌ Deactivate the virtual environment
deactivate               # Exit the virtual environment

# ▶️ Run a Python script (various ways)
python Lesson8_libraries.py      # Run the lesson script with the active Python

# 📦 Conda environment info
conda list              # Show packages installed in the current conda env