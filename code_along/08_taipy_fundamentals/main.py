from taipy.gui import Gui
import taipy.gui.builder as tgb

selected_fruit = "apple"
slider_value = 20

with tgb.Page() as page:
    tgb.text("# Hello there taipy", mode="md")
    tgb.text("Welcome to the world of programming")
    
    tgb.slider(value="{slider_value}", min = 1, max = 50, step=1)
    tgb.text("slider value is at {slider_value}")
    
    tgb.text("select your favorite fruit", mode="md")
    tgb.selector(value="{selected_fruit}", lov=["tomato", "apple", "avocado", "banana"], dropdown=True,)
    tgb.text("Yummy {selected_fruit}")
    tgb.image("assets/{selected_fruit}.jpg")
    
    
    
    
if __name__ == "__main__":
    Gui(page).run(dark_mode=False, use_reloader=True, port=8080)