---
layout: model
model_name: 'Gulf of Papua - uniform erodibility coefficient  !SITE_URL!/!POST_URL!/'
author: 
  - 'Rhiannon Garrett'
# Software options include Badlands, Underworld or Coupled
software: 'Badlands' #
version: 
  - 'Badlands 1.0'
# Provide a category from Depositional, Tectonic or Coupled
category: 'surface processes' #
subcategory: 'PNG'
# Image to display on the menu
thumbnail: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/08/Initial.png'
icon: 'globe'
# Animations to display
animation:
  mp4: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/09/GoP_35-0Ka-1.mp4'
  description: 'This model simulates the Late Quaternary landscape evolution of the Gulf of Papua, examining source-to-sink sediment transfer assuming a uniform erodibility coefficient. The simulation includes the surface uplift and subsidence history of the Gulf and uses present day precipitation rates. The simulation shows sediment delivered to the Gulf of Papua primarily by the Fly, Kikori and Purari Rivers and deposited in the western deep-sea basin, with shorter rivers draining the Papuan Peninsula contributing to sedimentation in the eastern Gulf. Sea level rise over the past 16 Kyr prevents the rivers draining the mainland from depositing directly into the deep-sea, with sediment becoming trapped on the submerged continental shelf.'
#Model setup
model_setup:
  url : 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/08/Initial_setup.png'
  description: 'The initial setup approximates the paleotopography by subtracting the vertical movement field from the present day topography. The Lambeck et al. (2014) sea level curve is applied to the simulation for the past 35 kyr. A) The present day topography, B) the magnitude of surface uplift and subsidence over the past 35 kyr, C) the paleotopography at 35 Ka and D) present day precipitation rates.'
# Describe the conditions/parameters for the models in a table or image
conditions:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/08/Table.png'
  table:
  description: 'Uniform erodibility coefficient and diffprop values.'


# Give text for model results
result:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/08/ResultsW.jpg'
  description: 'Sediment accumulation in the marine environment for A) the start of the simulation at 35 Ka, B) the end of Marine Isotope Stage 3 (MIS3), C) the end of MIS2 and D) present day.'

# Give citation or DOI for paper
citation:

# Online pointer to your model (Git/Binder/FTP etc.)
model_url: 

# Hashable search terms
keywords: ''

# Model location coordinates
location:
  title: Gulf of Papua - uniform erodibility coefficient
  image: https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/08/Initial.png
  url: 'https://atlas.bgh.org.au/gulf-of-papua/'
  latitude: -7.9
  longitude: 140.35

map: "true"

# Contact
contact: 
---

{{ page.location.url | replace: '!SITE_URL!', site.baseurl  | replace: '!POST_URL!', page.path }}