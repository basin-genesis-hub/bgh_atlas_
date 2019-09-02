---
layout: model
model_name: 'McClay style experiment suite'
author: 
  - 'Patrice F Rey'
# Software options include Badlands, Underworld or Coupled
software: 'Underworld' # 
version: 
  - 'Underworld 1.8'
# Provide a category from Depositional, Tectonic or Coupled
category: 'tectonic' # 
subcategory: 'extension'
# Image to display on the menu
#thumbnail: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/09/PR229_88.png'
icon: 'globe'
# Provide an animation gif to display along with a description
animation:
  mp4: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/08/A_PR221b.mp4'
  description: 'This is a sample video'
#Model setup
model_setup:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/09/McClay_InternalCondition-1.png'
  description: 'This suite of experiment is inspired by similar sandbox analog models from Kent McClay. The aim is to develop an *Underworld* 2D template capable of matching the modelling outcomes of the best sandbox experiments. Our template represents a domain 144 km long and 36 km deep, the top 12 km of which is made of air-like material. There is 16 km of sedimentary rocks (pre-rift package) distributed over 10 layers, the top 10 are 1.5 km thick. Underneath, there is 8 km of stronger rocks (i.e. larger cohesion and coefficient of friction). We include a salt-like layer (constant density 2000 kg/m3, viscosity 1e19 Pa.s), either at the surface of the model, or within top section of the pre-rift package. The density of the sediments increases with depth either incrementaly or following a dependence on the confining pressure to simulate compaction. During extension, the progressive burial of the salt layer under sediments of increasing density results in a density inversion. In some models we impose a pseudo-isostatic condition at the base of the model, to maintain the lithostatic pressure constant. The wall to the right moves away at 2 cm/yr. To mimic sandbox kinematic boundary conditions, we i/ turn off the isostasy, ii/ impose a constant velocity at the base of the model, as well as on the vertical wall of the left where it meets with the lower basal layer, and iii/ we add a thin, low viscosity layer, to decouple the sedimentary sequence from the backstop and the bottom layer.'
# Describe the conditions/parameters for the models in a table or image
conditions:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/09/Parameters.png'
  description: ''
# Give text for model results
result:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/09/A_StInv221b.mp4'
  description: 'This suite of experiments demonstrates that our *Underworld* 2D template is capable of delivering model outputs comparable to some of the best sandbox experiments facilities. Some of the advantages of our numerical sandox template include: i/ speed, as models can be set up in minutes and dozens of them can run in 24 to 48 hours or less; ii/ our numerical experiments keep track of temperature, stress, strain rate, and accumulated strain; iii/ the pressure- and temperature-dependent density and rheology of each individual layers can be specified; iv/ isostasy can be accounted for; and v/ our template allows for time-dependent boundary conditions and simple surface processes'

# Give citation or DOI for paper
citation: 'Patrice F Rey, 2019:'

# Online pointer to your model (Git/Binder/FTP etc.)
model_url: ''

# Hashable search terms
keywords: '' 

# Model location coordinates
location: 
  latitude: ''
  longitude: ''

# Contact 
contact:
---
