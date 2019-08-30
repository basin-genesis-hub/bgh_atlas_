---
# Please do not change layout field 
layout: model

# Give your model name
model_name: 'Continental accretion'

# Tell us about the authors. In case of more than one: 'X, Y, Z'
author: 'Louis Moresi'

# Tell us the software used for the model. Softwares include Underworld, Badlands, Badlands-Underworld, Badlands-GPlates-CitcomS
software: 'Underworld' # 

# Tell us about the particular version of software. In case of multiple, mention them in a list format by adding a bullet dash in the next line as shown
version: 
  - 'Underworld 1.7'
  # - 'Badlands 1.0'

# Provide a category from Depositional, Tectonic or Coupled
category: 'Tectonic' 

# Provide a sub category such as Compression, Extension, Strike-slip, Conceptual, Case-study.
subcategory: 'Compression'

# Provide a thumbnail image to be displayed with the list entry.  
thumbnail: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/07/SlabPlateauCollision_white_background.jpg'

# Please do not change the icon field
icon: 'globe'

# Provide an animation gif to display along with a description
animation:
  gifs: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/08/CollisionView6.gif'
  gdesc: 'This 3D mechanical model explores the dynamics of continental accretion by including a subducting slab, and overriding plate and mantle dynamics. The model displays the following phases: (1) a collisional stage when the microcontinental ribbon initially accretes to the overriding plate; (2) a transitional stage where the convergent subducting plate and trench reorganize through coeval trench advance and retreat in different parts of the boundary; and (3) the re-initiation of a stable subduction system behind the accreted microcontinent.'
  video: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/08/strati_bgh_quick.mp4'
  vdesc: 'This is a sample video'
# Provide an image to display for the model setup along with a description
model_setup:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/07/Moresi__et_al_2014_setup.jpg'
  description: 'Initial geometry of the distinct material domains in the numerical model, not to scale. The subducting plate is 100km thick, 3,000kmwide and 7,000kmin length, and is built from 4 layers. The overriding plate has three domains: a back-arc region (1,200 km) a transitional region (350 km) and a continental backstop (750 km), each of which comprises two layers of equal thickness. The indenting ribbon is 50km in thickness, 1,500km wide and 500km deep (perpendicular to the convergence direction). Each of the vertical boundaries is a symmetry plane.'

# Describe the conditions/parameters for the models in a table or image or both along with a description
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

# Provide results in an image and a text description
result:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/07/Moresi__et_al_2014_results.jpg'
  description: 'A comparison of velocities during collision, accretion and recovery. Shown are the velocities of the subducting plate (black lines), the retreating end of the plate boundary (‘Trench retreat rate’, green), the colliding end of the plate boundary ‘Trench advance rate’, red), and the cusp of the laterally retreating trench (‘Lateral rollback rate’, blue). Negative velocities indicate retreat, positive velocities indicate advance.'

# Provide citation or DOI for paper
citation: 'https://www.nature.com/articles/nature13033'

# Online pointer to your model resources (Git/Binder/FTP etc.)
model_url: 'doi:10.1038/nature13033'

# Hashable search terms to be used to make the models more discoverable
keywords: '' 

# Model location coordinates (near approximation)
location: 
  latitude: ''
  longitude: ''

# Contact details for corresponding authors
contact:
---
