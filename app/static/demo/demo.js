
type = ['primary', 'info', 'danger','success', 'warning' ]


analysisPlots = {

  
  initDocChart: function(){

        chartColor = '#FFFFFF';

        //This the general configuration for the Charts with Line Gradient Strokes

        gradientChartOptionsConfiguration = {
            maintainAspectRatio: false,
            legend: {
              display: false
            },
            tooltips: {
              bodySpacing: 4,
              mode: "nearest",
              intersect: 0,
              position: "nearest",
              xPadding: 10,
              yPadding: 10,
              caretPadding: 10
            },
            responsive: true,
            scales: {
              yAxes: [{
                display: 0,
                gridLines: 0,
                ticks: {
                  display: false
                },
                gridLines: {
                  zeroLineColor: "transparent",
                  drawTicks: false,
                  display: false,
                  drawBorder: false
                }
              }],
              xAxes: [{
                display: 0,
                gridLines: 0,
                ticks: {
                  display: false
                },
                gridLines: {
                  zeroLineColor: "transparent",
                  drawTicks: false,
                  display: false,
                  drawBorder: false
                }
              }]
            },
            layout: {
              padding: {
                left: 0,
                right: 0,
                top: 15,
                bottom: 15
              }
            }
        };


        ctx = document.getElementById('linechartExmaple').getContext('2d');

        gradientStroke = ctx.createLinearGradient(500, 0, 100, 0);
        gradientStroke.addColorStop(0, '#80b6f4');
        gradientStroke.addColorStop(1, chartColor);

        gradientFill = ctx.createLinearGradient(0, 170, 0, 50);
        gradientFill.addColorStop(0, "rgba(128, 182, 244, 0)");
        gradientFill.addColorStop(1, "rgba(249, 99, 59, 0.40)");

        myChart = new Chart(ctx, {
            type: 'line',
            responsive: true,
            data: {
              labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
              datasets: [{
                label: "Active Users",
                borderColor: "#f96332",
                pointBorderColor: "#FFF",
                pointBackgroundColor: "#f96332",
                pointBorderWidth: 2,
                pointHoverRadius: 4,
                pointHoverBorderWidth: 1,
                pointRadius: 4,
                fill: true,
                backgroundColor: gradientFill,
                borderWidth: 2,
                data: [542, 480, 430, 550, 530, 453, 380, 434, 568, 610, 700, 630]
              }]
            },
            options: gradientChartOptionsConfiguration
        });

        //same chart but another way of drawing it
        var data ={
            labels: ['JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
            datasets: [{
              label: "Data",
              fill: true,
              backgroundColor: gradientStroke,
              borderColor: '#d048b6',
              borderWidth: 2,
              borderDash: [],
              borderDashOffset: 0.0,
              pointBackgroundColor: '#d048b6',
              pointBorderColor: 'rgba(255,255,255,0)',
              pointHoverBackgroundColor: '#d048b6',
              pointBorderWidth: 20,
              pointHoverRadius: 4,
              pointHoverBorderWidth: 15,
              pointRadius: 4,
              data: [80, 100, 70, 80, 120, 80],
            }]      
        };

        var mychart = new Chart(ctx, {
            type:'line',
            data:data,
            options:gradientChartOptionsConfiguration
        })
    },


    initDashboardPageCharts: function() {

        gradientChartOptionsConfigurationWithTooltipBlue = {
          maintainAspectRatio: false,
          legend: {
            display: false
          },
    
          tooltips: {
            backgroundColor: '#f5f5f5',
            titleFontColor: '#333',
            bodyFontColor: '#666',
            bodySpacing: 4,
            xPadding: 12,
            mode: "nearest",
            intersect: 0,
            position: "nearest"
          },
          responsive: true,
          scales: {
            yAxes: [{
              barPercentage: 1.6,
              gridLines: {
                drawBorder: false,
                color: 'rgba(29,140,248,0.0)',
                zeroLineColor: "transparent",
              },
              ticks: {
                suggestedMin: 60,
                suggestedMax: 125,
                padding: 20,
                fontColor: "#2380f7"
              }
            }],
    
            xAxes: [{
              barPercentage: 1.6,
              gridLines: {
                drawBorder: false,
                color: 'rgba(29,140,248,0.1)',
                zeroLineColor: "transparent",
              },
              ticks: {
                padding: 20,
                fontColor: "#2380f7"
              }
            }]
          }
        };
    
        gradientBarChartConfiguration = {
          maintainAspectRatio: false,
          legend: {
            display: false
          },
    
          tooltips: {
            backgroundColor: '#f5f5f5',
            titleFontColor: '#333',
            bodyFontColor: '#666',
            bodySpacing: 4,
            xPadding: 12,
            mode: "nearest",
            intersect: 0,
            position: "nearest"
          },
          responsive: true,
          scales: {
            yAxes: [{
    
              gridLines: {
                drawBorder: false,
                color: 'rgba(29,140,248,0.1)',
                zeroLineColor: "transparent",
              },
              ticks: {
                suggestedMin: -0.01,
                suggestedMax: 1,
                padding: 20,
                fontColor: "#9e9e9e"
              }
            }],
    
            xAxes: [{
    
              gridLines: {
                drawBorder: false,
                color: 'rgba(29,140,248,0.1)',
                zeroLineColor: "transparent",
              },
              ticks: {
                padding: 20,
                fontColor: "#9e9e9e"
              }
            }]
          }
        };
        
        var chart_labels = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'];
        var chart_data = [100, 70, 90, 70, 85, 60, 75, 60, 90, 80, 110, 100];

        var char = document.getElementById("CountryChart").getContext("2d");

        var gradientStroke = char.createLinearGradient(0, 230, 0, 50);

        gradientStroke.addColorStop(1, 'rgba(29,140,248,0.2)');
        gradientStroke.addColorStop(0.4, 'rgba(29,140,248,0.0)');
        gradientStroke.addColorStop(0, 'rgba(29,140,248,0)'); //blue colors


        var myChartBar = new Chart(char, {
         type: 'bar',
         responsive: true,
         legend: {
           display: false
         },
         data: {
           labels: chart_labels,
           datasets: [{
             label: "Countries",
             fill: true,
             backgroundColor: gradientStroke,
             hoverBackgroundColor: gradientStroke,
             borderColor: '#1f8ef1',
             borderWidth: 2,
             borderDash: [],
             borderDashOffset: 0.0,
             data:chart_data,
           }]
         },
         options: gradientBarChartConfiguration
         });
    
        var ctx = document.getElementById("chartBig1").getContext('2d');
    
        var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);
    
        gradientStroke.addColorStop(1, 'rgba(72,72,176,0.1)');
        gradientStroke.addColorStop(0.4, 'rgba(72,72,176,0.0)');
        gradientStroke.addColorStop(0, 'rgba(119,52,169,0)'); //purple colors
        var config = {
          type: 'line',
          data: {
            labels: chart_labels,
            datasets: [{
              label: "Data Points",
              fill: true,
              backgroundColor: gradientStroke,
              borderColor: '#d346b1',
              borderWidth: 2,
              borderDash: [],
              borderDashOffset: 0.0,
              pointBackgroundColor: '#d346b1',
              pointBorderColor: 'rgba(255,255,255,0)',
              pointHoverBackgroundColor: '#d346b1',
              pointBorderWidth: 20,
              pointHoverRadius: 4,
              pointHoverBorderWidth: 15,
              pointRadius: 4,
              data: chart_data,
            }]
          },
          options: gradientChartOptionsConfigurationWithTooltipBlue
        };
        var myChartData = new Chart(ctx, config);

        $("#0").click(function() {
          var data = myChartData.config.data;
          data.datasets[0].data = chart_data;
          data.labels = chart_labels;
          myChartData.update();

          var BarData = myChartBar.data;
          BarData.datasets[0].data = chart_data;
          BarData.labels =chart_labels;
          myChartBar.update();
        });
        // Specific ajax for the get tweets
        $('#DemoSearchButton').click(function () {

          $.ajax({
            url: "demo/demo_tweets",

            type: "POST",

            data: { 
              query: $('#DemoFormInputGroup').val()
              
            },
            beforeSend:function(){

              //$('#searchBtn').attr('disabled', 'disabled');

              $('#process').css('display', 'block');
              $('#progbar').attr('style', 'width: 20%')
              $('#progbar').attr('aria-valuenow', '20');
              
            },
            success: function(response){

              //FOR THE PROGRESS BAR
              var percentage = 0;
              var timer = setInterval(function(){
              percentage = percentage + 20;

              progress_bar_process(percentage, timer, response);

              }, 1000);
            
              //--------------------------------//
             
            }
          });
          //Progress bar function
          function progress_bar_process(percentage, timer, response){
            $('.progress-bar').css('width', percentage + '%');
            if(percentage > 100){
                clearInterval(timer);
                $('#process').css('display', 'none');
                $('.progress-bar').css('width', '0%');
                //$('#save').attr('disabled', false);
                //$('#success_message').html(data);

               /* setTimeout(function(){
                    $('#success_message').html('');
                }, 5000) */

                //Plotting values
                const date = response.date //access the date object of the response
                const sentiments = response.sentiment_polarity //access the sentiment polarity object of the response
                const location = response.user_location //access the user location object of the response

                var chart_labels = Object.values(date) //access the values of the objects

                var chart_data = Object.values(sentiments)

                var chart_labels_bar = Object.values(location)

                //updating the linegraph

                var data = myChartData.config.data;

                data.datasets[0].data=chart_data;

                data.labels = chart_labels;

                myChartData.update();

                //updating the bar chart
                var BarData = myChartBar.data;
                BarData.labels = chart_labels_bar;
                BarData.datasets[0].data = chart_data;
                myChartBar.update();
            }

        }
      });    
    },
};    
