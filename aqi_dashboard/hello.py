from preswald import connect, get_df, table, text, plotly, sidebar, selectbox, slider, query
import plotly.express as px
from datetime import datetime

# Data Query Functions
def get_metrics_df(city1, city2, limit):
    sql = f'''
    SELECT date, city, pm2_5, pm10, no2, aqi
    FROM air_quality_health_dataset
    WHERE city = '{city1}' OR city = '{city2}'
    ORDER BY date ASC
    LIMIT {limit}
    '''
    return query(sql, "air_quality_health_dataset")

def get_population_density_df(city1, city2, limit):
    sql = f'''
    SELECT date, city, population_density, aqi
    FROM air_quality_health_dataset
    WHERE city = '{city1}' OR city = '{city2}'
    ORDER BY date ASC
    LIMIT {limit}
    '''
    return query(sql, "air_quality_health_dataset")

def get_hospital_df(city1, city2, limit):
    sql = f'''
    SELECT date, city, population_density, hospital_admissions
    FROM air_quality_health_dataset
    WHERE city = '{city1}' OR city = '{city2}'
    ORDER BY date ASC
    LIMIT {limit}
    '''
    return query(sql, "air_quality_health_dataset")

def get_weather_distribution_df(city1, city2, limit):
    sql = f'''
    SELECT date, city, aqi, temperature, humidity
    FROM air_quality_health_dataset
    WHERE city = '{city1}' OR city = '{city2}'
    ORDER BY date ASC
    LIMIT {limit}
    '''
    return query(sql, "air_quality_health_dataset")

def get_hospital_on_aqi_df(city1, city2, limit):
    sql = f'''
    SELECT date, city, aqi, hospital_admissions
    FROM air_quality_health_dataset
    WHERE city = '{city1}' OR city = '{city2}'
    ORDER BY date ASC
    LIMIT {limit}
    '''
    return query(sql, "air_quality_health_dataset")

# Chart Functions
def line_chart(df, x, y, color, title):
    return px.line(df, x=x, y=y, color=color, title=title)

def bar_chart(df, x, y, color, title):
    return px.bar(df, x=x, y=y, color=color, title=title)

def box_chart(df, x, y, color, title):
    return px.box(df, x=x, y=y, color=color, title=title)

def scatter_3d_chart(df, x, y, z, color, title):
    return px.scatter_3d(df, x=x, y=y, z=z, color=color, title=title)

# Enhanced Sidebar
sidebar(
    defaultopen=True,
    logo="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg",
    name="Air Quality Dashboard",
    description="Comprehensive air quality and health impact analysis"
)

connect()

# Main Dashboard Header
text("# Air Quality Health Impact Dashboard")
text("### Comprehensive analysis of air quality metrics and their health implications across cities")

df = get_df("air_quality_health_dataset")
count = df.shape[0]

# Control Panel Section
text("## Control Panel")
text("Select your preferred cities and data range to customize the analysis")

limit = slider(
    label="Number of data points to display",
    min_val=10,
    max_val=count,
    step=10,
    default=100
)

city_list = df["city"].unique().tolist()

choice1 = selectbox(
    label="Select the first city",
    options=city_list
)

choice2 = selectbox(
    label="Select the second city",
    options=city_list
)

# Air Quality Metrics Section
text("## Air Quality Metrics Over Time")
text("### Track key air quality indicators and their trends")

metrics_df = get_metrics_df(choice1, choice2, limit)

pm2_5_fig = line_chart(metrics_df, x="date", y="pm2_5", color="city", title=f"PM2.5 Levels Over Time - {choice1} vs {choice2}")
plotly(pm2_5_fig)

pm10_fig = line_chart(metrics_df, x="date", y="pm10", color="city", title=f"PM10 Levels Over Time - {choice1} vs {choice2}")
plotly(pm10_fig)

no2_fig = line_chart(metrics_df, x="date", y="no2", color="city", title=f"NO2 Levels Over Time - {choice1} vs {choice2}")
plotly(no2_fig)

aqi_fig = line_chart(metrics_df, x="date", y="aqi", color="city", title=f"Air Quality Index (AQI) Over Time - {choice1} vs {choice2}")
plotly(aqi_fig)

# Population and Health Impact Section
text("## Population Density & Health Impact Analysis")
text("### Understanding the relationship between population density, air quality, and health outcomes")

# Population Density vs AQI
population_density_df = get_population_density_df(choice1, choice2, limit)
density_box_fig = box_chart(population_density_df, x="population_density", y="aqi", color="city", title=f"Air Quality Index Distribution by Population Density - {choice1} vs {choice2}")
plotly(density_box_fig)

# Hospital Admissions vs Population Density
hospital_df = get_hospital_df(choice1, choice2, limit)
hospital_bar_fig = bar_chart(hospital_df, x="population_density", y="hospital_admissions", color="city", title=f"Hospital Admissions by Population Density - {choice1} vs {choice2}")
plotly(hospital_bar_fig)

# Weather and Environmental Factors Section
text("## Weather & Environmental Factors")
text("### 3D visualization of how temperature and humidity affect air quality")

# Weather Distribution 3D Scatter
weather_distribution_df = get_weather_distribution_df(choice1, choice2, limit)
weather_3d_fig = scatter_3d_chart(weather_distribution_df, x="temperature", y="humidity", z="aqi", color="city", title=f"3D Weather Impact on Air Quality - {choice1} vs {choice2}")
plotly(weather_3d_fig)

# Health Impact Analysis Section
text("## Health Impact Analysis")
text("### Direct correlation between air quality and hospital admissions")

# Hospital Admissions vs AQI
hospital_on_aqi_df = get_hospital_on_aqi_df(choice1, choice2, limit)
hospital_aqi_bar_fig = bar_chart(hospital_on_aqi_df, x="aqi", y="hospital_admissions", color="city", title=f"Hospital Admissions by Air Quality Index - {choice1} vs {choice2}")
plotly(hospital_aqi_bar_fig)

# Dashboard Footer
text("---")
text("### Dashboard Summary")
text(f"**Cities Analyzed:** {choice1} and {choice2}")
text(f"**Data Points:** {limit} records")
text(f"**Total Dataset Size:** {count:,} records")
text("**Last Updated:** " + datetime.now().strftime("%B %d, %Y"))






