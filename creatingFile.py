import pandas as pd
# Creating Data set with pandas library
file=pd.DataFrame([[21,31]],columns=["Apples","Bananas"],index=[1,2])
print(file)
files2=pd.DataFrame({"Apples":[22,44],"Bananas":[23,15]},index=[1,2])
print(files2)
quantities=['4 cups','1 cup','2 large','1 can']
items=['Flour','Milk','Eggs','Spam']
ingredients = pd.Series(quantities,index=items,name='Dinner')
print(ingredients)


# This is to read any data file
# reviews =pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv',index_col=0)