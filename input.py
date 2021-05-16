import pandas as pd

from scipy.spatial import distance_matrix
""" data taken from : https://www.sintef.no/projectweb/top/pdptw/li-lim-benchmark/100-customers/"""
def get_instance(str2):
    str1="pdp_400/"
    str3=".txt"
    instance=str1+str2+str3

    with open(instance) as f:
        count=0
        location=[]
        time_window=[]
        service_t=[]
        demand=[]
        pd_pair=[]
        for line in f:
            if count ==0:
                data=line.split()
                num_vehicles=int(data[0])
                v_cap=int(data[1])
                count+=1
            else:
                node = line.split()
                location.append((int(node[1]),int(node[2])))
                time_window.append([int(node[4]),int(node[5])])
                service_t.append(int(node[6]))
                demand.append(int(node[3]))
                if int(node[7]) == 0:
                    pd_pair.append([int(node[0]),int(node[8])])
                count+=1


    d=pd.DataFrame(location)

    dis=pd.DataFrame(distance_matrix(d.values,d.values,1),\
                           index=d.index,columns=d.index)

    matrix=dis.values.tolist()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j]=int(matrix[i][j])



    del pd_pair[0]


    data={}
    data['locations']=location
    data['time_matrix']=matrix
    data["distance_matrix"] = matrix
    data['time_windows']=time_window
    data['num_vehicles']=num_vehicles
    data['depot']=0
    data['pickups_deliveries']=pd_pair
    data['service_time']=service_t
    data['demands']=demand
    data['vehicle_capacities']=v_cap

    return data

if __name__ =="__main__":
    get_instance("lc101")