import montecarlo as mc

circle_radius = 300 #circle radius in pixels
window = (1920,1200) #window resolution
points = 10000 #number of total points

montecarlo_simulation = mc.MonteCarlo(window, circle_radius, points)
montecarlo_simulation.loop()