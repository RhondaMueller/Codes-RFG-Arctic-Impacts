# Codes - The impact of radiative forcing geoengineering on Arctic temperature extremes, wildfires, and permafrost thawing

##  File Descriptions
This repository contains code to run the analysis done for this paper:

- The ".gitignore" file ensures that unwanted files that exist within a Git repository are not tracked; e.g., checkpoints for Jupyter notebooks.

- The "environment.yml" file details the packages that are used in the Conda environment that underlies the principal analytical code in this repository.

### /analysis:

- The ipynb files within /analysis are structured according to the figure they provide the output to. The underlying data can be obtained from the references of the paper.

- The .py files within /analysis are python sub-scripts needed for some of the codes to run (ED Figures 1, 2 and 3).

### /data:

- 20x20_perma.txt are the pre-processed permafrost fraction per TNn Tmean data that were generated from the dataset of the European Space Agency’s Climate Change Initiative Permafrost project (Obu et al. 2021) and temperature data of the Climatic Research Unit TS4.01 (Harris et al. 2014).

- 20x20.txt are the pre-processed burned are per TXx Tmean data that were generated from a satellite data-driven fire frequency dataset (MCD64) (Gigli0 et al. 2015) and temperature data of the Climatic Research Unit TS4.01 (Harris et al. 2014).

## Instructions

All figures can be replicated by using these codes. As we used netcdf files that extracted for every variable seperately, the index pointing to the wanted variable (in our codes it is usually [0]) might need to be changed when using datasets containing several different variables.

These codes run on Python 3.9.7 and were created in Jupyter Notebook which can be installed locally or run from a browser (https://jupyter.org/). The environment with all the used packages is provided in the "environment.yml" file. For instruction on how to install the environment please refer to https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html.

## References:

Harris, I., Jones, P. D., Osborn, T. L., & Lister, D. H. Updated high-resolution grids of monthly climatic observations – the CRU TS3.10 Dataset. Int. J. Climatol. 34, 623–642 (2014). [https://doi.org/10.1002/joc.3711](https://doi.org/10.1002/joc.3711)

Giglio, L., Justice, C., Boschetti, L. & Roy, D. . MCD64A1 MODIS/Terra+Aqua Burned Area Monthly L3 Global 500m SIN Grid V006 [Data set]. NASA EOSDIS Land Processes DAAC. (2015). [https://doi.org/10.5067/MODIS/MCD64A1.006](https://doi.org/10.5067/MODIS/MCD64A1.006)

Obu, J. et al. ESA Permafrost Climate Change Initiative (Permafrost_cci): Permafrost extent for the Northern Hemisphere, v3.0. NERC EDS Centre for Environmental Data Analysis (2021). [https://doi:10.5285/6e2091cb0c8b4106921b63cd5357c97c](https://doi:10.5285/6e2091cb0c8b4106921b63cd5357c97c)

This repository and the scripts contained within were created by Rhonda C. Müller (rhonda.mueller (at) uzh.ch).
