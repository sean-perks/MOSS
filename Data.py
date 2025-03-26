import json
from pathlib import Path
import plotly.express as px
import plotly.io as pio
import random
import pandas as pd

# save in file
def write_json(dict, file_path = "StringHarmonics/text/accounts.json"):
    with open(file_path, 'w') as f:
        json.dump(dict, f)


# load back to verify
def read_json(file_path = "StringHarmonics/text/accounts.json"):
    with open(file_path, 'r') as f:
        my_dict = json.load(f)
    
    return my_dict

def build_index_data(needs_csv = r"mysite/2025_needs.csv"):
        """ 
        Builds data needed in index html. RETURNS FOUR things. 
        0. proj_species_dict is a dict with project as key and species for that project as list for values
        1. plant_dict is a dictionary of the data dataframe read from the main data source of seed needs (a csv)
        2. graph.json is a json of the seed collection timeline graph
        3. a html table of the df for mobile view

        Example usage:

        plant_dict, graph_json, table = build_index_data()
        """
        data = pd.read_csv(needs_csv)
        proj_species_dict = {}
        for x in data["Project"].unique():
            proj_species_dict[x] = list(data[data['Project'] == x]['Species'])

        plant_dict = data.to_dict(orient='list')
        fig = static_plot(data)
        graph_json = pio.to_json(fig)
        data = data.drop(["Normalized Size", "Seed Zone Ecoregion", "Text Position"], axis=1)

        table = data.to_html(classes='table table-striped', index=False)
        return proj_species_dict, plant_dict, graph_json, table

def get_project_data(proj, my_json="mysite/projects.json"):
    all_projects = read_json(my_json)
    proj_dict = all_projects[proj]
    return proj_dict

def get_project_plants(proj, my_json="mysite/project_plants.json"):
    all_projects = read_json(my_json)
    proj_dict = all_projects[proj]

    return proj_dict

def static_plot(
            data,
            x_axis="Collection Date",
            y_axis="Seed Zone Ecoregion",
            blob_size_normalized="Normalized Size",
            blob_size_original = "Lbs Needed",
            blob_color="Project",
            title = ""
):
    # Plot
    fig = px.scatter(
        data,
        x=x_axis,
        y=y_axis,
        size=blob_size_normalized,
        color=blob_color,
        text="Species",
        hover_name="Species",
        hover_data={blob_size_original: True, blob_size_normalized: False},
        title=title,
        size_max=75
    )

    fig.update_layout(
        autosize=True,
        height=1000,
    )
    # Update layout for a modern look
    fig.update_layout(
        autosize=True,
        height=1000,
        plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
        paper_bgcolor='rgba(0, 0, 0, 0)',  # Light background for the paper
        title_font=dict(size=20, color='darkgreen'),  # Title font styling
        xaxis=dict(
            #title=x_axis,
            title="",
            #title_font=dict(size=14, color='darkblue'),
            showgrid=True,
            gridcolor='darkgreen',  # Set grid lines to dark green
            gridwidth=1,  # Optional: Set grid line width
            griddash='dash',
            zeroline=True,
            zerolinecolor='lightgray'
        ),
        yaxis=dict(
            #title=y_axis,
            title="",
            #title_font=dict(size=14, color='darkblue'),
            showgrid=False,
            gridcolor='darkgreen',  # Set grid lines to dark green
            gridwidth=1,  # Optional: Set grid line width
            griddash='dash',
            zeroline=True,
            zerolinecolor='lightgray',
            tickangle=-90  # Rotate y-axis labels to 45 degrees
        ),
        margin=dict(l=70, r=60, t=40, b=70),    # Adjust margins

        legend = dict(
            orientation="h",  # Horizontal orientation
            yanchor="top",  # Anchor the legend to the bottom
            y=-0.2,  # Position it above the figure
            xanchor="center",  # Center the legend
            x=0.5  # Center the legend horizontally
        )
    )

    positions = ["bottom center", "top center", "bottom center", "middle left", "top center"]
    pos_list = []
    c = 0
    for x in range(len(data)):
        if c > 4:
            c = 0
        r = random.randint(0, 1)
        # print(r)
        pos_list.append(positions[c])
        c+=1

    data["Text Position"] = pos_list

    fig.update_traces(
        textposition = data["Text Position"],
        mode = "markers+text",
        textfont=dict(size=10),
        marker=dict(
            line=dict(
                color="black",
                width=.7
            )
        ),
        opacity=0.7
    )

    fig.update_xaxes()
    fig.update_yaxes()
    return fig


if __name__ == "__main__":
    data = pd.read_csv(r"MOSS/mysite/2025_needs.csv")
    fig = static_plot(data)
    graph_json = pio.to_json(fig)

    mhdf = data[data["Project"] == "Mount Hebo"]
    mhdf = mhdf.drop(["Normalized Size", "Seed Zone Ecoregion"], axis=1)
    print(mhdf.head())
    mh_table = mhdf.to_html()
    print(mh_table)