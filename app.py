import streamlit as st
from database_code import DB
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

db = DB()

st.sidebar.title('Flight Information')

select_option = st.sidebar.selectbox('Menu',['Project Description','Check Flights', 'Analytics'])


if select_option == 'Check Flights':
    st.title('Check Flights')
    city = db.fetch_city_names()
    print(city)
    col1,col2 = st.columns(2)
    with col1:
        start = st.selectbox('Start',sorted(city))

    with col2:
        destination = st.selectbox('Destination', sorted(city))

    if st.button('Details'):
        result = db.fetch_all_flights(start,destination)
        if len(result)==0:
            st.markdown("<h4 style='color: red;'>No flights exist between the selected cities.</h4>", unsafe_allow_html=True)
        else:
            # Fetch column names
            columns = [desc[0] for desc in db.mycursor.description]  # Get column names from cursor.description

            # Create a DataFrame with data and column names
            df = pd.DataFrame(result, columns=columns)

            # Display the DataFrame with headers
            st.dataframe(df)


if select_option == 'Analytics':
    col1,col2,col3 = st.columns(3)
    with col2:
        st.title('Analytics')

    st.write('')
    #st.write('')
    airline, frequency = db.daily_flight_frequency()

    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        ))

    st.subheader("Flight Frequency")
    st.plotly_chart(fig)

    #busy airport Bar-chart
    st.subheader("Busy Airport")
    city, frequency1 = db.busy_airport()
    fig = px.bar(
        x=city,
        y=frequency1
    )

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


    #expensive airlines
    st.subheader("Top 5 Expensive Airlines")

    result = db.expensive_airline()

    # Fetch column names
    columns = [desc[0] for desc in db.mycursor.description]  # Get column names from cursor.description

    # Create a DataFrame with data and column names
    df = pd.DataFrame(result, columns=columns)

    # Display the DataFrame with headers
    st.dataframe(df)


else:

    # Project Title
    st.title("Flight Information Dashboard")

    # Project Description
    st.subheader("Project Description")
    st.write("""
    The **Flight Information Dashboard** is a user-friendly web application designed to help travelers find flights between different cities. 
    Built using Streamlit and connected to a MySQL database, this tool allows users to search for flights and visualize data based on a dataset collected from Kaggle.
    """)

    # Key Features
    st.header("Key Features")
    st.write("""
    - **Search for Flights**: Users can select a starting city and a destination to view available flights, including airline names, departure times, and prices.
    - **No Flights Notification**: If there are no flights available for the selected route, a clear message will inform users.
    - **Visual Analytics**:
      - **Flight Frequency**: A pie chart displays how many flights each airline offers.
      - **Busy Airports**: A bar chart shows which airports have the most flights.
      - **Top Expensive Airlines**: A table lists the five airlines with the highest average prices.
    """)

    # Technology Used
    st.header("Technology Used")
    st.write("""
    - **Languages**: Python
    - **Framework**: Streamlit for the application interface, MySQL for the database
    - **Data Source**: Dataset collected from Kaggle
    - **Visualization**: Plotly for interactive charts
    """)

    # About Me
    st.header("About Me")
    st.write("""
    I’m **Fouzia Sharkar**, a Computer Science and Engineering graduate with a passion for data science. 
    I enjoy creating practical solutions that help people. This project reflects my goal of using technology to simplify travel planning and provide valuable insights.
    """)
















