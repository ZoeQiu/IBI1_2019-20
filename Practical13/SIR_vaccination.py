# import libraries and define necessary varibles
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
#number of infected people
i=[1]
#total population
N=10000
#numder of the susceptible under different rates of vaccination


#number of recovered people
r=[0]
# infection probability(beta)
b=0.3
# recovery probability(gamma)
g=0.05

#define the loop times 

t_list=[0]
#pick susceptible individuals at random to become infected randomly
#run the model for 1000 times
#numder of the susceptible under different rates of vaccination
for p in range (0,11):
 s=[int(N*(10-p)/10)]
for n in range (0,1000):
    infection=np.random.choice(range(2),s[n],p=[1-b*(i[n]/N), b*(i[n]/N)])

 #the populaton of infected people
    num_i= np.sum(infection== 1)
    recover=np.random.choice(range(2),i[n],p=[1-g,g]) 
    num_r= np.sum(recover == 1)
 #record the output 
    s.append(s[n]-num_i)
    i.append(i[n]+num_i-num_r)
    r.append(r[n]+num_r) 
    t_list.append(n)
#plot the picture
plt.plot(t_list,i,label=str(v*10)+'%',color=cm.viridis(p*20))
plt.figure(figsize=(6,4),dpi =150)
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.plot(t_list,s,label='Susceptible')
plt.plot(t_list,i,label='Infection')
plt.plot(t_list,r,label='Recovery')
#show the graph
plt.legend(loc='upper right')
from matplotlib import cm
plt.show()
#save the plot as image
plt.savefig('C:\\Users\\hh\\Desktop\\SIRmodel', type='png')
