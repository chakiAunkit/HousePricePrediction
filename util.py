from copyreg import pickle
import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_idx = __data_columns.index(location.lower())
    except:
        loc_idx = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_idx >= 0:
        x[loc_idx] = 1

        return np.round(__model.predict([x])[0], 2)


def get_location_names():
    global __locations
    return __locations


def load_saved_artifacts():
    print("Loading artifacts")

    global __data_columns
    global __locations
    global __model

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open('./artifacts/home_price_model.pickle', 'rb') as f:
        __model = pickle.load(f)


if __name__ == '__main__':
    load_saved_artifacts()
    #print(get_estimated_price('1st phase jp nagar', 10000, 7, 8))
