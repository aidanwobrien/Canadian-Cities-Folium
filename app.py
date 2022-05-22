from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
#     start_coords = (42.9849, -81.2453)
#     folium_map = folium.Map(
#         location=start_coords, 
#         zoom_start=7
#     )
#     folium_map.save("my_map.html")
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template("my_map.html")

if __name__ == '__main__':
    app.run(debug=True)