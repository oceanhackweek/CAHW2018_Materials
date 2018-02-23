# A common sonar data NetCDF file format

## Vision
Providing a common file format for storing active sonar data. **Active sonar** here refers to instruments that send out sounds into water and receive returning echoes. These include ADCP, scientific echosounders, and potentially multi-beam sonar in the future - need to find someone who's experienced with that. Scientific echosounders include Simrad EK60, EK80, ASL AZFP.

## Draft format
### dimensions --> all common for ADCP and sonar
- lat
- lon
- time [UTC time]
- depth [m]
- angle_alongship [degree]
- angle_athwardship [degree]
- frequency (?) **--> How to deal with EK80 data?**
- beam_number **--> ADCP only**

### variables
- power (what's a better name???): lat, lon, time, depth **--> key common variable between echosounder & ADCP**
- electronic_angle: lat, long, time --> split-beam echosounder only

### global attributes
- sounder_name
- survey_name
- transducer_count
- transect_name
- version
- absorption_coeff
- bandwidth
- channel --> remove
- frequency **--> here or dimensions?**
- pulse_length
- sample_interval
- sound_velocity
- temperature **--> remove, or can reserve for now**
- timestamp **--> ??? redundant? is this time at first ping?**
- transducer_depth
- transmit_power
- angle_offset_alongship
- angle_offset_athwart
- angle_sensitivity_alongship
- angle_sensitivity_athwartship
- beam_type
- beam_width_alongship
- beam_width_athwartship
- channel_id
- dir_x, dir_y, dir_z **--> what are these?**
- equiv_beam_angle
- gain
- gpt_software_version
- pos_x, pos_y, pos_z --> what are these?
- gain_table --> remove, already has gain
- pulse_length_table --> remove, already has pulse length
- sa_correction_table **--> substitute with sa**
