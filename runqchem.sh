#!/bin/bash

. `dirname $0`/qcrc 
qchem -nt 8 $1 $2 
