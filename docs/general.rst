.. _general:

============
General info
============

Bounding box
------------

| A bounding box is requested when data from DOV is downloaded with the use of pydov. 
  The bounding box is a rectangle that defines the area from where data will be downloaded.
| The bounding box is defined in Belgian Lambert72 (EPSG:31370) coordinates:

.. code-block:: console

  'LowerLeftX-LowerLeftY-UpperRightX-UpperRightY'
  
| If you want to have data from entire Flanders you can use the following as input for the bounding box:

.. code-block:: console

  'flanders'
