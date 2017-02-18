
# Cloud Microphysics simulation

######My attempt at creating a cloud microphysics simulation

This is intended to be a simulation of how water droplets form and get large enough to eventually 
fallout of clouds as rain.

## Math Basis

The math basis for this program is the spontaneous condensation of cloud water droplets 
and the subsequent collision and coalescence of the droplets.

Math formula come from 

### Condensation Model
* Page 99

Growth of condensed water droplets is given by: 

r(t) = sqrt(r_o**2 + 2*E*t)

r_ o is original droplet size. E is a special parameter. 

E = 1/(F_k + F+_d) ==> this value is dependent on pressure and temperature. 

Can expand the above equations using the definitions F_k and F_d

F_k: Can be estimated as -1 to a good accuracy

F_d  = (p*R_v*T)/(D*e_s(T)) 

p: density of water = 1000 [kg/m**3]

R_v: gas constant for water vapor = 461 [J K−1 kg−1]

T: Temperature = varies, [K]

D: Molecular Diffusion Coefficient: at T=0C: 2.06*10**-5 (m**2)/s

NOTE** D varies with temperature and would need a more accurate solution to calculate 
to a better approximation

e_s(T): saturated vapor pressure at temperature

Sufficient for drops larger than r = 10 µm



#### Role of Condensation Nuclei
* Page 81-81

### Collision Model
Condensation alone does not account for the presence of rain on the time scales typically observed.
This is because around r = 20 µm, the collisions of the droplets become important.

The volume of a sphere is given by: V=(4/3)π(r^3)

When two spheres collide, the new radius is given by r = (r_1^3 + r_2^3)^1/3 

This will be important when displaying the objects as 2D circles as the radius of the circles
will note simply add together as may be assumed. 

### Falling Droplets 
The falling of cloud droplets is governed by the radius of the drop and the strength of the updraft
velocity. Given a radius, it should be simple issue of getting updraft and downdraft difference in order 
to calculate the movement. 

One issues facing the model is a lack of horizontal motion. In a real cloud the droplets would be moving about,
both in the vertical and horizontal directions due to mixing within the cloud. A slight random horizontal motion
may be able to keep the system from achieving stead state due to lack of horizontal motion. 
# References
"A Short Course in Cloud Physics" 3rd edition by
R. R. Rogers and M. K. Yau

#TODO

* Get formula for all models
* How to create buttons, sliders, checkboxes and drop down menus
* Fill out math section on README.md


