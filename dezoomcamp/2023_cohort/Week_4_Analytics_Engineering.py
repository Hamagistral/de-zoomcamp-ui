import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title(layout="wide")

hide_pages(["Thank you"])

st.markdown("""### ⭐ If you are enjoying your learning experience please leave a Star <iframe src="https://ghbtns.com/github-btn.html?user=hamagistral&repo=de-zoomcamp-ui&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>
""", unsafe_allow_html=True)

st.markdown("---")

st.success("""
- Goal: Transforming the data loaded in DWH to Analytical Views developing a [dbt project](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_4_analytics_engineering/taxi_rides_ny/README.md).
- [Slides](https://docs.google.com/presentation/d/1xSll_jv0T8JF4rYZvLHfkJXYqUjPtThA/edit?usp=sharing&ouid=114544032874539580154&rtpof=true&sd=true)
""")

st.warning("""
#### Prerequisites
We will build a project using dbt and a running data warehouse. 
By this stage of the course you should have already: 
- A running warehouse (BigQuery or postgres) 
- A set of running pipelines ingesting the project dataset (week 3 completed): [Datasets list](https://github.com/DataTalksClub/nyc-tlc-data/)
    * Yellow taxi data - Years 2019 and 2020
    * Green taxi data - Years 2019 and 2020 
    * fhv data - Year 2019. """)

st.info("""_Note:_
  *  _A quick hack has been shared to load that data quicker, check instructions in [week3/extras](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_3_data_warehouse/extras)_
  * _If you recieve an error stating "Permission denied while globbing file pattern." when attemting to run fact_trips.sql this video may be helpful in resolving the issue_ 
""")


st.video("https://www.youtube.com/watch?v=kL3ZVNL9Y4A")

st.markdown("---")

st.info("""
#### Setting up dbt for using BigQuery (Alternative A - preferred)
You will need to create a dbt cloud account using [this link](https://www.getdbt.com/signup/) and connect to your warehouse [following these instructions](https://docs.getdbt.com/docs/dbt-cloud/cloud-configuring-dbt-cloud/cloud-setting-up-bigquery-oauth). More detailed instructions in [dbt_cloud_setup.md](dbt_cloud_setup.md)

_Optional_: If you feel more comfortable developing locally you could use a local installation of dbt as well. You can follow the [official dbt documentation](https://docs.getdbt.com/dbt-cli/installation) or follow the [dbt with BigQuery on Docker](docker_setup/README.md) guide to setup dbt locally on docker. You will need to install the latest version (1.0) with the BigQuery adapter (dbt-bigquery). 

#### Setting up dbt for using Postgres locally (Alternative B)
As an alternative to the cloud, that require to have a cloud database, you will be able to run the project installing dbt locally.
You can follow the [official dbt documentation](https://docs.getdbt.com/dbt-cli/installation) or use a docker image from oficial [dbt repo](https://github.com/dbt-labs/dbt/). You will need to install the latest version (1.0) with the postgres adapter (dbt-postgres).
After local installation you will have to set up the connection to PG in the `profiles.yml`, you can find the templates [here](https://docs.getdbt.com/reference/warehouse-profiles/postgres-profile)
""")


st.markdown("### 1. Introduction to analytics engineering")

st.video("https://www.youtube.com/watch?v=uF76d5EmdtU&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=32")
 
st.markdown("""* What is analytics engineering?
 * ETL vs ELT 
 * Data modeling concepts (fact and dim tables)""")

st.markdown("---")

st.markdown("### 2. Intro to dbt ")

st.video("https://www.youtube.com/watch?v=4eCouvVOJUw&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=33")

st.markdown("---")

st.info("#### Starting a dbt project")

st.markdown("### 3.1. Alternative a: Using BigQuery + dbt cloud")

st.video("https://www.youtube.com/watch?v=iMxh6s_wL4Q&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=35")

st.markdown("""* Starting a new project with dbt init (dbt cloud and core)
 * dbt cloud setup
 * project.yml""")

st.markdown("### 3.2. Alternative b: Using Postgres + dbt core (locally)")

st.video("https://youtube.com/watch?v=1HmL63e-vRs&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=36")

st.markdown("""* Starting a new project with dbt init (dbt cloud and core)
 * dbt core local setup
 * profiles.yml
 * project.yml""")

st.markdown("---")

st.markdown("### 4. Development of dbt models")

st.video("https://www.youtube.com/watch?v=UVI30Vxzd6c&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=36")

st.markdown("""* Anatomy of a dbt model: written code vs compiled Sources
 * Materialisations: table, view, incremental, ephemeral  
 * Seeds, sources and ref  
 * Jinja and Macros 
 * Packages 
 * Variables""")

st.info("_Note: This video is shown entirely on dbt cloud IDE but the same steps can be followed locally on the IDE of your choice_")

st.markdown("---")

st.markdown("### 5. Testing and documenting dbt models")

