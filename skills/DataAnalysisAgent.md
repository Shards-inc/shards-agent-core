# DataAnalysisAgent Skill

## Description
The `DataAnalysisAgent` is a specialized agent within the Shards AI Agent System designed to perform comprehensive data analysis and generate insightful reports. It can process both structured and unstructured data, identify trends, extract key information, and present findings in a clear and concise manner.

## Capabilities
- **Data Ingestion**: Ability to ingest data from various sources (e.g., databases, spreadsheets, APIs).
- **Data Cleaning and Preprocessing**: Handles missing values, outliers, and data inconsistencies.
- **Statistical Analysis**: Performs descriptive and inferential statistical analysis.
- **Pattern Recognition**: Identifies patterns, correlations, and anomalies within datasets.
- **Report Generation**: Creates detailed reports with summaries, key findings, and recommendations.
- **Visualization**: Generates various types of data visualizations (e.g., charts, graphs) to illustrate insights.

## Usage
The `DataAnalysisAgent` can be invoked to perform specific data analysis tasks. It requires a clear definition of the data source, the type of analysis required, and the desired output format.

### Example Task
```json
{
  "task": "Analyze Q1 2026 sales data from the 'sales_database' to identify top-performing products and regional sales trends. Generate a summary report with a bar chart of product sales and a line graph of regional performance over time."
}
```

## Integration
This agent can be integrated into larger workflows orchestrated by the `OrchestratorAgent` to provide data-driven insights for complex business processes.
