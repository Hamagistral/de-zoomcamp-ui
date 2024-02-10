import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title()

hide_pages(["Thank you"])

st.markdown("""### ⭐ If you are enjoying your learning experience please leave a Star <iframe src="https://ghbtns.com/github-btn.html?user=hamagistral&repo=de-zoomcamp-ui&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
## ❔ Asking questions

If you have any questions, ask them 
in the [`#course-data-engineering`](https://app.slack.com/client/T01ATQK62F8/C01FABYF2RG) channel in [DataTalks.Club](https://datatalks.club) slack.

To keep our discussion in Slack more organized, we ask you to follow these suggestions:

* Before asking a question, check [FAQ](https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit).
* Use threads. When you have a problem, first describe the problem shortly
  and then put the actual error in the thread - so it doesn't take the entire screen.
* Instead of screenshots, it's better to copy-paste the error you're getting in text.
  Use ` ``` ` for formatting your code.
  It's very difficult to read text from screenshots.
* Please don't take pictures of your code with a phone. It's even harder to read. Follow the previous suggestion,
  and in rare cases when you need to show what happens on your screen, take a screenshot.
* You don't need to tag the instructors when you have a problem. We will see it eventually.
* If somebody helped you with your problem and it's not in [FAQ](https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit), please add it there.
  It'll help other students.
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
 