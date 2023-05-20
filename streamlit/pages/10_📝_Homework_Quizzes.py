import streamlit as st

from homework_quizzes import show_week1_a_quizz, show_week1_b_quizz, show_week2_quizz, show_week3_quizz, show_week4_quizz, show_workshop, show_week5_quizz, show_week6_quizz

st.set_page_config(page_title="Homework Quizzes", page_icon='📝')

choice = st.selectbox("Choose Homework Week", ('Week 1 (A)', 'Week 1 (B)', 'Week 2', 'Week 3', 'Week 4',  'Week 4 Workshop', 'Week 5', 'Week 6'))

if choice == 'Week 1 (A)':
    show_week1_a_quizz()
elif choice == 'Week 1 (B)':
    show_week1_b_quizz()
elif choice == 'Week 2':
    show_week2_quizz()
elif choice == 'Week 3':
    show_week3_quizz()
elif choice == 'Week 4':
    show_week4_quizz()
elif choice == 'Week 4 Workshop':
    show_workshop()
elif choice == 'Week 5':
    show_week5_quizz()
elif choice == 'Week 6':
    show_week6_quizz()

st.markdown("---")

st.markdown("##### 🖼️ Course UI was made by [Hamagistral](https://github.com/Hamagistral)")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 