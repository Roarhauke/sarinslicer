#temp delete

import loadsettings
sets = loadsettings.loadSetFromFile("presets/test.json")
print(sets.name)
print(sets.volx)
print(sets.voly)
print(sets.volz)
print(sets.maxspeed)
print(sets.prefspeed)