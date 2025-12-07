import numpy as np

# a = np.array([1, 2, 3])        # 1-D array
# b = np.array([[1,2,3],[4,5,6],[7,8,9]])# 2-D array (matrix 2x3)
# c = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print(np.dot(b,c))

# for i in range(0,11,2):
    # print(i)
    
b = np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
# print(b[0,:])#Baris,Kolom
print(f"""    hasil jumlah baris ke-0 = {b[0,:].sum()}
    hasil jumlah baris ke-1 = {b[1,:].sum()}
    hasil jumlah baris ke-2 = {b[2, :].sum()}"""
      )