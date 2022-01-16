// console.log(d3.select("months").text())
document.addEventListener("DOMContentLoaded", function (e) {
  d3.select("#months").on("change", function (data) {
    let month = d3.select("#months").node().value;

    let url = `http://127.0.0.1:5000/accident-data/?month=${month}`;
    d3.json(url).then(function (response) {
      // console.log(response);
      plotData(response);
    });
  });

  d3.select("#states").on("change", function (data) {
    let state = d3.select("#states").node().value;

    let url = `http://127.0.0.1:5000/accident-data/?state=${state}`;
    d3.json(url).then(function (response) {
      // console.log(response);
      plotData(response);
    });
  });

  function plotData(data) {
    let car_model = [];
    let outcome = [];

    // For loop to populate arrays
    for (let i = 0; i < data.length; i++) {
      row = data[i];
      car_model.push(row.vehicle_model);
      outcome.push(row.doa_status);
    }

    // Trace1 Vehicle Model Data
    let trace1 = {
      values: car_model,
      labels: outcome,
      type: "pie",
    };

    // Create data array
    //  let data = [trace1, trace2];
    let chartData = [trace1];

    // Apply a title to the layout
    let layout = {
      title: "Fatal & Non-Fatal Outcomes by Vehicle Model",
      height: 400,
      width: 500
    };

    // Render the plot to the div tag with id "plot"
    Plotly.newPlot("plot-id", chartData, layout);
  }
});
