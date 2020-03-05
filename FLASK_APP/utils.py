## import libraries
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


## functions

## remove duplicates
def remove_duplicates(df):
    df = df.drop_duplicates(keep='first')
    return df

## convert all strain names to all lowercase
def lower_case_column(column_name):
    return df[column_name].str.lower()

## search by name keyword
def search_strains(keyword):
    return df[df['name'].str.contains(keyword)]

## get strain name from index
def get_name_from_index(index):
    strain_name = df.iloc[index][0]
    return strain_name

## get index number from strain name
def get_index_from_name(name):
    name_index = df[df['name'] == name].index[0]
    return name_index

## combine features into one column
def combine_features(row):
    return row['name'] + " " + row['flavors'] + " "+ row['race'] + " " + row['positive'] + " " + row['negative'] + " " + row['medical']  + " " + row['Rating'] + " " + row['Description']

## these are the columns we are going to use
features = ['name', 'flavors', 'race', 'positive', 'negative', 'medical', 'Rating', 'Description']

## drop duplicates
df = remove_duplicates(df)

## convert all columns to string for nlp
df = df.astype(str)

## make a combined features column
df['combined_features'] = df.apply(combine_features, axis=1)

## fill nans with emtpy string
for feature in features:
    df[feature] = df[feature].fillna('')

## make strain name titles lowercase for easier search
df['name'] = lower_case_column('name')

## the function
def recommend_strains(strain, num_of_strains=5):
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df['combined_features'])
    cosine_sim = cosine_similarity(count_matrix)
    strain_index = get_index_from_strain(strain)
    similar_strains = list(enumerate(cosine_sim[strain_index]))
    sorted_similar_strains = sorted(similar_strains, key= lambda x:x[1], reverse=True)
    recommended_strains = []
    i = 0
    for strain in sorted_similar_strains:
        recommended_strains.append(get_strain_from_index(strain[0]))
        i = i + 1
        if i > num_of_strains:
            break
    return recommended_strains
