import math
import matplotlib.pyplot as plt

#Colors
Green = '\033[92m'
Red = '\033[91m'
Reset = '\033[0m' 



# AEROLAB - AeroCalc v5 (i think)
print(f'{Green}  Welcome to AEROLAB AeroCalc   {Reset}')

print('Please choose an aircraft:')

print('1. F-16 (fighter jet)')
print('2. Cessna 172 (general aviation)')
print('3. ASK 21 (glider)')
print('4. L-39NG Skyfox (Mostly Jet trainer)')
print('5. Boeing 737-800 (Commercial airliner)')


choice = input('Enter the number (1, 2, 3, 4 or 5):')


# 1. F-16 
if choice == '1':
    plane_name = 'F-16'
    wing_area = 27.87   # m^2
    CL = 1.6           #lift coefficient
    CD = 0.0175         #drag coefficient
    empty_mass = 9207   #kg
    max_thrust = 131000 #N (with afterburner)

    print('\nChoose F-16 Loadout:')
    print('a. Clean (Light fuel, no weapons)')
    print('b. CAP (Air-to-Air: 2x AIM-9, 2x AIM-120, Centerline Tank)')
    print('c. SEAD (Anti-radar: 2x AGM-88 HARM, 2x AIM-120, ECM pod, 2x fuel tanks)')
    print('d. Strike (Bombs: 4x GBU-12 JDAM, 2x AIM-120, 2x Wing tanks)')
    print('e. CAS (Close Air Support: 4x GBU-12, 2x AIM-9, TGP pod, Centerline Tank)')
    print('f. Custom (Enter your own weight)')

    loadout = input('Enter letter (a-f):')

    # Empty F-16 is about 9200kg
    # Internal fuel (about 3200kg)
    base_mass = 9207 + 3200

    if loadout == 'a':
        extra_mass = 0 # no weapons just internal fuel 
        loadout_name = 'Clean'

    elif loadout == 'b':
        extra_mass = 170 + 304 + 1000 #Aim-9s + Aim-120s + tank
        loadout_name = 'CAP'

    elif loadout == 'c':
        extra_mass = 722 + 304 + 465 + 2000 #Harms + Aim-120s + ECM + Tanks
        loadout_name = 'SEAD'

    elif loadout == 'd':
        extra_mass = 1108 + 304 + 2000 # GBUs + Aim-120s + Tanks
        loadout_name = 'Strike'

    elif loadout == 'e':
        extra_mass = 1108 + 170 + 200 + 1000 # GBUs + Aim-9s + TGP + Tank 
        loadout_name = 'CAS'

    elif loadout == 'f':
        print('\n   Custom loadout   ')
        extra_mass = float(input('Enter extra weight for weapons/fuel (kg):')) 
        loadout_name = 'Custom'

    else:
        print(f'{Red}\nInvalid loadout letter dummy. Defaulting to CAP (Air-to-Air) loadout{Reset}')
        extra_mass = 170 + 304 + 1000
        loadout_name = 'CAP (Default)'


    # Final calculation
    mass = base_mass + extra_mass
    print(f'\nYou selected F-16 with {loadout_name} loadout')
    print(f'Total mass: {mass} kg')

# 2. Cessna setup
elif choice == '2':
    plane_name = 'Cessna 172'
    wing_area = 16.2
    CL = 1.5
    CD = 0.03
    empty_mass = 771
    max_thrust = 2600

    print('\nChoose Cessna Loadout:')
    print('a. Standard (Pilot + Fuel)')
    print('b. Dogfight mode (2x AIM-9)')

    cessna_choice = input('Enter  letter (a or b):')

    if cessna_choice == 'b':
        mass = empty_mass + 229 + 170 # Pilots + fuel + Weapons
        loadout_name = 'Dogfight mode'
        print(f'{Red}\nWarning: you put AMRAAMs on Cessna{Reset}')
    else:
        mass = empty_mass + 229
        loadout_name = 'Standard'

#   3. Glider
elif choice =='3':
    plane_name = 'ASK 21'
    wing_area = 17.95
    CL = 1.0 
    CD = 0.015
    empty_mass = 360
    max_thrust = 0

    print('\nChoose ASK 21 Loadout:')
    print('a. Instructor + YOU (Standard)')
    print('b. Instructor + Gun Pod (For making runway anywhere)')

    glider_choice = input('Enter letter (a or b):')

    if glider_choice == 'b':
        mass = empty_mass + 140 + 200
        loadout_name = 'Mass destruction'

    else:
        mass = empty_mass + 140
        loadout_name = 'Instructor + YOU'

#   4. L-39NG Skyfox
elif choice == '4':
    plane_name = 'L-39NG Skyfox'
    wing_area = 19.2
    CL = 1.4
    CD = 0.02
    empty_mass = 3100
    max_thrust = 16870

    print('\nChoose L-39s Loadout:')
    print('a. Trainer (Clean, light fuel)')
    print('b. Air-To-Air (2x AIM-9)')
    print('c. Ground Attack (Rockets and bombs)')

    l39_choice = input('Enter letter (a, b or c):')

    base_mass = 3100 + 1500 #internal fuel

    if l39_choice == 'a':
        extra_mass = 0
        loadout_name = 'Trainer'
    elif l39_choice == 'b':
        extra_mass = 170 #Aim 9s
        loadout_name = 'Air-to-Air'
    elif l39_choice == 'c':
        extra_mass = 500
        loadout_name = 'Ground Attack'
    else:
        print(f'{Red}\nInvalid-Defaulting to Trainer{Reset}')
        extra_mass = 0
        loadout_name = 'Trainer (Default)'

    mass = base_mass + extra_mass
    print(f'\nYou selected L-39NG with {loadout_name} loadout')
    print(f'Total mass: {mass} kg')

