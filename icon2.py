import csv

    
def opn_csv(x):
    '''opens "matrix" csv file of "0's" and "1's", returns list of lists'''
    with open(x) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        list_of_lists = list(reader)
        return list_of_lists

def uin_csv(): 
    '''user input for csv filename, returns string'''
    uin = input('enter csv file name: ')
    return uin

def uin_swp(): 
    '''user input for swap string, returns string'''
    uin = input('enter swap string: ')
    return uin

def uin_scl(): 
    '''user input for scale factor, returns int'''
    uin = input('enter scale factor: ')
    return int(uin)
        
def swap(x, y): 
    '''in list of lists, x, swaps "0" with y[0], "1" with y[1], from string y''' 
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == '0':
                x[i][j] = y[0]
            elif x[i][j] == '1':
                x[i][j] = y[1]
    return x
        
    
def prnt(x): 
    '''prints list of lists to console'''
    for i in range(len(x)):
        for j in range(len(x[i])):
            print(x[i][j], end = '')
        print('', end = '\n')
        
def scal(x, y): 
    '''takes list of lists, x, of size m by n, duplicates elements, returning list of lists of size ym by yn''' 
    '''scale on y axis by duplicating each list y times'''
    a = [] 
    for i in range(len(x)):
        for j in range(y):
            a.append(x[i])
          
    '''create list of empty lists'''    
    b = []
    for k in range(len(a)):
        b.append([])
    
    '''scale on x axis by duplicating each item of each list y times'''
    for l in range(len(a)):
        for m in range(len(a[l])):
                for n in range(y):
                    b[l].append(a[l][m])
    return b

def main():
    
    print("icon hw")
    icon = opn_csv(uin_csv())
    prnt(icon)
    prnt(swap(icon, uin_swp()))
    prnt(scal(icon, uin_scl()))
    
if __name__ == "__main__":
    main()
    
    
    