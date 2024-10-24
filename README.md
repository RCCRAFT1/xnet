# xnet

### about

xnet is a python-based application to facilitate the tracking, analysis, and identification of orbital objects (satellites, etc.)

### data formats

xnet uses many data formats to measure and calibrate itself:

- raw iq data (s16, s8)
- decoded bits (soft)
- processed bits (cadu)
- direct receive (sdr)

### supported stuff

xnet also supports many xyz, ptz rotators for dishes. they only need to be supported in satdump
xnet supports antenna switches, lnas, and sdrs for the use of live receieve

### use

run the start script with `python3 start.py` and follow the prompts
the program also supports pygame windows and plots for easier visual analysis. simply install the pygame script package and run the start script again with the pygame parameters provided
you can also run the `help` file to see the variety of commands available

### installation

simply clone the repository by `git clone https://github.com/rccraft1/xnet.git`
