import numpy as np

inputs = [1,2,3,4]
weights = [0.5,-0.8,0.10,0.7]
bias = 2
output = (inputs[0]*weights[0]+
        inputs[1]*weights[1]+
        inputs[2]*weights[2]+
        inputs[3]*weights[3]+
        bias)
print(output)