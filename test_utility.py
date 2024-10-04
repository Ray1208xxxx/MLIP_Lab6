import pytest
import pandas as pd
import numpy as np
from prediction_demo import data_preparation,data_split,train_model,eval_model

@pytest.fixture
def housing_data_sample():
    return pd.DataFrame(
      data ={
      'price':[13300000,12250000],
      'area':[7420,8960],
    	'bedrooms':[4,4],	
      'bathrooms':[2,4],	
      'stories':[3,4],	
      'mainroad':["yes","yes"],	
      'guestroom':["no","no"],	
      'basement':["no","no"],	
      'hotwaterheating':["no","no"],	
      'airconditioning':["yes","yes"],	
      'parking':[2,3],
      'prefarea':["yes","no"],	
      'furnishingstatus':["furnished","unfurnished"]}
    )

def test_data_preparation(housing_data_sample):
    feature_df, target_series = data_preparation(housing_data_sample)
    # Target and datapoints has same length
    assert feature_df.shape[0]==len(target_series)

    #Feature only has numerical values
    assert feature_df.shape[1] == feature_df.select_dtypes(include=(np.number,np.bool_)).shape[1]

@pytest.fixture
def feature_target_sample(housing_data_sample):
    feature_df, target_series = data_preparation(housing_data_sample)
    return (feature_df, target_series)


def test_data_split(feature_target_sample):
    return_tuple = data_split(*feature_target_sample)

    # Test if the length of return_tuple is 4
    assert len(return_tuple) == 4

    # Check if the splits are DataFrame and Series objects
    assert isinstance(return_tuple[0], pd.DataFrame)  # Training features
    assert isinstance(return_tuple[1], pd.DataFrame)  # Test features
    assert isinstance(return_tuple[2], pd.Series)  # Training target
    assert isinstance(return_tuple[3], pd.Series)  # Test target

    # Optional: Check if the sizes of the splits are correct (e.g., 70-30 split)
    total_rows = feature_target_sample[0].shape[0]
    assert return_tuple[0].shape[0] + return_tuple[1].shape[0] == total_rows
    assert return_tuple[2].shape[0] + return_tuple[3].shape[0] == total_rows
