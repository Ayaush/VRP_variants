from input import get_instance
from TSP_ort import main as tsp_solver
from VRP_ort import main as vrp_solver
from CVRP_ort import main as cvrp_solver
from VRPTW_ort import main as vrptw_solver
from PDVRP_ort import main as pdvrp_solver
from PDVRPTW_ort import main as pdptw_solver
from visualization import inputvisualize
from visualization import outputvisualize
"""possible option
    1. TSP
    2. VRP (minimum longest route)
    3. CVRP
    4. PDVRP
    5. VRPTW
    6. PDVRPTW         """
solver=6
instance="LC1_4_1"
def run_VRP_variant(case,data):
    if case ==1:
        return call_TSP(data)
    elif case ==2:
        return call_VRP(data)
    elif case ==3:
        return call_CVRP(data)
    elif case ==4:
        return call_PDVRP(data)
    elif case ==5:
        return call_VRPTW(data)
    elif case ==6:
        return call_PDVRPTW(data)


def call_TSP(fulldata):
    keys = ['distance_matrix', 'num_vehicles', 'depot']
    data = {x: fulldata[x] for x in keys}
    data["num_vehicles"] =1
    return tsp_solver(data)
def call_CVRP(fulldata):
    keys = ['distance_matrix','demands','vehicle_capacities', 'num_vehicles', 'depot']
    data = {x: fulldata[x] for x in keys}
    data["num_vehicles"] = 25
    capicity = [data['vehicle_capacities'] for i in range(data['num_vehicles'])]
    data['vehicle_capacities']=capicity
    return cvrp_solver(data)

def call_VRP(fulldata):
    keys = ['distance_matrix', 'num_vehicles', 'depot']
    data = {x: fulldata[x] for x in keys}
    data["num_vehicles"] = 25
    return vrp_solver(data)

def call_VRPTW(fulldata):
    keys = ['time_matrix','time_windows', 'num_vehicles', 'depot']
    data = {x: fulldata[x] for x in keys}
    return vrptw_solver(data)

def call_PDVRP(fulldata):
    keys = ['distance_matrix','pickups_deliveries', 'num_vehicles', 'depot']
    data = {x: fulldata[x] for x in keys}
    print(data['pickups_deliveries'])
    data['num_vehicles']=10
    return pdvrp_solver(data)

def call_PDVRPTW(fulldata):
    keys = ['time_matrix', 'time_windows','pickups_deliveries', 'num_vehicles', 'depot']
    data = {x: fulldata[x] for x in keys}
    #data['num_vehicles'] = 25
    return pdptw_solver(data)


if __name__ =="__main__":
    data=get_instance(instance)
    #inputvisualize(data)

    solution=run_VRP_variant(solver,data)
    print("here is the solution")
    print(solution)
    #outputvisualize(data,solution)

