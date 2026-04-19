import streamlit as st
import pandas as pd
import sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.cache
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_name)
    df['species'] = iris.target
    return df, iris.target_names

df, target_name = load_data()
