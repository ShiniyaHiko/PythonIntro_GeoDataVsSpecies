# PythonIntro_GeoDataVsSpecies
Project Submission
# Overview
This python project takes geological data and species richness of tedrapods, amphibians and memals and looks for possible correlations which are then ploted into a scatterplot.

This project used the dataset from the webpage [https://www.research-collection.ethz.ch/handle/20.500.11850/411821](https://www.research-collection.ethz.ch/handle/20.500.11850/411821). Because the whole dataset is quite big, 'copy_head.py' was used to shorten it to the first 5000 rows to work with. This subset can be found as 'global_data_5k.txt'.

The code is run as a Jupyter Notebook and consists of 3 blocks of code wich need to be run in order. The first is reading the .txt file as dataframe using panda. Next the second is searching for possibly interessting correlations using the Pearson correlation coefficent. And lastly the third is plotting every possibly interesting correlation into its own scatterplot.

Initially, a few lines were generated using ChatGPT and subsequently modified.
# Installation
Needed packages: Python 3.10, jupyterlab, pandas, scipy, seaborn, matplotlib

1. Download this repository.
	```git clone https://github.com/ShiniyaHiko/PythonIntro_GeoDataVsSpecies/tree/main```
2. Install needed packages via pip.
	```pip install jupyterlab, pandas, seaborn jupyter lab``` 
	in the project folder
3. Open the project using jupyterlab.

# Usage
Open the project using jupyterlab. Then run the 3 code blocks in order from top to bottom. Jupyterlab will show the output in the notebook.
# License
This project is licensed unter CC BY-NC-SA 4.0 - see LICENSE file for details.
