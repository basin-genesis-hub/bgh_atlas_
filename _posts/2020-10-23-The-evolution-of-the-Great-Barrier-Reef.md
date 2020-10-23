---
# Please do not change layout field and please make sure this file has a .md extension and please write all content with the '---' section.
layout: model

# Privacy (Public or Private)
privacy: public

# Give your model name
model_name: 'The evolution of the Great Barrier Reef'

# Tell us about the authors. In case of more than one please note them down as: 'X, Y, Z '
author: 
  - 'Amanda C. Thran , Madison East, Jody M. Webster , Tristan Salles, and Carole Petit'

# Tell us the software used for the model. Currently software options include Underworld, Badlands, Badlands-Underworld, Badlands-GPlates-CitcomS & pyGPlates
software: 'Badlands' 

# Tell us about the particular version of software. In case of multiple, mention them in a list format by adding a bullet dash in the next line as shown
version: 
  - 'Badlands 1.0'

# Provide a category from Depositional, Tectonic or Coupled
category: 'Depositional' 

# Provide a sub category such as Compression, Extension, Strike-slip, Conceptual, Case-study.
subcategory: ''

# Provide a thumbnail image to be displayed with the list entry.  
thumbnail: ''

# Please do not change the icon field and leave it as 'globe'
icon: 'globe'
  
# Provide an animation video (mp4) to display along with a description
animation:
  mp4: "https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2020/10/Noggin_361.mp4"
  description: 'This model simulates the geomorphological development and surface bedload processes on the Great Barrier Reef margin from the previous lowstand (~30 ka) to present. Erodibility was calibrated using sediment fluxes reported in the literature. Subsidence is considered negligible during this time, and present-day precipitation rates are used to force the model. The above simulation shows how the margin evolves over the course of the Holocene marine transgression, where the shelf becomes inundated and coral reefs (shown in orange) begin accreting on their antecedent platforms.'

# Provide an image to display for the model setup along with a description
model_setup:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2020/10/Fig.2.png'
  description: '(a) Original DEM spanning the computational domain. (b) Thickness representing the most recent Holocene reef growth on platforms. This layer was removed from the original DEM to produce the pre‐Holocene surface depicted in the next panel. (c) Smoothed pre‐Holocene topographic surface. (d) Artiﬁcial surface with carbonate platforms removed entirely.'

# Describe the conditions/parameters for the models in a table or image or both along with a description. Table is populated row-wise with each bullet point.
conditions:
  url: ''
  table:
  - Variables:  Non-Marine Erodibility
    Parameter: K_e
    Value: 1E-06
  - Variables:  Marine % Max Deposition
    Parameter:  diffprop
    Value: 0.01
  - Variables:  No. Time Steps To Distribute Marine Deposits
    Parameter:  diffnb
    Value: 5.
  - Variables:  Land sed. Transport by Wind
    Parameter:  caerial
    Value: 0.001
  - Variables:  Lake/Sea sed. Transport by Currents
    Parameter:  cmarine
    Value: 0.005
  - Variables:  Land sed. Transport by River  
    Parameter:  criver
    Value: 5.
    

  description: ''

# Provide results in an image and a text description
result:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2020/10/Fig.4.png'
  description: 'Drainage network evolution from lowstand (30 ka) to the beginning of the transgression (15 ka) for simulations containing carbonate platform topography (a) and no carbonate platforms (b). Major rivers and streams computed in the model are shown in blue, where drainage patterns at 30, 25, 20, and 15 ka are overlain over cumulative erosion and deposition over this period. Red areas around the carbonate platforms indicate deposition of both platform and ﬂuvial sediments.'

# Provide citation or DOI for paper
citation: 'https://doi.org/10.1029/2020GC008915'

# Online pointer to your model resources (Git/Binder/FTP etc.)
model_url: ''

# Hashable search terms to be used to make the models more discoverable
keywords: 'Sediment transport' 

# Model location coordinates (near approximation)
location:
  title: The evolution of the Great Artesian Basin
  image:
  url: ADD url
  url_text: View Model 
  latitude: -16
  longitude: 146

map: "true"

# Contact details for corresponding authors
contact: 'm.thran@unsw.edu.au'
---
