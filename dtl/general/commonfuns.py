import pickle
def save_as_pickle(data,path):
    """path should end as .pkl"""
    with open(path,"wb") as f:
        pickle.dump(data,f,pickle.HIGHEST_PROTOCOL)

def open_pickle(file_path):
    with open(file_path, 'rb') as f:
        my_file = pickle.load(f)
    return (my_file)
