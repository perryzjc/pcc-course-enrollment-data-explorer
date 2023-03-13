from flask import Flask, render_template, request
from backend.data_analysis.visualizer import Visualizer

app = Flask(__name__)
visualizer = Visualizer('/Users/jingchaozhong/Desktop/code/Data Science/pcc-course-enrollment-data-explorer/backend/data/data_source/2023/2023.csv')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/visualize_trend')
def visualize_trend():
    # construct an empty fig_json
    fig_json = visualizer.get_plotly_fig_json()
    return render_template('visualize-trend.html', fig_json=fig_json)


@app.route('/api/visualize_trend', methods=['POST'])
def api_visualize_trend():
    # crn read as int
    crn_lst = request.json['crn_lst']
    start_time = request.json['start_time']
    end_time = request.json['end_time']
    fig_json = visualizer.get_plotly_fig_json(crn_lst=crn_lst, start_time=start_time, end_time=end_time)
    return fig_json


if __name__ == '__main__':
    app.run(debug=True)
