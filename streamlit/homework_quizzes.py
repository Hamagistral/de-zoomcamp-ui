import streamlit as st
import streamlit_book as stb

def show_week1_a_quizz():
    st.markdown("### 📝 Week 1 Homework (A) : Docker & SQL")

    st.success("In this homework we'll prepare the environment and practice with Docker and SQL")

    st.markdown("---")

    st.markdown("## Question 1. Knowing docker tags")

    st.markdown("""Run the command to get information on Docker 
                ```
                docker --help
                ```
                Now run the command to get help on the "docker build" command""")

    stb.multiple_choice("Which tag has the following text? - *Write the image ID to the file* (Choose one)", options_dict={"`--imageid string`": False, "`--iidfile string`": True,
                        "`--idimage string`": False, "`--idfile string`": False}, success='Correct answer', error='Wrong answer', button='Check answer')

    st.markdown("---")

    st.markdown("## Question 2. Understanding docker first run ")

    st.markdown("""
    Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash.
    Now check the python modules that are installed (use pip list). """)

    stb.multiple_choice("How many python packages/modules are installed? (Choose one)", options_dict={"1": False, "6": False,
                        "3": True, "7": False}, success='Correct answer', error='Wrong answer', button='Check answer')

    st.markdown("---")

    st.markdown("### Prepare Postgres  ")

    st.info("""
    Run Postgres and load data as shown in the videos.
    We'll use the green taxi trips from January 2019:

    ```wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz```

    You will also need the dataset with zones:

    ```wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv```

    Download this data and put it into Postgres (with jupyter notebooks or with a pipeline)""")

    st.markdown("---")

    st.markdown("""
    ## Question 3. Count records 

    Tip: started and finished on 2019-01-15. 

    Remember that `lpep_pickup_datetime` and `lpep_dropoff_datetime` columns are in the format timestamp (date and hour+min+sec) and not in date.""")

    stb.multiple_choice("How many taxi trips were totally made on January 15? (Choose one)", options_dict={"20689": False, "20530": True,
                        "17630": False, "21090": False}, success='Correct answer', error='Wrong answer', button='Check answer')

    st.markdown("---")

    st.markdown("""
    ## Question 4. Largest trip for each day

    Use the pick up time for your calculations.""")

    stb.multiple_choice("Which was the day with the largest trip distance? (Choose one)", options_dict={"2019-01-18": False, "2019-01-28": False,
                        "2019-01-15": True, "2019-01-10": False}, success='Correct answer', error='Wrong answer', button='Check answer')

    st.markdown("---")

    st.markdown("## Question 5. The number of passengers")

    stb.multiple_choice("In 2019-01-01 how many trips had 2 and 3 passengers? (Choose one)", options_dict={"2: 1282 ; 3: 266": False, "2: 1532 ; 3: 126": False,
                        "2: 1282 ; 3: 254": True, "2: 1282 ; 3: 274": False}, success='Correct answer', error='Wrong answer', button='Check answer')

    st.markdown("---")

    st.markdown("""
    ## Question 6. Largest tip

    Note: it's not a typo, it's `tip` , not `trip`""")

    stb.multiple_choice("For the passengers picked up in the Astoria Zone which was the drop off zone that had the largest tip? We want the name of the zone, not the id. (Choose one)", options_dict={"Central Park": False, "Jamaica": False,
                        "South Ozone Park": False, "Long Island City/Queens Plaza": True}, success='Correct answer', error='Wrong answer', button='Check answer')
                
    st.markdown("---")

    st.markdown("""
    ## Submitting the solutions

    * Form for submitting: [Form](https://forms.gle/EjphSkR1b3nsdojv7)
    * You can submit your homework multiple times. In this case, only the last submission will be used. 

    Deadline: 30 January (Monday), 22:00 CET

    ----

    ## 🎥 Video Solution""")

    st.video("https://www.youtube.com/watch?v=KIh_9tZiroA")