# 5. 737
elif choice == '5':
    plane_name = 'Boeing 737-800'  
    wing_area = 124.6
    CL = 1.4
    CD = 0.022
    empty_mass = 41413
    max_thrust = 242000

    print('\nChoose Boeing 737 loadout:')
    print('a. Passanger (Full passangers, baggage and fuel)')
    print('b. Without passangers (Empty plane, max fuel) ')
    print('c Empty, Half fuel')


    boeing_choice = input('Enter letter (a, b or c):')

    if boeing_choice == 'a':
        mass = empty_mass + 20000
        loadout_name = 'Passangers'
    elif boeing_choice == 'b':
        mass = empty_mass + 20800
        loadout_name = 'Without passangers'
    else:
        mass = empty_mass + 10400
        loadout_name = 'Half fuel, Empty'


else:
    print(f'{Red}Invalid aircraft choice - Defaulting to Cessna 172{Reset}')
    plane_name = 'Cessna 172'
    wing_area  = 16.2
    CL = 1.5
    CD = 0.03
    mass = 1000
    max_thrust = 2600
    loadout_name = 'Standard'

print(f'\n{Green}You selected: {plane_name} ({loadout_name}) | Mass: {mass} kg{Reset}')

#Flight conditions
print(f'\n   Flight Conditions for {plane_name}   ')
velocity = float(input('Enter velocity (m/s):'))
altitude = float(input('Enter altitude (m):'))

#Calculations
g = 9.81
air_density = 1.225 * math.exp(-altitude / 8500)
dynamic_pressure = 0.5 * air_density * (velocity ** 2)

lift = dynamic_pressure * wing_area * CL
drag = dynamic_pressure * wing_area * CD
weight = mass * g

ld_ratio = lift / drag 
stall_speed_ms = math.sqrt((2 * weight) / (air_density * wing_area * CL))
wing_loading = mass / wing_area


velocity_knots = velocity / 0.514444
velocity_kmh = velocity * 3.6
altitude_feet = altitude / 0.3048
stall_speed_knots = stall_speed_ms / 0.514444
stall_speed_kmh = stall_speed_ms * 3.6

if max_thrust > drag and weight > 0:
    excess_power = (max_thrust - drag) * velocity
    climb_rate_ms = excess_power / weight
    climb_rate_ftmin = climb_rate_ms * 196.85
else:
    climb_rate_ms = 0
    climb_rate_ftmin = 0

if max_thrust == 0:
    glide_distance_km = (altitude * ld_ratio) / 1000
else:
    glide_distance_km = 0

# Results
print(f'{Green}\n   Results for {plane_name} ({loadout_name})   {Reset}')
print(f'Total Mass: {mass} kg')
print(f'Air Density: {air_density:.3f} kg/m3')
print(f'Dynamic Pressure: {dynamic_pressure:.2f} Pa')
print(f'Weight (Gravity): {weight:.2f} N')
print(f'Lift: {lift:.2f} N')
print(f'Drag: {drag:.2f} N')
print(f'L/D Ratio: {ld_ratio:.2f}')
print(f'Wing loading: {wing_loading:.2f} kg/m2')


print('\n   Speeds   ')
print(f'Velocity: {velocity:.1f} m/s | {velocity_knots:.1f} knots | {velocity_kmh:.1f} km/h')
print(f'Stall Speed: {stall_speed_ms:.1f} ms | {stall_speed_knots:.1f} knots | {stall_speed_kmh:.1f} km/h')

print('\n   Altitude and Performance   ')
print(f'Altitude {altitude:.1f} m | {altitude_feet:.1f} feet')
if max_thrust > 0:
    print(f'Climb rate: {climb_rate_ms:.2f} m/s | {climb_rate_ftmin:.0f} ft/min')
else:
    print(f'Glide distance from this altitude: {glide_distance_km:.2f} km')

if lift > weight:
    print(f'\n{Green}Status: Lift > Weight - Aircraft can climb{Reset}')
else:
    print(f'\n{Red}Status: Lift < Weight - Aircraft is falling!{Reset}')

# Graph
print(f'{Green}\nOpening graph... (close it to end and see results){Reset}')

speeds = []
lifts = []
drags = []
thrusts = []

for v in range(10, 251, 10):
    speeds.append(v)
    q = 0.5 * air_density * (v ** 2)
    lifts.append(q * wing_area * CL)
    drags.append(q * wing_area * CD)
    thrusts.append(max_thrust)

plt.plot(speeds, lifts, color = 'blue', label='Lift')
plt.plot(speeds, drags, color = 'orange', label = 'Drag')
plt.axhline(y=weight, color = 'red', linestyle = '--', label = 'Weight')
if max_thrust > 0:
    plt.axhline(y=max_thrust, color = 'green', linestyle = ':', label ='Max Thrust')

plt.axvline(x=stall_speed_ms, color = 'purple', linestyle='-.', label = 'Stall speed')


plt.title(f'Forces vs Velocity - {plane_name}')
plt.xlabel('Velocity (m/s)')
plt.ylabel('Force (N)')
plt.grid(True)
plt.legend()

plt.show()


print(f'{Green}Graph closed {Reset}')
print(f'{Green}PLEASE SCROLL BIT UP IN THIS TERMINAL TO SEE THE RESULTS{Reset}!And thanks for playing it!')











 