
import numpy as np
#from matplotlib.pyplot import *
#from matplotlib import *
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import glob 
import os

png_backup = None
from hambiplots import glob_format
def figsize_pgf(scale):
    fig_width_pt = 417.473 #469.755                          # Get this from LaTeX using \the\textwidth
    inches_per_pt = 1.0/72.27                       # Convert pt to inch
    golden_mean = (np.sqrt(5.0)-1.0)/2.0            # Aesthetic ratio (you could change this)
    fig_width = fig_width_pt*inches_per_pt*scale    # width in inches
    fig_height = fig_width*golden_mean              # height in inches
    fig_size = [fig_width,fig_height]
    return fig_size
 
pgf_with_latex = {                      # setup matplotlib to use latex for output
    "pgf.texsystem": "pdflatex",        # change this if using xetex or lautex
    "text.usetex": True,                # use LaTeX to write all text
    "font.family": "serif",
    "font.serif": [],                   # blank entries should cause plots to inherit fonts from the document
    "font.sans-serif": [],
    "font.monospace": [],
    "axes.labelsize": 10,               # LaTeX default is 10pt font.
    "font.size": 10,
    "legend.fontsize": 8,               # Make the legend/label fonts a little smaller
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "figure.figsize": figsize_pgf(0.6),     # default fig size of 0.6 textwidth
    "pgf.preamble": [
        r"\usepackage[utf8x]{inputenc}",    # use utf8 fonts becasue your computer can handle it :)
        r"\usepackage[T1]{fontenc}",        # plots will be generated using this preamble
        ]
    }

relevant_png_keys = ["pgf.texsystem",        # change this if using xetex or lautex
    "text.usetex",                # use LaTeX to write all text
    "font.family",
    "font.serif",                   # blank entries should cause plots to inherit fonts from the document
    "font.sans-serif",
    "font.monospace",
    "axes.labelsize",               # LaTeX default is 10pt font.
    "font.size",
    "legend.fontsize",               # Make the legend/label fonts a little smaller
    "xtick.labelsize",
    "ytick.labelsize",
    "figure.figsize",
    "pgf.preamble"]

def set_format(x):
    """ Choose a format from 
    .png  .pdf  .pgf """
    global glob_format, png_backup
    glob_format = x
    if x == 'pgf' or x == 'pdf':
        if glob_format == 'png':
            png_backup = {key:plt.rcParams[key] for key in relevant_png_keys}
        mpl.rcParams.update(pgf_with_latex)
    elif x == 'png':
        if not png_backup:
            png_backup = {key:plt.rcParams[key] for key in relevant_png_keys}
        mpl.rcParams.update(png_backup)
 
def save(filename, 
                   pgf_width=None, 
                   bbox_inches = 'tight', 
                   dpi = 240):
    
    #####
    ### if the filename containes the format, check consistency with the currently set format:
    #####
    
    global glob_format
    
    if filename[-4] == '.':
        
        desired_format = filename[-3:]
        filename = filename[:-4]
        if glob_format != desired_format:
            set_format(desired_format)
            print "Changed output format to ", desired_format
    
    #####
    ### check if a folder for the respective format exists:
    #####
    
    if '.\\'+glob_format in glob.glob('./*'):
        pass
    else: 
        os.makedirs(glob_format)
    
    #####
    ### save the figure:
    #####
    
    fig = plt.gcf()
    
    if glob_format:
        
        if glob_format == 'pgf':
            if pgf_width: width = pgf_width
            else: width = 0.65
            fig.set_size_inches(figsize_pgf(width))
            
        saveto = './'+glob_format+'/{}.'.format(filename)+glob_format
        plt.savefig(saveto,
               bbox_inches = bbox_inches,
                dpi = dpi)
        
    else: 
        pass
def get_std_X_YLOW_YUP(xvals, yvals):

    xvals = array(xvals)
    yvals = array(yvals)

    Y1 = [] 
    Y2 = []

    X = sorted(set(xvals))

    for xv in X:
        IND = argwhere(xvals == xv)
        avg = mean(yvals[IND])
        stdd = np.std(yvals[IND])

        Y1 += [avg-stdd]
        Y2 += [avg+stdd] 
    
    return X, Y1, Y2
def load_matplot_rcParams1():
    matplotlib.rc('font', size = 18) 
    matplotlib.rc('lines', linewidth=2)
    matplotlib.rc('axes', labelsize = 18)
    matplotlib.rc('axes', titlesize = 18)
    matplotlib.rc('ytick', labelsize = 14)
    matplotlib.rc('xtick', labelsize = 14)
    matplotlib.rc('legend', fontsize = 16)
    matplotlib.rc('legend', framealpha = 1)
def load_matplotlib_rcParams1():
    matplotlib.rc('font', size = 18) 
    matplotlib.rc('lines', linewidth=2)
    matplotlib.rc('axes', labelsize = 18)
    matplotlib.rc('axes', titlesize = 18)
    matplotlib.rc('ytick', labelsize = 14)
    matplotlib.rc('xtick', labelsize = 14)
    matplotlib.rc('legend', fontsize = 16)
    matplotlib.rc('legend', framealpha = 1)
