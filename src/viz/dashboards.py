"""Dashboard layout and integration."""

import streamlit as st
from .charts import BubbleChart, ParallelCoordinatesPlot, FacetedBarChart

class Dashboard:
    """Main dashboard class integrating all visualizations."""
    
    def __init__(self):
        self.bubble_chart = BubbleChart()
        self.parallel_coords = ParallelCoordinatesPlot()
        self.faceted_bars = FacetedBarChart()
    
    def run(self):
        """Runs the dashboard."""
        st.title("Chronic Disease Patterns in the US")
        
        # Sidebar controls
        st.sidebar.header("Filters")
        # Add your filter controls here
        
        # Main content
        st.header("Disease Prevalence by Region")
        # Add your visualizations here
        
        # Additional sections
        st.header("Multi-Disease Comparison")
        # Add more visualizations
        
        # Notes and documentation
        st.markdown("### Notes")
        st.markdown("Data source: CDC PLACES dataset")