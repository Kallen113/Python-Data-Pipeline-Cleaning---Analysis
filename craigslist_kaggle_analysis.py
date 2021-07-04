"""NB: Run this script using the kaggle_env virtual env
--Activate the virtualenv via: <<<.\Kaggle_env\Scripts\activate.ps1
(from following directory: D:\Coding and Code projects\Python\Data Science\Kaggle_projects)
"""
#data analysis and file import libraries:
import os
import pandas as pd
import  statsmodels.api as sm 

import seaborn as sns

#NB: for accessing kaggle API:
## import kaggle ## NB: see doc: <https://www.kaggle.com/docs/api>
## NB: <<<kaggle datasets list -s dataset_name   --- to look up dataset_name using kaggle API

#import craigslist listings data on rental units from Kaggle
#data were created from a web crawler run in Jan 2020:

## from  terminal, download dataset via: <<< kaggle datasets download -d "austinreese/usa-housing-listings"
## unzip via Powershell: <<< Expand-Archive -LiteralPath D:\Coding and Code projects\Python\Data Science\Kaggle_projects\usa-housing-listings.zip -DestinationPath "D:\Coding and Code projects\Python\Data Science\Kaggle_projects\usa-housing-listings"
### NB: unzipped file placed into the 'usa-housing-listings' directory from Kaggle_projects...


#

#import craigslist housing dataset:
def return_latest_CSV_file(direc):
    """Change directory to given folder, order the Excel files
    by date modified, and select ONLY the most recent file
    to be imported as dataframe:"""
    os.chdir(direc) #change to stated directory
    files_from_path = filter(os.path.isfile, os.listdir(direc))
    files_from_path = [os.path.join(direc, f) for f in files_from_path] # add path to each file
    files_from_path.sort(key=lambda x: os.path.getmtime(x), reverse=True) #sort 
    for i in range(1): #only import the LAST modified file (ie, 1st element from the DESC-sorted list)
        df = pd.read_csv(files_from_path[i].split('\\')[-1], delimiter=',') #parse path to only read in the Excel file name itself
    return df


 
#specify path
search_dir = r"D:\Coding and Code projects\Python\Data Science\Kaggle_projects\usa-housing-listings"
#return latest CSV file as a list of dataframes
clist_housing = return_latest_CSV_file(search_dir)

print(clist_housing)
#transform to dataframe--select only 1st element of the list
# clist_housing = pd.DataFrame(clist_housing)

# # sanity check--check # of columns and data types:
clist_housing.info()

#exploratory data analysis and summary stats
def exploratory_analysis(df):
    print(f"Here are some summary statistics of this dataset: {df.describe()}\n") #summary stats (and print new line)
    print(f"Here is the % of missing/null records for this dataset, by column: {df.isnull().sum()/len(df)}\n") #% missingness (and print new line)
    print(f"Correlation matrix for each column: {df.corr()}")

print(exploratory_analysis(clist_housing))


# text data exploratory analysis
def exploratory_analysis_Text_val_counts(df, text_col, normalize_boolean):
    print(df[text_col].value_counts(normalize=normalize_boolean))


# beds--NB: show relative frequency, so normalize=True:
exploratory_analysis_Text_val_counts(clist_housing, 'beds', True)


#home description:
exploratory_analysis_Text_data(clist_housing, 'description')

## data vizualizations:


#countplot function:
def countplot_col(df, col_to_plot, hue_option):
    sns.countplot(x=df[col_to_plot], data=df, hue=hue_option)


##countplot of beds (ie, bedrooms):
countplot_col(clist_housing, 'beds', None)



# #countplot of description:
countplot_col(clist_housing, 'description', None)
 


#kernel density estimate plot:
def kde_plot(df, col_to_plot):
    sns.kdeplot(data=df, 
    y=col_to_plot,
    palette='deep'
    )

# #kde plot of price:
kde_plot(clist_housing, 'price')

# #kde plot of sqft:
kde_plot(clist_housing, 'sqft')


# #kde plot of region:
kde_plot(clist_housing, 'region')


#countplot of region:




# ### Data cleaning:
# def clean_nulls(df):
#     df.fillna() #replace nulls with ??



# ###Regression analysis:

# #specify LHS and RHS variables:
# def specify_LHS_and_RHS(df, outcome_var, list_of_RHS_names):
#     dep_var = df[outcome_var]]  # specify outcome variable
#     df_RHS = df[[list_of_RHS_names]]  # specify independent variables
#     return dep_var, df_RHS

#list of columns names for RHS:
RHS_list_spec_one = ['',
'',
'',
'']

specify_LHS_and_RHS( , "price", RHS_list_spec_one)

# def lin_reg_analysis(outcome_var, df_RHS):
#     """ Perform linear regression analysis (OLS): 
#     estimate and fit model, and print results"""
#     df_RHS = sm.add_constant(df, prepend=Flase)  #add constant to regressors (ie, for RHS's)
#     reg = sm.OLS(dep_var, df_RHS) # estimate OLS model
#     reg_fitted = mod.fit() #fit model
#     print(reg_fitted.summmary()) # print regression results 



