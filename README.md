# uwEnergyHacks
Github repo for uwEnergyHacks

## Inspiration
Large office buildings waste a lot of energy for heating.
Reducing this energy usage makes individual people uncomfortable.
Customizing temperature per floor requires lots of expensive sensors and is thus not done.

## What it does
Buildings are typically divided up into heating quadrants. The Felix AI mobile client enables each each employee to vote on what they want the temperature to be. Then, Felix's intelligent backend uses Machine Learning algorithms to choose the optimum temperature for each quadrant which satisfies user preferences, energy efficiency settings and predicted future temperatures.

Each user is able to access their personal efficiency metrics and share them through Snapchat. 

## How we built it
The app was build on native iOS using Swift and the Snapchat SDK.
The data analytics prototype was built using Python and the libraries MatPlotLib and Numpy.

## Challenges we ran into
We were not able to test graph export feature (see video below) because the official iOS emulator does not enable you to download third party applications like Snapchat.
This was not solved, as our iPhones were not suitable for development.

We also ran into the issue of finding a balance of user preferences and energy price. We solved this using Machine Learning Algorithms.

## Accomplishments that we're proud of
We truly made a viable energy saving solution! We can see this saving lots of money and energy for large commercial buildings, and helping the environment.
## What we learned
We learned a great deal of things, such as how to use the Snapchat SDK, various data anlytics tricks but most importantly, how to think analyze large scale energy consumption.

## What's next for Felix AI
Based on feedback, we will continue iterating and working to reduce workplace energy inefficiency while increasing personal comfort!
