# Zillow Property Data Scraper and Form Filler

## Description
This project is a web scraping and automation tool that extracts property data from a Zillow clone website and automatically fills out a form with the scraped data. It uses requests and BeautifulSoup for web scraping, and selenium for browser automation.

## Features
Web Scraping: Uses requests to fetch the HTML content of the Zillow clone website and BeautifulSoup to parse and extract property data such as addresses, prices, and links.

Data Formatting: Processes and formats the scraped data to ensure it is in the correct format for further use.

Browser Automation: Uses selenium to automate the process of filling out a form with the scraped property data.

Environment Variables: Utilizes environment variables to securely store configuration settings.

## How It Works
Fetch HTML Content: Sends a GET request to the Zillow clone website to retrieve the HTML content.

Parse HTML: Uses BeautifulSoup to parse the HTML and extract property addresses, prices, and links.

Format Data: Processes the extracted data to ensure it is in the correct format.

Initialize WebDriver: Sets up the Selenium WebDriver using ChromeDriverManager and configures it to keep the browser open after the script finishes.

Fill Form: Automates the process of opening a new browser tab, filling out a form with the scraped data, and closing the tab.
