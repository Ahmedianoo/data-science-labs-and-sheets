
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
df= pd.read_csv("requirements_user_data.csv",parse_dates=["signup_date", "last_login"])


#TODO: Draw a box and whiskers diagram to detect outliers for the user salary
#HINT: use df.box_plot
plt.figure()
# WRITE CODE IN THIS LINE
plt.title("Boxplot of Monthly Salary")
plt.ylabel("Monthly Salary")
plt.show()
#########Question to Answer#############:
# Explain the diagram



#TODO Calculate Lower Quartile of purchase_amount
#HINT Use quantile function
# Q1 = 

#TODO Calculate Upper Quartile
# Q3 = 

#TODO Calculate Inter Quartile range
# IQR = 

#TODO Calculate Lower bound
# lower_bound =

#TODO Calculate Upper bound
# upper_bound = 

#TODO Extract the rows of the dfs that contain the outlier
# outliers = 

#TODO Uncomment the following lines after completing the above tasks
# print("Purchase Amount IQR Analysis")
# print("Q1:", Q1)
# print("Q3:", Q3)
# print("IQR:", IQR)
# print("Lower Bound:", lower_bound)
# print("Upper Bound:", upper_bound)
# print("Number of Outliers:", len(outliers))

#TODO Print the outliers user_id and purchase_amount only



#last login cant be in the future vaidation
today = datetime.today()
#TODO get all rows where the last_login is in the future
# future_login =


#TODO Uncomment the following lines after completing the above tasks
# print("\nFuture Last Login Dates:")
# print("Count:", len(future_login))

#TODO Print all extracted rows, print only user_id and last_login


#Questions to answer
#What kind of Validation dimension is this?
#ANSWER: 


#TODO get all rows where the signup_date is later than the last_login
# invalid_login_order = 

#TODO Uncomment the following lines after completing the above tasks
# print("\nLast Login Before Signup:")
# print("Count:", len(invalid_login_order))
# print(invalid_login_order[["user_id", "signup_date", "last_login"]])

#Questions to answer
#What kind of Validation dimension is this 
#ANSWER: 


#Country phone number check
countries = {
    "USA": "+1",
    "UK": "+44",
    "Canada": "+1",
    "Australia": "+61",
    "Germany": "+49"
}
#TODO using the given correct values of country codes extract the rows where the phone_code mismatches the user country
# HINT: You can do this on 2 steps, you can use the map function
# mismatches = 

#TODO Uncomment the following lines after completing the above tasks
# print("\nCountry ↔ Phone Code Mismatches:")
# print("Count:", len(mismatches))


#TODO Print all mismatches, print user_id, country, phone_code, correct_phone_code



#TODO Get the country distribution
#HINT: use value_counts
# country_distribution = 

#TODO Uncomment the following lines after completing the above tasks
# print("\nCountry Distribution (%):")
# print(country_distribution)


#TODO Get the dominant countries where the distribution is greater than 60%
# dominant_country = 

#TODO print the dominant_country


#Questions to answer
#What kind of Validation dimension is this 
#ANSWER: 
