
function initChart(lasts, conf) {
	// chart colors
	var colors = ['#0087DB','#CEEFFC', '#F1ECEC', '#E98181', '#EEC1C1', '#007bff', '#8E8E8E', '#fff'];

	/* large line chart */
	var chLineTem = document.getElementById("chLineTem");
	var chLineHum = document.getElementById("chLineHum");
	
	lasts.reverse();
	var labels = [];
	var dataTem = [];
	var dataHum = [];
	var dataTemMaxCnf = [];
	var dataHumMaxCnf = [];
	var dataTemMinCnf = [];
	var dataHumMinCnf = [];
	
	lasts.forEach(function(item) {
		dataTem.push(item.tem);
		dataHum.push(item.hum);
		dataTemMaxCnf.push(conf.tem_max);
		dataTemMinCnf.push(conf.tem_min);
		dataHumMaxCnf.push(conf.hum_max);
		dataHumMinCnf.push(conf.hum_min);

		labels.push(moment(item.date.$date).add(-60, 'minutes').format("DD-MM-YYYY HH:mm:ss"));
	});	

	var ctx = chLineTem.getContext("2d");
	var gradientStroke = ctx.createLinearGradient(0, 0, 0, 600);
	gradientStroke.addColorStop(0, colors[7]);
	gradientStroke.addColorStop(1, colors[3]);

	var gradientStrokeBottom = ctx.createLinearGradient(0, 0, 0, 600);
        gradientStrokeBottom.addColorStop(0, colors[7]);
        gradientStrokeBottom.addColorStop(1, colors[5]);

	var chartDataTem = {
  		labels: labels,
  
		datasets: [{
    			data: dataTem,
    			backgroundColor: gradientStrokeBottom,
    			borderColor: colors[5],
			fill: true,
    			borderWidth: 0,
			pointRadius: 0,
    			pointBackgroundColor: colors[1],
			borderJoinStyle: 'round',
  		}, {
                        data: dataTemMaxCnf,
			backgroundColor: gradientStroke,
                        borderColor: colors[3],
                        fill: false,
                        borderWidth: 1,
			borderDash: [10, 10],
                        pointRadius: 0,
                        pointBackgroundColor: colors[0],
                }, {
                        data: dataTemMinCnf,
                        backgroundColor: gradientStrokeBottom,
                        borderColor: colors[1],
                        fill: false, 
                        borderWidth: 1,
                        borderDash: [10, 10],
                        pointRadius: 0,
                        pointBackgroundColor: colors[0],
                }]
	};

        var chartDataHum = {
                labels: labels,

                datasets: [{
                        data: dataHum,
                        backgroundColor: gradientStrokeBottom,
                        borderColor: colors[5],
                        fill: true,
			pointRadius: 0,
                        borderWidth: 0,
                        pointBackgroundColor: colors[1],
			borderJoinStyle: 'round',
                }, {
                        data: dataHumMaxCnf,
                        backgroundColor: gradientStroke,
                        borderColor: colors[5],
                        fill: false,
                        borderWidth: 1,
                        borderDash: [10, 10],
                        pointRadius: 0,
                        pointBackgroundColor: colors[0],
                }, {
                        data: dataHumMinCnf,
                        backgroundColor: gradientStrokeBottom,
                        borderColor: colors[5],
                        fill: false,
                        borderWidth: 1,
                        borderDash: [10, 10],
                        pointRadius: 0,
                        pointBackgroundColor: colors[0],
                }]
        };

if (chLineTem) {
  new Chart(chLineTem, {
  type: 'line',
  data: chartDataTem,
  options: {
    responsive: true,

    scales: {
      yAxes: [{
        ticks: {
          display: true,
	  maxTicksLimit: 3,
	  padding: 3,
	  fontSize: 10,
	  fontColor: colors[6],
	  fontFamily: 'Quantico',
 	},
	gridLines: {
	 display: false,
	 drawBorder: false,
       	}
      }],
      xAxes: [{
        ticks: {
          display: false
        },
        gridLines: {
	 display: false
        }
      }]
    },
    legend: {
      display: false
    }
  }
  });
}

if (chLineHum) {
  new Chart(chLineHum, {
  type: 'line',
  data: chartDataHum,
  options: {
    responsive: true,

    scales: {
      yAxes: [{
        ticks: {
          display: true,
          maxTicksLimit: 3,
          padding: 3,
          fontSize: 10,
	  fontColor: colors[6],
	  fontFamily: 'Quantico',
        },
        gridLines: {
         display: false,
         drawBorder: false,
        }
      }],
      xAxes: [{
        ticks: {
          display: false
        },
        gridLines: {
         display: false
        }
      }]
    },
    legend: {
      display: false
    }
  }
  });
}

}
