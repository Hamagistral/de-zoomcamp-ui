import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title(layout="wide")

hide_pages(["Thank you"])

st.markdown("### 🧙‍♂️ Data Engineering Zoomcamp 2024 Cohort")

st.video("https://www.youtube.com/watch?v=AtRhA-NfS24")

st.markdown("""
* [Pre-launch Q&A stream](https://www.youtube.com/watch?v=91b8u9GmqB4)
* Launch stream with course overview (TODO)
* [Deadline calendar](https://docs.google.com/spreadsheets/d/e/2PACX-1vQACMLuutV5rvXg5qICuJGL-yZqIV0FBD84CxPdC5eZHf8TfzB-CJT_3Mo7U7oGVTXmSihPgQxuuoku/pubhtml)
* [Course Google calendar](https://calendar.google.com/calendar/?cid=ZXIxcjA1M3ZlYjJpcXU0dTFmaG02MzVxMG9AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ)
* [FAQ](https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit?usp=sharing)            

---
            
### 🏅 Course Leaderboard """)
            
st.info("You can find the course leaderboard [here](https://courses.datatalks.club/de-zoomcamp-2024/leaderboard)!")
            
st.markdown("""
---
               
### 📄 Syllabus


#### <a href="Module%201%20Introduction%20&%20Prerequisites" target='_self'>Module 1: Containerization and Infrastructure as Code</a>

* Course overview
* Introduction to GCP
* Docker and docker-compose
* Running Postgres locally with Docker
* Setting up infrastructure on GCP with Terraform
* Preparing the environment for the course
* Homework


#### <a href="Module%202%20Workflow%20Orchestration" target='_self'>Module 2: Workflow Orchestration</a>

* Data Lake
* Workflow orchestration
* Workflow orchestration
* Workflow orchestration with Mage
* Homework

#### <a href="Workshop%201%20Data%20Ingestion" target='_self'>Workshop 1: Data Ingestion</a>
            
#### <a href="Module%203%20Data%20Warehouse" target='_self'>Module 3: Data Warehouse</a>

* Data Warehouse
* BigQuery
* Partitioning and clustering
* BigQuery best practices
* Internals of BigQuery
* BigQuery Machine Learning

#### <a href="Module%204%20Analytics%20Engineering" target='_self'>Module 4: Analytics engineering</a>

* Basics of analytics engineering
* dbt (data build tool)
* BigQuery and dbt
* Postgres and dbt
* dbt models
* Testing and documenting
* Deployment to the cloud and locally
* Visualizing the data with google data studio and metabase

#### <a href="#" target='_self'>Module 5: Batch processing</a>

* Batch processing
* What is Spark
* Spark Dataframes
* Spark SQL
* Internals: GroupBy and joins

#### <a href="#" target='_self'>Module 6: Streaming</a>

* Introduction to Kafka
* Schemas (avro)
* Kafka Streams
* Kafka Connect and KSQL


#### <a href="#" target='_self'>Workshop 2: Stream Processing with SQL</a>
            
#### <a href="#" target='_self'>Project</a>

Putting everything we learned to practice

* Week 1 and 2: working on your project
* Week 3: reviewing your peers

---

### 📝 Architecture diagram""", unsafe_allow_html=True)

st.image("https://raw.githubusercontent.com/DataTalksClub/data-engineering-zoomcamp/main/images/architecture/photo1700757552.jpeg")

st.markdown("""
---

### 🛠️ Technologies
* **Google Cloud Platform (GCP)**: Cloud-based auto-scaling platform by Google
  * **Google Cloud Storage (GCS)**: Data Lake
  * **BigQuery**: Data Warehouse
* **Terraform**: Infrastructure-as-Code (IaC)
* **Docker**: Containerization
* **SQL**: Data Analysis & Exploration
* **Mage**: Workflow Orchestration     
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

Thanks to the course sponsors for making it possible to run this course

<p align="center">
  <a href="https://mage.ai/">
    <img height="120" src="https://raw.githubusercontent.com/DataTalksClub/data-engineering-zoomcamp/main/images/mage.svg">
  </a>
</p>


<p align="center">
  <a href="https://dlthub.com/">
    <img height="90" src="https://raw.githubusercontent.com/DataTalksClub/data-engineering-zoomcamp/main/images/dlthub.png">
  </a>
</p>

<p align="center">
  <a href="https://risingwave.com/">
    <img height="90" src="https://raw.githubusercontent.com/DataTalksClub/data-engineering-zoomcamp/main/images/rising-wave.png">
  </a>
</p>

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
