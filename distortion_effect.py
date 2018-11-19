"""
Created by: 
Author: Kanisha Agarwal
University Of Regina
200409921
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import matplotlib.pyplot as plt

# Header data is removed from kanishasine.dat to read the data.
data = pd.read_csv("input.dat", header = None, delimiter = r"\s+")

x = data [ 0 ]
y = data [ 1 ]

#t_list and amp_list are the lists created to store the values of time and amplitude respectively.
t_list  = [ ]
amp_list = [ ]

#sampling frequency
fs = 44100
  
#populate the lists with the contents of the columns read
for i in range ( 0 , int ( len ( x ) ) ):
 t_list.append ( float ( x.iloc [ i ] ) )
 amp_list.append ( float ( y.iloc [ i ] ) )   


#After distortion, writes the contents of file.
f = open (" out.dat ", " w ")

#Hard clipping Distortion effect is performed. 
i=0
while ( i <= len ( y ) – 1 ):
    if( amp_list [ i ] > 0.3 ):
        amp_list [ i ] = 0.3
    elif ( amp_list [ i ] <- 0.3 ):
        amp_list [ i ] =- 0.3
    i = i + 1

#Amplifier is used to compare the resulting signals.
for i in range (0 , int ( len ( y ) ) ):

#Amplification factor  = 2.5
amp_list [ i ] = amp_list [ i ] * 2.5

    
#Input signals plotted
plt.xlabel ( 'time' )
plt.ylabel ( 'amplitude' )   
plt.plot ( t_list , y )
plt.axis ( [ 0.0, 0.01 , -1 ,1 ] )
plt.show  ( )

#Output signals plotted after distortion effect
plt.xlabel ( 'time' )
plt.ylabel ( 'amplitude' )
plt.plot ( t_list , amp_list )
plt.axis ( [ 0, 0.01, -1, 1 ] )
plt.show ( )

#Writing into file
f.write ( " ;  Sample Rate " + str ( 44100 /8 ) + "\n")
f.write ( " ; Channels 1 " + "\n")

#simple inverse filter
for i in range ( 0 , int ( len ( t_list ) – 2 ) ):
f.write (str (t_list [ i ] )+ " " +str (((amp_list [ i ]))) + "\n" )  
   
#Closing the file
f.close ( )

“ “ “
Reference:
Professor Trevor Tomesh, University Of Regina
“ “ “
