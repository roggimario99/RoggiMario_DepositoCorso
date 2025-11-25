import numpy as np



#--------------------------------------------------
# metodo con gen diretta array 2d
#--------------------------------------------------

mat = np.random.randint(10, 51, (4,4))

#mat = np.reshape((4,4))


print("-"*60)
print(f"matrice: \n {mat}")

#--------------------------------------------------
# metodo con reshape
#--------------------------------------------------

N = 4 * 4 # numero elemneti

x = np.random.randint(10, 51, N)
arr = x.reshape((4,4))



print(f"matrice: \n {mat}")

#--------------------------------------------------
# fancy indexing
#--------------------------------------------------

ind_x = [0,1,2,3]
ind_y = [1,3,2,0]

el_selezionati = mat[ind_x,ind_y]

print(f"elementi selezionati: {el_selezionati}")

stop = mat.shape[0] + 1 # num. righe preso da shape + 1

righe_da_sel = np.arange(1,stop,2)


righe_dis = mat[righe_da_sel]


print("-"*60)
print(f"righe dispari: \n{righe_dis}")

#sol con slicing
righe_dis = mat[1:stop:2]
print(f"righe dispari (con slicing): \n{righe_dis}")

mat_mod = mat.copy()
mat_mod[ind_x,ind_y] += 10

print("-"*60)
print(f"matrice: \n {mat}")
print(f"matrice modificata: \n {mat_mod}")