st.video("https://www.youtube.com/watch?v=UishFmq1hLM&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=37")

st.markdown("""* Tests  
 * Documentation """)

st.info("_Note: This video is shown entirely on dbt cloud IDE but the same steps can be followed locally on the IDE of your choice_")

st.markdown("---")

st.info("#### Deploying a dbt project")

st.markdown("### 6.1. Alternative a: Using BigQuery + dbt cloud")

st.video("https://www.youtube.com/watch?v=rjf6yZNGX8I&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=38")

st.markdown("""* Deployment: development environment vs production 
 * dbt cloud: scheduler, sources and hosted documentation""")

st.markdown("### 6.2. Alternative b: Using Postgres + dbt core (locally)")

st.video("https://www.youtube.com/watch?v=Cs9Od1pcrzM&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=39")

st.markdown("""* Deployment: development environment vs production 
 * dbt cloud: scheduler, sources and hosted documentation""")

st.markdown("---")

st.info("#### Visualising the transformed data")

st.markdown("### 7.1. Google data studio Video")
st.video("https://www.youtube.com/watch?v=39nLTs74A3E&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=42")

st.markdown("### 7.2. Metabase Video")
st.video("https://www.youtube.com/watch?v=BnLkrA7a6gM&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=43")

st.markdown("""* Google data studio 
 * [Metabase (local installation)](https://www.metabase.com/)""")

st.info("""
### Advanced knowledge:
 * [Make a model Incremental](https://docs.getdbt.com/docs/building-a-dbt-project/building-models/configuring-incremental-models)
 * [Use of tags](https://docs.getdbt.com/reference/resource-configs/tags)
 * [Hooks](https://docs.getdbt.com/docs/building-a-dbt-project/hooks-operations)
 * [Analysis](https://docs.getdbt.com/docs/building-a-dbt-project/analyses)
 * [Snapshots](https://docs.getdbt.com/docs/building-a-dbt-project/snapshots)
 * [Exposure](https://docs.getdbt.com/docs/building-a-dbt-project/exposures)
 * [Metrics](https://docs.getdbt.com/docs/building-a-dbt-project/metrics)""")


st.markdown("---")

st.markdown("### 📝 Homework")

st.info("""
[Homework](Homework_Quizzes)

Or go to the [Homework Quizzes](Homework_Quizzes) section to answer directly there and get the solution.""")

st.markdown("---")

st.markdown("#### 🔧 Workshop: Maximizing Confidence in Your Data Model Changes with dbt and PipeRider")

st.info("""To learn how to use PipeRider together with dbt for detecting changes in model and data, sign up for a workshop [here](https://www.eventbrite.com/e/maximizing-confidence-in-your-data-model-changes-with-dbt-and-piperider-tickets-535584366257)

[More details](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2023/workshops/piperider.md)
""")

st.markdown("---")

st.markdown("""
## Community notes

* [Notes by Alvaro Navas](https://github.com/ziritrion/dataeng-zoomcamp/blob/main/notes/4_analytics.md)
* [Sandy's DE learning blog](https://learningdataengineering540969211.wordpress.com/2022/02/17/week-4-setting-up-dbt-cloud-with-bigquery/)
* [Notes by Victor Padilha](https://github.com/padilha/de-zoomcamp/tree/master/week4)
* [Marcos Torregrosa's blog (spanish)](https://www.n4gash.com/2023/data-engineering-zoomcamp-semana-4/)
* [Notes by froukje](https://github.com/froukje/de-zoomcamp/blob/main/week_4_analytics_engineering/notes/notes_week_04.md)
* [Notes by Alain Boisvert](https://github.com/boisalai/de-zoomcamp-2023/blob/main/week4.md)
* [Setting up Prefect with dbt by Vera](https://medium.com/@verazabeida/zoomcamp-week-5-5b6a9d53a3a0)
* [Blog by Xia He-Bleinagel](https://xiahe-bleinagel.com/2023/02/week-4-data-engineering-zoomcamp-notes-analytics-engineering-and-dbt/)
* [Setting up DBT with BigQuery by Tofag](https://medium.com/@fagbuyit/setting-up-your-dbt-cloud-dej-9-d18e5b7c96ba)
* [Blog post by Dewi Oktaviani](https://medium.com/@oktavianidewi/de-zoomcamp-2023-learning-week-4-analytics-engineering-with-dbt-53f781803d3e)
* [Notes from Vincenzo Galante](https://binchentso.notion.site/Data-Talks-Club-Data-Engineering-Zoomcamp-8699af8e7ff94ec49e6f9bdec8eb69fd)
* [Notes from Balaji](https://github.com/Balajirvp/DE-Zoomcamp/blob/main/Week%204/Data%20Engineering%20Zoomcamp%20Week%204.ipynb)

## Useful links

- [Visualizing data with Metabase course](https://www.metabase.com/learn/visualization/)

---

##### 🖼️ Course UI was made by [Hamagistral](https://github.com/Hamagistral)
""")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 