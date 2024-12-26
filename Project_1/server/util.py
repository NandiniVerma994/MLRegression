import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

#once loading locations is done now we need to write an estimated price function
def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)

#this will return you all the location names
def get_location_names():
    return __locations

#this method will load all the files from the artifacts and we will assign it to a
#global variable
def load_saved_artifacts():
    print("loading saved artifacts..start")
    global __data_columns
    global __locations
    global __model

    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]


    with open("./artifacts/banglore_home_prices_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))