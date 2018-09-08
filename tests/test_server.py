"""
Version:
"""

import pylab as pl
import sciris as sc
import scirisweb as sw


torun = [
#'browser', # Simple example of three figures
'advanced', # Illustrates separate legend plotting and direct editing of the JSON
]


if 'browser' in torun:
    figs = []
    for n in [10, 50]:
        fig = pl.figure()
        pl.plot(pl.rand(n), pl.rand(n))
        figs.append(fig)
    barfig = pl.figure()
    pl.bar(pl.arange(10), pl.rand(10))
    barjson = sw.mpld3ify(barfig)
    sw.browser(figs=figs+[barjson])



if 'advanced' in torun:
    
    def make_fig():
        fig = pl.figure()
        ax = fig.add_subplot(111)
        ax.plot([1,4,3,4,], label='mish')
        ax.plot([8,4,3,2], label='mush')
        return fig,ax

    fig,ax = make_fig()
    legend = sc.separatelegend(ax)
    
    json1 = sw.mpld3ify(fig,    jsonify=False)
    json2 = sw.mpld3ify(legend, jsonify=False)
    json2['axes'][0]['texts'][1]['text'] = 'mashed potatoes' # Change legend text
    json2['axes'][0]['paths'] = [] # Remove the box around the legend
    
    sw.browser([json1, json2])