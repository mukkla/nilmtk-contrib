# nilmtk-contrib

This repository contains all the state-of-the-art algorithms for the task of energy disaggregation implemented using NILMTK's Rapid Experimentation API

## Installation Details

We're currently testing a conda package. You can install in your current environment with:

```
conda install -c conda-forge -c nilmtk -c nilmtk/label/dev nilmtk-contrib
```

or create a dedicated environment (recommended) with:

```
conda create -n nilm -c conda-forge -c nilmtk -c nilmtk/label/dev nilmtk-contrib
```

Refer to this [notebook](https://github.com/nilmtk/nilmtk-contrib/tree/master/sample_notebooks) for using the nilmtk-contrib algorithms, using the new NILMTK-API.

## Dependencies

- NILMTK>=0.4
- scikit-learn>=0.21 (already required by NILMTK)
- Keras>=2.2.4 
- cvxpy>=1.0.0

**Note: For faster computation of neural networks, it is suggested that you install keras-gpu, since it can take advantage of GPUs. The algorithms AFHMM, AFHMM_SAC and DSC are CPU intensive, use a system with good CPU for these algorithms.**

