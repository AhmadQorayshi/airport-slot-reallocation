import pandas as pd
from random import randint
    
schedule_flie= 'Address of the Excel File of the Original Schedule of Flights'
          
connections_file = 'Address of the Excel File of Flight Connections'  

df_arrival_i=pd.read_excel(schedule_flie, sheet_name='arr_i')
df_arrival_j=pd.read_excel(schedule_flie, sheet_name='arr_j')
df_arrival_k=pd.read_excel(schedule_flie, sheet_name='arr_k')
df_departure_i=pd.read_excel(schedule_flie, sheet_name='dep_i')
df_departure_j=pd.read_excel(schedule_flie, sheet_name='dep_j')
df_departure_k=pd.read_excel(schedule_flie, sheet_name='dep_k')

df_connection_ij = pd.read_excel(connections_file, sheet_name='ij')
df_connection_ji = pd.read_excel(connections_file, sheet_name='ji')
df_connection_ki = pd.read_excel(connections_file, sheet_name='ki')
df_connection_jk = pd.read_excel(connections_file, sheet_name='jk')
df_connection_lk = pd.read_excel(connections_file, sheet_name='lk')

i_ij = list(df_connection_ij['i'])
j_ij = list(df_connection_ij['j'])

i_ji = list(df_connection_ji['i'])
j_ji = list(df_connection_ji['j'])

i_ki = list(df_connection_ki['i'])
k_ki = list(df_connection_ki['k'])

j_jk = list(df_connection_jk['j'])
k_jk = list(df_connection_jk['k'])

l_lk = list(df_connection_lk['l'])
k_lk = list(df_connection_lk['k'])

#................................  making dictionaries for flight connections ..................................................
d_ij={}    
d_ji={}
d_ki={}
d_jk={}
d_lk={}
for i,j in zip(i_ij, j_ij):           
    d_ij[i] = j 
for j,i in zip(j_ji, i_ji):  
    d_ji[j] = i 
for k,i in zip(k_ki, i_ki):  
    d_ki[k] = i 
for j,k in zip(j_jk, k_jk):  
    d_jk[j] = k 
for l,k in zip(l_lk, k_lk):  
    d_lk[l] = k 

#................................  Making dictionary of arrival and departure flights ......................................
i_num = list(df_arrival_i['i'])                  #set i   
scheduled_arrival_i = list(df_arrival_i['time']) 
scheduled_departure_i = list(df_departure_i['time'])    
scheduled_arrival_flights_i_dictionary={}                                        
scheduled_departure_flights_i_dictionary={}
for i , arr in zip(i_num,scheduled_arrival_i):
    scheduled_arrival_flights_i_dictionary[i]=arr
for i , dep in zip(i_num,scheduled_departure_i):
    scheduled_departure_flights_i_dictionary[i]=dep

j_num = list(df_arrival_j['j'])                   #set j
scheduled_arrival_j = list(df_arrival_j['time']) 
scheduled_departure_j = list(df_departure_j['time'])    
scheduled_arrival_flights_j_dictionary={}                                        
scheduled_departure_flights_j_dictionary={}
for j , arr in zip(j_num,scheduled_arrival_j):
    scheduled_arrival_flights_j_dictionary[j]=arr
for j , dep in zip(j_num,scheduled_departure_j):
    scheduled_departure_flights_j_dictionary[j]=dep

k_num = list(df_arrival_k['k'])                    #set k
scheduled_arrival_k = list(df_arrival_k['time']) 
scheduled_departure_k = list(df_departure_k['time'])    
scheduled_arrival_flights_k_dictionary={}                                       
scheduled_departure_flights_k_dictionary={}
for k , arr in zip(k_num,scheduled_arrival_k):
    scheduled_arrival_flights_k_dictionary[k]=arr
for k , dep in zip(k_num,scheduled_departure_k):
    scheduled_departure_flights_k_dictionary[k]=dep

