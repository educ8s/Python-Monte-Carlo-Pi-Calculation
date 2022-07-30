import montecarlo as mc

circle_radius = 300
window = (1920,1200)
points = 50000

montecarlo_simulation = mc.MonteCarlo(window, circle_radius, points)
montecarlo_simulation.loop()