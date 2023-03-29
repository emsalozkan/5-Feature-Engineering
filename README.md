# feature-engineering
This repository contains a collection of feature engineering techniques applied to improve predictive performance of a machine learning model.

**Here are the steps to load dataset using URL and output to csv file:**
>1. Update the **url** and **path** according to your own workspace. 
>2. Update the **datasetname** variable with the csv file name what you want.

in the <span style="color:blue">*load_export_data_nb.ipynb*</span> document and execute it.


**STUDY CASE 1- DIABETES**    
***Steps of analyzing dataset and train the model***
> [cs_diabetes_nb.ipynb](./workspaces/feature-engineering/notebooks/cs_diabetes_nb.ipynb)  is belonged to this case study. 

>1. Examine the overall picture. <span style="color:blue">*(from examine_data import check_df)*</span> 
>2. Classify the variables as numeric and categorical. <span style="color:blue">*(from classify_data import grab_col_names)*</span> 
>3. Analyze numeric and categorical variables. <span style="color:blue">*(from analyze_data import cat_summary, num_summary)*</span> 
>4. Analyze target variable. <span style="color:blue">*(from analyze_data import target_summary_with_num, target_summary_with_cat)*</span> 
>5. Analyze missing values. <span style="color:blue">*(from analyze_data import missing_value,missing_value_and_target)*</span>
>6. Analyze outliers. <span style="color:blue">*(from analyze_data import check_outlier, replace_with_thresholds, )*</span>
>7. Analyze correlation. <span style="color:blue">*(from analyze_data import corr_variable )*</span>
>8. Feature extraction <span style="color:blue">*(from extract_feature import set_insulin, set_age, set_BMI, set_Glucose, set_age_BMI, set_age_Glucose )*</span>
>9. Encoding <span style="color:blue">*(from encoding import label_encoding, one_hot_encoding )*</span>
>10. Feature Scaling <span style="color:blue">*(StandardScaler)*</span>
>11. Train the model <span style="color:blue">*(RandomForestClassifier)*</span>
>12. Feature importance <span style="color:blue">*(from feature_importance import feature_importance_plot)*</span>


**STUDY CASE 2- DIABETES**    
***Steps of analyzing dataset and train the model***
> [cs_telco_churn_analysis.ipynb](./workspaces/feature-engineering/notebooks/cs_diabetes_nb.ipynb)  is belonged to this case study. 

>1. Examine the overall picture. <span style="color:blue">*(from examine_data import check_df)*</span> 
>2. Classify the variables as numeric and categorical. <span style="color:blue">*(from classify_data import grab_col_names)*</span> 
>3. Analyze numeric and categorical variables. <span style="color:blue">*(from analyze_data import cat_summary, num_summary)*</span> 