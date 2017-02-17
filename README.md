
# Cloud Microphysics simulation

######My attempt at creating a cloud microphysics simulation

This is intended to be a simulation of how water droplets form and get large enough to eventually 
fallout of clouds as rain.

## Math Basis

The math basis for this program is the spontaneous condensation of cloud water droplets 
and the subsequent collision and coalescence of the droplets.

Math formula come from 

### Condensation Model

#### Role of Condensation Nuclei

### Collision Model
Condensation alone does not account for the presence of rain on the time scales typically observed.
This is because around r = 20 µm, the collisions of the droplets become important.

The volume of a sphere is given by: V=(4/3)π(r^3)

When two spheres collide, the new radius is given by r = (r_1^3 + r_2^3)^1/3 

This will be important when displaying the objects as 2D circles as the radius of the circles
will note simply add together as may be assumed. 
# References
"A Short Course in Cloud Physics" 3rd edition by
R. R. Rogers and M. K. Yau

#TODO

* Write some code - obviously.
* Get formula for all models
* How to create buttons, sliders, checkboxes and drop down menus
* Fill out math section on README.md


