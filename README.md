# Flight Information Dashboard

The **Flight Information Dashboard** is a user-friendly web application designed to help travelers find flights between different cities. It is built using **Streamlit** and connected to a **MySQL** database, allowing users to search for flights and visualize key data. The data used for this tool is sourced from a **Kaggle** dataset.

## Key Features

- **Search for Flights**:  
  Users can select a starting city and a destination to view available flights, including airline names, departure times, and prices.

- **No Flights Notification**:  
  If there are no flights available for the selected route, a clear message will inform users.

- **Visual Analytics**:
  - **Flight Frequency**: A pie chart displays how many flights each airline offers.
  - **Busy Airports**: A bar chart shows which airports have the most flights.
  - **Top Expensive Airlines**: A table lists the five airlines with the highest average prices.

## Technology Used

- **Languages**: Python
- **Framework**: Streamlit for the application interface
- **Database**: MySQL for the backend storage
- **Data Source**: Kaggle dataset
- **Visualization**: Plotly for interactive charts
