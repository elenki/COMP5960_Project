"""
Download CDC PLACES datasets.

This module handles downloading and initial saving of CDC PLACES datasets.
It includes functions for downloading single year data and batch downloading
multiple years.
"""

# Standard Library Imports
import logging
import sys
from pathlib import Path
import requests
import pandas as pd
from typing import Optional, List

# Setup paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

# Import project config
from config import (
    PLACES_DATASETS,
    RAW_DIR,
    get_file_path,
    is_valid_year,
    LOG_LEVEL,
    LOG_FORMAT
)

# Set up logging
logging.basicConfig(
    level=LOG_LEVEL,
    format=LOG_FORMAT
)
logger = logging.getLogger(__name__)

def download_places_data(year: int, force_download: bool = False) -> Optional[Path]:
    """
    Download CDC PLACES data for a specific year.

    Args:
        year: The year to download data for
        force_download: If True, download even if file exists

    Returns:
        Path to downloaded file or None if download failed
    
    Raises:
        ValueError: If year is not valid
    """
    if not is_valid_year(year):
        raise ValueError(f"Invalid year: {year}. Must be one of {list(PLACES_DATASETS.keys())}")
    
    output_path = get_file_path(year)

    # Create raw directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Skip if file exists and force_download is False
    if output_path.exists() and not force_download:
        logger.info(f"File for year {year} already exists at {output_path}")
        return output_path

    url = PLACES_DATASETS[year]['url']
    logger.info(f"Downloading data for {year} from {url}")
    
    try:
        # Stream the download to handle large files
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        
        logger.info(f"Successfully downloaded data to {output_path}")
        return output_path
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Error downloading data for year {year}: {str(e)}")
        return None

def validate_download(file_path: Path) -> bool:
    """
    Validate downloaded file by checking if it can be read as CSV.

    Args:
        file_path: Path to downloaded file

    Returns:
        True if file is valid, False otherwise
    """
    try:
        # Try reading first few rows to validate CSV format
        pd.read_csv(file_path, nrows=5)
        return True
    except Exception as e:
        logger.error(f"Error validating file {file_path}: {str(e)}")
        return False

def download_multiple_years(years: List[int], force_download: bool = False) -> List[Path]:
    """
    Download CDC PLACES data for multiple years.

    Args:
        years: List of years to download data for
        force_download: If True, download even if files exist

    Returns:
        List of paths to successfully downloaded files
    """
    downloaded_files = []
    
    for year in years:
        try:
            file_path = download_places_data(year, force_download)
            if file_path and validate_download(file_path):
                downloaded_files.append(file_path)
            else:
                logger.warning(f"Failed to download or validate data for year {year}")
        except Exception as e:
            logger.error(f"Error processing year {year}: {str(e)}")
            continue
    
    return downloaded_files

def main():
    """Main function to download all available years."""
    # Download all available years
    years = sorted(PLACES_DATASETS.keys())
    logger.info(f"Starting download for years: {years}")
    
    downloaded_files = download_multiple_years(years)
    
    logger.info(f"Successfully downloaded {len(downloaded_files)} files")
    for file_path in downloaded_files:
        logger.info(f"Downloaded: {file_path}")

if __name__ == "__main__":
    main()