#................................   sorting the arrival-departure dictionaries based on their times .....................................
scheduled_arrival_of_flights_i_sorted_dict = dict(sorted(scheduled_arrival_flights_i_dictionary.items(), key=lambda item: item[1]))  
scheduled_departure_of_flights_i_sorted_dict = dict(sorted(scheduled_departure_flights_i_dictionary.items(), key=lambda item: item[1]))  

scheduled_arrival_of_flights_j_sorted_dict = dict(sorted(scheduled_arrival_flights_j_dictionary.items(), key=lambda item: item[1]))  
scheduled_departure_of_flights_j_sorted_dict = dict(sorted(scheduled_departure_flights_j_dictionary.items(), key=lambda item: item[1]))  

scheduled_arrival_of_flights_k_sorted_dict = dict(sorted(scheduled_arrival_flights_k_dictionary.items(), key=lambda item: item[1]))  
scheduled_departure_of_flights_k_sorted_dict = dict(sorted(scheduled_departure_flights_k_dictionary.items(), key=lambda item: item[1]))  

#................................   listing flight numbers and their corresponding times ............................................
list_of_flights_i_arrival_number=list(scheduled_arrival_of_flights_i_sorted_dict.keys())
list_of_flights_i_arrival_time=list(scheduled_arrival_of_flights_i_sorted_dict.values())
list_of_flights_i_departure_number=list(scheduled_departure_of_flights_i_sorted_dict.keys())
list_of_flights_i_departure_time=list(scheduled_departure_of_flights_i_sorted_dict.values())

list_of_flights_j_arrival_number=list(scheduled_arrival_of_flights_j_sorted_dict.keys())
list_of_flights_j_arrival_time=list(scheduled_arrival_of_flights_j_sorted_dict.values())
list_of_flights_j_departure_number=list(scheduled_departure_of_flights_j_sorted_dict.keys())
list_of_flights_j_departure_time=list(scheduled_departure_of_flights_j_sorted_dict.values())

list_of_flights_k_arrival_number=list(scheduled_arrival_of_flights_k_sorted_dict.keys())
list_of_flights_k_arrival_time=list(scheduled_arrival_of_flights_k_sorted_dict.values())
list_of_flights_k_departure_number=list(scheduled_departure_of_flights_k_sorted_dict.keys())
list_of_flights_k_departure_time=list(scheduled_departure_of_flights_k_sorted_dict.values())
#..................................................................................................................................
    
arrival_bond_1 = []  
arrival_bond_2 = []
arrival_bond_3 = []
departure_bond_1 = []
departure_bond_2 = []

occupancy_arrival_bond_1 = 0  
occupancy_arrival_bond_2 = 0  
occupancy_arrival_bond_3 = 0 
occupancy_departure_bond_1 = 0
occupancy_departure_bond_2 = 0

anticipated_arrival_i = {}
actual_arrival_i = {}
actual_departure_i = {} 
actual_arrival_j = {}
actual_departure_j = {} 
actual_arrival_k = {}
actual_departure_k = {} 

ready_time_i = {}           
ready_time_j = {}       # => Earliest times for flights j to depart
ready_time_k = {}

for i in i_num:
    if i not in d_ki.values() and i not in d_ji.values():
        ready_time_i[i]=5
        
for j in list_of_flights_j_departure_number:
    if j not in d_ij.values():
        ready_time_j[j]=5 

for k in list_of_flights_k_departure_number:
    if k not in d_jk.values() and k not in d_lk.values():
        ready_time_k[k]=5
        
total_time = 2440  
minimum_turnaround_time = 35

for i in i_num:
    variation_arrival= randint(-2,2)
    scheduled_arrival_flights_i_dictionary[i]+=variation_arrival
 
