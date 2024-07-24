import pickle 
import os


def save_to_artifacts(obj, filename, artifact_folder='artifacts'):
    if not os.path.exists(artifact_folder):
        os.makedirs(artifact_folder)
    file_path = os.path.join(artifact_folder, filename)
    with open(file_path, 'wb') as f:
        pickle.dump(obj, f)
    
    return file_path

def load_from_artifacts(filename, artifact_folder='artifacts'):

    file_path = os.path.join(artifact_folder, filename)
    with open(file_path, 'rb') as f:
        obj = pickle.load(f)
    return obj


def load_artifact(filename):
    with open(filename, 'rb') as f:
        obj = pickle.load(f)
    return obj

def load_all_data(artifact_folder='artifacts'):
    X = load_from_artifacts('X.pkl', artifact_folder)
    X_train = load_from_artifacts('X_train.pkl', artifact_folder)
    X_val = load_from_artifacts('X_val.pkl', artifact_folder)
    y = load_from_artifacts('y.pkl', artifact_folder)
    y_train = load_from_artifacts('y_train.pkl', artifact_folder)
    y_val = load_from_artifacts('y_val.pkl', artifact_folder)
    dv = load_from_artifacts('dv.pkl', artifact_folder)
    
    return X, X_train, X_val, y, y_train, y_val, dv
