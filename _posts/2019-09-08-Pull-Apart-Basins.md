---
# Please do not change layout field 
layout: model

# Give your model name
model_name: 'Pull Apart Basins'

# Tell us about the authors. In case of more than one: 'X, Y, Z'
author: 
  - 'Patrice F. Rey, Tristan Salles, Claire Mallard, Luke Hardiman, Romain Beucher - BGH and Earthbyte Research Group, The University of Sydney, patrice.rey@sydney.edu.au'

# Tell us the software used for the model. Softwares include Underworld, Badlands, Badlands-Underworld, Badlands-GPlates-CitcomS
software: 'Badlands-Underworld' 

# Tell us about the particular version of software. In case of multiple, mention them in a list format by adding a bullet dash in the next line as shown
version: 
  - 'Underworld 1.8 and Underworld Geodynamics'
  - 'Badlands 1.0'

# Provide a category from Depositional, Tectonic or Coupled
category: 'Coupled' 

# Provide a sub category such as Compression, Extension, Strike-slip, Conceptual, Case-study.
subcategory: 'Strike-slip'

# Provide a thumbnail image to be displayed with the list entry.  
thumbnail: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/09/PA000x0055.jpg'

# Please do not change the icon field
icon: 'globe'
  
# Provide an animation video (mp4) to display along with a description
animation:
  mp4: "https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/09/A_PA000x.mp4"
  description: ''

# Provide an image to display for the model setup along with a description
model_setup:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/09/PA00xBC.png'
  description: 'Pull apart is an ideal tectonic setting to test the coupling between tectonic processes and surface processes. In this setting, lithospheric thinning can be extreme and localized, leading to very deep basins and thick accumulation of sediments. We hypothese that the redistribution of surface load from source-to-sink modulates the stress field in the upper crust where faults and fractures initiate and control the architecture of sedimentary basins. In this suite of experiments, we compare the same experiment with and without surface processes, and we consider a variety of scenario varying sea-level (-200m, -500m, -800m with respect to the position of the surface of the crust), and the rheology of the lithosphere. The dimension of the model is 384x256x128 km. It includes 8 km of air-like material, 40 km of crust (upper crust is in blue, lower crust in orange), 60 km of lithospheric mantle (green), and 20 km of asthenosphere (blue). Two vertical and parallel master faults are embedded into the lithosphere in the form of two pre-damaged prism with dimension 192x25x95 km, extending from 5 km below the surface of the crust down to base of the lithosphere. The damage inside these prisms follows a gaussian with peak damage in the center of the prism along the X and Y axes. These two faults are non-overlapping. Their walls and tips are separated by a gap of 48 km and 0 km respectively (see Figure above). A kinematic boundary condition designed to promote transcurrent tectonics is imposed on the two vertical walls normal to the X direction. The velocity component along X is ±1.92 cm/yr (see Figure), and we impose a velocity component along Z of 0.025 cm/yr to prevent rivers to fall off the grid. A free slip condition is attached to the base of the model and to the two vertical walls parallel to the direction of motion. A pseudo-isostatic boundary condition is imposed at the base of the model. Models are run for 10 myr. We have run this experiment using three numerical framework: Underworld 1.8, Underworld Geodynamics, and Badlands-Underworld Geodynamics. The Underworld 1.8 outputs were used to extract the velocity field close to the crust surface, and pass it into Badlands. The outcome of this "one way coupling" is presented in Luke Hardiman Honours thesis.'

