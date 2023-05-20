import streamlit as st

st.set_page_config(page_title="Dataset", page_icon='💾')

st.markdown("""

# NYC TLC Data 

Backup for NYC TLC data for the [DE Zoomcamp course](https://github.com/DataTalksClub/data-engineering-zoomcamp/)

CSV data:

* Yellow taxi data: https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/yellow
* Green taxi data: https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/green
* For-hire vehicles (FHV): https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/fhv
* For-hire vehicles high volume (FHVHV): https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/fhvhv
* Misc (zone lookup file): https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/misc

The data was copied from the [NYC TLC website](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
""")

st.markdown("---")

st.markdown("##### 🖼️ Course UI was made by [Hamagistral](https://github.com/Hamagistral)")