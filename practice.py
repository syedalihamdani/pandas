import pandas as pd

# file=pd.DataFrame([[1221,99]],columns=["1","2"],index=[2,3])
# print(file)

# files2=pd.DataFrame({"Apples":[22,44],"Bananas":[23,15]},index=[1,2])
# print(files2)

items=["Flour","Milk","Bread"]
quatities=["1cup","2 spuns","1 Liter"]
series=pd.Series(quatities,index=items,name="Dinner")
print(series)