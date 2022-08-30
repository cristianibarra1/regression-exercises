import pandas as pd
import env
import numpy as np

def get_connection(db, user=env.user, host=env.host, password=env.password):
    '''initiates sql connection'''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
#csv clean 
def clean_zillow():
    '''Read zillow csv file into a pandas DataFrame,
    renamed all of the columuns, replace NaN values with 0 ,
    keep all the 0 values, convert all columns to int64,
    return cleaned zillow DataFrame'''
    df=pd.read_csv('zillow.csv')
    df=df.astype('int64')
    df = df.fillna('0')
    df = df.rename(columns={'bedroomcnt': 'Bedrooms', 'bathroomcnt': 'Bathrooms','calculatedfinishedsquarefeet':'Squarefeet',
                       "taxvaluedollarcnt":'TaxesTotal','yearbuilt':'Year','taxamount':'Taxes','fips':'Fips'})
#sql clean   
def sqlclean_zillow():
    query = """
            
    SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips
    FROM properties_2017

    LEFT JOIN propertylandusetype USING(propertylandusetypeid)

    WHERE propertylandusedesc IN ("Single Family Residential",                       
                                  "Inferred Single Family Residential") """

    url = f"mysql+pymysql://{user}:{password}@{host}/zillow"
    df = pd.read_sql(query,url)
    df=df.astype('int64')
    df = df.fillna('0')
    df = df.rename(columns={'bedroomcnt': 'Bedrooms', 'bathroomcnt': 'Bathrooms','calculatedfinishedsquarefeet':'Squarefeet',
                       "taxvaluedollarcnt":'TaxesTotal','yearbuilt':'Year','taxamount':'Taxes','fips':'Fips'})
    return df

