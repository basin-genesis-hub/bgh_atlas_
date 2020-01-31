---
# Please do not change layout field 
layout: model

# Give your model name
model_name: 'Gippsland Basin'

# Tell us about the authors. In case of more than one: 'X, Y, Z'
author: 
  - 'Xuemei(Linda) Yang, Greg Smith'

# Tell us the software used for the model. Softwares include Underworld, Badlands, Badlands-Underworld, Badlands-GPlates-CitcomS
software: 'Badlands' # 

# Tell us about the particular version of software. In case of multiple, mention them in a list format by adding a bullet dash in the next line as shown
version: 
  - 'Badlands 1.0'

# Provide a category from Depositional, Tectonic or Coupled
category: 'Depositional & Tectonic' 

# Provide a sub category such as Compression, Extension, Strike-slip, Conceptual, Case-study.
subcategory: 'Case-study'

# Provide a thumbnail image to be displayed with the list entry.  
thumbnail: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/09/0.png'

# Please do not change the icon field
icon: 'globe'
  
# Provide an animation video (mp4) to display along with a description
animation:
  mp4: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/09/Gippsland_model.mp4'
  description: 'The model simulates the geological history of the Gippsland Basin, constrained by a realistic 3D structural and stratigraphic model built in Petrel software. The aim is to assess and calibrate the theoretical tectonic and sedimentary models using empirical data for a rift basin.  The Badlands models are used to assess and measure the relative effect of significant variables for sedimentary basins, including: extension, subsidence, uplift, erosion, climate, sea level change and sedimentation of non-marine, marine, shelf and carbonate sequences.'

# Provide an image to display for the model setup along with a description
model_setup:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/09/model-setup.jpg'
  description: 'The thickness maps are input as burial displacement maps to simulate extension/subsidence history. The input maps are generated from the 3D realistic Petrel model.  This model is based on seismic interpretation of all the open file 3D and 2D seismic surveys and correlation of over 250 offshore wells and more than 1000 onshore wells or bores. The interpreted seismic surfaces and well data are used to create thickness maps between the main horizons (e.g. topography, mid Miocene, top Latrobe Group, base Tertiary, top Strzelecki Group, top Basement).'

# Describe the conditions/parameters for the models in a table or image or both along with a description
conditions:
  url: ''
  table:
  - Uncertainties/Variables: Non Marine Erodibility
    Parameter: erodibility
    value: 2.e-7
  - Uncertainties/Variables: Rainfall
    Parameter: precipitation [m/a]
    value: ∝ Elevation
  - Uncertainties/Variables: (Rainfall * Area) exponent m
    Parameter: m
    value: 0.5
  - Uncertainties/Variables: Slope exponent n
    Parameter: n
    value: 1.2
  - Uncertainties/Variables: Slope Minimum for Flood-plain Deposition
    Parameter: slp_cr
    value: 0.001
  - Uncertainties/Variables: Non-Marine % Max Deposition
    Parameter: perc_dep
    value: 0.4
  - Uncertainties/Variables: Land sed. Transport by River
    Parameter: criver
    value: 10
  - Uncertainties/Variables: Land sed. Transport by Wind
    Parameter: caerial
    value: 0.001
  - Uncertainties/Variables: Lake/Sea sed. Transport by Currents
    Parameter: cmarine
    value: 0.005
  - Uncertainties/Variables: No. Time Steps To Distribute Marine Deposits
    Parameter: diffnb
    value: 40
  - Uncertainties/Variables: Marine % Max Deposition
    Parameter: diffprop
    value: 0.000005

  description: ''

# Provide results in an image and a text description
result:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/09/Gippsland.png'
  description: 'The modelling results indicate several insights for the Gippsland Basin.  The initial paleo-topography at ~137 Ma comprised extensive highlands covering the entire region.  The Early Cretaceous paleo-environment was intracratonic, with sediment transport from east to west, and in the late Early Cretaceous included an inland sea. The Mid Cretaceous uplift caused emergence of the entire basin, substantial regional erosion and changed the basin architecture. Subsidence associated with Tasman Sea rifting formed the Central Deep and flipped the fluvial paleo-drainage system towards the east. Latrobe Group sediments then filled the basin, the early Late Cretaceous fluvial and lacustrine sediments (including potential source rocks and good sandstone reservoirs) being progressively transgressed by marginal marine and marine sediments with rising sea levels to flood most areas by the Oligocene. Since then non-marine sediments, dominated by thick coals, were confined to the west behind a thick aggrading and prograding carbonate shelf incised by deep submarine canyons. The very rapid burial of the Latrobe Group was accompanied by slow inversion which resulted in generation, migration and entrapment of substantial hydrocarbons in large anticlines and unconformity traps.'

# Provide citation or DOI for paper
citation: ''

# Online pointer to your model resources (Git/Binder/FTP etc.)
model_url: ''

# Hashable search terms to be used to make the models more discoverable
keywords: '' 

# Model location coordinates (near approximation)
location: 
  latitude: -37.8136
  longitude: 144.9631

# Contact details for corresponding authors
contact: xuemei.yang@postgrad.curtin.edu.au ; gregory.c.smith@curtin.edu.au
---
