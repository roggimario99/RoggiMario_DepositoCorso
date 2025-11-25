import numpy as np

arr = np.loadtxt("dati1d_random.txt")

file = open("results.txt","w")
file.close

#indicatori statistici

def stat_analysys(arr, print_file = True):
    min_val = np.min(arr)
    max_val = np.max(arr)
    mean = np.mean(arr)
    std = np.std(arr)

    print(f"min: {min_val}")
    print(f"max: {max_val}")
    print(f"mean: {mean}")
    print(f"standard deviation: {std}")
    
    if print_file:
        with open("results.txt","a") as file:
            file.write(f"min: {min_val}\n")
            file.write(f"max: {max_val}\n")
            file.write(f"mean: {mean}\n")
            file.write(f"standard deviation: {std}\n")
            file.write("\n")
#analisi posizionali


def pos_analysys(arr, print_file = True):
    ind_val_min = np.argmin(arr)
    ind_val_max = np.argmax(arr)
    mediana = np.percentile(arr, 50)

    print(f"indice del val max: {ind_val_min}")
    print(f"indice del val min: {ind_val_max}")
    print(f"median: {mediana}")
    
    if print_file:
        with open("results.txt","a") as file:
            file.write(f"indice del val max: {ind_val_min}\n")
            file.write(f"indice del val min: {ind_val_max}\n")
            file.write(f"median: {mediana}\n")
            file.write("\n")    
            
stat_analysys(arr)

pos_analysys(arr)