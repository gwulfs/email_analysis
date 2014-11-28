import json
import numpy as np
import matplotlib.pyplot as plt
import pdb

files = [ "Positive_10k.json", "headProblemsExtended_10k.json",
          "a_10k.json", "hearLoud_10k.json",
          "an_10k.json", "hearSoft_10k.json",
          "discrepancy_10k.json", "hearSpeak_10k.json",
          "exclusives_10k.json", "negative_10k.json",
          "fillers_10k.json", "negativemarkers_10k.json",
          "fillersyouth_10k.json", "the_10k.json",
          "headProblems_10k.json", "think_10k.json" ]

for filename in files:
    with open('results/{}'.format(filename), 'r') as f:
        r = json.load(f)

    counts = []
    wordnum = []
    for key, value in r.items():
        wordnum.append(int(key))
        counts.append(value.get('+', 0))
    plt.scatter(wordnum, counts)
    plt.savefig('plots/{}.png'.format(filename[:-5]))
    plt.close()
