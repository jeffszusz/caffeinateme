#!/usr/bin/python


def caffeinate(volumeOfWater=10):
    # Step 1:
    # Find the weight in grams of coffee needed for a given volume of water

    # 1 fl. oz of water weighs approx 28 grams
    weightOfWater = volumeOfWater * 28  # grams

    # A weight ratio of 1:16 coffee to water makes a perfect cup
    weightOfCoffee = weightOfWater / 16.0  # grams

    return formatResults(volumeOfWater, weightOfCoffee)


def formatResults(waterVolume, coffeeWeight):
    message = "For {} fl. oz of water, grind {} grams of coffee beans."
    message = message.format(waterVolume, coffeeWeight)
    return message

print(caffeinate())

# Step 2:
# Make the program accept values in the terminal and output the results
#   if there are command-line arguments, use the volume value(s) provided
#   if there are no arguments, use defaults of 8, 10 and 12 fl. oz