def set_rcParams(id = 1):
    if id == 1:
        matplotlib.rc('font', size = 18) 
        matplotlib.rc('lines', linewidth=2)
        matplotlib.rc('axes', labelsize = 18)
        matplotlib.rc('axes', titlesize = 18)
        matplotlib.rc('ytick', labelsize = 14)
        matplotlib.rc('xtick', labelsize = 14)
        matplotlib.rc('legend', fontsize = 16)
        matplotlib.rc('legend', framealpha = 1)
def set_rcParams(id = 1):
    if id == 1:
        matplotlib.rc('font', size = 18) 
        matplotlib.rc('lines', linewidth=2)
        matplotlib.rc('axes', labelsize = 18)
        matplotlib.rc('axes', titlesize = 18)
        matplotlib.rc('ytick', labelsize = 14)
        matplotlib.rc('xtick', labelsize = 14)
        matplotlib.rc('legend', fontsize = 16)
        matplotlib.rc('legend', framealpha = 1)
        matplotlib.rc('figure', facecolor = 'white')
def set_rcParams(id = 1):
    """
    1: standard
    2: dark background 
    """
    if id == 1:
        matplotlib.rc('font', size = 18) 
        matplotlib.rc('lines', linewidth=2)
        matplotlib.rc('axes', labelsize = 18)
        matplotlib.rc('axes', titlesize = 18)
        matplotlib.rc('ytick', labelsize = 14)
        matplotlib.rc('xtick', labelsize = 14)
        matplotlib.rc('legend', fontsize = 16)
        matplotlib.rc('legend', framealpha = 1)
        matplotlib.rc('figure', facecolor = 'white')
        
    if id == 2: 
        matplotlib.rc('ytick', color = 'white')
        matplotlib.rc('xtick', color = 'white')
        matplotlib.rc('font', size = 18) 
        matplotlib.rc('lines', linewidth=2)
        matplotlib.rc('axes', labelsize = 18)
        matplotlib.rc('axes', titlesize = 18)
        matplotlib.rc('ytick', labelsize = 14)
        matplotlib.rc('xtick', labelsize = 14)
        matplotlib.rc('legend', fontsize = 16)
        matplotlib.rc('legend', framealpha = 1)
        #matplotlib.rc('figure', facecolor = 'white')
def set_rcParams(id = 1):
    """
    1: standard
    2: dark background 
    """
    if id == 1:
        matplotlib.rc('font', size = 18) 
        matplotlib.rc('lines', linewidth=2)
        matplotlib.rc('axes', labelsize = 18)
        matplotlib.rc('axes', titlesize = 18)
        matplotlib.rc('ytick', labelsize = 14)
        matplotlib.rc('xtick', labelsize = 14)
        matplotlib.rc('legend', fontsize = 16)
        matplotlib.rc('legend', framealpha = 1)
        matplotlib.rc('figure', facecolor = 'white')
        
    if id == 2: 
        matplotlib.rc('ytick', color = 'white')
        matplotlib.rc('xtick', color = 'white')
        matplotlib.rc('font', size = 18) 
        matplotlib.rc('lines', linewidth=2)
        matplotlib.rc('axes', labelsize = 18)
        matplotlib.rc('axes', titlesize = 18)
        matplotlib.rc('ytick', labelsize = 14)
        matplotlib.rc('xtick', labelsize = 14)
        matplotlib.rc('legend', fontsize = 16)
        matplotlib.rc('legend', framealpha = 1)
        matplotlib.rc('figure', facecolor = 'black')
        matplotlib.rc('grid', color = 'white')
def set_rcParams(id = 1):
    """
    1: standard
    2: dark background 
    """
    if id == 1:
        matplotlib.rc('font', size = 18) 
        matplotlib.rc('lines', linewidth=2)
        matplotlib.rc('axes', labelsize = 18)
        matplotlib.rc('axes', titlesize = 18)
        matplotlib.rc('ytick', labelsize = 14)
        matplotlib.rc('xtick', labelsize = 14)
        matplotlib.rc('legend', fontsize = 16)
        matplotlib.rc('legend', framealpha = 1)
        matplotlib.rc('figure', facecolor = 'white')
        
    if id == 2: 
        matplotlib.rc('ytick', color = 'white')
        matplotlib.rc('xtick', color = 'white')
        matplotlib.rc('font', size = 18) 
        matplotlib.rc('lines', linewidth=2)
        matplotlib.rc('axes', labelsize = 18)
        matplotlib.rc('axes', titlesize = 18)
        matplotlib.rc('ytick', labelsize = 14)
        matplotlib.rc('xtick', labelsize = 14)
        matplotlib.rc('legend', fontsize = 16)
        matplotlib.rc('legend', framealpha = 1)
        matplotlib.rc('grid', color = 'white')
        matplotlib.rc('figure', facecolor = '0.1')
