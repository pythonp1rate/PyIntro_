# MOST IMPORTANT - Must be first command!
st.set_page_config(
    page_title="My App",
    page_icon="🎈", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Most commonly used methods:
st.title()          # Big title
st.write()          # General output
st.text_input()     # Text field
st.button()         # Clickable button
st.selectbox()      # Dropdown
st.slider()         # Range slider
st.dataframe()      # Data table
st.plotly_chart()   # Interactive plot
st.columns()        # Layout columns
st.sidebar.*        # Sidebar elements
@st.cache_data      # Performance caching
st.session_state    # Persistent state