document.addEventListener('DOMContentLoaded', function() {
Highcharts.chart('correlation_heatmap_count',
{
  chart: {
  margin: [40,
null,
80,
null],
  marginBottom: 80,
  marginTop: 40,
  type: 'heatmap'
},
  colorAxis: {
  max: 233.0,
  min: 0,
  reversed: false,
  maxColor: '#00C1FF',
  minColor: '#FFFFFF'
},
  legend: {
  align: 'right',
  layout: 'vertical',
  margin: 0,
  symbolHeight: 280,
  verticalAlign: 'top',
  y: 25
},
  series: [{
  data: [{
  value: 232.0,
  x: 0,
  y: 0
},
{
  value: 232.0,
  x: 0,
  y: 1
},
{
  value: 231.0,
  x: 0,
  y: 2
},
{
  value: 232.0,
  x: 0,
  y: 3
},
{
  value: 232.0,
  x: 1,
  y: 0
},
{
  value: 233.0,
  x: 1,
  y: 1
},
{
  value: 232.0,
  x: 1,
  y: 2
},
{
  value: 233.0,
  x: 1,
  y: 3
},
{
  value: 231.0,
  x: 2,
  y: 0
},
{
  value: 232.0,
  x: 2,
  y: 1
},
{
  value: 232.0,
  x: 2,
  y: 2
},
{
  value: 232.0,
  x: 2,
  y: 3
},
{
  value: 232.0,
  x: 3,
  y: 0
},
{
  value: 233.0,
  x: 3,
  y: 1
},
{
  value: 232.0,
  x: 3,
  y: 2
},
{
  value: 233.0,
  x: 3,
  y: 3
}],
  name: 'Correlation',
  dataLabels: {
  enabled: true
},
  type: 'heatmap'
}],
  title: {
  text: 'Correlation count matrix'
},
  xAxis: {
  categories: ['PFOS',
'PFHxS',
'PFNA',
'PFOA'],
  title: {
  text: 'Parameter'
}
},
  yAxis: {
  categories: ['PFOS',
'PFHxS',
'PFNA',
'PFOA'],
  reversed: true,
  title: {
  text: 'Parameter'
}
}
},
);
});