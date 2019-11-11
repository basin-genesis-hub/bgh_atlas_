---
layout: model
model_name: 'Source-to-sink stratigraphic modelling'
author: 
  - 'Xuesong Ding, Tristan Salles, Nicolas Flament, Patrice Rey'

# Software options include Badlands, Underworld or Coupled
software: 'Badlands' #
version: 
  - 'Badlands 1.0'

# Provide a category from Depositional, Tectonic or Coupled
category: 'Depositional' #
subcategory: 'Conceptual of Stratigraphic Modelling'

# Image to display on the menu
thumbnail: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/11/S2S-Initial-Setting.pdf'
icon: 'globe'

# Animations to display
animation:
  mp4: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/11/S2S-Strata.mp4'
  description: 'The sedimentary architecture of basin margins reflects the interplay between the rate of change of accommodation creation (dA) and the rate of change of sediment supply (dS). Understanding the quantitative relationship between changes in dA/dS and depositional patterns can help to constrain the contributing factors of the formation of basin margins. This work investigates the development of stratigraphic sequences in a source-to-sink context using Badlands, and proposes quantitative stratigraphic interpretations based on two well-established techniques: the trajectory analysis method (Helland-Hansen & Hampson, 2009) and the accommodation succession method (Neal & Abreu, 2009; Neal et al., 2016).'

#Model setup
model_setup:
  url : 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/11/S2S-Initial-Setting.pdf'
  description: 'Model setup of a source-to-sink generic case. (a) The initial surface consisting of the mountain range (source area), alluvial plain (transfer zone) and continental margin (sink area). (b) Eustatic sea level and its rate of change over 30 Myr. (c) Distance-dependent stretching factor and the resulting thermal subsidence at 10, 20 and 30 Myr across the continental margin.'

# Describe the conditions/parameters for the models in a table or image or both along with a description
conditions:
  url: ''
  table:
  - Variables: Non Marine Erodibility
    Parameter: K_e
    value: 1.e-7
  - Variables: Rainfall
    Parameter: P [m/a]
    value: 2.0
  - Variables: (Rainfall * Area) exponent m
    Parameter: m
    value: 0.5
  - Variables: Slope exponent n
    Parameter: n
    value: 1.0
  - Variables: Slope Minimum for Flood-plain Deposition
    Parameter: slp_cr
    value: 0.001
  - Variables: Non-Marine % Max Deposition
    Parameter: perc_dep
    value: 0.75
  - Variables: Land sed. Transport by River
    Parameter: criver
    value: 10
  - Variables: Land sed. Transport by Wind
    Parameter: caerial
    value: 0.001
  - Variables: Lake/Sea sed. Transport by Currents
    Parameter: cmarine
    value: 0.005
  - Variables: No. Time Steps To Distribute Marine Deposits
    Parameter: diffnb
    value: 5
  - Variables: Marine % Max Deposition
    Parameter: diffprop
    value: 0.9

  description: ''

# Give text for model results
result:
  mp4: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/11/S2S-Topo-Erodep.mp4'
  description: 'Left panel shows the topography evolution over 36 Myr. Right panel shows the cumulative erosion and deposition over 36 Myr.'
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/11/S2S-Strata.jpg'
  description: 'Temporal evolution of stratal stacking patterns at 10 Myr (a), at 20 Myr (b) and at 30 Myr (c). Light-grey solid lines represent timelines at 0.5 Myr intervals. Coloured solid lines with timing in millions of years (Myr) are identified stratigraphic surfaces. Stratal stacking patterns are coloured by paleo-depth used to represent different depositional environments. Four sequences, no. 1 to no. 4, are defined. (d) Inset in (c): eustatic sea level curve and its rate of change. Coloured dots indicate the timing of corresponding stratigraphic surfaces. The paleo-depth and topography shown in this figure are directly produced by our post-processing tool.'
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/11/S2S-3D-Strata.png'
  description: '3D stratal stacking patterns on five dip-oriented cross sections (CS1 to CS5) and two along-strike cross sections. Key stratigraphic surfaces on CS1 to CS5 are identified and coloured accordingly.'
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/11/S2S-Trajectory-interpretation.pdf'
  description: 'Interpretation of trajectory classes based on analysis of shoreline and shelf-edge trajectories. (a) Shelf-edge trajectory classes based on manually picking the shelf-edge trajectory (magenta dots) on the final output of stratal stacking pattern. (b) Automatically picking shelf-edge trajectory classes based on calculated time-dependent shelf-edge positions in (d). (c) Automatically defined shoreline trajectory classes based on calculated time-dependent shoreline positions in (e). Time labels indicate the timing of each trajectory class formation.'
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/11/S2S-AS-Interpretation.pdf'
  description: 'Interpretation workflow based on the accommodation succession method. Step 1 includes marking stratal terminations (i.e. toplap, onlap and downlap represented using small arrows) and manually picking the break in slope as offlap break. The refilling of incised channels is shown in red, indicating erosional surfaces. Based on the marked stratal contacts, three stratal stacking trends (solid arrows) and three stratigraphic surfaces (coloured solid lines) are then defined in Steps 2 and 3. The three interpreted stacking patterns are filled with different colours, with their bounding times marked (Step 4). Each stacking pattern reflects the evolving ratio between rate of accommodation creation (δA) and rate of sediment supply (δS). (c) Automatically defined stacking patterns according to the calculated temporal evolution of δA − δS (> 0, < 0 and decreasing, or < 0 and increasing) (d).'


# Give citation or DOI for paper
citation: Ding, X., Salles, T., Flament, N., and Rey, P.: Quantitative stratigraphic analysis in a source-to-sink numerical framework, Geosci. Model Dev., 12, 2571–2585, https://doi.org/10.5194/gmd-12-2571-2019, 2019.

# Online pointer to your model (Git/Binder/FTP etc.)
model_url: 'https://github.com/XuesongDing/GMD-models'

# Hashable search terms
keywords: 'Badlands, Stratigraphic modelling, Source-to-sink'

# Model location coordinates
location:
  - latitude: ''
  - longitude: ''

# Contact
contact: Xuesong Ding (xuesong.ding@epss.ucla.edu)
---
