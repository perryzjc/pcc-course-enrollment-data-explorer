$(document).ready(function() {
  // Initialize an object to keep track of unique CRNs
  let crns = [];
  let figure = {};
  let minTime = "";
  let maxTime = "";

  // Add CRN button click handler
  $('#add-crn-btn').click(function() {
    let crn = $('#crn-input').val();
    if (crn === '') {
      // Display an error message if the input field is empty
      $('#error-message').text('Please enter a CRN.');
      $('#error-message').show();
    } else if (crns.includes(crn)) {
      // Display an error message if the CRN is already in the list
      $('#error-message').text('The CRN is already in the list.');
      $('#error-message').show();
    } else {
      crns.push(crn);
      updateCrnList();
      requestData()
      visualizeTrend();
      // Clear the error message if there was one
      $('#error-message').hide();
    }
  });

  // Remove CRN button click handler
  $('#remove-crn-btn').click(function() {
    let crn = $('#crn-input').val();
    if (crn === '') {
      // Display an error message if the input field is empty
      $('#error-message').text('Please enter a CRN.');
      $('#error-message').show();
    } else if (!crns.includes(crn)) {
      // Display an error message if the CRN is not in the list
      $('#error-message').text('The CRN is not in the list.');
      $('#error-message').show();
    } else {
      let index = crns.indexOf(crn);
      crns.splice(index, 1);
      updateCrnList();
      removeCRNFromFigure(crn);
      visualizeTrend()
      // Clear the error message if there was one
      $('#error-message').hide();
    }
  });

  $('#apply-time-range-btn').click(function() {
    // Filter the data based on the selected time range
    let filteredData = filterDataByTimeRange(figure.data);
    // Update the Plotly plot with the filtered data
    updatePlot(filteredData);
  });

  function filterDataByTimeRange(data) {
    // if data is empty, do nothing
    if (data.length === 0) {
        return data;
    }
    let startTime = $('#start-time-input').val();
    let endTime = $('#end-time-input').val();
    let filteredData = [];
    // if start time is empty, set it to min time
    if (startTime === "") {
        startTime = minTime;
    }
    // if end time is empty, set it to max time
    if (endTime === "") {
        endTime = maxTime;
    }
    for (let i = 0; i < data.length; i++) {
      let trace = data[i];
      let filteredTrace = {
        x: [],
        y: [],
        mode: trace.mode,
        name: trace.name,
        line: trace.line
      };
      for (let j = 0; j < trace.x.length; j++) {
        let x = trace.x[j];
        let y = trace.y[j];
        if (x >= startTime && x <= endTime) {
          filteredTrace.x.push(x);
          filteredTrace.y.push(y);
        }
      }
      filteredData.push(filteredTrace);
    }
    return filteredData;
  }

  function updatePlot(filteredData) {
    Plotly.newPlot('plot', filteredData, figure.layout);
  }

  function setMinTime(fig) {
    minTime = "";
    const xValues = fig.data.flatMap(trace => trace.x);
    minTime = findExtremeValue(xValues, (currentValue, extremeValue) => currentValue < extremeValue);
  }

  function setMaxTime(fig) {
    maxTime = "";
    const xValues = fig.data.flatMap(trace => trace.x);
    maxTime = findExtremeValue(xValues, (currentValue, extremeValue) => currentValue > extremeValue);
  }

  function findExtremeValue(arr, comparisonFn) {
    return arr.reduce((extremeValue, currentValue) => {
      if (extremeValue === null || comparisonFn(currentValue, extremeValue)) {
        return currentValue;
      }
      return extremeValue;
    }, null);
  }

  function updateCrnList() {
    // Clear the current list and add all CRNs
    $('#crn-select').empty();
    for (let crn of crns) {
        $('#crn-select').append(`<option value="${crn}">${crn}</option>`);
    }
  }

  function visualizeTrend() {
    //apply time range
    let filteredData = filterDataByTimeRange(figure.data);
    updatePlot(filteredData);
  }

  function requestData() {
    const int_crns = crns.map(crn => parseInt(crn));
    // Send request to server
    $.ajax({
      url: '/api/visualize_trend',
      type: 'POST',
      contentType: 'application/json',
      // but crn should read as int
      data: JSON.stringify({
        crn_lst: int_crns,
        start_time: $('#start-time-input').val(),
        end_time: $('#end-time-input').val()
      }),
      success: function(fig_json) {
        // Render the returned figure JSON
        figure = JSON.parse(fig_json);
        Plotly.newPlot('plot', figure.data, figure.layout);
        setMinTime(figure);
        setMaxTime(figure);
      },
      error: function() {
        console.log('Error fetching data from server.');
      }
    });
  }

  // remove crn from figure data directly don need to request data again
  function removeCRNFromFigure(crn) {
    let index = -1;
    for (let i = 0; i < figure.data.length; i++) {
      if (figure.data[i].name === crn) {
        console.log("remove crn from figure data");
        index = i;
        console.log(index);
        break;
      }
    }
    if (index !== -1) {
      figure.data.splice(index, 1);
    }
  }
});
