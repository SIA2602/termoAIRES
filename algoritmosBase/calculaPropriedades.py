import CoolProp as CP
from CoolProp.CoolProp import PropsSI

def celsiusToKelvin(celsius):
	return(celsius + 273.15)

def kelvinToCelsius(kelvin):
	return(kelvin - 273.15)

def barToPascal(bar):
	return (bar*100000.0)

m = 123 #[kg/h]
T_liq = celsiusToKelvin(53)
T_suc = celsiusToKelvin(12.4)
P_suc_comp = barToPascal(2.1 + 1.02)
P_liq_comp = barToPascal(15.6 + 1.02)

T_sat_evap = PropsSI('T', 'P', P_suc_comp, 'Q', 1, 'R134a')
print('T_sat_evap = ', round(kelvinToCelsius(T_sat_evap),2), u"\u00B0"+'C')

T_sat_liq = PropsSI('T', 'P', P_liq_comp, 'Q', 1, 'R134a')
print('T_sat_liq = ', round(kelvinToCelsius(T_sat_liq),2), u"\u00B0"+'C')

h1 = PropsSI('H', 'P', P_suc_comp, 'Q', 1, 'R134a')
print('h1 = ', round(h1/1000.,2), 'kJ/kg')

h3 = PropsSI('H', 'T', T_liq, 'Q', 0, 'R134a')
print('h3 = ', round(h3/1000.,2), 'kJ/kg')

subResfriamento = T_sat_liq - T_liq
print('subResfriamento = ', round(subResfriamento,2), 'K')

superAquecimento = T_suc - T_sat_evap
print('superAquecimento = ', round(superAquecimento,2), 'K')

Q_evap = m*((h1-h3)/1000.0)/3600.
print('Q_evap = ', Q_evap, 'kW')