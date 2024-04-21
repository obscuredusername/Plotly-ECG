import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# Function to generate the pie chart
def generate_pie_chart(data, headers):
    # Convert the data and headers to a pandas DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Count the occurrences of each disease
    disease_counts = df[['DX1', 'DX2', 'DX3']].stack().value_counts()

    # Combine diseases with counts less than 1200 into 'Others' category
    disease_counts = disease_counts[disease_counts >= 1200]
    others_count = sum(disease_counts[disease_counts < 1200])
    disease_counts = disease_counts[disease_counts >= 1200]
    disease_counts['Others'] = others_count

    figure = go.Figure(data=[go.Pie(labels=disease_counts.index, values=disease_counts.values,hole=0.6)])
    figure.update_layout(
        title="Disease Distribution",
        autosize=False,
        width=800,
        height=600
    )   

    return figure
 
def generate_line_chart(data, headers):
    df = pd.DataFrame(data, columns=headers)

    dx1_counts = df['DX1'].value_counts().reset_index()
    dx1_counts.columns = ['DX1', 'Count']
    dx1_counts = dx1_counts.sort_values(by='DX1')

    fig = px.line(dx1_counts, x='DX1', y='Count')

    fig.update_layout(yaxis=dict(range=[0, 20000]), xaxis_title='DX1', yaxis_title='Count')

    return fig

def generate_bar_chart(data, headers):
    # Convert the data and headers to a pandas DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Reshape the data to create a single 'Disease' column
    diseases = df[['DX1', 'DX2', 'DX3']].values.flatten()
    genders = df['Gender'].values.repeat(3)
    df = pd.DataFrame({'Disease': diseases, 'Gender': genders})

    # Drop missing values (empty cells)
    df = df.dropna(subset=['Disease'])

    # Group the data by disease and gender, and calculate the count
    grouped_data = df.groupby(['Disease', 'Gender']).size().reset_index(name='Count')

    # Create the bar chart
    fig = go.Figure()

    # Add bars for each disease and gender
    for gender in grouped_data['Gender'].unique():
        gender_data = grouped_data[grouped_data['Gender'] == gender]
        fig.add_trace(go.Bar(
            x=gender_data['Disease'],
            y=gender_data['Count'],
            name=gender,
            text=gender_data['Count'],
            textposition='auto'
        ))

    # Customize the layout
    fig.update_layout(
        title='Distribution of Diseases by Gender',
        xaxis_title='Disease',
        yaxis_title='Count',
        barmode='group',
        width=1500,
        height=700
    )
    return fig

def generate_agebar_chart(data, headers):
    # Convert the data and headers to a pandas DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Drop missing values (empty cells)
    df = df.dropna(subset=['Age'])

    # Convert age column to numeric data type
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

    # Define age groups
    age_groups = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90+']

    # Assign each age to an age group
    df['Age Group'] = pd.cut(df['Age'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, float('inf')], labels=age_groups, right=False)

    # Group the data by age group and calculate the count
    grouped_data = df.groupby('Age Group').size().reset_index(name='Count')

    # Create the bar chart
    fig = go.Figure(data=go.Bar(
        x=grouped_data['Age Group'],
        y=grouped_data['Count'],
        text=grouped_data['Count'],
        textposition='auto'
    ))

    # Customize the layout
    fig.update_layout(title='Age Group Distribution', xaxis_title='Age Group', yaxis_title='Count',width= 1500)

    return fig




def generate_agepie_chart(data, headers):
    # Convert the data and headers to a pandas DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Reshape the data to create a single 'Disease' column
    diseases = df[['DX1', 'DX2', 'DX3']].values.flatten()
    genders = df['Gender'].values.repeat(3)
    df = pd.DataFrame({'Disease': diseases, 'Gender': genders})

    # Drop missing values (empty cells)
    df = df.dropna(subset=['Disease'])

    # Group the data by gender and calculate the count
    grouped_data = df.groupby('Gender').size().reset_index(name='Count')

    # Create the pie chart
    fig = go.Figure(data=go.Pie(
        labels=grouped_data['Gender'],
        values=grouped_data['Count'],
        textinfo='label+percent',
        insidetextorientation='radial',
        hole=0.6
    ))

    # Customize the layout
    fig.update_layout(
        title='Distribution of Diseases by Gender',
    )

    return fig