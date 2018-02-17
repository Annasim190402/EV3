from ev3dev.auto import *
import time

m = Motor(OUTPUT_D)
m.run_timed(time_sp=3000, speed_sp=500)

