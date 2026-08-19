#!/bin/bash

echo "HOME directory:"
echo $HOME

echo "Calculation;"
bc << EOF
23934/44343
EOF

echo "Files in HOME starting with D: "
ls $HOME/D*

echo "Username information:"
grep "$USER" /etc/passwd

