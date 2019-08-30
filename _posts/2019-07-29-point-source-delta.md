---
layout: model
model_name: 'point source delta'
author: 
  - 'Sara Morón'
# Software options include Badlands, Underworld or Coupled
software: 'Badlands' #
version: 
  - 'Badlands 1.0'
# Provide a category from Depositional, Tectonic or Coupled
category: 'surface processes' #
subcategory: 'fluvio-deltaic'
# Image to display on the menu
thumbnail: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/07/Delta_output.tif'
icon: 'globe'
# Animations to display
animation:
  mp4: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/08/ezgif-5-6ef0e36af546-1.gif'
  description: 'This model explores the response of deltas to high-frequency flexural isostatic adjustments to sea-level. The simulations take into account the response of flexural isostatic adjustments to both water and sedimet load. Our simulations show that flexural isostatic adjustments: (1) can be of high frequency and bidirectional, (2) are related to both the sediment and water load with the later being resposible for 30% of the flexural deflection. This cyclic behavior of the flexural compensation is the response of how the load and the water column is being shifted spatially. These results illustrate that flexural isostasy directly responds to eustatic changes and because there is a relationship between eustasy and climate during contrasting climatic regimes there would be a direct response to the sediment storage and the flexural response to the load partitioning.'
#Model setup
model_setup:
  url : 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/07/Delta_setup.jpg'
  description: 'The initial configuration of the modeling domain resembles the topography of a natural source to sink system with relief on the headwaters, a decrease in slope on the continental plain and successive changes on the gradient of the continental shelf and the continental slope. To ensure that our simulations mimic a funnel-like drainage basin shape in the continental domain and sediment is delivered to the marine domain through a point-source we imposed a longitudinal topographic low in the middle of the modeling domain.'
# Describe the conditions/parameters for the models in a table or image
conditions:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/07/Moresi__et_al_2014_BC-1.jpg'
  table:
  - Parameter: precipitation [m/a]
    value: 1
  - Parameter: erodibility coefficient
    value: 4.e-7
  - Parameter: diffprop
    value: 0.075
  - Parameter: elastic thickness [km]
    value: 50
  description: 'We extracted sea-level fluctuations spanning 10 Myr from the global sea-level curves published by Kominz et al., (2008). The extracted intervals span the Oligocene (specifically 33.9 Ma to 23.9 Ma) and the Paleocene (specifically 66.0 Ma to 56.0 Ma) and were chosen to represent contrasting ice house and green house periods, respectively. These simulations are then compared to a suite flexurally-compensated models. The sea-level curves we used have observations each 0.1 Myr and the time step of the simulations are designed to capture changes in that time resolution. In all the simulations we first let the simulations run for 2 Myr without any sea-level fluctuations so that the delta can reach dynamic equilibrium without any base level disturbances. For a more comprenhensive list of parameters go to https://github.com/saraemp/delta'


# Give text for model results
result:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/07/Delta_ms_metrics_Fig3.jpg'
  description: '(A) Sea-level curves from the Oligocene (33.9 - 23.9 Ma) and the Paleocene (66.0 - 56.0 Ma), which were used in the simulations to represent contrasting ice house (blue) and green (green) house periods, respectively. Notice the difference in the amplitude between the two curves. The first 2 Myr do not have any sea-level fluctuations so that the delta can reach dynamic equilibrium without any base level disturbances. (B) Computed flexural deflection through time (C) Basinward distance through time, note how transit distances are at least two times larger in the cases with no flexure (D) Boxplots display the 25 and 75 percentiles of the river mouth migration data, the central line in each box represents the median and the bars extending from each box represent the 10 and 90 percentiles for each group of data. IH= Ice House, GH=Green House, F = Flexurally compensated, NF= Non-Flexurally compensated. (E-F) Synthetic stratigraphy extracted from simulations IH F, GH F, IH NF, GH NF expressed as the stratigraphic thickness for each time step (100,000 Myr). Vertical exaggeration is 100.'

# Give citation or DOI for paper
citation:

# Online pointer to your model (Git/Binder/FTP etc.)
model_url: 'https://github.com/saraemp/delta'

# Hashable search terms
keywords: ''

# Model location coordinates
location:
  - latitude: ''
  - longitude: ''

# Contact
contact:
---
