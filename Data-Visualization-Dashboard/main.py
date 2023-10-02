import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns


st.markdown("""
<style>
.title-text {
    font-size: 36px;
    font-weight: bold;
    color: #333;
    text-align: center;
    margin-bottom: 20px;
}
.description-text {
    font-size: 20px;
    color: #444;
    text-align: center;
    margin-bottom: 30px;
    line-height: 1.5;
}
</style>
""", unsafe_allow_html=True)


st.markdown('<p class="title-text">Data Visualization Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="description-text">Welcome to the Data Visualization Dashboard.</p>', unsafe_allow_html=True)

st.sidebar.header("Customize Visualization")

# File upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load data
    data = pd.read_csv(uploaded_file)

    # Data preview
    st.subheader("Data Preview")
    st.dataframe(data.head())

    # Select columns for visualization
    selected_columns = st.sidebar.multiselect(
        "Choose columns for visualization", data.columns, data.columns.tolist()[:2]
    )

    if selected_columns:
        # Choose chart type
        chart_type = st.sidebar.selectbox(
            "Select Chart Type",
            ["Histogram", "Line Chart", "Scatter Plot", "Bar Chart", "Box Plot", "Pair Plot", "Pie Chart", "Heatmap", "Count Plot"],
        )

        if chart_type == "Histogram":
            st.subheader("Histogram")
            for column in selected_columns:
                fig = px.histogram(data, x=column, title=f"Histogram of {column}")
                st.plotly_chart(fig)

        elif chart_type == "Line Chart":
            st.subheader("Line Chart")
            x_column = st.selectbox("Select x-axis", selected_columns)
            y_column = st.selectbox("Select y-axis", selected_columns)
            fig = px.line(data, x=x_column, y=y_column, title=f"Line Chart: {x_column} vs {y_column}")
            st.plotly_chart(fig)

        elif chart_type == "Scatter Plot":
            st.subheader("Scatter Plot")
            x_column = st.selectbox("Select x-axis", selected_columns)
            y_column = st.selectbox("Select y-axis", selected_columns)
            fig = px.scatter(data, x=x_column, y=y_column, title=f"Scatter Plot: {x_column} vs {y_column}")
            st.plotly_chart(fig)

        elif chart_type == "Bar Chart":
            st.subheader("Bar Chart")
            x_column = st.selectbox("Select x-axis (categorical)", selected_columns)
            y_column = st.selectbox("Select y-axis (numeric)", selected_columns)
            fig = px.bar(data, x=x_column, y=y_column, title=f"Bar Chart: {x_column} vs {y_column}")
            st.plotly_chart(fig)

        elif chart_type == "Box Plot":
            st.subheader("Box Plot")
            x_column = st.selectbox("Select x-axis (categorical)", selected_columns)
            y_column = st.selectbox("Select y-axis (numeric)", selected_columns)
            fig = px.box(data, x=x_column, y=y_column, title=f"Box Plot: {x_column} vs {y_column}")
            st.plotly_chart(fig)

        elif chart_type == "Pair Plot":
            st.subheader("Pair Plot")
            selected_numeric_columns = data[selected_columns].select_dtypes(include=['number']).columns
            if len(selected_numeric_columns) >= 2:
                pair_plot = sns.pairplot(data=data, vars=selected_numeric_columns)
                st.pyplot(pair_plot)

        elif chart_type == "Pie Chart":
            st.subheader("Pie Chart")
            pie_column = st.selectbox("Select column for the Pie Chart", selected_columns)
            pie_data = data[pie_column].value_counts()
            fig = px.pie(values=pie_data.values, names=pie_data.index, title=f"Pie Chart: {pie_column}")
            st.plotly_chart(fig)

        elif chart_type == "Heatmap":
            st.subheader("Heatmap")
            heatmap_data = data[selected_columns].corr()
            sns.heatmap(heatmap_data, annot=True, cmap="coolwarm", linewidths=0.5)
            st.pyplot()

        elif chart_type == "Count Plot":
            st.subheader("Count Plot")
            count_column = st.selectbox("Select column for the Count Plot", selected_columns)
            sns.countplot(data=data, x=count_column)
            st.pyplot()

    st.sidebar.header("Data Details")
    st.sidebar.write(f"Number of Rows: {data.shape[0]}")
    st.sidebar.write(f"Number of Columns: {data.shape[1]}")


    st.sidebar.markdown("## Connect with Me")
    st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/prikshit7766/)")
    st.sidebar.markdown("[GitHub](https://github.com/Prikshit7766)")

# Add an option to download the data
if uploaded_file is not None and st.button("Download Data as CSV"):
    st.write("Downloading data as CSV...")
    csv = data.to_csv(index=False)
    st.download_button(
        label="Click to download",
        data=csv,
        file_name="data.csv",
        key="download-data",
    )