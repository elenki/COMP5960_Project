# Visual exploration of chronic disease patterns across the United States
PLACES (Population Level Analysis and Community Estimates) data from the CDC provides county-level estimates of chronic disease prevalence, health outcomes, and health behaviors. This project aims to create an interactive dashboard for visualizing chronic disease patterns across the United States using CDC PLACES data.

## Analysis Goals
### Geographic Patterns
- Visualize geographic patterns of chronic disease prevalence across the United States
- Analyze urban-rural differences in chronic disease prevalence and health outcomes
- Identify specific regions or clusters where specific chronic diseases are more prevalent than others

### Impact of Social Determinants
- Explore the relationship between social determinants of health and chronic disease prevalence
- Anlayze the impact of income, education, and other social determinants on health outcomes
- Analyze the relationship between health behaviors and chronic disease prevalence

### Temporal Trends
- Analyze temporal trends in chronic disease prevalence and health outcomes

## Visualization Approach
Altair will be used to create interactive visualizations for exploring chronic disease patterns across the United States. The following types of visualizations will be created:
- To visualize geographic patterns, we will primarily use choropleth maps to show chronic disease prevalence at different geographic levels (e.g., state, county). We may also use other linked visualizations for interactive exploration or to show additional information.
- To explore the relationship between social determinants and chronic disease prevalence, we will use scatter plots, bar charts, bubble charts, and other visualizations to show the relationship between different variables. We will also create a parallel coordinates plot to show patterns across multiple variables.
- For temporal trends, we will use line charts, area charts, and other visualizations to show how chronic disease prevalence has changed over time.

## Data Sources
- [CDC PLACES Data](https://www.cdc.gov/places/index.html): County-level estimates of chronic disease prevalence, health outcomes, and health behaviors
- Data will be downloaded from the CDC PLACES website and preprocessed for visualization
- Additional data sources may be included to explore the relationship between social determinants and chronic disease prevalence
- Data definitions are available in the [PLACES Data Dictionary](https://www.cdc.gov/places/measure-definitions/index.html)

## Tools and Libraries
- Python: Data preprocessing, analysis, and visualization
- Altair: Interactive visualization library for creating visualizations

## Team Members
- [Chetan Elenki]
- [Kalpana Simhadri]
- [Nathaniel Masson]

Part of course project for Applied Data Visualization course (COMP5960) at the University of Utah - Fall 2024 semester - [Course Website](https://www.dataviscourse.net/2024-applied/)