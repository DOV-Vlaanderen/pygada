.. _data_input:

==========
Data-input
==========

There are two data-input options for pygada.

1. You can download data from the `subsoil database of Flanders`_ (DOV) with the use of `pydov`_. 
2. You can use your own dataset.

.. _subsoil database of Flanders: https://www.dov.vlaanderen.be/
.. _pydov: https://pydov.readthedocs.io/en/stable/

| In the first case, the scripts to download soil- and groundwaterdata from DOV is integrated in pygada.
| As user you can use all the functionalities of pydov to `query on attribute properties`_, to `query on location`_, to `sort the data`_, to `use a limit number of WFS features returned`_, etc.
| For the specific PFAS-dataset you can only `query on location`_ and `use a limit number of WFS features returned`_ from pydov for the moment. In addition to those functionalities you can query on the medium.

.. _query on attribute properties: https://pydov.readthedocs.io/en/stable/query_attribute.html
.. _query on location: https://pydov.readthedocs.io/en/stable/query_location.html
.. _sort the data: https://pydov.readthedocs.io/en/stable/sort_limit.html
.. _use a limit number of WFS features returned: https://pydov.readthedocs.io/en/stable/sort_limit.html

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

.. dropdown:: Possible parameters
    :animate: fade-in
    
    From the following parameters groundwater data can be downloaded.
    
    .. tab-set::

        .. tab-item:: Bodem_biologisch

            - Beworteling diepte
            - Diepte van de wormgangen

        .. tab-item:: Bodem_boring

            - Diameter van de boor
            - Techniek van de boring
            - Type van de boring

        .. tab-item:: Bodem_chemisch

            - Anorganische C - percentage
            - Cadmium
            - Calciumcarbonaatgehalte
            - CEC totaal
            - C/N ratio
            - fe2o3
            - Kalkgehalte_beschrijvend
            - Oxalaat extraheerbaar aluminium
            - Oxalaat extraheerbaar ijzer
            - Organische C - percentage
            - pH CaCl2
            - pH H2O
            - pH KCl
            - Sorptie minerale fractie
            - Sorptie organische fractie
            - Sorptie totaal
            - Sorptie totaal HCL
            - Sorptie totaal NH4Cl
            - Sorptie verzadigingsgraad
            - Totale C - percentage
            - Totale N - percentage
            - Uitwisselbare calcium
            - Uitwisselbare magnesium
            - Uitwisselbare K

        .. tab-item:: Bodem_fysisch_structuur

            - Bulkdensiteit bodem totaal - gemeten
            - Consistentie
            - Consistentie - kleverigheid
            - Consistentie - plasticiteit
            - Horizontstructuur - gradatie - aardewerk
            - Horizontstructuur - gradatie - FAO
            - Horizontstructuur - grootteklasse - aardewerk
            - Horizontstructuur - grootteklasse - FAO
            - Horizontstructuur - type - aardewerk
            - Horizontstructuur - type - FAO
            - Mineralen - andere
            - Mineralen - glauconiet
            - Mineralen - kwarts
            - Mineralen - mica glimm
            - Mineralen - opaal
            - Mineralen - rk
            - Mineralen - schisten
            - Mineralen - veldspaat

        .. tab-item:: Bodem_fysisch_textuur

            - Mediaan van de textuurfracties
            - Textuur - granulometrie - klasse bodemkartering
            - Textuur - granulometrisch - gedetailleerd
            - Textuur - granulometrisch - klassen bodemkartering met Zg
            - Textuur - grove fractie (groter dan 2000 µm)
            - Textuur - handmatig - fout groter dan 5%
            - Textuur - handmatig - gedetailleerd
            - Textuur - handmatig - klassen bodemkartering
            - Textuur - percentage org. materiaal H2O2 30%
            - Textuur - type zand
            - Textuurfracties

        .. tab-item:: Bodem_fysisch_vocht
        
            - Diepte (grond)watertafel t.o.v. maaiveld
            - Drainage Aardewerk-doorlaatbaarheid
            - Drainage Aardewerk - interne drainage
            - Drainage Aardewerk - klasse
            - Drainage Aardewerk - oppervlakkige drainage
            - Gley roest - aantal
            - Gley roest - begrenzing
            - Gley roest - contrast
            - Gley roest - grootte
            - Gley roest - kleur volgens Munsell - CHROMA
            - Gley roest - kleur volgens Munsell - HUE_getal
            - Gley roest - kleur volgens Munsell - HUE_letters
            - Gley roest - kleur volgens Munsell - VALUE
            - Gley roest - vorm
            - Ksat
            - Reductie in horizont(ja/nee)
            - Roest - kleur omschrijving
            - Vochtgehalte gradatie
            - Vochtgehalte gradatie: nat, vochtig, droog
            - Vochtgehalte luchtdroge grond

        .. tab-item:: Bodem_kleur

            - Kleur omschrijving
            - Kleur volgens Munsell - CHROMA (kleur1)
            - Kleur volgens Munsell - CHROMA (kleur2)
            - Kleur volgens Munsell - CHROMA (kleur3)
            - Kleur volgens Munsell - HUE_getal (kleur1)
            - Kleur volgens Munsell - HUE_getal (kleur2)
            - Kleur volgens Munsell - HUE_getal (kleur3)
            - Kleur volgens Munsell - kleurcode
            - Kleur volgens Munsell - VALUE (kleur1)
            - Kleur volgens Munsell - VALUE (kleur2)
            - Kleur volgens Munsell - VALUE (kleur3)
            - Kleur volgens Munsell - HUE_letters (kleur1)
            - Kleur volgens Munsell - HUE_letters (kleur2)
            - Kleur volgens Munsell - HUE_letters (kleur3)

        .. tab-item:: Bodem_terrein

            - Aard van de stenige bijmenging
            - Bodemgebruik
            - Bodemgebruik Aardewerk
            - Coördinaat - Bonne - E
            - Coördinaat - Bonne - N
            - Coördinaat - Bonne - W
            - Geologische aard - afzettingswijze laag 1
            - Geologische aard - afzettingswijze laag 2
            - Geologische aard - afzettingswijze laag 3
            - Geologische aard - afzettingswijze laag 4
            - Geologische aard - andere kenmerken laag 1
            - Geologische aard - andere kenmerken laag 2
            - Geologische aard - andere kenmerken laag 3
            - Geologische aard - andere kenmerken laag 4
            - Geologische aard - bovenliggend laag 1
            - Geologische aard - bovenliggend laag 2
            - Geologische aard - bovenliggend laag 3
            - Geologische aard - bovenliggend laag 4
            - Geologische aard - bovenliggend laag 5
            - Geologische aard - bovenliggend laag 6
            - Geologische aard - lithologie laag 1
            - Geologische aard - lithologie laag 2
            - Geologische aard - lithologie laag 3
            - Geologische aard - lithologie laag 4
            - Geologische aard - lithologie laag 5
            - Geologische aard - lithologie laag 6
            - Geologische aard - tijdperk laag 1
            - Geologische aard - tijdperk laag 2
            - Geologische aard - tijdperk laag 3
            - Geologische aard - tijdperk laag 4
            - Geologische aard - tijdperk laag 5
            - Geologische aard - tijdperk laag 6
            - Reliëf - aard
            - Reliëf - expositie
            - Reliëf - helling enkelvoudig
            - Reliëf - helling meervoudig
            - Reliëf - geschatte lengte
            - Reliëf - landvorm
            - Reliëf - microreliëf
            - Reliëf - situering
            - Reliëf - vorm van de helling
            - Stenen
            - Vegetatie
            - Weersomstandigheden

        .. tab-item:: Bodemanalyse parameters

            - vegetatie

        .. tab-item:: Instrument parameters

            - Temperatuur
            - Volumetrisch vochtgehalte

PFAS-pydov
----------
.. dropdown:: Possible mediums
    :animate: fade-in
    
    From the following mediums PFAS data can be downloaded.
    
    .. tab-set::

        - all
        - biota
        - effluent
        - groundwater
        - migration
        - pure product
        - rainwater
        - soil
        - soil water
        - surface water
        - waste water
For more information check `the corresponding pydov documentation`_.

.. _the corresponding pydov documentation: https://github.com/DOV-Vlaanderen/pydov/blob/master/contrib/PFAS_concentrations/README.md

Personal dataset
----------------
