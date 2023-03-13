from flask import Flask, render_template, request
from backend.data_analysis.visualizer import Visualizer
from backend.data_analysis.data_frame_processor import DataFrameProcessor

app = Flask(__name__)
data_frame_processor = DataFrameProcessor('/Users/jingchaozhong/Desktop/code/Data Science/pcc-course-enrollment-data-explorer/backend/data/data_source/2023/2023.csv')
visualizer = Visualizer(data_frame_processor)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/visualize_trend')
def visualize_trend():
    # construct an empty fig_json
    fig_json = visualizer.get_plotly_fig_json()
    return render_template('visualize-trend.html', fig_json=fig_json, all_crn=data_frame_processor.get_all_crn())


@app.route('/api/visualize_trend', methods=['POST'])
def api_visualize_trend():
    # crn read as int
    crn_lst = request.json['crnLst']
    start_time = request.json['startTime']
    end_time = request.json['endTime']
    if not data_frame_processor.crn_lst_valid(crn_lst):
        return 'Contain invalid CRN'
    fig_json = visualizer.get_plotly_fig_json(crn_lst=crn_lst, start_time=start_time, end_time=end_time)
    return fig_json


if __name__ == '__main__':
    app.run(debug=True)