def set_rcParams(id = 1):
    """
    1: standard
    2: dark background 
    """
    if id == 1:
        matplotlib.rc('font', size = 18) 
        matplotlib.rc('lines', linewidth=2)
        matplotlib.rc('axes', labelsize = 18)
        matplotlib.rc('axes', titlesize = 18)
        matplotlib.rc('ytick', labelsize = 14)
        matplotlib.rc('xtick', labelsize = 14)
        matplotlib.rc('legend', fontsize = 16)
        matplotlib.rc('legend', framealpha = 1)
        matplotlib.rc('figure', facecolor = 'white')
        
    if id == 2: 
        matplotlib.rc('ytick', color = 'white')
        matplotlib.rc('xtick', color = 'white')
        matplotlib.rc('font', size = 18) 
        matplotlib.rc('lines', linewidth=2)
        matplotlib.rc('axes', labelsize = 18)
        matplotlib.rc('axes', titlesize = 18)
        matplotlib.rc('ytick', labelsize = 14)
        matplotlib.rc('xtick', labelsize = 14)
        matplotlib.rc('legend', fontsize = 16)
        matplotlib.rc('legend', framealpha = .1)
        matplotlib.rc('grid', color = 'white')
        matplotlib.rc('figure', facecolor = '0.1')
def set_rcParams(id = 1):
    """
    1: standard
    2: dark background 
    """
    if id == 1:
        matplotlib.rc('font', size = 18) 
        matplotlib.rc('lines', linewidth=2)
        matplotlib.rc('axes', labelsize = 18)
        matplotlib.rc('axes', titlesize = 18)
        matplotlib.rc('ytick', labelsize = 14)
        matplotlib.rc('xtick', labelsize = 14)
        matplotlib.rc('legend', fontsize = 16)
        matplotlib.rc('legend', framealpha = 1)
        matplotlib.rc('figure', facecolor = 'white')
        
    if id == 2: 
        matplotlib.rc('ytick', color = 'white')
        matplotlib.rc('xtick', color = 'white')
        matplotlib.rc('font', size = 18) 
        matplotlib.rc('lines', linewidth=2)
        matplotlib.rc('axes', labelsize = 18)
        matplotlib.rc('axes', titlesize = 18)
        matplotlib.rc('ytick', labelsize = 14)
        matplotlib.rc('xtick', labelsize = 14)
        matplotlib.rc('legend', fontsize = 16)
        matplotlib.rc('legend', framealpha = .4)
        matplotlib.rc('grid', color = 'white')
        matplotlib.rc('figure', facecolor = '0.1')
def set_rcParams(id = 1):
    """
    1: standard
    2: dark background 
    """
    if id == 1:
        matplotlib.rc('font', size = 18) 
        matplotlib.rc('lines', linewidth=2)
        matplotlib.rc('axes', labelsize = 18)
        matplotlib.rc('axes', titlesize = 18)
        matplotlib.rc('ytick', labelsize = 14)
        matplotlib.rc('xtick', labelsize = 14)
        matplotlib.rc('legend', fontsize = 16)
        matplotlib.rc('legend', framealpha = 1)
        matplotlib.rc('figure', facecolor = 'white')
        
    if id == 2: 
        matplotlib.rc('ytick', color = 'white')
        matplotlib.rc('xtick', color = 'white')
        matplotlib.rc('font', size = 18) 
        matplotlib.rc('lines', linewidth=2)
        matplotlib.rc('axes', labelsize = 18)
        matplotlib.rc('axes', titlesize = 18)
        matplotlib.rc('ytick', labelsize = 14)
        matplotlib.rc('xtick', labelsize = 14)
        matplotlib.rc('legend', fontsize = 16)
        matplotlib.rc('legend', framealpha = .4)
        matplotlib.rc('grid', color = 'white')
        matplotlib.rc('xlabel', color = 'white')
        matplotlib.rc('ylabel', color = 'white')
        matplotlib.rc('figure', facecolor = '0.1')
def set_rcParams(id = 1):
    """
    1: standard
    2: dark background 
    """
    if id == 1:
        matplotlib.rc('font', size = 18) 
        matplotlib.rc('lines', linewidth=2)
        matplotlib.rc('axes', labelsize = 18)
        matplotlib.rc('axes', titlesize = 18)
        matplotlib.rc('ytick', labelsize = 14)
        matplotlib.rc('xtick', labelsize = 14)
        matplotlib.rc('legend', fontsize = 16)
        matplotlib.rc('legend', framealpha = 1)
        matplotlib.rc('figure', facecolor = 'white')
        
    if id == 2: 
        matplotlib.rc('ytick', color = 'white')
        matplotlib.rc('xtick', color = 'white')
        matplotlib.rc('font', size = 18) 
        matplotlib.rc('lines', linewidth=2)
        matplotlib.rc('axes', labelsize = 18)
        matplotlib.rc('axes', titlesize = 18)
        matplotlib.rc('ytick', labelsize = 14)
        matplotlib.rc('xtick', labelsize = 14)
        matplotlib.rc('legend', fontsize = 16)
        matplotlib.rc('legend', framealpha = .4)
        matplotlib.rc('grid', color = 'white')
        matplotlib.rc('axes', labelcolor = 'white')
        matplotlib.rc('figure', facecolor = '0.1')