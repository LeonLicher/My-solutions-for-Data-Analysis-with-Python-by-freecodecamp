import numpy as np

def calculate(list):
    if len(list)<9:
        raise ValueError("List must contain nine numbers.")
    arr=np.array(list).reshape(3,3)
    print(arr)

    mean_values=[
        
        [arr[:,0].mean(),arr[:,1].mean(),arr[:,2].mean()],
        [arr[0,:].mean(),arr[1,:].mean(),arr[2,:].mean()],
        arr[:,:].mean()
    ]

    variance_values=[
        [arr[:,0].var(),arr[:,1].var(),arr[:,2].var()],
        [arr[0,:].var(),arr[1,:].var(),arr[2,:].var()],
        
        arr[:,:].var()
    ]

    std_dev_values=[
        [arr[:,0].std(),arr[:,1].std(),arr[:,2].std()],
        [arr[0,:].std(),arr[1,:].std(),arr[2,:].std()],
        
        arr[:,:].std()
    ]

    max_values=[
        [arr[:,0].max(),arr[:,1].max(),arr[:,2].max()],
        [arr[0,:].max(),arr[1,:].max(),arr[2,:].max()],
        
        arr[:,:].max()
    ]

    min_values=[
        [arr[:,0].min(),arr[:,1].min(),arr[:,2].min()],
        [arr[0,:].min(),arr[1,:].min(),arr[2,:].min()],
        
        arr[:,:].min()
    ]

    sum_values = [
        [arr[:,0].sum(),arr[:,1].sum(),arr[:,2].sum()],
        [arr[0,:].sum(),arr[1,:].sum(),arr[2,:].sum()],
        
        arr[:,:].sum()
    ]

    calculations ={
    'mean':mean_values, 
    'variance':variance_values, 
    'standarddeviation':std_dev_values, 
    'max':max_values,   
    'min':min_values,   
    'sum':sum_values
    }





    return calculations

print(calculate([2,6,2,8,4,0,1,5,7]))