from vpython import *
# gravitation constant
G = 6.67e-11

intial_pos1 = vector(-4e11,0,0) 
intial_pos2 = vector(4e11,0,0) 

# circumsecondary planet
# planet_initial_pos = vector(7e11,0,0)
# planet_initial_velocity = vector(0,0,1e2) 

#circumprimary planet
planet_initial_pos = vector(0,0,0)
planet_initial_velocity = vector(0,0,4e4) 


star1 = sphere(pos = intial_pos1, radius=8e10, color = color.yellow, make_trail = True, interval = 10, retain = 50)
star1.mass = 6e30
star1.p = vector(0,0,1e4) * star1.mass

star2 = sphere(pos = intial_pos2, radius = 4e10, color = color.blue, make_trail = True)
star2.mass = 3e30
star2.p = -star1.p

planet = sphere(pos = planet_initial_pos, radius = 2e10, color = color.green, make_trail = True, trail_type = "points", interval = 10, retain = 50)
planet.mass = 1e25
planet.p = planet_initial_velocity * planet.mass

dt = 1e5

while True:
    rate(200)
    distance = star2.pos - star1.pos
    dist1 = star1.pos - planet.pos
    dist2 = star2.pos - planet.pos
    
    f1 = G * star1.mass * planet.mass * dist1.hat / mag(dist1)**2
    f2 = G * star2.mass * planet.mass * dist2.hat / mag(dist2)**2
    tf = f1+f2
  
    Force = G * star1.mass * star2.mass * distance.hat / mag(distance)**2
    
    star1.p = star1.p + Force*dt
    star2.p = star2.p - Force*dt
    planet.p = planet.p + tf*dt
    
    star1.pos = star1.pos + (star1.p/star1.mass) * dt
    star2.pos = star2.pos + (star2.p/star2.mass) * dt
    planet.pos = planet.pos + (planet.p/planet.mass) * dt
  
