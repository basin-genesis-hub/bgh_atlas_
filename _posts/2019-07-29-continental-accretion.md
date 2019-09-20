---
layout: model
model_name: 'Continental accretion'
author:
  - 'L. Moresi, P. G. Betts, M. S. Miller & R. A. Cayley'
  - ''
# Software options include Badlands, Underworld or Coupled
software: 'Underworld' # 
version: 
  - 'Underworld 1.0'
# Provide a category from Depositional, Tectonic or Coupled
category: 'tectonic' # 
subcategory: 'compression'
# Image to display on the menu
#thumbnail: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/07/SlabPlateauCollision_white_background.jpg'
icon: 'globe'
# Animations to display
animation:
  mp4: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/09/CollisionView6.mp4'
  description: 'This 3D mechanical model explores the dynamics of continental accretion by including a subducting slab, and overriding plate and mantle dynamics. The model displays the following phases: (1) a collisional stage when the microcontinental ribbon initially accretes to the overriding plate; (2) a transitional stage where the convergent subducting plate and trench reorganize through coeval trench advance and retreat in different parts of the boundary; and (3) the re-initiation of a stable subduction system behind the accreted microcontinent.'
#Model setup
model_setup:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/07/Moresi__et_al_2014_setup.jpg'
  description: 'Initial geometry of the distinct material domains in the numerical model, not to scale. The subducting plate is 100km thick, 3,000kmwide and 7,000kmin length, and is built from 4 layers. The overriding plate has three domains: a back-arc region (1,200 km) a transitional region (350 km) and a continental backstop (750 km), each of which comprises two layers of equal thickness. The indenting ribbon is 50km in thickness, 1,500km wide and 500km deep (perpendicular to the convergence direction). Each of the vertical boundaries is a symmetry plane.'
# Describe the conditions/parameters for the models in a table or image
conditions:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/07/Moresi__et_al_2014_BC-1.jpg'
  table:
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
