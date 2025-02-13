# final_project_ironhack

**Climate Change and Mental Health Analysis**
This project explores the connection between climate change and mental health. It leverages three key datasets:

Climate Change Data: A dataset on various climate indicators over time (e.g., temperature changes, CO2 emissions, etc.).
Mental Health Survey Data: A dataset containing responses to a questionnaire about mental health, focusing on issues like anxiety, depression, and stress that may be linked to concerns about climate change.
Climate Change-related Reddit Posts: Data collected via the Reddit API, which provides insight into how users are discussing climate change.
The aim of this project is to analyze whether climate change affects mental health outcomes, using both direct survey responses and indirect data from public discussions.

**Project Structure**
1. Data Gathering
Climate Change Dataset: Contains various climate indicators, such as temperature changes, CO2 emissions, etc., spanning multiple years.
Mental Health Survey Dataset: Contains survey responses regarding mental health, potentially reflecting concerns and stressors linked to climate change.
Reddit Data: Public posts and comments related to climate change are collected via the Reddit API. This data provides context for understanding public sentiment and concerns about climate change.
2. Data Cleaning & Preprocessing
Climate Change Dataset: This dataset is cleaned by handling missing values, checking for any outliers, and ensuring that relevant columns (e.g., temperature, CO2 emissions) are correctly formatted.
Mental Health Survey Dataset: Cleaning involves handling missing responses and ensuring that the survey data related to mental health and climate concerns is properly structured.
Reddit Data: Text data is preprocessed to extract relevant content from Reddit posts, focusing on climate change discussions.
3. Analysis & Visualizations
Correlation Between Climate Change and Mental Health: The project examines the relationship between climate change indicators (e.g., rising temperatures, emissions) and mental health responses, such as anxiety and stress. Key trends will be identified to see if changes in climate correspond to higher rates of mental health issues.
Geographical and Temporal Analysis: The project looks at how climate impacts mental health across different regions and time periods. This could involve visualizing disaster events, such as extreme weather, and their effects on mental health.
Climate Change Discussion on Reddit: The project also explores how climate change is discussed on Reddit, including which topics are most commonly mentioned, and the potential link between these discussions and the rise of mental health concerns.
4. Key Findings
Climate and Mental Health Correlation: Insights into how various climate-related factors (e.g., temperature, emissions, natural disasters) may contribute to mental health issues.
Geographic and Temporal Patterns: Identification of regions and timeframes where the mental health effects of climate change are most pronounced.
Public Perception of Climate Change: A comprehensive understanding of how people are talking about climate change and whether these discussions align with mental health concerns.
Tools and Libraries Used
Pandas: For data manipulation and cleaning.
Matplotlib/Seaborn: For visualizing the data (e.g., trend graphs, bar charts, heatmaps).
Reddit API: Used to collect data from Reddit using the PRAW (Python Reddit API Wrapper) library.
Jupyter Notebook: For developing and running the analysis step-by-step.
How to Run the Project
Prerequisites:

Install the necessary libraries:
pip install pandas matplotlib seaborn praw
Data Files:

Ensure you have access to the climate change dataset and the mental health survey dataset.
You will need to set up the Reddit API credentials to collect data from Reddit. Please follow the Reddit API documentation to create a developer account and obtain API keys.
Running the Notebook:

Open the Jupyter notebook and execute the cells in sequence to clean, analyze, and visualize the data.
Reddit API Setup:

To collect data from Reddit, you must set up a Reddit developer account and obtain API keys. More details can be found in the Reddit API documentation.
Conclusion
This project offers a thorough examination of how climate change might impact mental health, combining direct survey data, climate indicators, and public discussion insights. By investigating these areas, it provides valuable insights into the real-world effects of climate change on individuals' mental well-being.

