#!/bin/bash

. `dirname $0`/qcrc 
echo qchem -nt $2 $3 $1 
echo 1 = $1
echo 2 = $2
echo 3 = $3
qchem -nt $2 $3 $1

