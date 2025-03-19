# Analyzing Renewable Energy Adoption Through Data Science

This repository contains files for the individual course project in SER494: Data Science for Software Engineers (fall 2024) created by Gonzalo Allendes for partial fulfillment of the course requirements.

It was cleared by course staff (R. Acuna) for public release on 1/12/2025.

As part of the class project requirements, the final paper can be found [at this link](https://drive.google.com/file/d/1iTLeK5HtBBmtzcjQrepcu-sGbRNS4RSR/view?usp=drive_link).

### 1. Overview

This project analyzes global trends in renewable energy adoption by processing and visualizing data from multiple sources, including IRENA 2024, Environmental Performance Index (EPI) 2024, and World Bank Population Data. The analysis focuses on public investments, renewable energy capacity, and environmental performance.

### 2. How to Run


1. Create a Python 3.12 virtual environment and install dependencies using ```requirements.txt.```


2. Run the main script:
    ```
    python wf_core.py
    ```

### 3. Components

- **wf_core.py**: 
    
    ```
    Runs data processing (wf_dataprocessing.py) and visualization (wf_visualization.py).
    ```

- **wf_dataprocessing.py**:
    ```
    1) Computes Public Flows per Capita from investment and population data.
    
    2) Calculates the Renewable Energy Share of Electricity Production.
    
    3) Computes Renewable Energy Capacity per Capita.
    
    4) Integrates Environmental Performance Index (EPI) and 
       CDA (Carbon Dioxide Adjusted Emissions Growth Rate).
    ```
- **wf_visualization.py**:
    ```
    1) Generates summary statistics and correlation matrices.
    
    2) Produces scatter plots and bar charts illustrating key findings.
    ```

### 5. Markdown Files Explanation

This repository contains several .md files that document various aspects of the project:

```5.1. project_proposal_initial.md```

- Title: Analyzing Global Trends in Renewable Energy Adoption
- Purpose: This document outlines the research problem, key research questions, and intellectual merit of the study. It
defines the project scope and lists potential data sources, such as IRENA, the World Bank, and the EPI report.

```5.2. project_proposal_revised.md```

- Title: Revised Project Proposal: Analyzing Global Trends in Renewable Energy Adoption
- Purpose: This updated version refines the research questions, methodology, and scope based on initial findings
and feedback. It provides a clearer framework for data analysis and expected outcomes.

```5.3. project_exploration.md```

- Title: Exploratory Data Munging and Visualization
- Purpose: Describes initial exploratory data analysis, including dataset descriptions and preliminary
interpretations of trends in renewable energy adoption. It provides key insights into data integrity, field meanings, and early patterns observed.

```5.4. project_ml_experimentation.md```

- Title: Machine Learning Experimentation
- Purpose: Documents the various machine learning models tested on the dataset, including preprocessing steps, feature 
selection, and hyperparameter tuning. It outlines model performance comparisons and initial insights.

```5.5. project_ml_evaluation.md```

- Title: Machine Learning Evaluation and Results
- Purpose: Summarizes the performance of the final machine learning model, including validation metrics, error 
analysis, and interpretation of results. It discusses the significance of the findings and potential improvements.
