import json
import numpy as np
import plotly.plotly as py
from plotly.graph_objs import *
from secrets import key
py.sign_in('gwulf', key)
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

        trace1 = Scatter(x=wordnum, y=counts)
        data = Data([trace1])
        layout = Layout(
            title=filename[:-5],
            xaxis=XAxis(
                title='Word Number',
                showgrid=False,
                zeroline=False
            ),
            yaxis=YAxis(
                title='{} count'.format(filename[:-9]),
                showline=False
            )
        )
        fig = Figure(data=data, layout=layout)
        plot_url = py.plot(fig, filename=filename[:-5])
