import numpy as np

def calculate(list):
    import numpy as np
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    elif len(list) == 9:
        arr = np.array([
    [list[0],list[1],list[2]], # 0
    [list[3],list[4],list[5]], # 1
    [list[6],list[7],list[8]]  # 2
    ])
    print(arr)
    '''
result:
  0 1 2
[[0 1 2] 0
 [3 4 5] 1
 [6 7 8]] 2
    '''
    #mean
    mean_ax1 = [arr[:,0].mean(),arr[:,1].mean(),arr[:,2].mean()]
    mean_ax2 = [arr[0].mean(),arr[1].mean(),arr[2].mean()]
    flat_mean = arr.mean()

    #variance
    var_ax1 = [np.var(arr[:,0]),np.var(arr[:,1]),np.var(arr[:,2])]
    var_ax2 = [np.var(arr[0]),np.var(arr[1]),np.var(arr[2])]
    flat_var = np.var(arr)

    #Standar Deviation
    std_ax1 = [np.std(arr[:,0]),np.std(arr[:,1]),np.std(arr[:,2])]
    std_ax2 = [np.std(arr[0]),np.std(arr[1]),np.std(arr[2])]
    flat_std = np.std(arr)

    #Max
    max_ax1 = [np.max(arr[:,0]),np.max(arr[:,1]),np.max(arr[:,2])]
    max_ax2 = [np.max(arr[0]),np.max(arr[1]),np.max(arr[2])]
    flat_max = np.max(arr)

    #Min
    min_ax1 = [np.min(arr[:,0]),np.min(arr[:,1]),np.min(arr[:,2])]
    min_ax2 = [np.min(arr[0]),np.min(arr[1]),np.min(arr[2])]
    flat_min = np.min(arr)

    #Sum
    sum_ax1 = [np.sum(arr[:,0]),np.sum(arr[:,1]),np.sum(arr[:,2])]
    sum_ax2 = [np.sum(arr[0]),np.sum(arr[1]),np.sum(arr[2])]
    flat_sum = np.sum(arr)

    #Dictionary
    calculations = {
      'mean':[mean_ax1,mean_ax2,flat_mean],
      'variance':[var_ax1,var_ax2,flat_var],
      'standard deviation':[std_ax1,std_ax2,flat_std],'max':[max_ax1,max_ax2,flat_max],
      'min':[min_ax1,min_ax2,flat_min],
      'sum':[sum_ax1,sum_ax2,flat_sum]
      }

    return calculations