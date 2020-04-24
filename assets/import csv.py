import pandas as pd 
  
# to read csv file named "samplee" 
a = pd.read_csv("../assets/data/my_weather_data.csv") 
  
# to save as html file 
# named as "Table" 
a.to_html("my_weather_data.html") 
  
# assign it to a  
# variable (string) 
html_file = a.to_html() 