# Describe the conditions/parameters for the models in a table or image or both along with a description
conditions:
  url: ''
  table:
  - Parameters (SI):  
    Sediments:
    Upper Crust 0-4-8-12-16 km: 
    Lower Crust 16-28-40 km:
    Litho Mantle 40-100 km:
    Asthe Mantle 100-120 km:
  - Parameters (SI):  Reference density (kg m-3)
    Sediments: 2300
    Upper Crust 0-4-8-12-16 km: 2500, 2540, 2150, 2620
    Lower Crust 16-28-40 km: 2750, 2850
    Litho Mantle 40-100 km: 3370
    Asthe Mantle 100-120 km: 3395
  - Parameters (SI): Thermal expansivity (K-1)
    Sediments: 3e-5
    Upper Crust 0-4-8-12-16 km: 3e-5
    Lower Crust 16-28-40 km: 3e-5
    Litho Mantle 40-100 km: 3e-5
    Asthe Mantle 100-120 km: 3e-5
  - Parameters (SI):  Thermal diffusivity (m2 s-1)
    Sediments: 1e-6
    Upper Crust 0-4-8-12-16 km: 1e-6
    Lower Crust 16-28-40 km: 1e-6
    Litho Mantle 40-100 km: 1e-6
    Asthe Mantle 100-120 km: 1e-6
  - Parameters (SI):  Radiogenic heat production (microW m-3)
    Sediments: 0.95
    Upper Crust 0-4-8-12-16 km: 0.95, 0.85, 0.75, 0.65
    Lower Crust 16-28-40 km: 0.55, 0.45
    Litho Mantle 40-100 km: 0.02
    Asthe Mantle 100-120 km: 0.02
  - Parameters (SI):  Heat capacity (J K-1 kg-1)
    Sediments: 1000
    Upper Crust 0-4-8-12-16 km: 1000
    Lower Crust 16-28-40 km: 1000
    Litho Mantle 40-100 km: 1000
    Asthe Mantle 100-120 km: 1000
  - Parameters (SI): Max yield stress (MPa)
    Sediments : 500
    Upper Crust 0-4-8-12-16 km: 1000, 1000, 600, 1000
    Lower Crust 16-28-40 km: 1250, 1250
    Litho Mantle 40-100 km: 2000
    Asthe Mantle 100-120 km: 2000
  - Parameters (SI):  Initial cohesion (MPa)
    Sediments: 10
    Upper Crust 0-4-8-12-16 km: 10, 10, 10, 10
    Lower Crust 16-28-40 km: 20, 20
    Litho Mantle 40-100 km: 10
    Asthe Mantle 100-120 km: 10
  - Parameters (SI): Cohesion after weakening (MPa)
    Sediments: 2
    Upper Crust 0-4-8-12-16 km: 2, 2, 2, 2
    Lower Crust 16-28-40 km: 4, 4
    Litho Mantle 40-100 km: 2
    Asthe Mantle 100-120 km: 2
  - Parameters (SI): Coefficient of friction
    Sediments: 0.577
    Upper Crust 0-4-8-12-16 km: 0.577, 0.577, 0.577, 0.577
    Lower Crust 16-28-40 km: 0.577, 0.577
    Litho Mantle 40-100 km: 0.577
    Asthe Mantle 100-120 km: 0.577
  - Parameters (SI): Coefficient of friction after weakening 
    Sediments: 0.1154
    Upper Crust 0-4-8-12-16 km: 0.1154, 0.1154, 0.1154, 0.1154
    Lower Crust 16-28-40 km: 0.1154, 0.1154
    Litho Mantle 40-100 km: 0.1154
    Asthe Mantle 100-120 km: 0.1154
  - Parameters (SI):  Saturation strain (%)
    Sediments: 20
    Upper Crust 0-4-8-12-16 km: 20, 20, 20, 20
    Lower Crust 16-28-40 km: 20, 20
    Litho Mantle 40-100 km: 20
    Asthe Mantle 100-120 km: 20
  - Parameters (SI):  Activation energy (kJ mol-1)
    Sediments: 135
    Upper Crust 0-4-8-12-16 km: 135, 135, 135, 135
    Lower Crust 16-28-40 km: 244, 244
    Litho Mantle 40-100 km: 520
    Asthe Mantle 100-120 km: 520
  - Parameters (SI): Power law exponent
    Sediments: 3.1
    Upper Crust 0-4-8-12-16 km: 3.1, 3.1, 3.1, 3.1
    Lower Crust 16-28-40 km: 3.2, 3.2
    Litho Mantle 40-100 km: 3.5
    Asthe Mantle 100-120 km: 3.5
  - Parameters (SI): Pre-exponential factor (MPa-n s-1)
    Sediments: 6.607e-8  
    Upper Crust 0-4-8-12-16 km: 6.607e-8, 6.607e-8, 6.607e-8, 6.607e-8
    Lower Crust 16-28-40 km: 0.1, 0.1
    Litho Mantle 40-100 km: 1600
    Asthe Mantle 100-120 km: 1600
  - Parameters (SI): activation Volume (m3/mole)  
    Sediments: 0
    Upper Crust 0-4-8-12-16 km: 0, 0, 0, 0
    Lower Crust 16-28-40 km: 0, 0
    Litho Mantle 40-100 km: 0.00023
    Asthe Mantle 100-120 km: 0.00023 
  - Parameters (SI): waterFugacity   
    Sediments: NA
    Upper Crust 0-4-8-12-16 km: NA, NA, NA, NA
    Lower Crust 16-28-40 km: NA, NA
    Litho Mantle 40-100 km: 1000
    Asthe Mantle 100-120 km: 1000 
  - Parameters (SI): waterFugacity exponent 
    Sediments: NA 
    Upper Crust 0-4-8-12-16 km: NA, NA, NA, NA
    Lower Crust 16-28-40 km: NA, NA
    Litho Mantle 40-100 km: 1.2
    Asthe Mantle 100-120 km: 1.2 

  description: 'Air temperature is maintained at 273K, bottom temperature at 1603K.'

# Provide results in an image and a text description
result:
  url: 'https://www.earthbyte.org/BGH_Wordpress/wp-content/uploads/2019/09/Internal10myr.jpg'
  description: 'This model allows us to compare the outcomes of Underworld 1.8 and Underworld Geodynamics. We found that in Underworld 1.8 the fractures field is sharper with better defined faults that includes a range of fracture types (extensional fractures, shear fractures, ridel R and R prime). In comparison in Underworld Geodynamics the region of plastic deformation is far less detailed. In terms of stress differences ... '

# Provide citation or DOI for paper
citation: 'Rey, Salles, Mallard, Hardiman and Beucher 2019:'

# Online pointer to your model resources (Git/Binder/FTP etc.)
model_url: 'doi:'

# Hashable search terms to be used to make the models more discoverable
keywords: '' 

# Model location coordinates (near approximation)
location: 
  latitude: ''
  longitude: ''

# Contact details for corresponding authors
contact: patrice.rey@sydney.edu.au
---
