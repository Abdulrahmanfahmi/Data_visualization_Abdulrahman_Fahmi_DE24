from taipy.gui import Gui
import taipy.gui.builder as tgb
import pandas as pd
from utils.constans import DATA_DIRECTORY

df = pd.read_excel(DATA_DIRECTORY / "ans_l14_ansokningar_yh_utb_beslut_2025.xlsx")

with tgb.Page() as page:
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