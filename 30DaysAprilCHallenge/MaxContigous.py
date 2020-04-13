L= [0,0,1,1,1,1,0,0,0,0]
#dict = {"1":"dasdsa"}
dict = {}
#print ( "1" in dict)
count=0
dict[0] = {'first':-1, 'lenght':0}
#print (dict)
for ind in range(len(L)):
    if (L[ind] ==1):
        count =count +1
        if count in dict:
            #print (dict)
            dict[count] ={'first':dict[count]['first'] ,  'lenght':(ind-dict[count]['first'])}
        else:
            dict[count] ={'first':ind, 'lenght':0}
    else: #=='0'
        count =count -1
        if count in dict:
            #print (dict[count])
            dict[count] ={'first':dict[count]['first'], 'lenght':(ind-dict[count]['first'])}
        else:
            dict[count] ={'first':ind, 'lenght':0}

max = -1
for key in dict:
     if(dict[key]['lenght']>max):   
        max = dict[key]['lenght']
print (max)
#print (max(dict, key =dict['lenght']))