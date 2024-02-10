import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title()

hide_pages(["Thank you"])

st.markdown("This streamlit app is a user-friendly interface designed by [Hamagistral](https://github.com/Hamagistral) to enhance your learning experience for the **DE Zoomcamp** course offered by [DataTalksClub.](https://datatalks.club/)")

st.image("https://i.ytimg.com/vi/bkJZDmreIpA/maxresdefault.jpg")

st.markdown("""
### 📚 Course Description
       
DE Zoomcamp is a comprehensive data engineering course that covers various aspects of building scalable and efficient data pipelines. The course provides a hands-on approach to learning key concepts, tools, and technologies used in the field of data engineering.

### 🛠️ Features

- **Easy navigation**: The DE Zoomcamp UI simplifies access to course materials, including READMEs, YouTube videos, and homework assignments, making it convenient for you to follow along and complete the course at your own pace.
- **Streamlined interface**: The UI draws inspiration from the well-known CS50 course UI, providing a clean and intuitive design that enhances your learning experience.
- **Interactive capabilities**: Streamlit's interactive elements enable you to interact with the course materials, explore code examples, and experiment with the concepts learned during the course.

### 👨‍💻 Usage

To get started, simply navigate through the different sections of the UI using the sidebar menu. You can access the course materials, watch the instructional videos, complete the homework assignments, and delve deeper into the world of data engineering.

### ⭕ Disclaimer

This UI is created by a student as a personal project to facilitate personal learning and is not officially affiliated with DataTalksClub or the DE Zoomcamp course. All course materials and resources belong to their respective owners.

### 📨 Feedback

Your feedback is valuable! If you encounter any issues, have suggestions for improvements, or would like to contribute to this project, please post an issue in the [project repository](https://github.com/Hamagistral/de-zoomcamp-ui/issues).

### 👨‍🏫 Acknowledgements

Special thanks to DataTalksClub for providing the DE Zoomcamp course and inspiring this UI project.

### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=hamagistral&repo=de-zoomcamp-ui&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>

If you liked the project please leave a star. """, unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 