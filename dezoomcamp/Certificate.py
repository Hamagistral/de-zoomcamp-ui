import streamlit as st
from hashlib import sha1
from st_pages import add_page_title, hide_pages

add_page_title()

hide_pages(["Thank you"])

def compute_hash(email):
    return sha1(email.encode('utf-8')).hexdigest()

def compute_certificate_id(email):
    email_clean = email.lower().strip()
    return compute_hash(email_clean + '_')

st.balloons()

st.markdown("""
### 🎉 Congratulations on finishing the course! 🎈

Here's a certificate example :""")

st.image("https://i.postimg.cc/Y0sSShYg/certificate-dezoomcamp.png")

st.markdown("#### Here's how you can get your certificate.")

st.info("You're only able to claim your certificate if you have completed the course with the 2023 cohort.")

email_adress = st.text_input('First, enter your email adress :', placeholder="never.give.up@gmail.com")

if st.button('Generate Certificate'):
    cohort = 2023
    course = 'dezoomcamp'
    id = compute_certificate_id(email_adress)
    url = f"https://certificate.datatalks.club/{course}/{cohort}/{id}.pdf"

    st.success(f"✨ Certificate url : {url}")

st.markdown("---")

st.error("Unfortunatly only students who took the course with the cohort are able to claim a certificate.")

st.info("""    
As mentionned in the FAQ :  

**Can I follow the course in a self-paced mode and get a certificate?**
               
No, you can only get a certificate if you finish the course with the cohort. We don't award certificates for the self-paced mode.""")

st.markdown("""## Adding to LinkedIn

You can add your certificate to LinkedIn:

* Log in to your LinkedIn account, then go to your profile.
* On the right, in the "Add profile" section dropdown, choose "Background" and then select the drop-down triangle next to "Licenses & Certifications".
* In "Name", enter "Data Engineering Zoomcamp".
* In "Issuing Organization", enter "DataTalksClub".
* (Optional) In "Issue Date", enter the time when the certificate was created.
* (Optional) Select the checkbox This certification does not expire. 
* Put your certificate ID.
* In "Certification URL", enter the URL for your certificate.

[Adapted from here](https://support.edx.org/hc/en-us/articles/206501938-How-can-I-add-my-certificate-to-my-LinkedIn-profile-)
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
