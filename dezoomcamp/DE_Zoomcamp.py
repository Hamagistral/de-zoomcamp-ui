import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()

show_pages(
    [   
        Page("dezoomcamp/DE_Zoomcamp.py", "DE Zoomcamp", "💻"),

        # # 2024 Content
        Section("DE Zoomcamp 2024", "🧙‍♂️"),
        Page("dezoomcamp/2024_cohort/Course_Overview.py", "Course Overview", "📚", in_section=True),
        Page("dezoomcamp/2024_cohort/Module_1_Introduction_&_Prerequisites.py", "Module 1 Introduction & Prerequisites", "1️⃣", in_section=True),
        Page("dezoomcamp/2024_cohort/Module_2_Workflow_Orchestration.py", "Module 2 Workflow Orchestration", "2️⃣", in_section=True),
        Page("dezoomcamp/2024_cohort/Workshop_1_Data_Ingestion.py", "Workshop 1 Data Ingestion", "🛠️", in_section=True),
        Page("dezoomcamp/2024_cohort/Module_3_Data_Warehouse.py", "Module 3 Data Warehouse and BigQuery", "3️⃣", in_section=True),
        Page("dezoomcamp/2024_cohort/Module_4_Analytics_Engineering.py", "Module 4 Analytics Engineering", "4️⃣", in_section=True,),

        # 2023 Content
        Section("DE Zoomcamp 2023", "👨‍🔧"),
        Page("dezoomcamp/2023_cohort/Course_Overview.py", "Course Overview", "📚", in_section=True),
        Page("dezoomcamp/2023_cohort/Week_1_Introduction_&_Prerequisites.py", "Week 1 Introduction & Prerequisites", "1️⃣", in_section=True),
        Page("dezoomcamp/2023_cohort/Week_2_Workflow_Orchestration.py", "Week 2 Workflow Orchestration", "2️⃣", in_section=True),
        Page("dezoomcamp/2023_cohort/Week_3_Data_Warehouse.py", "Week 3 Data Warehouse", "3️⃣", in_section=True),
        Page("dezoomcamp/2023_cohort/Week_4_Analytics_Engineering.py", "Week 4 Analytics Engineering", "4️⃣", in_section=True),
        Page("dezoomcamp/2023_cohort/Week_5_Batch _processing.py", "Week 5 Batch processing", "5️⃣", in_section=True),
        Page("dezoomcamp/2023_cohort/Week_6_Stream_Processing.py", "Week 6 Stream Processing", "6️⃣", in_section=True),
        Page("dezoomcamp/2023_cohort/Week_7_Project.py", "Week 7 Project", "7️⃣", in_section=True),
        Page("dezoomcamp/2023_cohort/Homework_Quizzes.py", "Homework Quizzes", "📝", in_section=True),
        
        Page("dezoomcamp/Dataset.py", "Dataset", icon="💾", in_section=False),
        Page("dezoomcamp/Certificate.py", "Certificate", "📜", in_section=False),
        Page("dezoomcamp/FAQ.py", "FAQ", "❔", in_section=False),
        Page("dezoomcamp/Contact.py", "Contact", icon="📩", in_section=False),   
        Page("dezoomcamp/Contact_thanks.py", "Thank you", icon="💌"),   
        Page("dezoomcamp/About.py", "About", icon="🖼️", in_section=False) 
    ]
)

hide_pages(["Thank you"])

st.markdown("### 👨‍🔧 Data Engineering Zoomcamp by [DataTalksClub](https://datatalks.club/)")

st.image("https://pbs.twimg.com/media/FmmYA2YWYAApPRB.png")

st.info("Original Course Repository on [Github](https://github.com/DataTalksClub/data-engineering-zoomcamp)")

st.markdown("---")

with st.expander("Sign up here for 2024 Cohort"):
    st.markdown("""
    
    <a href="https://airtable.com/appzbS8Pkg9PL254a/shr6oVXeQvSI5HuWD"><img src="https://user-images.githubusercontent.com/875246/185755203-17945fd1-6b64-46f2-8377-1011dcb1a444.png" height="50" /></a>

    #

    - Register in [DataTalks.Club's Slack](https://datatalks.club/slack.html)
    - Join the [`#course-data-engineering`](https://app.slack.com/client/T01ATQK62F8/C01FABYF2RG) channel
    - Join the [course Telegram channel with announcements](https://t.me/dezoomcamp)
    - The videos are published on [DataTalks.Club's YouTube channel](https://www.youtube.com/c/DataTalksClub) in [the course playlist](https://www.youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
    - [Frequently asked technical questions](https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit?usp=sharing)
        
    #""", unsafe_allow_html=True)

st.markdown("""
### 👨‍🎓 Taking the course

##### 👨‍👦‍👦 2024 Cohort

* **Start**: 15 January 2024 (Monday) at 17:00 CET
* **Registration link**: https://airtable.com/shr6oVXeQvSI5HuWD
* [Cohort folder](cohorts/2024/) with homeworks and deadlines 


##### 👨‍🔧 Self-paced mode

All the materials of the course are freely available, so that you
can take the course at your own pace

* Follow the suggested syllabus (see below) week by week
* You don't need to fill in the registration form. Just start watching the videos and join Slack
* Check [FAQ](https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit?usp=sharing) if you have problems
* If you can't find a solution to your problem in FAQ, ask for help in Slack

### 🔎 Overview""", unsafe_allow_html=True)


st.image("https://raw.githubusercontent.com/DataTalksClub/data-engineering-zoomcamp/main/images/architecture/photo1700757552.jpeg")


st.markdown("""
### 📓 Prerequisites

To get the most out of this course, you should feel comfortable with coding and command line
and know the basics of SQL. Prior experience with Python will be helpful, but you can pick
Python relatively fast if you have experience with other programming languages.

Prior experience with data engineering is not required.

### 👨‍🏫 Instructors

- [Ankush Khanna](https://linkedin.com/in/ankushkhanna2)
- [Victoria Perez Mola](https://www.linkedin.com/in/victoriaperezmola/)
- [Alexey Grigorev](https://linkedin.com/in/agrigorev)
- [Matt Palmer](https://www.linkedin.com/in/matt-palmer/)
- [Luis Oliveira](https://www.linkedin.com/in/lgsoliveira/)
- [Michael Shoemaker](https://www.linkedin.com/in/michaelshoemaker1/)

Past instructors:

- [Sejal Vaidya](https://www.linkedin.com/in/vaidyasejal/)
- [Irem Erturk](https://www.linkedin.com/in/iremerturk/)

### ❔ Asking for help in Slack

The best way to get support is to use [DataTalks.Club's Slack](https://datatalks.club/slack.html). Join the [`#course-data-engineering`](https://app.slack.com/client/T01ATQK62F8/C01FABYF2RG) channel.

To make discussions in Slack more organized:

* Follow [these recommendations](asking-questions.md) when asking for help
* Read the [DataTalks.Club community guidelines](https://datatalks.club/slack/guidelines.html)

---
            
### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=hamagistral&repo=de-zoomcamp-ui&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
            
##### 🖼️ Course UI was made by [Hamagistral](https://github.com/Hamagistral) 
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 