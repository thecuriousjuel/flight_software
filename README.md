# BeepSat (pycubedmini version)

Currently we have 3 versions of software, basic, advanced and state_machine.
Basic and advanced are drop in replacements for the upstream versions.
While state_machine restructures the advanced flight software to work with a state_machine.
For the state_machine version of the software there are two independent parts, the "frame" where the state_machine implementation resides along with a few other helpful utilities.
And the "plugins" where the actual specific hardware dependent parts of the flight software are.

To build the flight software you run `sh build.sh {plugin}` where `{plugin}` is the part of the code that depends on hardware/purpose.

## Locally running the test version of the software
To build the files run `sh build.sh plugs/test` and to run it run `sh run.sh`. 

## Building the actual flight software
build: `sh build.sh frame plugs/test`
run: copy over files to the CIRCUITPY drive (don't automate with rm -rf *, as this has led to corrupting the file system in the past)

## Software Architecture Overview

We have the folder `frame/` which contains the barebones sattelite state machine code, and the main.py. 
This code is independent of wheter you are using pycubedmini, pycubed, or running your very own test script.

We also have the folders `plugs/{name}` where each `name` represents a certain "plugin" that you attach to the frame using the build script.
Here is where the platform/implementation specific details go, each {name} represents an entirely different set of flight software, be it 
flight software targetting pycubedmini, pycubed or an emulator.

In order to see a basic example run `sh build.sh plugs/example` and to run it run `sh run.sh`. 
This example emulates the pycubed library, so that it can be run locally on your computer. 


## License (same as upstream)
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />
- Hardware in this repository is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
- Software/firmware in this repository is licensed under MIT unless otherwise indicated.
