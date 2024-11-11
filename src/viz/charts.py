"""Core visualization components for the dashboard."""

import altair as alt
import pandas as pd
from typing import Optional, Dict, Any

class BubbleChart:
    """Interactive bubble chart showing disease prevalence by region."""
    
    def __init__(self, width: int = 800, height: int = 500):
        self.width = width
        self.height = height
        
    def create_chart(self, 
                    data: pd.DataFrame, 
                    x_column: str,
                    y_column: str,
                    size_column: str,
                    color_column: str,
                    tooltip_columns: Optional[list] = None) -> alt.Chart:
        """Creates an interactive bubble chart.
        
        Args:
            data: DataFrame containing the data to visualize
            x_column: Column name for x-axis
            y_column: Column name for y-axis
            size_column: Column name for bubble size
            color_column: Column name for bubble color
            tooltip_columns: List of column names to show in tooltip
            
        Returns:
            Altair Chart object
        """
        # Base chart
        base = alt.Chart(data).encode(
            x=alt.X(x_column),
            y=alt.Y(y_column),
            size=alt.Size(size_column),
            color=alt.Color(color_column),
            tooltip=tooltip_columns or [x_column, y_column, size_column, color_column]
        )
        
        # Add interactive elements
        chart = base.mark_circle().properties(
            width=self.width,
            height=self.height
        ).interactive()
        
        return chart

class ParallelCoordinatesPlot:
    """Interactive parallel coordinates plot for multi-disease comparison."""
    
    def __init__(self, width: int = 800, height: int = 500):
        self.width = width
        self.height = height
    
    def create_chart(self,
                    data: pd.DataFrame,
                    dimensions: list,
                    color_by: str) -> alt.Chart:
        """Creates a parallel coordinates plot.
        
        Args:
            data: DataFrame containing the data
            dimensions: List of columns to use as dimensions
            color_by: Column name to use for line color
            
        Returns:
            Altair Chart object
        """
        # Normalize the data for better visualization
        scaled_df = data.copy()
        for dim in dimensions:
            if dim != color_by:
                scaled_df[dim] = (data[dim] - data[dim].min()) / (data[dim].max() - data[dim].min())
        
        # Create the parallel coordinates
        chart = alt.Chart(scaled_df).transform_fold(
            dimensions,
            as_=['Dimension', 'Value']
        ).mark_line().encode(
            x='Dimension:N',
            y='Value:Q',
            color=alt.Color(f'{color_by}:N'),
            detail='index:N',
            tooltip=dimensions
        ).properties(
            width=self.width,
            height=self.height
        ).interactive()
        
        return chart

class FacetedBarChart:
    """Faceted bar chart for disease prevalence comparison."""
    
    def __init__(self, width: int = 800, height: int = 500):
        self.width = width
        self.height = height
    
    def create_chart(self,
                    data: pd.DataFrame,
                    category_column: str,
                    value_column: str,
                    facet_column: str,
                    sort_by: Optional[str] = None) -> alt.Chart:
        """Creates a faceted bar chart.
        
        Args:
            data: DataFrame containing the data
            category_column: Column name for categories
            value_column: Column name for values
            facet_column: Column name for faceting
            sort_by: Optional column name to sort by
            
        Returns:
            Altair Chart object
        """
        chart = alt.Chart(data).mark_bar().encode(
            x=alt.X(f'{value_column}:Q'),
            y=alt.Y(f'{category_column}:N',
                   sort=alt.EncodingSortField(field=sort_by) if sort_by else None),
            tooltip=[category_column, value_column]
        ).properties(
            width=self.width,
            height=self.height
        ).facet(
            facet=alt.Facet(f'{facet_column}:N', columns=2)
        ).interactive()
        
        return chart