import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title()

hide_pages(["Thank you"])

st.markdown("## Thank you for reaching out! 🙌🏻")

st.markdown("Thank you for taking the time to provide your feedback. Your input is valuable to us.")

st.info("We appreciate your contribution, we will review your ideas or address the reported bugs as soon as possible.")

st.toast('Your message was submitted successfully!', icon='💌')

st.link_button("Get back to **learning** 👨🏻‍🎓", "https://dezoomcamp.streamlit.app/")