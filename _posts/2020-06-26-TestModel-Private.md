---
# Please do not change layout field and please make sure this file has a .md extension and please write all content with the '---' section.
layout: model

# Privacy (Public or Private)
privacy: public

# Give your model name
model_name: 'Test Model'

# Tell us about the authors. In case of more than one please note them down as: 'X, Y, Z - Organization'
author: 
  - 'Patrice F. Rey - BGH and Earthbyte Research Group, The University of Sydney, patrice.rey@sydney.edu.au'

# Tell us the software used for the model. Currently software options include Underworld, Badlands, Badlands-Underworld, Badlands-GPlates-CitcomS & pyGPlates
software: 'pyGPlates' 

# Tell us about the particular version of software. In case of multiple, mention them in a list format by adding a bullet dash in the next line as shown
version: 
  - 'Underworld 1.8'
  - 'Badlands 1.0'

# Provide a category from Depositional, Tectonic or Coupled
category: 'Tectonic' 

# Provide a sub category such as Compression, Extension, Strike-slip, Conceptual, Case-study.
subcategory: 'Extension'

# Provide a thumbnail image to be displayed with the list entry.  
thumbnail: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/09/PR229_88.png'

# Please do not change the icon field and leave it as 'globe'
icon: 'globe'
  
# Provide an animation video (mp4) to display along with a description
animation:
  mp4: "https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/08/A_PR221b.mp4"
  description: ''

# Provide an image to display for the model setup along with a description
model_setup:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/09/McClay_InternalCondition-1.png'
  description: 'This suite of experiments is inspired by similar sandbox analog models from Kent McClay. Here, the aim is to develop an Underworld 2D template capable of matching the modelling outcomes of the best sandbox experiments. Our template represents a domain 144 km long and 36 km deep, the top 12 km of which is made of air-like material. There is 16 km of sedimentary rocks (pre-rift sequence) distributed over 10 layers, the top 10 are 1.5 km thick. Underneath, there is 8 km of stronger rocks (i.e. larger cohesion and coefficient of friction). We include a salt-like layer (constant density 2000 kg/m3, viscosity 1e19 Pa.s), either at the surface of the model, or within top section of the pre-rift sequence. The density of the sediments increases with depth either incrementaly or following a dependence on the confining pressure to simulate compaction. During extension, the progressive burial of the salt layer under sediments of increasing density results in a density inversion. In some models we impose a pseudo-isostatic condition at the base of the model, to maintain the lithostatic pressure constant. The wall to the right moves away at 2 cm/yr. To mimic sandbox kinematic boundary conditions, we i/ turn off the isostasy, ii/ impose a constant velocity at the base of the model, as well as on the vertical wall on the left where it meets with the lower basal layer, and iii/ we add a thin, low viscosity layer, to decouple the sedimentary sequence from the backstop and the bottom layer.'

# Describe the conditions/parameters for the models in a table or image or both along with a description. Table is populated row-wise with each bullet point.
conditions:
  url: ''
  table:
  - Parameters (SI):  
    Sediment 0-16 km: 
    Deep sediment 16-24 km:
  - Parameters (SI):  Reference temperature (K)
    Sediment 0-16 km: 273.15
    Deep sediment 16-24 km: 273.15
  - Parameters (SI):  Reference density (kg m-3)
    Sediment 0-16 km: 1,800
    Deep sediment 16-24 km: 2,700
  - Parameters (SI):  Compressibility (Pa-1)
    Sediment 0-16 km: 1.42x10^-9
    Deep sediment 16-24 km: 1.42x10-9
  - Parameters (SI): Thermal expansivity (K-1)
    Sediment 0-16 km: 3x10-5
    Deep sediment 16-24 km: 3x10-5
  - Parameters (SI):  Thermal diffusivity (m2 s-1)
    Sediment 0-16 km: 1x10-6
    Deep sediment 16-24 km: 1x10-6
  - Parameters (SI):  Radiogenic heat production (W m-3)
    Sediment 0-16 km: 1.2 x 10-6
    Deep sediment 16-24 km: 0.6 x 10-6
  - Parameters (SI):  Heat capacity (J K-1 kg-1)
    Sediment 0-16 km: 1,000
    Deep sediment 16-24 km: 1,000
  - Parameters (SI): Max yield stress (MPa)
    Sediment 0-16 km: 100
    Deep sediment 16-24 km: 100
  - Parameters (SI):  Initial cohesion (MPa)
    Sediment 0-16 km: 0 to10
    Deep sediment 16-24 km: 0 to10
  - Parameters (SI): Cohesion after weakening (MPa)
    Sediment 0-16 km: 0 to 2
    Deep sediment 16-24 km: 0 to 2
  - Parameters (SI): Coefficient of friction
    Sediment 0-16 km: 0.567
    Deep sediment 16-24 km: 0.567
  - Parameters (SI): Coefficient of friction after weakening 
    Sediment 0-16 km: 0.112
    Deep sediment 16-24 km: 0.112
  - Parameters (SI):  Saturation strain
    Sediment 0-16 km: 0.2
    Deep sediment 16-24 km: 0.2
  - Parameters (SI): Viscosity (Pa.s) 
    Sediment 0-16 km: 1e22
    Deep sediment 16-24 km: NA
  - Parameters (SI):  Activation energy (kJ mol-1)
    Sediment 0-16 km: NA 
    Deep sediment 16-24 km: 244
  - Parameters (SI): Power law exponent
    Sediment 0-16 km: NA
    Deep sediment 16-24 km: 3.2
  - Parameters (SI): Pre-exponential factor (MPa-n s-1)  
    Sediment 0-16 km: NA
    Deep sediment 16-24 km: 1e-2


  description: ''

# Provide results in an image and a text description
result:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/09/PR229_88.png'
  description: 'This suite of experiments demonstrates that our Underworld 2D template is capable of delivering model outputs comparable to some of the best sandbox experiments facilities. Some of the advantages of our numerical sandox template include: i/ speed, as models can be set up in minutes and dozens of them can be run in 24 to 48 hours; ii/ our numerical experiments keep track of temperature, stress, strain rate, and accumulated strain; iii/ the pressure- and temperature-dependent density and rheology of each individual layers can be specified; iv/ isostasy can be accounted for; and v/ our template allows for time-dependent boundary conditions and simple surface processes.'

# Provide citation or DOI for paper
citation: 'Patrice F. Rey, 2019:'

# Online pointer to your model resources (Git/Binder/FTP etc.)
model_url: 'doi:'

# Hashable search terms to be used to make the models more discoverable
keywords: '' 

# Model location coordinates (near approximation)
location: 
  latitude: ''
  longitude: ''

# Contact details for corresponding authors
contact: ''
---
