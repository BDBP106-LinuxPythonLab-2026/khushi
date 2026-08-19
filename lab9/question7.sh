#!/bin/bash

mass=1
speed=299792458

energy=$(bc << EOF
$mass * $speed^2
EOF
)

echo "Mass = $mass kg"
echo "Speed of light = $speed m/s"
echo "Energy-mass equivalence = 
$energy Joules"
