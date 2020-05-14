# import libraries and define necessary varibles
import numpy as np
import matplotlib.pyplot as plt
#number of infected people
i=[1]
#numder of the susceptible
s=[9999]
#total population
N=10000
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
plt.figure(figsize=(6,4),dpi =150)
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.plot(t_list,s,label='Susceptible')
plt.plot(t_list,i,label='Infection')
plt.plot(t_list,r,label='Recovery')
#show the legend
plt.legend(loc='upper right')
plt.show()
#save the plot as image
plt.savefig('C:\\Users\\hh\\Desktop\\SIRmodel', type='png')



