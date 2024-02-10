import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title(layout="wide")

hide_pages(["Thank you"])

st.info("""
The goal of this project is to apply everything we learned
in this course and build an end-to-end data pipeline.

Remember that to pass the project, you must evaluate 3 peers. If you don't do that, your project can't be considered compelete.

* [2023 Projects](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2023/project.md)
* [2022 Projects](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2022/project.md)""")

st.markdown("---")

st.markdown("""### ⭐ If you are enjoying your learning experience please leave a Star <iframe src="https://ghbtns.com/github-btn.html?user=hamagistral&repo=de-zoomcamp-ui&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>
""", unsafe_allow_html=True)

st.markdown("""
---

## 📋 Problem statement

For the project, we will ask you to build a dashboard with two tiles. 

For that, you will need:

* Select a dataset that you're interested in (see [datasets](#datasets) below.)
* Create a pipeline for processing this dataset and putting it to a datalake
* Create a pipeline for moving the data from the lake to a data warehouse
* Transform the data in the data warehouse: prepare it for the dashboard
* Create a dashboard

---

## ⚙️ Data Pipeline 

The pipeline could be stream or batch: this is the first thing you'll need to decide 

* If you want to consume data in real-time and put them to data lake - go with stream.
* If you want to run things periodically (e.g. hourly/daily), go with batch

---

## 🛠️ Technologies 

You don't have to limit yourself to technologies covered in the course. You can use alternatives as well:

* Cloud: AWS, GCP, Azure or others
* Infrastructure as code (IaC): Terraform, Pulumi, Cloud Formation, ...
* Workflow orchestration: Airflow, Prefect, Luigi, ...
* Data Wareshouse: BigQuery, Snowflake, Redshift, ...
* Batch processing: Spark, Flink, AWS Batch, ...
* Stream processing: Kafka, Pulsar, Kinesis, ...

If you use something that wasn't covered in the course, 
be sure to explain what the tool does.

If you're not certain about some tools, ask in Slack.

---

## 📊 Dashboard

You can build a dashboard with any of the tools shown in the course (Data Studio or Metabase) or any other BI tool of your choice. If you do use another tool, please specify and make sure that the dashboard is somehow accessible to your peers. 

Your dashboard should contain at least two tiles, we suggest you include:

- 1 graph that shows the distribution of some categorical data 
- 1 graph that shows the distribution of the data across a temporal line

Make sure that your graph is clear to understand by adding references and titles. 

Example of a dashboard:""")

st.image("https://user-images.githubusercontent.com/4315804/159771458-b924d0c1-91d5-4a8a-8c34-f36c25c31a3c.png")

st.markdown("""---

## 🧑‍💻 Peer review criteria

* **Problem description**
    * 0 points: Problem is not described
    * 1 point: Problem is described but shortly or not clearly 
    * 2 points: Problem is well described and it's clear what the problem the project solves
* **Cloud**
    * 0 points: Cloud is not used, things run only locally
    * 2 points: The project is developed in the cloud
    * 4 points: The project is developed in the cloud and IaC tools are used
* **Data ingestion (choose either batch or stream)**
    * Batch / Workflow orchestration
        * 0 points: No workflow orchestration
        * 2 points: Partial workflow orchestration: some steps are orchestrated, some run manually
        * 4 points: End-to-end pipeline: multiple steps in the DAG, uploading data to data lake
    * Stream
        * 0 points: No streaming system (like Kafka, Pulsar, etc)
        * 2 points: A simple pipeline with one consumer and one producer
        * 4 points: Using consumer/producers and streaming technologies (like Kafka streaming, Spark streaming, Flink, etc)
* **Data warehouse**
    * 0 points: No DWH is used
    * 2 points: Tables are created in DWH, but not optimized
    * 4 points: Tables are partitioned and clustered in a way that makes sense for the upstream queries (with explanation)
* **Transformations (dbt, spark, etc)**
    * 0 points: No tranformations
    * 2 points: Simple SQL transformation (no dbt or similar tools)
    * 4 points: Tranformations are defined with dbt, Spark or similar technologies
* **Dashboard**
    * 0 points: No dashboard
    * 2 points: A dashboard with 1 tile
    * 4 points: A dashboard with 2 tiles
* **Reproducibility**
    * 0 points: No instructions how to run code at all
    * 2 points: Some instructions are there, but they are not complete
    * 4 points: Instructions are clear, it's easy to run the code, and the code works

---

<a name="datasets"></a>
## 💾 Datasets

Here are some datasets that you could use for the project:


* [Kaggle](https://www.kaggle.com/datasets)
* [AWS datasets](https://registry.opendata.aws/)
* [UK government open data](https://data.gov.uk/)
* [Github archive](https://www.gharchive.org)
* [Awesome public datasets](https://github.com/awesomedata/awesome-public-datasets)
* [Million songs dataset](http://millionsongdataset.com)
* [Some random datasets](https://components.one/datasets/)
* [COVID Datasets](https://www.reddit.com/r/datasets/comments/n3ph2d/coronavirus_datsets/)
* [Datasets from Azure](https://docs.microsoft.com/en-us/azure/azure-sql/public-data-sets)
* [Datasets from BigQuery](https://cloud.google.com/bigquery/public-data/)
* [Dataset search engine from Google](https://datasetsearch.research.google.com/)
* [Public datasets offered by different GCP services](https://cloud.google.com/solutions/datasets)
* [European statistics datasets](https://webgate.acceptance.ec.europa.eu/eurostat/data/database)
* [Datasets for streaming](https://github.com/ColinEberhardt/awesome-public-streaming-datasets)
* [Dataset for Santander bicycle rentals in London](https://cycling.data.tfl.gov.uk/)
* [Common crawl data](https://commoncrawl.org/) (copy of the internet)
* [NASA's EarthData](https://search.earthdata.nasa.gov/search) (May require introductory geospatial analysis)
* Collection Of Data Repositories
  * [Part 1](https://www.kdnuggets.com/2022/04/complete-collection-data-repositories-part-1.html) (from agriculture and finance to government)
  * [Part 2](https://www.kdnuggets.com/2022/04/complete-collection-data-repositories-part-2.html) (from healthcare to transportation)

It's not mandatory that you use a dataset from this list. You can use any dataset you want.

---

## 🚀 Going the extra mile 

If you finish the project and you want to improve it, here are a few things you can do:

* Add tests
* Use make
* Add CI/CD pipeline 

This is not covered in the course and this is entirely optional.

If you plan to use this project as your portfolio project, it'll 
definitely help you to stand out from others.

> **Note**: this part will not be graded. 

#### 🔗 Some links to refer to:

* [Unit Tests + CI for Airflow](https://www.astronomer.io/events/recaps/testing-airflow-to-bulletproof-your-code/)
* [CI/CD for Airflow (with Gitlab & GCP state file)](https://engineering.ripple.com/building-ci-cd-with-airflow-gitlab-and-terraform-in-gcp)
* [CI/CD for Airflow (with GitHub and S3 state file)](https://programmaticponderings.com/2021/12/14/devops-for-dataops-building-a-ci-cd-pipeline-for-apache-airflow-dags/)
* [CD for Terraform](https://towardsdatascience.com/git-actions-terraform-for-data-engineers-scientists-gcp-aws-azure-448dc7c60fcc)
* [Spark + Airflow](https://medium.com/doubtnut/github-actions-airflow-for-automating-your-spark-pipeline-c9dff32686b)

---

##### 🖼️ Course UI was made by [Hamagistral](https://github.com/Hamagistral)
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 