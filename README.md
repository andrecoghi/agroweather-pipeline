# Agroweather Pipeline

ETL pipeline using open government data for agriculture and climate analysis. Built with Apache Airflow, PostgreSQL, and Metabase for data orchestration, storage, and visualization.

## Architecture

- **Apache Airflow**: Orchestrates the ETL pipeline with daily scheduling
- **PostgreSQL**: Data warehouse for processed agricultural data
- **Metabase**: Business intelligence and data visualization
- **Docker Compose**: Containerized deployment

## Project Structure

```
agroweather-pipeline/
├── airflow/
│   ├── dags/
│   │   └── etl_ibge.py          # Main ETL DAG
│   ├── logs/                    # Airflow execution logs
│   └── entrypoint.sh           # Container initialization
├── etl/
│   ├── extract/
│   │   └── fake_ibge_data.py    # Data extraction module
│   ├── transform/
│   │   └── clean_ibge_data.py   # Data transformation module
│   └── load/
│       └── load_to_postgres.py  # Data loading module
├── data/
│   ├── raw/                     # Raw extracted data
│   └── processed/               # Cleaned transformed data
├── docker-compose.yml           # Service orchestration
├── requirements.txt             # Python dependencies
└── .env                        # Environment variables
```

## ETL Pipeline

The pipeline consists of three main stages:

1. **Extract**: Generates sample IBGE agricultural data
2. **Transform**: Cleans and standardizes the data format
3. **Load**: Inserts processed data into PostgreSQL

### Data Schema

The `agricultural_production` table contains:
- `year`: Production year
- `municipality`: City/municipality name
- `state`: State abbreviation
- `crop`: Type of agricultural product
- `harvested_area_ha`: Harvested area in hectares
- `production_ton`: Production volume in tons
- `value_thousand_reais`: Economic value in thousands of reais

## Quick Start

### Prerequisites
- Docker and Docker Compose
- Git

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd agroweather-pipeline
```

2. Start the services:
```bash
docker-compose up -d --build
```

3. Access the applications:
   - **Airflow UI**: http://localhost:8080
   - **Metabase**: http://localhost:3000
   - **PostgreSQL**: localhost:5432

### Running the Pipeline

1. Open Airflow UI at http://localhost:8080
2. Enable the `etl_ibge` DAG
3. Trigger a manual run or wait for the daily schedule

## Services

### Airflow
- **Webserver**: Port 8080
- **Scheduler**: Runs ETL jobs daily
- **Executor**: Sequential (suitable for development)

### PostgreSQL
- **Database**: `agroweather`
- **User**: `admin`
- **Password**: `admin`
- **Port**: 5432

### Metabase
- **Port**: 3000
- Connect to PostgreSQL for data visualization

## Development

### Adding New Data Sources
1. Create extraction module in `etl/extract/`
2. Add transformation logic in `etl/transform/`
3. Update loading process in `etl/load/`
4. Modify the DAG in `airflow/dags/`

### Dependencies
- pandas: Data manipulation
- psycopg2-binary: PostgreSQL adapter
- sqlalchemy: Database toolkit

## Monitoring

- Airflow logs: `airflow/logs/`
- Pipeline execution status via Airflow UI
- Data quality checks through Metabase dashboards

## Environment Variables

Configure in `.env`:
- `POSTGRES_USER`: Database username
- `POSTGRES_PASSWORD`: Database password
- `POSTGRES_DB`: Database name
