.. _data_input:

==========
Data-input
==========

There are two data-input options for pygada.

1. You can download data from the `subsoil database of Flanders`_ (DOV) with the use of `pydov`_ . 
2. You can use your own dataset.

.. _subsoil database of Flanders: https://www.dov.vlaanderen.be/
.. _pydov: https://pydov.readthedocs.io/en/stable/

| In the first case, the scripts to download soil- and groundwaterdata from DOV is integrated in pygada.
| As user you only have to define the parameter(s) and the bounding box. 

Groundwater-pydov
-----------------

.. dropdown:: Possible parameters
    :animate: fade-in
    
    From the following parameters groundwater data can be downloaded.
    
    .. tab-set::
        
        .. tab-item:: Andere parameters

            - %AfwijkBalans
            - P2O5
            - Si
       
        .. tab-item:: Anionen

            - Br                
            - Cl
            - CO3
            - F
            - HCO3
            - NO2
            - NO3
            - OH
            - PO4
            - PO4(Tot.)
            - SO4
            - SomAN
        
        .. tab-item:: Chemisch PFAS

            - 4:2 FTS
            - 4H-PFUnDA
            - 6:2 diPAP
            - 6:2 FTS
            - 6:2/8:2 diPAP
            - 8:2 diPAP
            - 8:2 FTS
            - 8:2 FTUCA
            - 9Cl-PF3ONS
            - 10:2 FTS
            - ADONA
            - EtPFOSA
            - EtPFOSAA
            - HFPO-DA
            - HPFHpA
            - MePFOSA
            - MePFOSAA
            - P37DMOA
            - PFBA
            - PFBS
            - PFBSA
            - PFDA
            - PFDoDA
            - PFDoDS
            - PFDS
            - PFECHS
            - PFHpA
            - PFHpS
            - PFHxA
            - PFHxDA
            - PFHxS
            - PFNA
            - PFNS
            - PFOA
            - PFOAbranched
            - PFOAtotal
            - PFODA
            - PFOS
            - PFOSA
            - PFOSbranched
            - PFOStotal
            - PFPeA
            - PFPeS
            - PFTeDA
            - PFTrDA
            - PFTrDS
            - PFUnDA
            - PFUnDS

        .. tab-item:: Fysico chemische parameters
            
            - DOC
            - droogrest
            - EC
            - EC(Lab.)
            - EC(Veld)
            - Eh°
            - H(tot)
            - O2
            - pH
            - pH(Lab.)
            - pH(Veld)
            - T
            - TAM
            - TAP
            - TDS
            - Temp.
            - TOC

        .. tab-item:: Kationen
        
            - Ca
            - Fe 
            - Fe2+
            - Fe3+
            - Fe(Tot.)
            - K
            - Mg
            - Mn
            - Na
            - NH4 
            - SomKAT
            - Sr

        .. tab-item:: Niet relevante metabolieten van pesticiden

            - AMPA
            - BAM
            - Dchdzn
            - meta4
            - meta8
            - Metola-S-ESA
            - VIS
        
        .. tab-item:: Organische verbindingen
            
            - CN
            - Per
            - Tri

        .. tab-item:: Pesticiden actieve stoffen
        
            - 245t     
            - 24d
            - 24db
            - 5ClFenol
            - Ala
            - Atraz
            - Bentaz
            - brom
            - Carben
            - Carbet
            - Chloridaz
            - Chlortol
            - Clproph
            - Cyana
            - Dicam
            - Dichlorpr
            - Diur
            - Ethofum
            - Fenoprop
            - flufe
            - fluopicolide
            - Fluroxypyr
            - Glyfos
            - Hexaz
            - Imida
            - Isoprot
            - Linur
            - Linur_mono
            - mcpa
            - mcpb
            - Mecopr
            - Mesotri
            - Metami
            - Metaza
            - Methabenz
            - Metobro
            - metola-S
            - Metox
            - Prometr
            - PropaCl
            - Propan
            - Propaz
            - Sebu
            - Simaz
            - Terbu
            - Terbutryn
            - trichlorpyr
            - Triflox
        
        .. tab-item:: Relevante metabolieten van pesticiden

            - atr_des
            - Atr_desisoprop
            - chazr
            - DMS
            - meta9
            - meta11
            - Terbu_des
        
        .. tab-item:: Zware metalen
        
            - Al
            - As
            - B
            - Ba
            - Cd
            - Co
            - Cr
            - Cu
            - Hg
            - Ni
            - Pb
            - Sb
            - Sn
            - Ti
            - Zn


Soil-pydov
----------

PFAS-pydov
----------

Personal dataset
----------------
