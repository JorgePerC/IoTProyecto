import progressbar 
import time 
  
  

widgets = ['Loading: ', progressbar.AnimatedMarker()] 
bar = progressbar.ProgressBar(widgets=widgets).start() 
    
for i in range(50): 
    time.sleep(0.1) 
    bar.update(i) 
