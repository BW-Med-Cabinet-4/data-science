## import libraries
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


## get the data
df = pd.read_csv('https://raw.githubusercontent.com/med-cabinet-5/data-science/master/data/cannabis.csv')
df.head()

## functions

## remove duplicates
def remove_duplicates(df):
    df = df.drop_duplicates(keep='first')
    return df

## convert all strain names to all lowercase
def lower_case_column(column_name):
    return df[column_name].str.lower()

## search by strain keyword
def search_strains(keyword):
    return df[df['Strain'].str.contains(keyword)]

## get strain name from index
def get_strain_from_index(index):
    strain_name = df.iloc[index][0]
    return strain_name

## get index number from strain
def get_index_from_strain(strain):
    strain_index = df[df['Strain'] == strain].index[0]
    return strain_index

## combine features into one column
def combine_features(row):
    return row['Strain'] +" "+ row['Type'] + " "+ row['Rating'] + " " + row['Effects'] + " " + row['Flavor'] + " " + row['Description']

## these are the columns we are going to use
features = ['Strain', 'Type', 'Rating', 'Effects', 'Flavor', 'Description']

## drop duplicates
df = remove_duplicates(df)

## convert all columns to string for nlp
df = df.astype(str)

## make a combined features column
df['combined_features'] = df.apply(combine_features, axis=1)

## fill nans with emtpy string
for feature in features:
    df[feature] = df[feature].fillna('')

## make strain titles lowercase for easier search
df['Strain'] = lower_case_column('Strain')

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
