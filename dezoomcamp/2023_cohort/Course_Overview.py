import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title(layout="wide")

hide_pages(["Thank you"])

st.markdown("#")

st.markdown("### 👨‍🔧 Data Engineering Zoomcamp 2023 Cohort")

st.video("https://www.youtube.com/watch?v=-zpVha7bw5A")

st.markdown("---")

st.markdown("""### 📄 Syllabus


#### <a href="Week%201%20Introduction%20&%20Prerequisites" target='_self'>Week 1: Introduction & Prerequisites</a>

* Course overview
* Introduction to GCP
* Docker and docker-compose
* Running Postgres locally with Docker
* Setting up infrastructure on GCP with Terraform
* Preparing the environment for the course


#### <a href="Week%202%20Workflow%20Orchestration" target='_self'>Week 2: Workflow Orchestration</a>

* Data Lake
* Workflow orchestration
* Introduction to Prefect
* ETL with GCP & Prefect
* Parametrizing workflows
* Prefect Cloud and additional resources


#### <a href="Week%203%20Data%20Warehouse" target='_self'>Week 3: Data Warehouse</a>

* Data Warehouse
* BigQuery
* Partitioning and clustering
* BigQuery best practices
* Internals of BigQuery
* Integrating BigQuery with Airflow
* BigQuery Machine Learning


#### <a href="Week%204%20Analytics%20Engineering" target='_self'>Week 4: Analytics Engineering</a>

* Basics of analytics engineering
* dbt (data build tool)
* BigQuery and dbt
* Postgres and dbt
* dbt models
* Testing and documenting
* Deployment to the cloud and locally
* Visualizing the data with google data studio and metabase


#### <a href="Week%205%20Batch%20processing" target='_self'>Week 5: Batch Processing</a>

* Batch processing
* What is Spark
* Spark Dataframes
* Spark SQL
* Internals: GroupBy and joins


#### <a href="Week%206%20Stream%20Processing" target='_self'>Week 6: Streaming Processing</a>

* Introduction to Kafka
* Schemas (avro)
* Kafka Streams
* Kafka Connect and KSQL


#### <a href="Week%207%20Project" target='_self'>Week 7: Project</a>

Putting everything we learned to practice

* Week 7: Working on your project""", unsafe_allow_html=True)

st.markdown("""
---

### 🛠️ Technologies
            
* **Google Cloud Platform (GCP)**: Cloud-based auto-scaling platform by Google
  * **Google Cloud Storage (GCS)**: Data Lake
  * **BigQuery**: Data Warehouse
* **Terraform**: Infrastructure-as-Code (IaC)
* **Docker**: Containerization
* **SQL**: Data Analysis & Exploration
* **Prefect**: Workflow Orchestration
* **dbt**: Data Transformation
* **Spark**: Distributed Processing
* **Kafka**: Streaming

---

### ⚒️ Tools

For this course, you'll need to have the following software installed on your computer:

* Docker and Docker-Compose
* Python 3 (e.g. via [Anaconda](https://www.anaconda.com/products/individual))
* Google Cloud SDK
* Terraform

See <a href="Week_1_Introduction_&_Prerequisites" target='_self'>Week 1</a> for more details about installing these tools""", unsafe_allow_html=True)

st.info("""**Note:** NYC TLC changed the format of the data we use to parquet. But you can still access the csv files [here](https://github.com/DataTalksClub/nyc-tlc-data).""")

st.markdown("---")

st.markdown("""
### 💌 Supporters and partners

Thanks to the course sponsors for making it possible to create this course

<a href="https://www.prefect.io/">
    <img height="100" style="margin-right: 4rem;" src="https://github.com/DataTalksClub/mlops-zoomcamp/raw/main/images/prefect.png">
</a>

<a href="https://www.piperider.io/">
    <img height="130" src="https://github.com/DataTalksClub/data-engineering-zoomcamp/raw/main/images/piperider.png">
</a>

#
Do you want to support our course and our community? Please reach out to [alexey@datatalks.club](alexey@datatalks.club)
            
---
            
### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=hamagistral&repo=de-zoomcamp-ui&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
            
##### 🖼️ Course UI was made by [Hamagistral](https://github.com/Hamagistral)""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
