---
# Please do not change layout field 
layout: model

# Give your model name
model_name: 'Uncertainty of Tectonic Reconstructions by Plate ID'

# Tell us about the authors. In case of more than one: 'X, Y, Z'
author: 
  - 'Ben R. Mather - EarthByte Group, The University of Sydney'

# Tell us the software used for the model. Softwares include Underworld, Badlands, Badlands-Underworld, Badlands-GPlates-CitcomS
software: 'pyGPlates' # 

# Tell us about the particular version of software. In case of multiple, mention them in a list format by adding a bullet dash in the next line as shown
version: 
  - 'pyGPlates rev. 22'

# Provide a category from Depositional, Tectonic or Coupled
category: 'surface processes' 

# Provide a sub category such as Compression, Extension, Strike-slip, Conceptual, Case-study.
subcategory: 'Conceptual'

# Provide a thumbnail image to be displayed with the list entry.  
thumbnail: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2020/01/PlateID_assignment_unstructured.png'

# Please do not change the icon field
icon: 'globe'
  
# Provide an animation video (mp4) to display along with a description
animation:
  mp4: "https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2020/01/uncertainty_pid.mp4"
  description: 'The animation depicts the difference between various plate reconstructions through time'

# Provide an image to display for the model setup along with a description
model_setup:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2020/01/PlateID_assignment_unstructured.png'
  description: 'We seed a bunch of points on the sphere using the legendary spherical meshing package, stripy (https://www.github.com/underworldcode/stripy), that remain static through time as we query the plate ID at each lat/lon coordinate through time using pyGPlates. Iterating through a wide selection of plate reconstructions, we determine where on the sphere the plate IDs match and where they do not. A score is kept for how many reconstructions have contradicting plate IDs - i.e. if a point at 142,35 (lon/lat) has a different plate ID for 3 reconstructions, then it is assigned an uncertainty rating of 3.'

# Describe the conditions/parameters for the models in a table or image or both along with a description
conditions:
  url: ''
  table:
  - Rotation files: Global EarthByte model
    Year: 2019
    Published: Tectonics
    Valid range: 250 - 0 Ma
  - Rotation files: Matthews et al.
    Year: 2016
    Published: Global and Planetary Change
    Valid range: 410 - 0 Ma
  - Rotation files: Muller et al. (AREPS)
    Year: 2015
    Published: Annual Reviews of Earth and Planetary Science
    Valid range: 230 - 0 Ma
  - Rotation files: Shephard et al.
    Year: 2013
    Published: Earth Science Reviews
    Valid range: 200 - 0 Ma
  - Rotation files: Seton et al.
    Year: 2012
    Published: Earth Science Reviews
    Valid range: 200 - 0 Ma
  - Rotation files: Gurnis et al. (Caltech)
    Year: 2012
    Published: Computers & Geoscience
    Valid range: 140 - 0 Ma


  description: ''

# Provide results in an image and a text description
result:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2020/01/uncertainty_rating_unstructured.png'
  description: 'It is not unexpected that the greatest different rotation models occurs at plate boundaries. Also, it is clear that the plate IDs assigned to certain continents have changed as plate reconstructions are updated. A caveat is that rotations of the plates with respect to the absolute reference frame are not captured, just the region occupied by a plate. Nonetheless this is a useful tool to compare how a plate reconstruction stacks up against others. It is a good validation experiment to examine whether any new plate reconstruction is wildly different to those that came before.'

# Provide citation or DOI for paper
citation: 'Ben R. Mather, 2020:'

# Online pointer to your model resources (Git/Binder/FTP etc.)
model_url: 'doi:'

# Hashable search terms to be used to make the models more discoverable
keywords: 'pyGPlates, stripy' 

# Model location coordinates (near approximation)
location:
  title: Location Pakistan
  url: '!SITE_URL!/!POST_URL!/'
  url_text: View Model 
  latitude: 30
  longitude: 69

map: "true"
# Contact details for corresponding authors
contact:
---
