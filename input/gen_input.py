#/usr/bin/env python

import sys
sys.path.append('./scripts')

import json
import numpy as np
import armadillo as arma
import subprocess as sub
import os

if __name__ == '__main__':

    with open('default.json') as f:
        ini = json.load(f)


    hams = np.zeros((2, 2), dtype=complex)
    hams[0, 0] = 0.5
    hams[1, 1] = -0.5

    qmds = np.zeros((2, 2), dtype=complex)
    qmds[0, 1] = 1.0
    qmds[1, 0] = 1.0

    arma.save(hams, ini['syst']['hamsFile'])
    arma.save(qmds, ini['syst']['qmdsFile'])

    jsonInit = {
        "bath": {
            "temperature": 1.0
        },
        "prop": {
            "dt": 0.01,
            "nt": 200000,
        },
    }

    with open('input.json', 'w') as f:
        json.dump(jsonInit, f, indent=4)
