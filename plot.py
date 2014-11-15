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
	f = open('results/{}'.format(filename), 'r')
	r = json.load(f)
	f.close()

	i = 0
	counts = []
	wordnum = []
	x = ['0','10000','20000','30000','40000','50000','60000','70000']
	for indx in x:
    		counts.append(r[indx]['+'])
    		wordnum.append(int(indx))
    	plt.scatter(wordnum, counts)
    	plt.savefig('plots/{}.png'.format(filename[:-5]))