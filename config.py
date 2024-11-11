"""Configuration settings for the project."""

import os
from pathlib import Path
from typing import Dict, List, Any

# Directory Setup
PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
FIGURES_DIR = DATA_DIR / "figures"
CACHE_DIR = DATA_DIR / "cache"

# Create directories if they don't exist
for directory in [DATA_DIR, RAW_DIR, PROCESSED_DIR, FIGURES_DIR, CACHE_DIR]:
    directory.mkdir(exist_ok=True, parents=True)

# Data Processing Settings
DEFAULT_ENCODING = "utf-8"
DATE_FORMAT = "%Y-%m-%d"
CHUNK_SIZE = 10000  # For processing large files

# CDC PLACES API endpoints configuration
PLACES_DATASETS: Dict[int, Dict[str, str]] = {
    2024: {
        'url': 'https://data.cdc.gov/api/views/yjkw-uj5s/rows.csv',
        'name': 'PLACES-Census-Tract-Data-GIS-Friendly-Format-2024',
        'measures_url': 'https://data.cdc.gov/api/views/yjkw-uj5s'
    },
    2023: {
        'url': 'https://data.cdc.gov/api/views/hky2-3tpn/rows.csv',
        'name': 'PLACES-Census-Tract-Data-GIS-Friendly-Format-2023',
        'measures_url': 'https://data.cdc.gov/api/views/hky2-3tpn'
    },
    2022: {
        'url': 'https://data.cdc.gov/api/views/shc3-fzig/rows.csv',
        'name': 'PLACES-Census-Tract-Data-GIS-Friendly-Format-2022',
        'measures_url': 'https://data.cdc.gov/api/views/shc3-fzig'
    },
    2021: {
        'url': 'https://data.cdc.gov/api/views/mb5y-ytti/rows.csv',
        'name': 'PLACES-Census-Tract-Data-GIS-Friendly-Format-2021',
        'measures_url': 'https://data.cdc.gov/api/views/mb5y-ytti'
    },
    2020: {
        'url': 'https://data.cdc.gov/api/views/ib3w-k9rq/rows.csv',
        'name': 'PLACES-Census-Tract-Data-GIS-Friendly-Format-2020',
        'measures_url': 'https://data.cdc.gov/api/views/ib3w-k9rq'
    }
}

# Health Measures Configuration
HEALTH_MEASURES_CONFIG = {
    'health_outcomes': {
        'ARTHRITIS': 'Arthritis among adults aged ≥18 years',
        'BPHIGH': 'High blood pressure among adults aged ≥18 years',
        'CANCER': 'Cancer (excluding skin cancer) among adults aged ≥18 years',
        'CASTHMA': 'Current asthma among adults aged ≥18 years',
        'CHD': 'Coronary heart disease among adults aged ≥18 years',
        'COPD': 'Chronic obstructive pulmonary disease among adults aged ≥18 years',
        'DEPRESSION': 'Depression among adults aged ≥18 years',
        'DIABETES': 'Diagnosed diabetes among adults aged ≥18 years',
        'HIGHCHOL': 'High cholesterol among adults aged ≥18 years',
        'STROKE': 'Stroke among adults aged ≥18 years'
    },
    
    'prevention': {
        'ACCESS2': 'Current lack of health insurance among adults aged 18-64 years',
        'CHECKUP': 'Visits to doctor for routine checkup within the past year among adults aged ≥18 years',
        'CHOLSCREEN': 'Cholesterol screening among adults aged ≥18 years',
        'COLON_SCREEN': 'Fecal occult blood test, sigmoidoscopy, or colonoscopy among adults aged 50-75 years',
        'DENTAL': 'Visits to dentist or dental clinic among adults aged ≥18 years',
        'MAMMOUSE': 'Mammography use among women aged 50-74 years',
        'BPMED': 'Taking medicine for high blood pressure control among adults aged ≥18 years with high blood pressure'
    },
    
    'health_risk_behaviors': {
        'BINGE': 'Binge drinking among adults aged ≥18 years',
        'CSMOKING': 'Current smoking among adults aged ≥18 years',
        'LPA': 'No leisure-time physical activity among adults aged ≥18 years',
        'OBESITY': 'Obesity among adults aged ≥18 years',
        'SLEEP': 'Sleeping less than 7 hours among adults aged ≥18 years'
    },
    
    'disabilities': {
        'HEARING': 'Hearing disability among adults aged ≥18 years',
        'VISION': 'Vision disability among adults aged ≥18 years',
        'COGNITION': 'Cognitive disability among adults aged ≥18 years',
        'MOBILITY': 'Mobility disability among adults aged ≥18 years',
        'SELFCARE': 'Self-care disability among adults aged ≥18 years',
        'INDEPLIVE': 'Independent living disability among adults aged ≥18 years',
        'DISABILITY': 'All disability types among adults aged ≥18 years'
    },
    
    'health_status': {
        'GHLTH': 'Mental health not good for ≥14 days among adults aged ≥18 years',
        'MHLTH': 'Mental health not good for ≥14 days among adults aged ≥18 years',
        'PHLTH': 'Physical health not good for ≥14 days among adults aged ≥18 years',
        'TEETHLOST': 'All teeth lost among adults aged ≥65 years'
    },
    
    'social_needs': {
        'ISOLATION': 'Social isolation among adults aged ≥18 years',
        'FOODINSECU': 'Food insecurity among adults aged ≥18 years',
        'HOUSINSECU': 'Housing insecurity among adults aged ≥18 years',
        'SHUTUTILITY': 'Utility shutoff among adults aged ≥18 years',
        'LACKTRPT': 'Lack of transportation among adults aged ≥18 years',
        'EMOTIONSPT': 'Lack of emotional support among adults aged ≥18 years'
    },
    
    'sdoh': {
        'FOODSTAMP': 'Food stamp benefits among adults aged ≥18 years'
        # Note: More SDOH measures could be derived from geographic and demographic data
    }
}

