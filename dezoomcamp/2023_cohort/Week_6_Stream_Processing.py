import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title(layout="wide")

hide_pages(["Thank you"])

st.info("""
### Code structure
* [Java examples](java)
* [Python examples](python)
* [KSQLD examples](ksqldb)

### Confluent cloud setup
Confluent cloud provides a free 30 days trial for, you can signup [here](https://www.confluent.io/confluent-cloud/tryfree/)
""")

st.success("- [Slides](https://docs.google.com/presentation/d/1bCtdCba8v1HxJ_uMm9pwjRUC-NAMeB-6nOG2ng3KujA/edit?usp=sharing)")

st.markdown("---")

st.markdown("""### ⭐ If you are enjoying your learning experience please leave a Star <iframe src="https://ghbtns.com/github-btn.html?user=hamagistral&repo=de-zoomcamp-ui&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("## 1. Introduction to Stream Processing")

st.markdown("### 1.1. Introduction")

st.video("https://www.youtube.com/watch?v=hfvju3iOIP0")

st.markdown("### 1.2. What is stream processing")

st.video("https://www.youtube.com/watch?v=WxTxKGcfA-k")

st.markdown("---")

st.markdown("## 2.  Introduction to Kafka")

st.markdown("### 2.1. What is Kafka ?")

st.video("https://www.youtube.com/watch?v=zPLZUDPi4AY")

st.markdown("### 2.2. Confluent Cloud")

st.video("https://www.youtube.com/watch?v=ZnEZFEYKppw")

st.markdown("### 2.3. Kafka Producer Consumer")

st.video("https://www.youtube.com/watch?v=aegTuyxX7Yg")

st.markdown("---")

st.markdown("## 3. Kafka Configuration")

st.video("https://www.youtube.com/watch?v=SXQtWyRpMKs")

st.info("[Kafka Configuration Reference](https://docs.confluent.io/platform/current/installation/configuration/)")

st.markdown("---")

st.markdown("## 4. Kafka Streams")

st.info("""- [Slides](https://docs.google.com/presentation/d/1fVi9sFa7fL2ZW3ynS5MAZm0bRSZ4jO10fymPmrfTUjE/edit?usp=sharing)
- [Streams Concepts](https://docs.confluent.io/platform/current/streams/concepts.html)""")

st.markdown("### 4.1. Kafka Streams Basics")

st.video("https://www.youtube.com/watch?v=dUyA_63eRb0")

st.markdown("### 4.2. Kafka Stream Join")

st.video("https://www.youtube.com/watch?v=NcpKlujh34Y")

st.markdown("### 4.3. Kafka Stream Testing")

st.video("https://www.youtube.com/watch?v=TNx5rmLY8Pk")

st.markdown("### 4.4. Kafka Stream Windowing")

st.video("https://www.youtube.com/watch?v=r1OuLdwxbRc")

st.markdown("### 4.5. Kafka Ksqldb & Connect")

st.video("https://www.youtube.com/watch?v=r1OuLdwxbRc")

st.markdown("### 4.6. Kafka Schema registry")

st.video("https://www.youtube.com/watch?v=tBY_hBuyzwI")

st.markdown("---")

st.markdown("## 5. Faust - Python Stream Processing")

st.info("""
- [Faust Documentation](https://faust.readthedocs.io/en/latest/index.html)
- [Faust vs Kafka Streams](https://faust.readthedocs.io/en/latest/playbooks/vskafka.html)""")

st.markdown("---")

st.markdown("## 6. Pyspark - Structured Streaming")

st.info("Please follow the steps described under [pyspark-streaming](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_6_stream_processing/python/streams-example/pyspark/README.md)")

st.markdown("### 6.1. Kafka Streaming with Python")

st.video("https://www.youtube.com/watch?v=Y76Ez_fIvtk")

st.markdown("### 6.2. Pyspark Structured Streaming")

st.video("https://www.youtube.com/watch?v=5hRJ8-6Fpyk")

st.markdown("---")

st.markdown("## 7. Kafka Streams with JVM library")

st.info("""- [Confluent Kafka Streams](https://kafka.apache.org/documentation/streams/)
- [Scala Example](https://github.com/AnkushKhanna/kafka-helper/tree/master/src/main/scala/kafka/schematest)""")

st.markdown("---")

st.markdown("## 8. KSQL and ksqlDBy")

st.info("""- [Introducing KSQL: Streaming SQL for Apache Kafka](https://www.confluent.io/blog/ksql-streaming-sql-for-apache-kafka/)
- [ksqlDB](https://ksqldb.io/)""")

st.markdown("---")

st.markdown("## 9. Kafka Connect")

st.info("""- [Making Sense of Stream Data](https://medium.com/analytics-vidhya/making-sense-of-stream-data-b74c1252a8f5)""")

st.markdown("---")

st.markdown("""
### Docker

##### Starting cluster

---

### Command line for Kafka

##### Create topic

```
bash
./bin/kafka-topics.sh --create --topic demo_1 --bootstrap-server localhost:9092 --partitions 2
```
""")

st.markdown("---")

st.markdown("### 📝 Homework")

st.info("""
[Homework Form](https://forms.gle/rK7268U92mHJBpmW7)

The homework is mostly theoretical. In the last question you have to provide working code link, please keep in mind that this
question is not scored.

Or go to the [Homework Quizzes](Homework_Quizzes) section to answer directly there and get the solution.

Deadline: 13 March 2023, 22:00 CET""")

st.markdown("---")

st.markdown("""
## Community notes

* [Notes by Alvaro Navas](https://github.com/ziritrion/dataeng-zoomcamp/blob/main/notes/6_streaming.md )
* [Marcos Torregrosa's blog (spanish)](https://www.n4gash.com/2023/data-engineering-zoomcamp-semana-6-stream-processing/)

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