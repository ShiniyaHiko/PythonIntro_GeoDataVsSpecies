# PythonIntro_GeoDataVsSpecies
Project Submission
# Overview
This python project uses geological data and species richness of tedrapods, amphibians and memals and searches for possible correlations, which are then ploted into a scatterplot.

This project used the Global geologic, topographic and biological dataset from the webpage [https://www.research-collection.ethz.ch/handle/20.500.11850/411821](https://www.research-collection.ethz.ch/handle/20.500.11850/411821). The whole dataset is quite big, so 'copy_head.py' was used to shorten it to the first 5000 rows to work with. This subset can be found as 'global_data_5k.txt', which are comma seperated values.

The code is run as a Jupyter Notebook and consists of 3 blocks of code, which need to be run in order. The first reads the .txt file as dataframe using pandas. Next, the second is searching for possibly interessting correlations using the Pearson correlation coefficent. And lastly, the third is plotting every possibly interesting correlation into its own scatterplot.

Initially, a few lines were generated using ChatGPT and subsequently modified.
# Installation
Needed packages: Python 3.10, pandas, scipy, seaborn, matplotlib, jupyter lab

1. Download this repository.

	```git clone https://github.com/ShiniyaHiko/PythonIntro_GeoDataVsSpecies.git```	
2. Go into the repository.

	```cd PythonIntro_GeoDataVsSpecies```
	
3. Create a virtual enviroment.

	```python -m venv env```
	
4. Activate the virtual enviroment.
	
	Windows:
	```env/Scripts/activate.bat```
	
	Linux/Mac:
	```source env/bin/activate```
	
4. Install needed packages via pip.
 
	```pip install pandas seaborn jupyterlab scipy``` 
	
	in the project folder
3. Open the project using jupyterlab.

	```jupyter lab```

# Usage
Open the project using jupyterlab. Then run the 3 code blocks in order from top to bottom. Jupyterlab will show the output in the notebook.
# License
This project is licensed unter CC BY-NC-SA 4.0 - see LICENSE file for details.
