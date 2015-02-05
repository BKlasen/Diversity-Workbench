long_lat = "Lat"  # -- diesen Wert in Long ändern, wenn die andere Spalte berechnet werden soll.

v = cells[long_lat]["value"].replace('~','').replace(',','.').strip()

if '-' in v and v[0]!='-':
	v = v.split('-')[0]
v = v.split('°')


if len(v)==1:
	[deg, sign] = v[0].split(' ')
	deg = float(deg)
	min = 0.0
	sec = 0.0
else:
	deg = float(v[0])
	if v[1] in ('E','W','N','S'):
		min = 0.0
		sec = 0.0
		sign = v[1]
	else:
		min = float(v[1].split("'")[0])/60.0
		residue = v[1].split("'")[1:]

		sec = 0.0

		if len(residue)>2:
			sec = float(residue[0])/60/60
			sign = residue[2]
		elif len(residue)==2:
			sec = float(residue[0])
			sign = residue[1]
		elif len(residue)==1:
			sign = residue[0]
		else:
			sign = 'X'  # -- assume positive direction

if sign in ('S', 'W'):
	sign = -1.0
else:
	sign=1.0


return round((deg+min+sec)*sign,5)

