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
  mp4: "https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2020/10/Noggin_361-2.mp4"
  description: 'This model simulates the geomorphological development and surface bedload processes on the Great Barrier Reef margin from the previous lowstand (~30 ka) to present. Erodibility was calibrated using sediment fluxes reported in the literature. Subsidence is considered negligible during this time, and present-day precipitation rates are used to force the model. The above simulation shows how the margin evolves over the course of the Holocene marine transgression, where the shelf becomes inundated and coral reefs (shown in orange) begin accreting on their antecedent platforms.'

# Provide an image to display for the model setup along with a description
model_setup:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2020/10/Fig.2.png'
  description: 'Bathymetry and topography were extracted from a digital elevation model (DEM) spanning the entire Great Barrier Reef margin (3DGBR). This surface was used to construct a “pre-Holocene” surface and a “no platforms” surface. For the “pre-Holocene” surface, Holocene carbonate accretion by reefs is “shaved off” the platforms using a simplifying assumption (15 m total vertical accretion during the Holocene, derived from sediment cores). For the “no platforms” surface, platforms were removed from bathymetry and the continental shelf was smoothed. Subsidence is assumed to be minimal over the course of the simulation.(a) Original DEM spanning the computational domain. (b) Thickness representing the most recent Holocene reef growth on platforms. This layer was removed from the original DEM to produce the pre‐Holocene surface depicted in the next panel. (c) Smoothed pre‐Holocene topographic surface. (d) Artiﬁcial surface with carbonate platforms removed entirely.'

# Describe the conditions/parameters for the models in a table or image or both along with a description. Table is populated row-wise with each bullet point.
conditions:
  url: ''
  table:
  - Parameter:  Simulation start time (yrs)
    Value: -30000
  - Parameter:  Simulation end time (yrs)
    Value: 0
  - Parameter:  Maximum time step (yrs)
    Value: 100
  - Parameter:  Critical slope used to force deposition on alluvial plain (m/m)
    Value: 0.005
  - Parameter:  Maximum percentage deposition on alluvial plain
    Value: 50%
  - Parameter:  m (from Stream Power Law) 
    Value: 0.5
  - Parameter:  n (from Stream Power Law)
    Value: 1
  - Parameter:  Ke (land)
    Value: 9E-08
  - Parameter:  Ke (shelf and marine)
    Value: 7.5E-06
  - Parameter:  Critical density of water+sediment flux to trigger hyperpycnal (kg/m3)
    Value: 1000.025
  - Parameter:  Kd (land; m2/yr)
    Value: 0.0008
  - Parameter:  Kd (shelf and marine; m2/yr) 
    Value: 0.0001
  - Parameter:  Kd (landslides; m2/yr)
    Value: 0.2
  - Parameter:  Scaling parameter alpha
    Value: 2000
  - Parameter:  Critical slope to trigger landslide (m/m)
    Value: 0.25
  - Parameter:  Mean grain size diameter (mm; for wave module)
    Value: 0.1
  - Parameter:  Wave sediment diffusion coefficient
    Value: 50
  - Parameter:  Wave sediment entrainment coefficient 
    Value: 0.5
  - Parameter:  Maximum wave-induced erosion per time step (m)
    Value: 0.2
  - Parameter:  Maximum wave base (m)
    Value: 20
  - Parameter:  Significant wave height (m) 
    Value: 2.0
  - Parameter:  Predominant wave direction
    Value: West
  - Parameter:  Maximum vertical accretion rate (shallow coral assemblage)
    Value: 1.2 cm/yr
  - Parameter:  Maximum vertical accretion rate (deep coral assemblage)
    Value: 1.0 cm/yr
    

  description: ''

# Provide results in an image and a text description
result:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2020/10/Fig.4.png'
  description: 'Simulation shows the different configurations of river networks simulated from 30-15 ka (during the last lowstand). When reef platforms are present, rivers are diverted around the platforms and deposit their sediments within inter-platform passages. When reef platforms are removed, sediments are diffusely deposited on the upper continental slope. Drainage network evolution from lowstand (30 ka) to the beginning of the transgression (15 ka) for simulations containing carbonate platform topography (a) and no carbonate platforms (b). Major rivers and streams computed in the model are shown in blue, where drainage patterns at 30, 25, 20, and 15 ka are overlain over cumulative erosion and deposition over this period. Red areas around the carbonate platforms indicate deposition of both platform and ﬂuvial sediments.'

# Provide citation or DOI for paper
citation: 'doi.org/10.1029/2020GC008915'

# Online pointer to your model resources (Git/Binder/FTP etc.)
model_url: ''

# Hashable search terms to be used to make the models more discoverable
keywords: 'Sediment transport' 

# Model location coordinates (near approximation)
location:
  title: The evolution of the Great Artesian Basin
  image:
  url: 'https://atlas.bgh.org.au/The-evolution-of-the-Great-Barrier-Reef/'
  url_text: View Model 
  latitude: -16
  longitude: 146

map: "true"

# Contact details for corresponding authors
contact: 'm.thran@unsw.edu.au'
---