for time in range(total_time):  
    if occupancy_arrival_bond_1 > 0:  
        occupancy_arrival_bond_1 -= 1  
    if occupancy_arrival_bond_2 > 0:  
        occupancy_arrival_bond_2 -= 1  
    if occupancy_arrival_bond_3 > 0:  
        occupancy_arrival_bond_3 -= 1  
    if occupancy_departure_bond_1 > 0:  
        occupancy_departure_bond_1 -= 1  
    if occupancy_departure_bond_2 > 0:  
        occupancy_departure_bond_2 -= 1 
           
    #..................................................Arrival Flights i................................................        
    if list_of_flights_i_departure_number:
        for i in list_of_flights_i_departure_number:
            if scheduled_departure_flights_i_dictionary[i] <= time and ready_time_i[i] <= time:
                actual_departure_i[i]= max(scheduled_departure_flights_i_dictionary[i] , ready_time_i[i])
                if scheduled_departure_flights_i_dictionary [i] < actual_departure_i [i]:
                    anticipated_arrival_i [i] = scheduled_arrival_flights_i_dictionary [i] + (actual_departure_i [i] - scheduled_departure_flights_i_dictionary[i])
                else:
                    anticipated_arrival_i [i] = scheduled_arrival_flights_i_dictionary [i]
                list_of_flights_i_departure_number.remove(i)
                
    if list_of_flights_i_arrival_number: 
        for i in list_of_flights_i_arrival_number:       
            if occupancy_arrival_bond_1 <= 0 and scheduled_arrival_flights_i_dictionary[i] <= time \
                and anticipated_arrival_i[i]<= time:                                                                    #Flight Bound 1
                occupancy_arrival_bond_1 = 3  
                actual_arrival_i[i] = time 
                variation_TU = randint(-5,5) 
                if i in d_ij.keys():
                    ready_time_j [d_ij[i]] = actual_arrival_i[i] + minimum_turnaround_time + variation_TU         
                arrival_bond_1.append(i) 
                list_of_flights_i_arrival_number.remove(i)
                continue
        
            if list_of_flights_i_arrival_number and occupancy_arrival_bond_2 <= 0 and \
                scheduled_arrival_flights_i_dictionary[i] <= time and anticipated_arrival_i[i]<= time:                   #Flight Bound 2
                occupancy_arrival_bond_2 = 3 
                actual_arrival_i[i] = time
                variation_TU = randint(-5,5)
                if i in d_ij.keys():
                    ready_time_j [d_ij[i]] = actual_arrival_i[i] + minimum_turnaround_time + variation_TU   
                arrival_bond_2.append(i)       
                list_of_flights_i_arrival_number.remove(i)  
                continue 
            
            if list_of_flights_i_arrival_number and occupancy_arrival_bond_3 <= 0 and \
                scheduled_arrival_flights_i_dictionary[i] <= time and anticipated_arrival_i[i]<= time:                   #Flight Bound 3
                occupancy_arrival_bond_3 = 3 
                actual_arrival_i[i] = time 
                variation_TU = randint(-5,5) 
                if i in d_ij.keys():
                    ready_time_j [d_ij[i]] = actual_arrival_i[i] + minimum_turnaround_time + variation_TU
                arrival_bond_3.append(i)         
                list_of_flights_i_arrival_number.remove(i)  
                          
            #.........................................Departure Flights j..........................................
    if list_of_flights_j_departure_number:
        for j in list_of_flights_j_departure_number:      
            if occupancy_departure_bond_1 <= 0 and scheduled_departure_flights_j_dictionary[j] <= time and \
                ready_time_j[j] <= time:                                                                              #Flight Bound 1
                occupancy_departure_bond_1 = 2  
                actual_departure_j [j] = time 
                if scheduled_departure_flights_j_dictionary [j] < actual_departure_j [j]:
                    actual_arrival_j [j] = scheduled_arrival_flights_j_dictionary [j] + (actual_departure_j [j] - scheduled_departure_flights_j_dictionary[j])
                else:
                    actual_arrival_j[j] = scheduled_arrival_flights_j_dictionary [j]
                if j in d_ji.keys():
                    ready_time_i [d_ji[j]] = actual_arrival_j[j] + minimum_turnaround_time 
                if j in d_jk.keys():
                    ready_time_k [d_jk[j]] = actual_arrival_j[j] + minimum_turnaround_time 
                departure_bond_1.append(j)  
                list_of_flights_j_departure_number.remove(j)
                continue  

            if list_of_flights_j_departure_number and \
                occupancy_departure_bond_2 <= 0 and scheduled_departure_flights_j_dictionary[j] <= time and \
                ready_time_j[j] <= time:                                                                               #Flight Bound 1 
                occupancy_departure_bond_2 = 2 
                actual_departure_j [j] = time  
                if scheduled_departure_flights_j_dictionary [j] < actual_departure_j [j]:
                    actual_arrival_j [j] = scheduled_arrival_flights_j_dictionary [j] + (actual_departure_j [j] - scheduled_departure_flights_j_dictionary[j])
                else:
                    actual_arrival_j[j] = scheduled_arrival_flights_j_dictionary [j]
                if j in d_ji.keys():
                    ready_time_i [d_ji[j]] = actual_arrival_j[j] + minimum_turnaround_time
                if j in d_jk.keys():
                    ready_time_k [d_jk[j]] = actual_arrival_j[j] + minimum_turnaround_time 
                departure_bond_2.append(j)             
                list_of_flights_j_departure_number.remove(j)
        
            #.........................................Downstream Flights k..........................................        
    if list_of_flights_k_departure_number:
        for k in list_of_flights_k_departure_number:
            if scheduled_departure_flights_k_dictionary[k] <= time and ready_time_k[k] <= time:
                actual_departure_k[k]=max(scheduled_departure_flights_k_dictionary[k] , ready_time_k[k])
                if scheduled_departure_flights_k_dictionary [k] < actual_departure_k [k]:
                    actual_arrival_k [k] = scheduled_arrival_flights_k_dictionary [k] + (actual_departure_k [k] - scheduled_departure_flights_k_dictionary[k])
                else:
                    actual_arrival_k[k] = scheduled_arrival_flights_k_dictionary [k]
                if k in d_ki.keys():
                    ready_time_i [d_ki[k]] = actual_arrival_k[k] + minimum_turnaround_time
                if k in d_lk.keys():
                    ready_time_k [d_lk[k]] = actual_arrival_k[k] + minimum_turnaround_time
                list_of_flights_k_departure_number.remove(k)

