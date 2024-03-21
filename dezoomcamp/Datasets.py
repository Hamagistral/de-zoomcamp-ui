import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title()

hide_pages(["Thank you"])

st.markdown("""### ⭐ If you are enjoying your learning experience please leave a Star <iframe src="https://ghbtns.com/github-btn.html?user=hamagistral&repo=de-zoomcamp-ui&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""

## 💾 NYC TLC Data 

Backup for NYC TLC data for the [DE Zoomcamp course](https://github.com/DataTalksClub/data-engineering-zoomcamp/)

CSV data:

* Yellow taxi data: https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/yellow
* Green taxi data: https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/green
* For-hire vehicles (FHV): https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/fhv
* For-hire vehicles high volume (FHVHV): https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/fhvhv
* Misc (zone lookup file): https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/misc

The data was copied from the [NYC TLC website](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
            
---

## 💾 Capstone Project Datasets
            
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
  * [part 1](https://www.kdnuggets.com/2022/04/complete-collection-data-repositories-part-1.html) (from agriculture and finance to government)
  * [part 2](https://www.kdnuggets.com/2022/04/complete-collection-data-repositories-part-2.html) (from healthcare to transportation)

It's not mandatory that you use a dataset from this list. You can use any dataset you want.
""")

st.markdown("---")

st.markdown("##### 🖼️ Course UI was made by [Hamagistral](https://github.com/Hamagistral)")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 