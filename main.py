# AEROLAB - AeroCalc
# Basic aerodynamic calculations
 
air_density = 1.225       # Air density (kg/m^3)
velocity = 50     # Velocity (m/s)
wing_area = 15   #Wing area (m^2)
CL = 0.8          # Lift coefficient
CD = 0.04         # Drag coefficient


dynamic_pressure = 0.5 * air_density * (velocity ** 2)
lift = dynamic_pressure * wing_area * CL
drag = dynamic_pressure * wing_area * CD



print('--- AEROLAB AeroCalc --- ')
print('Dynamic pressure:', round (dynamic_pressure, 2), 'Pa')
print('Lift:', round (lift, 2), 'N')
print('Drag:', round (drag, 2), 'N')
