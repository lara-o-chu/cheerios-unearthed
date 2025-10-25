from pybricks.tools import hub_menu

from blue_mission import run_blue_mission
from minecart_mission import run_minecart_mission
from pirate_boat import run_pirate_boat

# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("B", "M", "S")

# Based on the selection, run a program.
if selected == "B":
    run_blue_mission()
elif selected == "M":
    run_minecart_mission()
elif selected == "S":
    run_pirate_boat

 

