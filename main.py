# Basic Simulation for Human Population to 1M people
import argparse

parser = argparse.ArgumentParser(description='Process inputs.')
parser.add_argument('total_population', metavar='P', type=int, nargs='+',
                    help='an integer for the total_population')

parser.add_argument('growth', metavar='g', type=float, nargs='+',
                    help='a float for the growth')


args = parser.parse_args()

totalPopulation = args.total_population[0]
growthFactor = args.growth[0]
dayCount = 0 #Every 2 months the population is reported
total_days = 0
while totalPopulation < 1000000:
    totalPopulation *= growthFactor
    #Every 56th day, population is reported
    dayCount += 1
    total_days += 1
    if dayCount == 56: 
        dayCount = 0
        print("Total Population: %s"%totalPopulation)

print("Days to Reach 1M people:%s"%total_days)