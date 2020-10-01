from Consultor import Consultor
import pandas as pd

cons = Consultor("Romao")

mat1 = [[1,2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2,1]]
mat2 = [9,8,7,6,5,4,3,2,1]

# arquivo = pd.read

dfMat = pd.DataFrame(mat1)


print(dfMat)

print(cons.corr(6,7))
corr = dfMat.corr()
print(corr)

