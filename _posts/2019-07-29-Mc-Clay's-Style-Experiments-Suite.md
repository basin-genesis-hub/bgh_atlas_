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
#thumbnail: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/07/SlabPlateauCollision_white_background.jpg'
icon: 'globe'
# Provide an animation gif to display along with a description
animation:
  mp4: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/08/A_McClay200_nomghr_Insta-1.mp4'
  description: 'This is a sample video'
#Model setup
model_setup:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/08/McClay100.0004.png'
  description: 'This suite of experiment is inspired by similar sandbox analog models from Kent McClay. The model represents a domain 144 km long and 36 km deep, the top 12 km of which is made of air-like material. There is 16 km of sedimentary rocks distributed over 10 layers, the top 10 are 1.5 km thick. Underneath, there is 8 km of stronger rocks (i.e. larger cohesion and coefficient of friction). The fourth layer from the top is a salt-like layer (density 2000 kg/m3, viscosity 1e19 Pa.s). Otherwise, density increases with depth. We impose a pseudo-isostatic condition at the base of the model, to maintain the lithostatic pressure constant. This is a major difference with analog experiments. The wall to the right moves away at 2 cm/yr. '
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
  description: 'Viscosity, density and yield strength for each of the domains in the model setup for a 80-Myr-old lithosphere'
# Give text for model results
result:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/07/Moresi__et_al_2014_results.jpg'
  description: 'A comparison of velocities during collision, accretion and recovery. Shown are the velocities of the subducting plate (black lines), the retreating end of the plate boundary (‘Trench retreat rate’, green), the colliding end of the plate boundary ‘Trench advance rate’, red), and the cusp of the laterally retreating trench (‘Lateral rollback rate’, blue). Negative velocities indicate retreat, positive velocities indicate advance.'

# Give citation or DOI for paper
citation: 'https://www.nature.com/articles/nature13033'

# Online pointer to your model (Git/Binder/FTP etc.)
model_url: 'doi:10.1038/nature13033'

# Hashable search terms
keywords: '' 

# Model location coordinates
location: 
  latitude: ''
  longitude: ''

# Contact 
contact:
---
