## Overview

This interactive dashboard provides comprehensive analysis of air quality metrics and their health implications across different cities. It visualizes relationships between air pollution (PM2.5, PM10, NO2, AQI), weather conditions (temperature, humidity), population density, and hospital admissions.

## Features

- **Multi-city comparison** of air quality metrics
- **Time-series analysis** of pollution levels
- **Correlation visualization** between air quality and health outcomes
- **3D weather impact analysis** on air quality
- **Interactive controls** for customizing data views
- **Responsive design** works on different screen sizes

## Data Sources

The dashboard uses the `air_quality_health_dataset` which contains:

- Air quality metrics: AQI, PM2.5, PM10, NO2, O3
- Weather data: temperature, humidity
- Health outcomes: hospital admissions
- Demographic data: population density, hospital capacity
- Geographic data: city names, urban/rural classification

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nabi-noor/presswald-assessment.git
   cd presswald-assessment
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the dashboard:
   ```bash
   preswald run
   ```

## Usage

1. **Control Panel**:
   - Select two cities for comparison
   - Adjust the number of data points to display

2. **Air Quality Metrics**:
   - View trends of PM2.5, PM10, NO2, and AQI over time
   - Compare pollution levels between cities

3. **Population & Health Impact**:
   - Analyze relationships between population density and air quality
   - Examine hospital admissions patterns

4. **Weather Factors**:
   - 3D visualization of temperature/humidity impact on AQI

5. **Health Impact Analysis**:
   - Direct correlation between AQI and hospital admissions

## Code Structure

```
air-quality-dashboard/
├── app.py                
├── README.md             
├── requirements.txt      
├── data/                 
|── images/
├── preswald.toml
├── secrets.toml               
```