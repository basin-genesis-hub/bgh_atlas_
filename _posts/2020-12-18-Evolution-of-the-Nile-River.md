---
# Please do not change layout field and please make sure this file has a .md extension and please write all content with the '---' section.
layout: model

# Privacy (Public or Private)
privacy: public

# Give your model name
model_name: 'The influence of dynamic topography, climate, and tectonics on the Nile River source-to-sink system'

# Tell us about the authors. In case more than one please note them down as: 'X, Y, Z - Organization'
author: 
  - 'Christopher Alfonso, Tristan Salles, Claire Mallard, Sabin Zahirovic - BGH and EarthByte Research Group, The University of Sydney'

# Tell us the software used for the model. Currently software options include Underworld, Badlands, Badlands-Underworld, Badlands-GPlates-CitcomS & pyGPlates
software: 'Badlands'

# Tell us about the particular version of software. In case of multiple, mention them in a list format by adding a bullet dash in the next line as shown
version: 'Badlands v2.0.25'

# Provide a category from Depositional, Tectonic or Coupled
category: 'Depositional' 

# Provide a sub category such as Compression, Extension, Strike-slip, Conceptual, Case-study.
subcategory: 'Case-study'

# Provide a thumbnail image to be displayed with the list entry.  
thumbnail: 'https://raw.githubusercontent.com/cpalfonso/Nile-honours/main/results/thumbnail.png'

# Please do not change the icon field and leave it as 'globe'
icon: 'globe'
  
# Provide an animation video (mp4) to display along with a description
animation:
  mp4: "https://raw.githubusercontent.com/cpalfonso/Nile-honours/main/results/animation.mp4"
  description: ''

# Provide an image to display for the model setup along with a description
model_setup:
  url: 'https://raw.githubusercontent.com/cpalfonso/Nile-honours/main/inputs/fig.png'
  description: 'This is a sample of the Badlands landscape evolution models created for the Honours thesis of Christopher Alfonso (2020). These experiments were designed to test the possible impact of different dynamic topography scenarios on the evolution of the Nile River and Delta, as raised by Faccenna et al. (2019; Nature Geoscience, v. 12, no. 12, p. 1012-1017). The tested dynamic topography scenarios were obtained from Hassan et al. (2015; G-Cubed, v. 16, no. 5, p. 1465-1489) and Hassan et al. (2020; Geoscience Frontiers, v. 11, no. 5, p. 1669-1680). The landscape evolution models encompassed the northeast corner of Africa, including the Arabian Peninsula, and covered the past 40 Myr.'

# Describe the conditions/parameters for the models in a table or image or both along with a description. Table is populated row-wise with each bullet point.
conditions:
  url: ''
  table:
  - Parameter: Model time (Ma)
    Value: 40–0
  - Parameter: Maximum time step (Myr)
    Value: 0.2
  - Parameter: m (Stream Power law)
    Value: 0.5
  - Parameter: n (Stream Power law)
    Value: 1.0
  - Parameter: Erodibility (Kd; Stream Power law)
    Value: 3.0e-07
  - Parameter: Critical slope to force alluvial plain deposition
    Value: 0.001
  - Parameter: Maximum alluvial plain deposition (%)
    Value: 75
  - Parameter: Number of steps used for submarine sediment deposition (diffnb)
    Value: 5
  - Parameter: Maximum submarine sediment deposition (%; diffprop)
    Value: 0.05
  - Parameter: Subaerial diffusion coefficient (Khl; Soil Creep law)
    Value: 0.25
  - Parameter: Submarine diffusion coefficient (Khl; Soil Creep law)
    Value: 0.5
  - Parameter: Submarine diffusion coefficient for river-transported sediments (Khl; Soil Creep law)
    Value: 5.0
  - Parameter: Sediment surface porosity (%)
    Value: 61.6
  - Parameter: Sediment porosity exponential coefficient (/km)
    Value: 0.486
  - Parameter: Mantle density (kg/m^3; for gFlex calculations)
    Value: 3375
  - Parameter: Sediment density (kg/m^3; for gFlex calculations)
    Value: 2670
  - Parameter: Young's Modulus (GPa; for gFlex calculations)
    Value: 175.0


  description: 'Paleoprecipitation maps were obtained from the global paleoclimate reconstructions of Valdes et al. (2021; Climates of the Past, no. 3-4), modified according to local climate proxies (e.g. palynology). Vertical motions were derived from published global dynamic topography models, combined with tectonic activity approximated using a range of proxies; these proxies included unroofing estimates calculated from thermochronological data and estimates of the total original thickness of the c. 31 Ma flood basalts which cover the Ethiopian Plateau. Horizontal plate motions were incorporated into the models, derived from the global plate reconstructions used to produce the dynamic topography scenarios. The preferred model, presented here, used a hybrid dynamic topography scenario, derived primarily from the model M3 of Hassan et al. (2015) and incorporating the Afar Plume signal from the model M2 of Hassan et al. (2020). For more information on the input parameters used, see the model GitHub page (<a href="https://github.com/cpalfonso/Nile-honours">https://github.com/cpalfonso/Nile-honours</a>).'

# Provide results in an image and a text description
result:
  url: 'https://raw.githubusercontent.com/cpalfonso/Nile-honours/main/results/fig.png'
  description: "These experiments demonstrated that dynamic subsidence in North Africa, caused by the subducting Tethyan slab to the north, was crucial to the formation and longevity of the Nile over 30-40 Myr. In the upper Nile catchment, the effects of the Afar Plume provided a strong control on the river's evolution. Erosion of the plume-related Ethiopian Plateau flood basalts supplied a huge volume of sediment to the early Nile. Furthermore, changes in dynamic topography associated with the plume's motion relative to the African plate influenced erosion rates, sediment supply, and the morphology of the Nile drainage network."

# Provide citation or DOI for paper
citation: 'https://doi.org/10.5281/zenodo.4321852'

# Online pointer to your model resources (Git/Binder/FTP etc.)
model_url: 'https://github.com/cpalfonso/Nile-honours'

# Hashable search terms to be used to make the models more discoverable
keywords: 'Nile Dynamic Topography' 

# Model location coordinates (near approximation)
location:
  title: Evolution of the Nile River
  image:
  url: https://members.atlas.bgh.org.au/Evolution-of-the-Nile-River/
  url_text: View Model 
  latitude: 14.5
  longitude: 34.0

map: "true"

# Contact details for corresponding authors
contact:
  - 'calf6244@uni.sydney.edu.au'
  - 'tristan.salles@sydney.edu.au'
  - 'claire.mallard@sydney.edu.au'
  - 'sabin.zahirovic@sydney.edu.au'
---
