from typing import Callable, Dict, Tuple, Union

from pandas import Series
from scipy.sparse._csr import csr_matrix
from sklearn.base import BaseEstimator

from utils.models.sklearn import load_class, tune_hyperparameters
from utils.data_preparation.artifacts import load_from_artifacts
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def hyperparameter_tuning(
    model_class_name: str,
    training_set: Dict[str, Union[Series, csr_matrix]],
    *args,
    **kwargs,
) -> Tuple[
    Dict[str, Union[bool, float, int, str]],
    csr_matrix,
    Series,
    Callable[..., BaseEstimator],
]:
    X_path, X_train_path, X_val_path, y_path, y_train_path, y_val_path, _ = training_set['build']
    # print(training_set['build'])
    X = load_from_artifacts(X_path.split('\\')[1])
    X_train = load_from_artifacts(X_train_path.split('\\')[1])
    X_val = load_from_artifacts(X_val_path.split('\\')[1])
    y = load_from_artifacts(y_path.split('\\')[1])
    y_train = load_from_artifacts(y_train_path.split('\\')[1])
    y_val = load_from_artifacts(y_val_path.split('\\')[1])
    # X = load_from_artifacts(X_path.split('\\')[1])

    model_class = load_class(model_class_name)

    hyperparameters = tune_hyperparameters(
        model_class,
        X_train=X_train,
        y_train=y_train,
        X_val=X_val,
        y_val=y_val,
        max_evaluations=kwargs.get('max_evaluations'),
        random_state=kwargs.get('random_state'),
    )
    print(hyperparameters)
    return hyperparameters, X_path.split('\\')[1],y_path.split('\\')[1],str(dict(cls=model_class, name=model_class_name))