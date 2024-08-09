# ₦ Selenium Automation and Using BeautifulSoup for webscraping victoria island Lagos rental houses for prediction using machine learning 

[![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)](https://www.python.org)  [![](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/) [![](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org) [![](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org) [![](https://img.shields.io/badge/conda-342B029.svg?&style=for-the-badge&logo=anaconda&logoColor=white)](https://www.anaconda.com)


![lagos pic](https://github.com/Algora-NG/VI_HOUSE_PRICE_PREDICTION/assets/157173680/b8cc8333-cd0c-4ea8-a932-3c1dfeb21dbe)

## Introduction

This project focuses on automating the web scraping of rental house listings in Victoria Island, Lagos, using Selenium, and applying machine learning techniques to predict rental prices. The vibrant real estate market in Victoria Island presents a rich dataset for analysis, and understanding the rental pricing patterns can offer valuable insights to potential renters and real estate investors.

### Objectives

  Primarily, the objectives of this project are:
  
● Web Scraping: Automate the collection of rental house data from real estate website. Key data points include rental price, number of bedrooms, bathrooms, toilets, and parking spaces.

● Data Cleaning and Preprocessing: Clean and preprocess the scraped data to ensure it is suitable for analysis and machine learning model training.

● Exploratory Data Analysis (EDA): Perform EDA to understand the relationships between various features and the rental price.

● Model Training: Train various machine learning models to predict rental prices based on the collected data.

● Model Evaluation: Evaluate the performance of the models using appropriate metrics and select the best-performing model.

● Deployment: Deploy the predictive model using Streamlit to provide an interactive web application where users can input property features and get rental price predictions.

## Tools and Technologies Used

  I utilized the following tools and technologies for this project
  
● Selenium: For web scraping and automation of data collection.

● BeautifulSoup: For parsing HTML content.

● Pandas: For data manipulation and analysis.

● Scikit-Learn: For building and evaluating machine learning models.

● Streamlit: For deploying the predictive model as an interactive web application.


## How Selenium was Utilized

Selenium was utilized in this project to automate the process of web scraping rental house data from the NigeriaPropertyCentre website. The goal was to collect data efficiently and accurately to build a comprehensive dataset for machine learning models to predict rental prices. Here’s an in-depth look at how Selenium was used:

#### Browser Automation

Selenium's WebDriver was employed to control a web browser, mimicking the actions of a human user. By automating the browser, Selenium can navigate through web pages, interact with elements, and extract information without manual intervention.

#### Navigating to the Website

Selenium initiated a browser instance and directed it to the NigeriaPropertyCentre website. This automation ensures that the browser consistently reaches the correct webpage every time the script is executed, providing a reliable starting point for data collection.

####  Interacting with Web Elements
Selenium interacted with various web elements on the page to set up the search parameters. This involved:

   -  Clicking Tabs and Links: Selenium clicked on the "For Rent" tab to filter properties available for rent. This action ensured that only rental properties were displayed.
     
  - Selecting Dropdown Options: Selenium selected specific options from dropdown menus to refine the search criteria. For example, it chose "House" as the property type, and set the minimum and maximum rental prices. This selection narrowed down the search results to only those listings that met the specified criteria.

   - Entering Text: Selenium filled in the search bar with the desired location, "vi, Lagos," to focus the search on properties in Victoria Island.

#### Form Submission

After setting all the search parameters, Selenium submitted the form to execute the search. This involved clicking the search button, which triggered the website to display the filtered search results.

#### Waiting for Page Load

Selenium included strategic pauses to ensure that each webpage and element fully loaded before the script attempted the next interaction. These pauses helped to avoid errors caused by trying to interact with elements that had not yet appeared on the page.


KINDLY CLICK ON THE LINK TO SEE MY SELENIUM CODE: https://github.com/PATRICK079/VI_RealEstate_Predictions.git


## How BeautifulSoup was Utilized

BeautifulSoup is a powerful Python library used for parsing HTML and XML documents. It creates parse trees from page source code that can be used to extract data easily. In this project, BeautifulSoup was utilized to parse and extract detailed information from the HTML content of the NigeriaPropertyCentre website after Selenium automated the navigation and search processes. Here’s a detailed look at how BeautifulSoup was employed:

#### Fetching the HTML Content

After Selenium navigated to the search results page and the desired data was loaded, the page's HTML content was fetched using the requests library. By simulating a browser request with appropriate headers, BeautifulSoup ensured that the server recognized the request as coming from a real browser, facilitating access to the webpage content.

####  Parsing the HTML Document

BeautifulSoup parsed the HTML content fetched by the requests library. It created a structured tree of the HTML document, enabling easy navigation and data extraction. This parsing transformed the raw HTML into a BeautifulSoup object, which provided various methods to search and navigate the document.

#### Navigating the HTML Structure

BeautifulSoup allowed for efficient navigation through the HTML structure of the webpage. By examining the HTML elements, classes, and IDs, BeautifulSoup identified and targeted specific elements containing the data of interest. For example, it located the main container that held the property listings.

#### Extracting Data from HTML Elements
Once the relevant HTML elements were identified, BeautifulSoup extracted the required data. This involved:

 - Identifying Tags and Attributes: BeautifulSoup searched for specific HTML tags and attributes that contained the desired data. For example, it identified div tags with specific class names or attributes that represented individual property listings.
   
- Extracting Text and Attributes: BeautifulSoup extracted the text content and attributes (such as URLs or image sources) from the targeted HTML elements. This process gathered information such as property prices, locations, number of bedrooms, bathrooms, and other relevant details.

####  Handling Nested Elements

BeautifulSoup efficiently handled nested HTML elements. It navigated through parent-child relationships within the HTML document to extract data from deeply nested elements. This capability was crucial for extracting comprehensive information about each property listing, as details were often nested within multiple layers of HTML tags.

#### Storing and Structuring Data

After extracting the data, BeautifulSoup facilitated the organization and storage of the information in a structured format, such as lists or dictionaries. This structured data was then ready for further analysis and processing, enabling the development of machine learning models for rental price prediction.

####  Handling Multiple Listings

BeautifulSoup was used to iterate through multiple property listings on the results page. By identifying and looping through each listing element, BeautifulSoup extracted data from each property, ensuring a comprehensive dataset covering all listings on the page



KINDLY CLICK ON THE LINK TO SEE MY BeautifulSoup CODE and process: https://github.com/PATRICK079/VI_RealEstate_Predictions.git

###  Data importation, exploration and preprocessing


  I imported my dataset as a csv file and  dove into the dataset by gaining insights into the various features and their distributions, i understood the relationships between different vairables and their potential impact on predicting rental houses.

I started off by exploring with countplot on the bedroom feature  to visualize the number of bedrooms in my dataset; similarly, i did same accros other features.

I also did a pairplot with some continous features ( numeric) with hue as my target to visualize if i would have a clearer seperation between prices.

I did more exploration using the bar plot on some numerical features,other  data visualizations were done including correlation matrix and heatmap.

kindly check this link for the complete data exploration: https://github.com/PATRICK079/VI_RealEstate_Predictions.git 

I started the data preprocessing stage by

- Making sure the right data type was asigned to each feature using info()

- Checked for outliers using the box plot on the continous features or using the descritive statistical summary

- Train_test_split the dataset

- Encoded my categorical featurs using get_dummies both on train and test dataset

- I performed feature scaling using MinMax scaler. I fit only on Train and transform train and test. The scaling was done Linear Regression and Elasticnet model alone. 

kindly check this link for the complete data proprocessing: https://github.com/PATRICK079/VI_RealEstate_Predictions.git  

## Model Development
  
To solve this project I built some predictive models looking for the best model possible for my predictions and afterwards made comparisons of each model complexity and generalization. The following models were utilized in this project  

- Linear Regression
- polynomial Regression
- Elastinet ( LASSO/RIDGE) 

  BELOW IS THE SUMMARY METRICS OF THE BUILT MODELS

<img width="985" alt="Screen Shot 2024-08-09 at 17 24 31" src="https://github.com/user-attachments/assets/a609f1ab-b316-4a16-8629-b3a7994da52f">



FROM THE ABOVE SUMMARY; IT IS EVIDENT THAT POLYNOMIAL REGRESSION IS MY BEST PERFORMING MODEL. HENCE, POLYNOMIAL REGRESSION WOULD BE SAVED AND DEPLOYED USING STREAMLIT 


# MODEL DEPLOYMENT

   My best performing model was saved, including the my columns and ploynimal converter. To put the model into use, i had to deploy the model harnessing the capability of
   
   streamlit.

BELOW IS STREAMLIT CODE

  <img width="928" alt="Screen Shot 2024-08-09 at 17 37 47" src="https://github.com/user-attachments/assets/7a98c0a3-9acc-409e-97d6-dcc2f4d22bcf">

KINDLY INTERACT WITH THE DEPLOYED MODEL VIA THIS LINK AND LEAVE A FEEDBACK: https://virealestatehouseprices.streamlit.app/ 
