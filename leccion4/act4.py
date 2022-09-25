import pdb
pdb.set_trace()

# listas de compresión
enteros = [[2,4,1], [1,2,3,4,5,6,7,8], [100,250,43]]
maximos = [[num for num in sublista if num==max(sublista)] for sublista in enteros]

print(maximos)