def show_week1_b_quizz():
    st.markdown("### 📝 Week 1 Homework (B) : Terraform")

    st.success("In this homework we'll prepare the environment by creating resources in GCP with Terraform.")

    st.info("""
    In your VM on GCP install Terraform. Copy the files from the course repo 
    [here](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_1_basics_n_setup/1_terraform_gcp/terraform) to your VM.

    Modify the files as necessary to create a GCP Bucket and Big Query Dataset.""")

    st.markdown("---")

    st.markdown("## Question 1. Creating Resources")

    st.markdown("""
    After updating the main.tf and variable.tf files run:
    
    ```
    terraform apply
    ```
    
    Paste the output of this command into the homework submission form.""")

    st.markdown("""
    ## Submitting the solutions

    * Form for submitting: [Form](https://forms.gle/S57Xs3HL9nB3YTzj9)
    * You can submit your homework multiple times. In this case, only the last submission will be used. 

    Deadline: 30 January (Monday), 22:00 CET""")

def show_week2_quizz():
    st.markdown("### 📝 Week 2 Homework : Workflow Orchestration")

    st.success("The goal of this homework is to familiarise users with workflow orchestration and observation.")

    st.markdown("---")

    st.markdown("## Question 1. Load January 2020 data")

    st.markdown("Using the `etl_web_to_gcs.py` flow that loads taxi data into GCS as a guide, create a flow that loads the green taxi CSV dataset for January 2020 into GCS and run it. Look at the logs to find out how many rows the dataset has.")
    
    stb.multiple_choice("How many rows does that dataset have?", options_dict={"447,770": True, "766,792": False,
                        "299,234": False, "822,132": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 2. Scheduling with Cron")

    st.markdown("Cron is a common scheduling specification for workflows.")
    
    stb.multiple_choice("Using the flow in `etl_web_to_gcs.py`, create a deployment to run on the first of every month at 5am UTC. What’s the cron schedule for that?", options_dict={"`0 5 1 * *`": True, "`0 0 5 1 *`": False,
                        "`5 * 1 0 *`": False, "`* * 5 1 0`": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 3. Loading data to BigQuery")

    st.markdown("""
    Using `etl_gcs_to_bq.py` as a starting point, modify the script for extracting data from GCS and loading it into BigQuery. This new script should not fill or remove rows with missing values. (The script is really just doing the E and L parts of ETL).

    The main flow should print the total number of rows processed by the script. Set the flow decorator to log the print statement.

    Parametrize the entrypoint flow to accept a list of months, a year, and a taxi color.

    Make any other necessary changes to the code for it to function as required.

    Create a deployment for this flow to run in a local subprocess with local flow code storage (the defaults).

    Make sure you have the parquet data files for Yellow taxi data for Feb. 2019 and March 2019 loaded in GCS. Run your deployment to append this data to your BiqQuery table.""")
    
    stb.multiple_choice("How many rows did your flow code process?", options_dict={"14,851,920": True, "12,282,990": False,
                        "27,235,753": False, "11,338,483": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 4. Github Storage Block")

    st.markdown("""
    Using the `web_to_gcs` script from the videos as a guide, you want to store your flow code in a GitHub repository for collaboration with your team. Prefect can look in the GitHub repo to find your flow code and read it. Create a GitHub storage block from the UI or in Python code and use that in your Deployment instead of storing your flow code locally or baking your flow code into a Docker image.

    Note that you will have to push your code to GitHub, Prefect will not push it for you.

    Run your deployment in a local subprocess (the default if you don’t specify an infrastructure). Use the Green taxi data for the month of November 2020.""")
    
    stb.multiple_choice("How many rows were processed by the script?", options_dict={"88,019": True, "192,297": False,
                        "88,605": False, "190,225": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 5. Email or Slack notifications")

    st.markdown("""
    Q5. It’s often helpful to be notified when something with your dataflow doesn’t work as planned. Choose one of the options below for creating email or slack notifications.

    The hosted Prefect Cloud lets you avoid running your own server and has Automations that allow you to get notifications when certain events occur or don’t occur.

    Create a free forever Prefect Cloud account at app.prefect.cloud and connect your workspace to it following the steps in the UI when you sign up.

    Set up an Automation that will send yourself an email when a flow run completes. Run the deployment used in Q4 for the Green taxi data for April 2019. Check your email to see the notification.

    Alternatively, use a Prefect Cloud Automation or a self-hosted Orion server Notification to get notifications in a Slack workspace via an incoming webhook.

    Join my temporary Slack workspace with this [link](https://temp-notify.slack.com/join/shared_invite/zt-1odklt4wh-hH~b89HN8MjMrPGEaOlxIw#/shared-invite/error). 400 people can use this link and it expires in 90 days.

    In the Prefect Cloud UI create an [Automation](https://docs.prefect.io/latest/cloud/automations/) or in the Prefect Orion UI create a [Notification](https://docs.prefect.io/latest/ui/notifications/) to send a Slack message when a flow run enters a Completed state. Here is the Webhook URL to use: https://hooks.slack.com/services/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

    Test the functionality.

    Alternatively, you can grab the webhook URL from your own Slack workspace and Slack App that you create.""")
    
    stb.multiple_choice("How many rows were processed by the script?", options_dict={"`125,268`": False, "`377,922`": False,
                        "`728,390`": False, "`514,392`": True}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 6. Secrets")

    st.markdown("Prefect Secret blocks provide secure, encrypted storage in the database and obfuscation in the UI. Create a secret block in the UI that stores a fake 10-digit password to connect to a third-party service.")
    
    stb.multiple_choice("Once you’ve created your block in the UI, how many characters are shown as asterisks (*) on the next page of the UI?", options_dict={"5": False, "6": False,
                        "8": True, "10": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("""
    ## Submitting the solutions
    
    * Form for submitting: [From](https://forms.gle/PY8mBEGXJ1RvmTM97)
    * You can submit your homework multiple times. In this case, only the last submission will be used.
    
    Deadline: 8 February (Wednesday), 22:00 CET

    ## 🎥 Video Solution""")
    
    st.video("https://youtu.be/L04lvYqNlc0")

    st.info("Homework [Code](https://github.com/discdiver/prefect-zoomcamp/tree/main/flows/04_homework)")
    
def show_week3_quizz():
    st.markdown("### 📝 Week 3 Homework : Data Warehouse")

    st.info("""
            **Important Note:**

            You can load the data however you would like, but keep the files in .GZ Format. If you are using orchestration such as Airflow or Prefect do not load the data into Big Query using the orchestrator.
            Stop with loading the files into a bucket.

            **Note:** You can use the CSV option for the GZ files when creating an External Table

            **Setup:**    

            Create an external table using the fhv 2019 data.  
            Create a table in BQ using the fhv 2019 data (do not partition or cluster this table).  
            
            Data can be found here: https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/fhv""")

    st.markdown("---")

    st.markdown("## Question 1.")
    
    stb.multiple_choice("What is the count for fhv vehicle records for year 2019?", options_dict={"65,623,481": False, "43,244,696": True,
                        "22,978,333": False, "13,942,414": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 2.")

    st.markdown("Write a query to count the distinct number of affiliated_base_number for the entire dataset on both the tables.")

    stb.multiple_choice("What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?", 
                        options_dict={"25.2 MB for the External Table and 100.87MB for the BQ Table": False, 
                                      "225.82 MB for the External Table and 47.60MB for the BQ Table": False,
                                      "0 MB for the External Table and 0MB for the BQ Table": False, 
                                      "0 MB for the External Table and 317.94MB for the BQ Table": True}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 3.")
    
    stb.multiple_choice("How many records have both a blank (null) PUlocationID and DOlocationID in the entire dataset?", options_dict={"717,748": True, "1,215,687": False,
                        "5": False, "20,332": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 4.")
    
    stb.multiple_choice("What is the best strategy to optimize the table if query always filter by pickup_datetime and order by affiliated_base_number?", 
                        options_dict={"Cluster on pickup_datetime Cluster on affiliated_base_number": False, 
                                      "Partition by pickup_datetime Cluster on affiliated_base_number": True,
                                      "Partition by pickup_datetime Partition by affiliated_base_number": False, 
                                      "Partition by affiliated_base_number Cluster on pickup_datetime": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 5.")

    st.markdown("""
    Implement the optimized solution you chose for question 4. Write a query to retrieve the distinct affiliated_base_number between pickup_datetime 2019/03/01 and 2019/03/31 (inclusive).
    Use the BQ table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 4 and note the estimated bytes processed.""")
    
    stb.multiple_choice("What are these values? Choose the answer which most closely matches.", 
                        options_dict={"12.82 MB for non-partitioned table and 647.87 MB for the partitioned table": False, 
                                      "647.87 MB for non-partitioned table and 23.06 MB for the partitioned table": True,
                                      "582.63 MB for non-partitioned table and 0 MB for the partitioned table": False, 
                                      "646.25 MB for non-partitioned table and 646.25 MB for the partitioned table": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 6.")
    
    stb.multiple_choice("Where is the data stored in the External Table you created?", options_dict={"Big Query": False, "GCP Bucket": True,
                        "Container Registry": False, "Big Table": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 7.")
    
    stb.true_or_false("It is best practice in Big Query to always cluster your data:", False, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## (Not required) Question 8.")
    
    st.markdown("""
    A better format to store these files may be parquet. Create a data pipeline to download the gzip files and convert them into parquet. Upload the files to your GCP Bucket and create an External and BQ Table.
    """)

    st.info("Note: Column types for all files used in an External Table must have the same datatype. While an External Table may be created and shown in the side panel in Big Query, this will need to be validated by running a count query on the External Table to check if any errors occur.")
    
    st.markdown("---")

    st.markdown("""
    ## Submitting the solutions

    * Form for submitting: [Form](https://forms.gle/rLdvQW2igsAT73HTA)
    * You can submit your homework multiple times. In this case, only the last submission will be used.

    Deadline: 13 February (Monday), 22:00 CET

    --- 

    ## 🎥 Video Solution""")
    
    st.video("https://www.youtube.com/watch?v=j8r2OigKBWE")

def show_week4_quizz():
    st.markdown("### 📝 Week 4 Homework : Analytics Engineering")

    st.success("In this homework, we'll use the models developed during the week 4 videos and enhance the already presented dbt project using the already loaded Taxi data for fhv vehicles for year 2019 in our DWH.")

    st.info("""
            This means that in this homework we use the following data [Datasets list](Dataset)

            * Yellow taxi data - Years 2019 and 2020
            * Green taxi data - Years 2019 and 2020
            * fhv data - Year 2019.

            We will use the data loaded for:

            * Building a source table: stg_fhv_tripdata
            * Building a fact table: fact_fhv_trips
            * Create a dashboard

            If you don't have access to GCP, you can do this locally using the ingested data from your Postgres database instead. If you have access to GCP, you don't need to do it for local Postgres - only if you want to.

            > **Note**: if your answer doesn't match exactly, select the closest option""")

    st.markdown("---")

    st.markdown("## Question 1.")

    st.markdown("You'll need to have completed the ['Build the first dbt models'](https://www.youtube.com/watch?v=UVI30Vxzd6c&ab_channel=DataTalksClub%E2%AC%9B) video and have been able to run the models via the CLI. You should find the views and models for querying in your DWH.")
    
    stb.multiple_choice("What is the count of records in the model fact_trips after running all models with the test run variable disabled and filtering for 2019 and 2020 data only (pickup datetime)?", 
                        options_dict={"41648442": False, "51648442": False,
                        "61648442": True, "71648442": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 2.")

    st.markdown("You will need to complete 'Visualising the data' videos, either using [google data studio](https://www.youtube.com/watch?v=39nLTs74A3E&ab_channel=DataTalksClub%E2%AC%9B) or [metabase](https://www.youtube.com/watch?v=BnLkrA7a6gM&ab_channel=DataTalksClub%E2%AC%9B).")
    
    stb.multiple_choice("What is the distribution between service type filtering by years 2019 and 2020 data as done in the videos?", 
                        options_dict={"89.9/10.1": True, "94/6": False,
                        "76.3/23.7": False, "99.1/0.9": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 3.")

    st.markdown("Create a staging model for the fhv data for 2019 and do not add a deduplication step. Run it via the CLI without limits (is_test_run: false). Filter records with pickup time in year 2019.")
    
    stb.multiple_choice("What is the count of records in the model stg_fhv_tripdata after running all models with the test run variable disabled ?", 
                        options_dict={"33244696": False, "43244696": True,
                        "53244696": False, "63244696": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 4.")

    st.markdown("""
    Create a core model for the stg_fhv_tripdata joining with dim_zones. Similar to what we've done in fact_trips, keep only records with known pickup and dropoff locations entries for pickup and dropoff locations. 
    Run it via the CLI without limits (is_test_run: false) and filter records with pickup time in year 2019.""")
    
    stb.multiple_choice("What is the count of records in the model fact_fhv_trips after running all dependencies with the test run variable disabled ?", 
                        options_dict={"12998722": False, "22998722": True,
                        "32998722": False, "42998722": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 5.")

    st.markdown("""
    Create a dashboard with some tiles that you find interesting to explore the data. 
    One tile should show the amount of trips per month, as done in the videos for fact_trips, based on the fact_fhv_trips table.""")
    
    stb.multiple_choice("What is the month with the biggest amount of rides after building a tile for the fact_fhv_trips table?", 
                        options_dict={"March": False, "April": False,
                        "January": True, "December": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("""
    ## Submitting the solutions

    * Form for submitting: [Form](https://forms.gle/6A94GPutZJTuT5Y16)
    * You can submit your homework multiple times. In this case, only the last submission will be used.

    Deadline: 25 February (Saturday), 22:00 CET

    --- 

    ## 🎥 Video Solution""")
    
    st.video("https://www.youtube.com/watch?v=I_K0lNu9WQw")

def show_week5_quizz():

    st.markdown("### 📝 Week 5 Homework : Batch Processing")

    st.success("In this homework we'll put what we learned about Spark in practice.")

    st.info("For this homework we will be using the FHVHV 2021-06 data found here. [FHVHV Data](https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhvhv/fhvhv_tripdata_2021-06.csv.gz)")

    st.markdown("---")

    st.markdown("## Question 1.")

    st.markdown("""
    Install Spark and PySpark

    1. Install Spark
    2. Run PySpark
    3. Create a local spark session
    4. Execute spark.version.""")
    
    stb.multiple_choice("What's the output?", 
                        options_dict={"3.3.2": True, "2.1.4": False,
                        "1.2.3": False, "5.4": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 2.")

    st.markdown("""
    **HVFHW June 2021**

    Read it with Spark using the same schema as we did in the lessons.
    We will use this dataset for all the remaining questions.
    Repartition it to 12 partitions and save it to parquet.""")
    
    stb.multiple_choice("What is the average size of the Parquet (ending with .parquet extension) Files that were created (in MB)? Select the answer which most closely matches.", 
                        options_dict={"2MB": False, "24MB": True,
                        "100MB": False, "250MB": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 3.")

    st.markdown("""
    **Count records**

    Consider only trips that started on June 15.""")
    
    stb.multiple_choice("How many taxi trips were there on June 15?", 
                        options_dict={"308,164": False, "12,856": False,
                        "452,470": True, "50,982": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 4.")

    st.markdown("""
    **Longest trip for each day**

    Now calculate the duration for each trip.""")
    
    stb.multiple_choice("How long was the longest trip in Hours?", 
                        options_dict={"66.87 Hours": True, "243.44 Hours": False,
                        "7.68 Hours": False, "3.32 Hours": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 5.")

    st.markdown("""
    **User Interface**""")
    
    stb.multiple_choice("Spark’s User Interface which shows application's dashboard runs on which local port?", 
                        options_dict={"80": False, "443": False,
                        "4040": True, "8080": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 6.")

    st.markdown("""
    ** Most frequent pickup location zone**
   
    Load the zone lookup data into a temp view in Spark
    [Zone Data](https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv)""")

    
    stb.multiple_choice("Using the zone lookup data and the fhvhv June 2021 data, what is the name of the most frequent pickup location zone?", 
                        options_dict={"East Chelsea": False, "Astoria": False,
                        "Union Sq": False, "Crown Heights North": True}, success='Correct answer', error='Wrong answer', button='Check answer')

    st.markdown("---")

    st.markdown("""
    ## Submitting the solutions

    * Form for submitting: [Form](https://forms.gle/EcSvDs6vp64gcGuD8)
    * You can submit your homework multiple times. In this case, only the last submission will be used.

    Deadline: 06 March (Monday), 22:00 CET

    --- 

    ## 🎥 Video Solution""")
    
    st.video("https://www.youtube.com/watch?v=ldoDIT32pJs")

def show_week6_quizz():
    st.markdown("### 📝 Week 6 Homework : Stream Processing")

    st.info("In this homework, there will be two sections, the first session focus on theoretical questions related to Kafka and streaming concepts and the second session asks to create a small streaming application using preferred programming language (Python or Java).")

    st.markdown("---")

    st.markdown("## Question 1.")
    
    stb.multiple_choice("Please select the statements that are correct", 
                        options_dict={"Kafka Node is responsible to store topics": True, "Zookeeper is removed from Kafka cluster starting from version 4.0": True,
                        "Retention configuration ensures the messages not get lost over specific period of time.": True, 
                        "Group-Id ensures the messages are distributed to associated consumers": True}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 2.")

    stb.multiple_choice("Please select the Kafka concepts that support reliability and availability", 
                        options_dict={"Topic Replication": True, "Topic Partioning": False,
                        "Consumer Group Id": False, "Ack All": True}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 3.")

    stb.multiple_choice("Please select the Kafka concepts that support scaling", 
                        options_dict={"Topic Replication": False, "Topic Paritioning": True,
                        "Consumer Group Id": True, "Ack All": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 4.")

    stb.multiple_choice("Please select the attributes that are good candidates for partitioning key. Consider cardinality of the field you have selected and scaling aspects of your application", 
                        options_dict={"payment_type": True, "vendor_id": True, "passenger_count": False, "total_amount": False,
                        "tpep_pickup_datetime": False, "tpep_dropoff_datetime": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 5.")

    stb.multiple_choice("Which configurations below should be provided for Kafka Consumer but not needed for Kafka Producer", 
                        options_dict={"Deserializer Configuration": True, "Topics Subscription": True, "Bootstrap Server": False,
                        "Group-Id": True, "Offset": True, "Cluster Key and Cluster-Secret": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 6.")

    st.markdown("""
    Please implement a streaming application, for finding out popularity of PUlocationID across green and fhv trip datasets. 
    Please use the datasets [fhv_tripdata_2019-01.csv.gz](https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/fhv) and [green_tripdata_2019-01.csv.gz](https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/green)

    PS: If you encounter memory related issue, you can use the smaller portion of these two datasets as well, it is not necessary to find exact number in the question.

    Your code should include following

    1. Producer that reads csv files and publish rides in corresponding kafka topics (such as rides_green, rides_fhv)
    2. Pyspark-streaming-application that reads two kafka topics and writes both of them in topic rides_all and apply aggregations to find most popular pickup location.""")

    st.markdown("---")

    st.markdown("""

    ## Submitting the solutions

    * Form for submitting: [Form](https://forms.gle/rK7268U92mHJBpmW7)
    * You can submit your homework multiple times. In this case, only the last submission will be used.

    Deadline: 13 March (Monday), 22:00 CET

    --- 

    ## Solution

    Solution on [Github](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2023/week_6_stream_processing/homework.md)

    For Question 6 ensure :

    1. Download fhv_tripdata_2019-01.csv and green_tripdata_2019-01.csv under resources/fhv_tripdata and resources/green_tripdata resprctively. ps: You need to unzip the compressed files

    2. Update the client.properties settings using your Confluent Cloud api keys and cluster.

    3. And create the topics(all_rides, fhv_taxi_rides, green_taxi_rides) in Confluent Cloud UI

    4. Run Producers for two datasets

        ```
        python3 producer_confluent --type green
        python3 producer_confluent --type fhv
        ```  

    5. Run pyspark streaming  

        ``` 
        ./spark-submit.sh streaming_confluent.py
        ```  """)

def show_workshop():
    st.markdown("### 🔧 Workshop: Maximizing Confidence in Your Data Model Changes with dbt and PipeRider")

    st.success("To learn how to use PipeRider together with dbt for detecting changes in model and data, sign up for a workshop")

    st.markdown(" ## 🎥 Video")

    st.video("https://www.youtube.com/watch?v=O-tyUOQccSs")

    st.info("[Repository](https://github.com/InfuseAI/taxi_rides_ny_duckdb)")

    st.markdown("---")

    st.markdown("## 📝 Homework")

    st.info("""
    The following questions follow on from the original Week 4 homework, and so use the same data as required by those questions:  
 
    [Week 4 Homework ](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2023/week_4_analytics_engineering/homework.md)

    Yellow taxi data - Years 2019 and 2020 Green taxi data - Years 2019 and 2020 fhv data - Year 2019.""")

    st.markdown("## Question 1.")

    st.markdown("You will need to run PipeRider and check the repor")
    
    stb.multiple_choice("What is the distribution between vendor id filtering by years 2019 and 2020 data?", 
                        options_dict={"70.1/29.6/0.5": False, "60.1/39.5/0.4": True,
                        "90.2/9.5/0.3": False, "80.1/19.7/0.2": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 2.")

    st.markdown("You will need to run PipeRider and check the repor")
    
    stb.multiple_choice("What is the composition of total amount (positive/zero/negative) filtering by years 2019 and 2020 data?", 
                        options_dict={"51.4M/15K/48.6K": False, "21.4M/5K/248.6K": False,
                        "61.4M/25K/148.6K": True, "81.4M/35K/14.6K": False}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("---")

    st.markdown("## Question 3.")

    st.markdown("You will need to run PipeRider and check the repor")
    
    stb.multiple_choice("What is the numeric statistics (average/standard deviation/min/max/sum) of trip distances filtering by years 2019 and 2020 data?", 
                        options_dict={"1.95/35.43/0/16.3K/151.5M": False, "3.95/25.43/23.88/267.3K/281.5M": False,
                        "5.95/75.43/-63.88/67.3K/81.5M": False, "2.95/35.43/-23.88/167.3K/181.5M": True}, success='Correct answer', error='Wrong answer', button='Check answer')
    
    st.markdown("""
    ## Submitting the solutions

    * Form for submitting: [Form](https://forms.gle/WyLQHBu1DNwNTfqe8)
    * You can submit your homework multiple times. In this case, only the last submission will be used.

    Deadline: 20 March, 22:00 CET

    --- 

    ## 🎥 Video Solution""")
    
    st.video("https://www.youtube.com/watch?v=inNrUys7W8U")