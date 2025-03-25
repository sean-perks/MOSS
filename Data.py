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
            title = "2025 Seed Collection Priority Collection Timeline"
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

    fig.update_xaxes(title=x_axis)
    fig.update_yaxes(title=y_axis)
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