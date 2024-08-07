# ₦ Selenium Automation and webscraping victoria island Lagos rental houses for prediction using machine learning 

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






