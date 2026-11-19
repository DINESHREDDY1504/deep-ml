import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    mat=np.array(matrix)
    means=0
    if(mode=='column'):
        means=mat.mean(axis=0)
    else:
        means=mat.mean(axis=1)    
    return means