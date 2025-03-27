#######################################################################################################################################################
# 
# Name: Shraddha Thakre
# SID: 740100657
# Exam Date: 27-03-2025
# Module: BEMM458 Programming in Business analytics
# Github link for this assignment:  
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 

# Initialize an empty list to store (start, end) positions

#list of words 
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}
#initailized of empty list to store (start,end ) positions 
my_list[]

my_key[7,7]
#my student id starts with 7 and ends with 7 

#loop through assign keys 
for key in my_key:
    word=key_comments[key]
    start=customer_feedback.find(word)
    
#if word is found find end index and appendex 
    if start != -1:
        end=start len(word)
        my_list.append((start,end))
        
print(my_list)
        

##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:
# Insert last two digits of ID number here:

# Write your code for Operating Profit Margin

# Write your code for Revenue per Customer

# Write your code for Customer Churn Rate

# Write your code for Average Order Value

# Call your designed functions here
# write your code 

# Insert your SID digits here
first_two_digits = 74  #  first two digits
last_two_digits = 57   #  last two digits

# Sample values derived from your SID digits for demonstration
operating_profit = first_two_digits * 3000     
revenue = last_two_digits * 2000                
total_revenue = first_two_digits * 5000        
total_customers = last_two_digits + 100       
lost_customers = last_two_digits // 2          
number_of_orders = first_two_digits + 20        

#function 1: Operating profit :
def operating_profit_margin(profit,revenue):
    return(profit/revenue)*100

#function 2: Revenue per Customer:
def revenue_per_customer(total_revenue, total_customers):
    return (total_revenue / total_customers)

# Function 3: Customer Churn Rate
def customer_churn_rate(lost_customers, total_customers):
    return (lost_customers / total_customers) * 100

# Function 4: Average Order Value
def average_order_value(total_revenue, number_of_orders):
    return (total_revenue / number_of_orders)

print("operating profit margin:", operating_profit_margin(operating_profit, revenue))
print("Revenue per Customer:", revenue_per_customer(total_revenue, total_customers))
print("Customer Churn Rate:", customer_churn_rate(lost_customers, total_customers))
print("Average Order Value:", average_order_value(total_revenue, number_of_orders))


##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here

#importing the libraries
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression

price = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1)
demand = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])


#applying linear regreession model 
model=LinearRegression()
model.fit(price,demand)

#predecting demand at price  £52
price_52=np.array([[52]])
predicted_demand = model.predict(prices.reshape(-1, 1))
revenue= price*predicted_demand

#finding price that maximizes the revenue 
max_revenue_index=np.argmax(revenue)
optimal_price=prices[max_revenue_index]
max_revenue= revenue[max_revenue_index]

print("Demand at 52 pounds:", round(predicted_demand_52[0]))
print("optimal price for maximum revenue:", optimal_price )
print("maximum revenue:",round(max_revenue))


##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max-value = integer(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='O', markercolor='green', markeredgcolor='red', linestyle='--', lable='Random Numbers', color='blue');
plt.title(Line Chart of 100 Random Numbers)
plt.xlabel="Index"
plt.ylabel="Random Number"
plt.legend('---')
plt.grid(True)
plt.show()

#write your code here 
# solution
import ramdom
import matplotlib.pyplot as plt 
# generating 100 random numbers between 1 and 740100657(student id number)
max_value=int(input("Enter student id number:"))
random_numbers=[random.randint(1, max_value )for i in range (100) ]
print(random_numbers)

#student id number: 740100657




