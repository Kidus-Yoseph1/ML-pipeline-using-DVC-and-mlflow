import pandas as pd 
import os
import sys
import yaml

### Load parametrs from yaml file

params = yaml.safe_load(open('params.yaml'))['preprocess']

def preprocess(input_path, output_path):
    data = pd.read_csv(input_path)
    
    os.makedirs(os.path.dirname(output_path), exist_ok= True)
<<<<<<< HEAD
    data.to_csv(output_path, index= False)
    print(f"preprocessed data saved to {output_path}")
    
    
if __name__ == "__main__" :
    preprocess(params["input"], params["output"])
=======
    data.to_csv(output_path, header = None, index= False)
    print(f"preprocessed data saved to {output_path}") 
    
    
if __name__ == "__main__" :
    preprocess(params["input"], params["output"]) 
>>>>>>> 5c155b326bad31df8dd1296221147917d3f5680f
