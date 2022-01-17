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
    let count = 1;
    var counter = ""
    // For loop to populate arrays
    for (let i = 0; i < data.length; i++) {
        
      
        row = data[i];
        car_model.push(row.vehicle_model)
        outcome.push(row.doa_status)

        if (outcome[i] == outcome[i+1])
        {
            count +=1;
        }
            else
        {
            counter += outcome[i] + count;
            count=1;

}
    }    
    

    // Trace1 Vehicle Model Data (count of vehicle type involved in accidents)
    let trace1 = {
      x: car_model,
      y: counter,
      type: "bar",
    };

    // Create data array
    //  let data = [trace1, trace2];
    let chartData = [trace1];

    // Apply a title to the layout
    let layout = {
      height: 400,
      width: 500
    };

    // Render the plot to the div tag with id "plot"
    Plotly.newPlot("plot-id", chartData, layout);
  

    // line chart
    var trace2 = {

        x: ["January", "February", "March", "April", "May","June", "July", "August", "September", "October", "November", "December"],
        y: outcome,
        type: 'line'
      };
      
      var linedata = [trace2];
      
      
      Plotly.newPlot('line-id', linedata);

}




})
;





// title: "Fatal & Non-Fatal Outcomes by Vehicle Model",
