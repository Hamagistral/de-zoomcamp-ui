import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title(layout="wide")

hide_pages(["Thank you"])

st.markdown("""### ⭐ If you are enjoying your learning experience please leave a Star <iframe src="https://ghbtns.com/github-btn.html?user=hamagistral&repo=de-zoomcamp-ui&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("## 1. Introduction")

st.markdown("### 1.1. Introduction to Batch Processing")

st.video("https://youtu.be/dcHe5Fl3MF8?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("### 1.2. Introduction to Spark")

st.video("https://youtu.be/FhaqbEOuQ8U?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("---")

st.markdown("## 2. Installation")

st.info("""
Follow these intructions to install Spark:

* [Windows](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_5_batch_processing/setup/windows.md)
* [Linux](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_5_batch_processing/setup/linux.md)
* [MacOS](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_5_batch_processing/setup/macos.md)

And follow [this](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_5_batch_processing/setup/pyspark.md) to run PySpark in Jupyter""")

st.markdown("### (Optional) Installing Spark (Linux)")

st.video("https://youtu.be/hqUbB9c8sKg?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("---")

st.markdown("### 3. Spark SQL and DataFrames")

st.markdown("### 3.1. First Look at Spark/PySpark")

st.video("https://youtu.be/r_Sf6fCB40c?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("### 3.2. Spark Dataframes")

st.video("https://youtu.be/ti3aC1m3rE8?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("### 3.3. (Optional) Preparing Yellow and Green Taxi Data")

st.video("https://youtu.be/CI3P4tAtru4?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.info("""Script to prepare the Dataset [download_data.sh](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_5_batch_processing/code/download_data.sh)

**Note**: The other way to infer the schema (apart from pandas) for the csv files, is to set the `inferSchema` option to `true` while reading the files in Spark.""")

st.markdown("### 3.4. SQL with Spark")

st.video("https://www.youtube.com/watch?v=uAlp2VuZZPY&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("---")

st.markdown("### 4. Spark Internals")

st.markdown("### 4.1. Anatomy of a Spark Cluster")

st.video("https://youtu.be/68CipcZt7ZA&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("### 4.2. GroupBy in Spark")

st.video("https://youtu.be/9qrDsY_2COo&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("### 4.3. Joins in Spark")

st.video("https://youtu.be/lu7TrqAWuH4&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("---")

st.markdown("### 5. (Optional) Resilient Distributed Datasets")

st.markdown("### 5.1 Operations on Spark RDDs")

st.video("https://youtu.be/Bdu-xIrF3OM&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("### 5.2. Spark RDD mapPartition")

st.video("https://youtu.be/k3uB2K99roI&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("---")

st.markdown("### 6 Running Spark in the Cloud")

st.markdown("### 6.1 Connecting to Google Cloud Storage")

st.video("https://youtu.be/Yyz293hBVcQ&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("### 6.2. Creating a Local Spark Cluster")

st.video("https://youtu.be/HXBwSlXo5IA&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("### 6.3. Setting up a Dataproc Cluster")

st.video("https://youtu.be/osAiAYahvh8&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("### 6.4. Connecting Spark to Big Query")

st.video("https://youtu.be/HIm2BOj8C0Q&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb")

st.markdown("---")

st.markdown("### 📝 Homework")

st.info("""
[Homework](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2023/week_5_batch_processing/homework.md)
Or go to the [Homework Quizzes](Homework_Quizzes) section to answer directly there and get the solution.""")

st.markdown("---")

st.markdown("""
## Community notes

* [Notes by Alvaro Navas](https://github.com/ziritrion/dataeng-zoomcamp/blob/main/notes/5_batch_processing.md)
* [Sandy's DE Learning Blog](https://learningdataengineering540969211.wordpress.com/2022/02/24/week-5-de-zoomcamp-5-2-1-installing-spark-on-linux/)
* [Notes by Alain Boisvert](https://github.com/boisalai/de-zoomcamp-2023/blob/main/week5.md)
* [Alternative : Using docker-compose to launch spark by rafik](https://gist.github.com/rafik-rahoui/f98df941c4ccced9c46e9ccbdef63a03) 
* [Marcos Torregrosa's blog (spanish)](https://www.n4gash.com/2023/data-engineering-zoomcamp-semana-5-batch-spark)
* [Notes by Victor Padilha](https://github.com/padilha/de-zoomcamp/tree/master/week5)

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