'''
we did not start a project yet.
'''

fruitlist = ['am','jam', 'kathal','apple','kela','lichu']
count = 0

for i in range(2,len(fruitlist)):
    count +=1
    if fruitlist[i] == "apple":
        print(f"apple is in {count} index")