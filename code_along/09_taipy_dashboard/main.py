from taipy.gui import Gui
import taipy.gui.builder as tgb
import pandas as pd
from utils.constans import DATA_DIRECTORY

df = pd.read_excel(DATA_DIRECTORY/"resultat-ansokningsomgang-2024 (1).xlsx", sheet_name="Tabell 3", skiprows=5)

with tgb.page() as page:
    with tgb.part(class_name="container card"):
        tgb.text("MYH dashboard 2024", mode="md")
        
        with tgb.layout(columns="2 1"):
            with tgb.part(class_name="card"):
                tgb.text("Graph")
                
            with tgb.part(class_name="card"):
                 tgb.text("Filters")
                 
            with tgb.part(class_name="card"):
                tgb.text("Raw data")
                
                


if __name__ == "__main__":
    Gui(page).run(dark_mode=False, use_reloader=True, port=8081) 