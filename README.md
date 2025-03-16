# Gender Disparities in STEM Fields

This project investigates why there are fewer women in STEM fields, particularly in subjects like Mechanics, Mathematics, Physics, and Engineering. The analysis was conducted on a dataset provided by [Kaggle](https://www.kaggle.com/datasets/krishnanshverma/academic-performance-of-university-student-dataset?resource=download).

## Project Overview

### Main Question:
Why are there fewer women in fields such as Mechanics, Mathematics, Physics, and Engineering?

### Secondary Questions:
1. **Do women really have fewer representations in STEM fields?**
    - We tested this question and confirmed that yes, there are fewer women in these fields compared to men.
    
2. **Why are there fewer women in these fields?**
    - We hypothesized that women must work harder than men to get into and succeed in these fields. 
    - **Key Finding**: The average GPA before entering the university for women in Mechanics is 3.9, while for men it is 3.4. This difference suggests that women have to make greater efforts to enter these programs. This is further explored in the project.

### Dataset
The data used in this project is from the **academic_performance_dataset_V2.csv**. You can access the dataset on Kaggle [here](https://www.kaggle.com/datasets/krishnanshverma/academic-performance-of-university-student-dataset?resource=download).

### Tools Used:
- **Python**
- **Jupyter Notebook** (`Ana.ipynb`)
- **Dash** for interactive dashboards
- **Plotly** for data visualization
- **Pandas** for data manipulation

## How to Run the Project

### Prerequisites:
Make sure you have the following libraries installed:
- `dash`
- `plotly`
- `pandas`
- `matplotlib`
- `numpy`
- `jupyter` (to run the notebook)

To install the dependencies, you can use the following command:

```bash
pip install dash plotly pandas matplotlib numpy jupyter
```
### Methodology

#### Data Processing
- The dataset was cleaned, and relevant columns were extracted to analyze the gender distribution across different academic programs.
- We reclassified program codes into broader categories (e.g., Biology, Computer Science, Mechanics, etc.) to facilitate comparison across related fields.

#### Data Analysis
- We used Plotly for interactive visualizations like treemaps and line graphs to show the distribution of gender and CGPA across various programs and years.
- We analyzed the average GPA of students before entering university to highlight the difference between male and female students in STEM fields.
- We created two different Dash dashboards to provide an interactive way of exploring the data and visualizing the insights.

#### Key Tools & Libraries Used
- **Dash**: For building interactive web dashboards.
- **Plotly**: For creating interactive charts and visualizations.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For generating static plots (e.g., GPA comparison over years).

#### Dashboard 1: Gender Distribution and Topic Visualization
This dashboard displays the number of women and men per program code and the percentage of women across different topics over the years.
It includes:
- A line graph showing the number of women and men by year for a selected program.
- A treemap showing the percentage of women by topic over the years.

#### Dashboard 2: GPA Comparison and Treemaps
This dashboard focuses on the GPA comparison between men and women and provides a treemap visualization for average GPAs by subject.
It includes multiple visualizations, including:
- A bar graph showing the total records by program and year.
- A bar graph showing female records by program and year.
- A treemap showing the average GPA of women and men in different subjects.
- A line graph for comparing GPA before entering university.

### Running the Project:
1. Clone the repository and navigate to the project directory:
```bash
  git clone <repository-url>
  cd <repository-directory>
```
2. Run the first dashboard:
   - Open the `dashboard.py` file to start the first dashboard.
   - Execute the following command to launch the first dashboard:
    ```bash
        python dashboard.py
    ```
   - The dashboard will run on a local web server, and you can view it in your browser at the address provided in the terminal (usually something like `http://127.0.0.1:8050`).
3. Switch to the second dashboard:
   - After exploring the first dashboard, you can view the second dashboard by opening `Ana.ipynb` in Jupyter Notebook or JupyterLab.
   - Execute the cells related to the second dashboard within the notebook to launch the interactive visualization for the second dashboard.

### Conclusion
The project aims to shed light on the gender disparities in STEM fields and provide insights into the challenges women face in these areas. The findings suggest that women have to exert more effort to enter and succeed in fields such as Mechanics, Mathematics, Physics, and Engineering.




