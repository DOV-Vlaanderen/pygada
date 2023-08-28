.. _demo_dataset:

============
Demo dataset
============

A representative PFAS demo dataset is created in function of the examples.

| The PFAS soil and groundwater data is downloaded through pydov on 03/08/2023.
| For now, the focus is on the :download:`combined soil <../pygada/datasets/PFAS/gecombineerde_bodem_dataset.csv>` and :download:`combined groundwater <../pygada/datasets/PFAS/gecombineerde_grondwater_dataset.csv>` datasets.

--------------------------------------------
Combined soil and groundwater datasets pydov
--------------------------------------------

| The first step was performing a quality control, including a data exploration and cleaning.

**Soil and groundwater dataset**

- Transform date to datetime and remove unrealistic dates
- Drop rows with sum parameters*
- Drop rows with higher than detection condition
- Drop rows with unrealistic units
- Replace parameter values

*The sum parameters already containing some interpretation. The lower bound principle, a value lower than the detection limit is equal to zero.

**Soil dataset**

- Drop rows with an empty date

**Groundwater dataset**

- Replace NaN detection_condition
- Drop rows with empty `top_m_mv` and/or `basis_m_mv`


**The full analysis step-by-step per matrix can be found in the following notebooks.**

.. toctree::
   :maxdepth: 1

   notebooks/data_preparation/PFAS/quality_control_groundwater.ipynb
   notebooks/data_preparation/PFAS/quality_control_soil.ipynb

The cleaned datasets (:download:`soil <../pygada/datasets/PFAS/combined_soil_dataset_cleaned.txt>` and :download:`groundwater <../pygada/datasets/PFAS/combined_groundwater_dataset_cleaned.txt>`) are combined into one (see following notebook), which results in :download:`the demo dataset <../pygada/datasets/PFAS/demo_dataset.txt>`).

.. toctree::
   :maxdepth: 1

   notebooks/data_preparation/PFAS/demo_test_dataset.ipynb

