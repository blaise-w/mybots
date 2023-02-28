import os
import hillclimber
import parallelHillClimber

phc = parallelHillClimber.PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()