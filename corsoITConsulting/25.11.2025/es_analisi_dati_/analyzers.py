import numpy as np

#arr = np.loadtxt("dati1d_random.txt")

#----------------------------------------------
#load dei dati
#----------------------------------------------

def data_load(nome_file):
    if nome_file.split(".")[-1] == "txt":
        data =np.loadtxt(nome_file)
        
    if nome_file.split(".")[-1] == "csv":
        data =np.loadtxt(nome_file, delimiter=",")
        
    return data

#---------------------------------------------
#indicatori statistici
#---------------------------------------------

def stat_analysys(arr, print_file = True):
    dim = len(arr.shape)

    min_val = np.min(arr, axis = dim -1)   #se l'array è bidimensionale esegue l'operzione riga per riga
    max_val = np.max(arr, axis = dim -1)
    mean = np.mean(arr, axis = dim -1)
    std = np.std(arr, axis = dim -1)

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

#---------------------------------------------            
#analisi posizionali
#---------------------------------------------

def pos_analysys(arr, print_file = True):
    dim = len(arr.shape)
    
    ind_val_min = np.argmin(arr, axis = dim -1)    #se l'array è bidimensionale esegue l'operzione riga per riga
    ind_val_max = np.argmax(arr, axis = dim -1)
    mediana = np.percentile(arr, 50, axis = dim -1)

    print(f"indice del val max: {ind_val_min}")
    print(f"indice del val min: {ind_val_max}")
    print(f"median: {mediana}")
    
    if print_file:
        with open("results.txt","a") as file:
            file.write(f"indice del val max: {ind_val_min}\n")
            file.write(f"indice del val min: {ind_val_max}\n")
            file.write(f"median: {mediana}\n")
            file.write("\n")   


#mat = np.loadtxt("dati2d_random.txt")

#---------------------------------------------            
#analisi per assi
#---------------------------------------------

def by_axis_analysys(mat, print_file = True):
    
    """"Performa somma e media riga per riga (y) e colona per colonna (x)"""
    
    dim = len(mat.shape)
    axis = np.arange(dim)
    

    sum_x = np.sum(mat, axis = axis[0])  #se l'array è unodimensionale sum_x = sum_y
    sum_y = np.sum(mat, axis = axis[-1])
    mean_x = np.mean(mat, axis = axis[0])  #se l'array è unodimensionale mean_x = mean_y
    mean_y = np.mean(mat, axis = axis[-1])
        
        
    print(f"somma per col: {sum_x}")
    print(f"somma per righe: {sum_y}")
    print(f"media per col: {mean_x}")
    print(f"media per righe: {mean_y}")
    
    if print_file:
        with open("results.txt","a") as file:
            file.write(f"somma per col: {sum_x}")
            file.write(f"somma per righe: {sum_y}")
            file.write(f"media per col: {mean_x}")
            file.write(f"media per righe: {mean_y}")
            file.write("\n")  

#---------------------------------------------            
#operazioni matriciali e algebriche
#---------------------------------------------

def do_dot_(mat, mat2):
    do_dot = False
    if mat.shape[1] == mat2.shape[0]:
        do_dot = True
    return do_dot
    

def matrix_analysys(mat, mat2, print_file = True):
    do_dot = do_dot_(mat, mat2)
        
    if do_dot: dot = np.dot(mat, mat2)
    transpose = np.transpose(mat)  #se l'array è unodimensionale restituise l'array stesso
    norm = np.linalg.norm(mat)
    cov_mat = np.cov(mat.T)  #se l'array è unodimensionale restituise la varianza


    if do_dot: print(f"dot product: {dot}")
    print(f"transpose:\n{transpose}")
    print(f"norm: {norm}")
    print(f"covariance matrix:\n{cov_mat}")

    if print_file:
        with open("results.txt", "a") as file:
            if do_dot: file.write(f"dot product: {dot}\n")
            file.write(f"transpose:\n{transpose}\n")
            file.write(f"norm: {norm}\n")
            file.write(f"covariance matrix:\n{cov_mat}\n")
            file.write("\n")

           