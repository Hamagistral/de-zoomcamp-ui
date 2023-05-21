import streamlit as st

st.set_page_config(page_title="Course Overview", page_icon='📚')

st.markdown("## 📚 Course Overview")

st.video("https://www.youtube.com/watch?v=-zpVha7bw5A")

st.markdown("---")

st.markdown("""## 📄 Syllabus


#### <a href="Week_1_Introduction_&_Prerequisites" target='_self'>Week 1: Introduction & Prerequisites</a>

* Course overview
* Introduction to GCP
* Docker and docker-compose
* Running Postgres locally with Docker
* Setting up infrastructure on GCP with Terraform
* Preparing the environment for the course


#### <a href="Week_2_Workflow_Orchestration" target='_self'>Week 2: Workflow Orchestration</a>

* Data Lake
* Workflow orchestration
* Introduction to Prefect
* ETL with GCP & Prefect
* Parametrizing workflows
* Prefect Cloud and additional resources


#### <a href="Week_3_Data_Warehouse" target='_self'>Week 3: Data Warehouse</a>

* Data Warehouse
* BigQuery
* Partitioning and clustering
* BigQuery best practices
* Internals of BigQuery
* Integrating BigQuery with Airflow
* BigQuery Machine Learning


#### <a href="Week_4_Analytics_Engineering" target='_self'>Week 4: Analytics Engineering</a>

* Basics of analytics engineering
* dbt (data build tool)
* BigQuery and dbt
* Postgres and dbt
* dbt models
* Testing and documenting
* Deployment to the cloud and locally
* Visualizing the data with google data studio and metabase


#### <a href="Week_5_Batch_processing" target='_self'>Week 5: Batch Processing</a>

* Batch processing
* What is Spark
* Spark Dataframes
* Spark SQL
* Internals: GroupBy and joins


#### <a href="Week_6_Stream_Processing" target='_self'>Week 6: Streaming Processing</a>

* Introduction to Kafka
* Schemas (avro)
* Kafka Streams
* Kafka Connect and KSQL


#### <a href="Week_7_Project" target='_self'>Week 7: Project</a>

Putting everything we learned to practice

* Week 7: Working on your project


---

### 📝 Architecture diagram""", unsafe_allow_html=True)

st.image("https://github.com/DataTalksClub/data-engineering-zoomcamp/raw/main/images/architecture/arch_2.png")

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

st.markdown("##### 🖼️ Course UI was made by [Hamagistral](https://github.com/Hamagistral)")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
