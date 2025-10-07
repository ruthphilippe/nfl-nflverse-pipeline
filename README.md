🏈 NFL Data Pipeline & Game Score Prediction

Automating NFL data collection, cleaning, and machine learning predictions

**Overview**

This project automates the collection of NFL game data using nflreadpy (powered by the nflverse project), stores it in AWS S3, and builds a machine learning model to predict future game scores. It’s designed to demonstrate a full end-to-end data pipeline — from automated ingestion to cloud storage and predictive modeling.

**Features**

**Automated Data Pipeline**

Fetches daily NFL data (schedules, team & player stats, injuries)

Cleans and stores it as partitioned Parquet files in AWS S3

Organized by season and run date (e.g., season=2024/run_date=2025-10-07/)

**Machine Learning Model**

Uses LinearRegression from Scikit-learn to predict game scores

Trains on historical team statistics

Evaluated using Mean Absolute Error (MAE)

Produces realistic predictions for upcoming games

**AWS Integration**

Outputs are uploaded automatically to S3:

s3://nfl-data-ruth/nfl/predictions/run_date=YYYY-MM-DD/predictions.csv

🧾 Example Output

Training Results

**Mean Absolute Error: 2.64**


**Predictions**

   week home_team away_team  predicted_home_score  predicted_away_score
0    19       PHI        GB                  28.1                  24.5
1    19        TB       WAS                  22.8                  23.2
2    19        LA       MIN                  21.3                  23.5
3    20        KC       HOU                  24.3                  20.5
4    20       DET       WAS                  29.8                  23.2

☁️ AWS Output Structure
s3://nfl-data-ruth/
│
├── nfl/
│   ├── bronze/
│   │   ├── schedules/
│   │   ├── team_stats_week/
│   │   └── injuries/
│   └── predictions/
│       └── run_date=2025-10-07/
│           └── predictions.csv

⚙️ Setup Instructions

Clone the repo

git clone https://github.com/ruthphilippe/nfl-nflverse-pipeline.git
cd nfl-nflverse-pipeline

Run locally

python pipeline.py
python model_pipeline.py

Workflow is configured in .github/workflows/daily.yml

**Key Learnings**

Building cloud-based data pipelines using AWS S3

Automating ETL + ML workflows via GitHub Actions

Integrating nflverse open datasets into predictive analytics

Structuring production-ready ML projects for portfolio or Upwork jobs

Author

Ruth Philippe
Data Scientist & Machine Learning Engineer
📍 Santo Domingo, Dominican Republic
🔗 github.com/ruthphilippe
💼 linkedin.com/in/ruthphilippe