# Helper functions for accessing measures
def get_measures_by_category(category: str) -> List[str]:
    """Get list of measure codes for a specific category."""
    return list(HEALTH_MEASURES_CONFIG.get(category, {}).keys())

def get_all_measures() -> List[str]:
    """Get list of all measure codes."""
    return [measure for category in HEALTH_MEASURES_CONFIG.values() 
            for measure in category.keys()]

def get_measure_description(measure: str) -> str:
    """Get description for a specific measure code."""
    for category in HEALTH_MEASURES_CONFIG.values():
        if measure in category:
            return category[measure]
    return None

# Define measure types for data processing
MEASURE_TYPES = {
    'prevalence': '_CrudePrev',
    'confidence_interval': '_Crude95CI'
}

# Column name helpers
def get_prevalence_column(measure: str) -> str:
    """Get the prevalence column name for a measure."""
    return f"{measure}_CrudePrev"

def get_ci_column(measure: str) -> str:
    """Get the confidence interval column name for a measure."""
    return f"{measure}_Crude95CI"

# Visualization Settings
CHART_SETTINGS = {
    'width': 800,
    'height': 500,
    'margin': {
        'top': 20,
        'right': 30,
        'bottom': 40,
        'left': 50
    },
    'font_family': 'Arial',
    'title_font_size': 20,
    'axis_font_size': 12,
    'tooltip_font_size': 10
}

# Color Schemes
COLOR_SCHEMES = {
    'sequential': 'blues',
    'diverging': 'red_blue',
    'categorical': 'category10',
    'highlight': '#ff7f0e',
    'background': '#ffffff',
    'choropleth': {
        'scheme': 'blues',
        'steps': 9,
        'reverse': False
    }
}

# Geographic Settings
REGION_MAPPINGS: Dict[str, List[str]] = {
    "Northeast": ["CT", "ME", "MA", "NH", "RI", "VT", "NJ", "NY", "PA"],
    "Midwest": ["IL", "IN", "MI", "OH", "WI", "IA", "KS", "MN", "MO", "NE", "ND", "SD"],
    "South": ["DE", "FL", "GA", "MD", "NC", "SC", "VA", "WV", "AL", "KY", "MS", "TN", "AR", "LA", "OK", "TX"],
    "West": ["AZ", "CO", "ID", "MT", "NV", "NM", "UT", "WY", "AK", "CA", "HI", "OR", "WA"]
}

# Population Size Categories
POPULATION_CATEGORIES = {
    'small': (0, 50000),
    'medium': (50000, 500000),
    'large': (500000, float('inf'))
}

# Data Quality Thresholds
DATA_QUALITY = {
    'min_population': 1000,
    'max_missing_pct': 20.0,
    'confidence_interval_threshold': 95
}

# Cache Settings
CACHE_ENABLED = True
CACHE_TIMEOUT = 3600  # seconds

# Error Messages
ERROR_MESSAGES = {
    'data_not_found': 'Dataset for year {} not found',
    'invalid_measure': 'Invalid health measure: {}',
    'processing_error': 'Error processing data: {}',
    'visualization_error': 'Error creating visualization: {}'
}

# Logging Configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

def get_file_path(year: int) -> Path:
    """Helper function to get file path for a given year."""
    return RAW_DIR / f"places_{year}.csv"

def get_processed_file_path(year: int, measure: str) -> Path:
    """Helper function to get processed file path for a given year and measure."""
    return PROCESSED_DIR / f"places_{year}_{measure.lower()}.csv"

def get_figure_path(name: str, year: int = None) -> Path:
    """Helper function to get figure file path."""
    if year:
        return FIGURES_DIR / f"{name}_{year}.png"
    return FIGURES_DIR / f"{name}.png"

def get_cache_path(name: str) -> Path:
    """Helper function to get cache file path."""
    return CACHE_DIR / f"{name}.pkl"

# Validation helper
def is_valid_measure(measure: str) -> bool:
    """Check if a health measure is valid."""
    return measure in get_all_measures()

def is_valid_year(year: int) -> bool:
    """Check if a year is valid."""
    return year in PLACES_DATASETS