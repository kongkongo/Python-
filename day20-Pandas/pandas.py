import   pandas     as      pd
import   numpy     as      np


nums=[1,2,3,4,5]
s=pd.Series(nums)
print(s)


fruits = ['Orange','Banana','Mangao']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)

# Creating Pandas Series from a Dictionary
dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
s = pd.Series(dct)
print(s) 

data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
# Adding a New Column添加一列
weights = [74, 78, 69]
df['Weight'] = weights
print(df)

