var index = [];
var voltage = [];
var current = [];
var temperature = [];
var socc = [];


window.onload = function getData() {
  fetch("http://127.0.0.1:5000//api/instant_data")
    .then((response) => response.json())
    .then((data) => {
      console.log(data[0])
      var currentTime = document.getElementById("currentTime");
      var currentVoltage = document.getElementById("currentVoltage");
      var currentCurrent = document.getElementById("currentCurrent");
      var currentTemperature = document.getElementById("currentTemperature");
      var currentSocc = document.getElementById("currentSocc");



      currentTime.innerHTML = data.pop()[1];
      currentVoltage.innerHTML = `${data.pop()[0]} V`;
      currentCurrent.innerHTML = `${data.pop()[2]} A`;
      currentTemperature.innerHTML = `${data.pop()[3]} °C`;
      currentSocc.innerHTML = `${data.pop()[5]}%`;


      for (var j = 0; j < data.length; j++) {
        index.push(j);
        voltage.push(data[j][0]);
        current.push(data[j][2]);
        temperature.push(data[j][3]);
        socc.push(data[j][5]);


      }
    })
    .catch((error) => console.error("Error fetching data:", error))
    .finally(() => {
      var donchart = document.getElementById("donut").getContext("2d");
      var donut = new Chart(donchart, {
        type: "doughnut",
        data: {
          labels: ["Charging", "Discharging"],
          datasets: [
            {
              data: [500, 250], // Specify the data values array

              borderColor: ["#fff", "#fff"],
              backgroundColor: ["#ccc", "#666"], // Add custom color background (Points and Fill)
              borderWidth: 0, // Specify bar border width
            },
          ],
        },
        options: {
          responsive: true, // Instruct chart js to respond nicely.
          maintainAspectRatio: true, // Add to prevent default behaviour of full-width/height
        },
      });
      var ctx = document.getElementById("myChart").getContext("2d");
      var chart = new Chart(ctx, {
        type: "line",
        data: {
          labels: index,
          datasets: [
            {
              label: "Voltage",
              backgroundColor: "#ccc",
              borderColor: "#666",
              data: voltage,
            },
          ],
        },

        options: {
          elements: {
            point: {
              radius: 0,
            },
          },
          layout: {
            padding: 10,
          },
          legend: {
            display: false,
            position: "bottom",
          },
          title: {
            display: false,
            text: "Voltage Curve",
          },
          scales: {
            yAxes: [
              {
                scaleLabel: {
                  display: true,
                  labelString: "Voltage (V)",
                },
              },
            ],
            xAxes: [
              {
                ticks: {
                  autoSkip: true,
                  maxTicksLimit: 20,
                },
                scaleLabel: {
                  display: true,
                  labelString: "Time (minutes)",
                },
              },
            ],
          },
        },
      });
      var ctxCurrent = document.getElementById("current").getContext("2d");
      var chartCurrent = new Chart(ctxCurrent, {
        type: "line",
        data: {
          labels: index,
          datasets: [
            {
              label: "Current",
              backgroundColor: "#ccc",
              borderColor: "#666",
              data: current,
            },
          ],
        },

        options: {
          elements: {
            point: {
              radius: 0,
            },
          },
          layout: {
            padding: 10,
          },
          legend: {
            display: false,
            position: "bottom",
          },
          title: {
            display: false,
            text: "Current Curve",
          },
          scales: {
            yAxes: [
              {
                scaleLabel: {
                  display: true,
                  labelString: "Current (A)",
                },
              },
            ],
            xAxes: [
              {
                ticks: {
                  autoSkip: true,
                  maxTicksLimit: 20,
                },
                scaleLabel: {
                  display: true,
                  labelString: "Time (minutes)",
                },
              },
            ],
          },
        },
      });
      var ctxTemperature = document.getElementById("temperature").getContext("2d");
      var chartTemperature = new Chart(ctxTemperature, {
        type: "line",
        data: {
          labels: index,
          datasets: [
            {
              label: "Temperature",
              backgroundColor: "#ccc",
              borderColor: "#666",
              data: temperature,
            },
          ],
        },

        options: {
          elements: {
            point: {
              radius: 0,
            },
          },
          layout: {
            padding: 10,
          },
          legend: {
            display: false,
            position: "bottom",
          },
          title: {
            display: false,
            text: "Temperature Curve",
          },
          scales: {
            yAxes: [
              {
                scaleLabel: {
                  display: true,
                  labelString: "Temperature (°C)",
                },
              },
            ],
            xAxes: [
              {
                ticks: {
                  autoSkip: true,
                  maxTicksLimit: 20,
                },
                scaleLabel: {
                  display: true,
                  labelString: "Time (minutes)",
                },
              },
            ],
          },
        },
      });
      var ctxSocc = document.getElementById("socc").getContext("2d");
      var chartSocc = new Chart(ctxSocc, {
        type: "line",
        data: {
          labels: index,
          datasets: [
            {
              label: "SOC",
              backgroundColor: "#ccc",
              borderColor: "#666",
              data: socc,
            },
          ],
        },

        options: {
          elements: {
            point: {
              radius: 0,
            },
          },
          layout: {
            padding: 10,
          },
          legend: {
            display: false,
            position: "bottom",
          },
          title: {
            display: false,
            text: "SOC Curve",
          },
          scales: {
            yAxes: [
              {
                scaleLabel: {
                  display: true,
                  labelString: "SOC (%)",
                },
              },
            ],
            xAxes: [
              {
                ticks: {
                  autoSkip: true,
                  maxTicksLimit: 20,
                },
                scaleLabel: {
                  display: true,
                  labelString: "Time (minutes)",
                },
              },
            ],
          },
        },
      });
    });
};