#...............................................Save to Excel File...............................................................
a_arrival_i = pd.DataFrame(list(actual_arrival_i.items()), columns=['i', 'Arrival_i'])  
a_departure_i = pd.DataFrame(list(actual_departure_i.items()), columns=['i', 'Departure_i']) 
ready_i=pd.DataFrame(list(ready_time_i.items()), columns=['i', 'Ready time']) 
a_arrival_j = pd.DataFrame(list(actual_arrival_j.items()), columns=['j', 'Arrival_j'])  
a_departure_j = pd.DataFrame(list(actual_departure_j.items()), columns=['j', 'Departure_j'])  
ready_j=pd.DataFrame(list(ready_time_j.items()), columns=['j', 'Ready time']) 
a_arrival_k = pd.DataFrame(list(actual_arrival_k.items()), columns=['k', 'Arrival_k'])  
a_departure_k = pd.DataFrame(list(actual_departure_k.items()), columns=['k', 'Departure_k']) 
ready_k=pd.DataFrame(list(ready_time_k.items()), columns=['k', 'Ready time']) 
 
with pd.ExcelWriter('Address of the Output Excel File', engine='openpyxl') as writer:  
    a_arrival_i.to_excel(writer, sheet_name='Arrival_i', index=False)  
    a_departure_i.to_excel(writer, sheet_name='Departure_i', index=False)
    ready_i.to_excel(writer, sheet_name='Ready Time i', index=False)     
    a_arrival_j.to_excel(writer, sheet_name='Arrival_j', index=False)  
    a_departure_j.to_excel(writer, sheet_name='Departure_j', index=False) 
    ready_j.to_excel(writer, sheet_name='Ready Time j', index=False)      
    a_arrival_k.to_excel(writer, sheet_name='Arrival_k', index=False)  
    a_departure_k.to_excel(writer, sheet_name='Departure_k', index=False) 
    ready_k.to_excel(writer, sheet_name='Ready Time k', index=False)     
                    
