document.addEventListener('DOMContentLoaded', function() {
Highcharts.chart('correlation_heatmap',
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
  max: 1,
  min: 0,
  reversed: false,
  maxColor: '#f8902d',
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
  value: 1.0,
  x: 0,
  y: 0,
  name: '232'
},
{
  value: 0.2,
  x: 0,
  y: 1,
  name: '232'
},
{
  value: 0.33,
  x: 0,
  y: 2,
  name: '231'
},
{
  value: 0.37,
  x: 0,
  y: 3,
  name: '232'
},
{
  value: 0.2,
  x: 1,
  y: 0,
  name: '232'
},
{
  value: 1.0,
  x: 1,
  y: 1,
  name: '233'
},
{
  value: 0.06,
  x: 1,
  y: 2,
  name: '232'
},
{
  value: 0.6,
  x: 1,
  y: 3,
  name: '233'
},
{
  value: 0.33,
  x: 2,
  y: 0,
  name: '231'
},
{
  value: 0.06,
  x: 2,
  y: 1,
  name: '232'
},
{
  value: 1.0,
  x: 2,
  y: 2,
  name: '232'
},
{
  value: 0.18,
  x: 2,
  y: 3,
  name: '232'
},
{
  value: 0.37,
  x: 3,
  y: 0,
  name: '232'
},
{
  value: 0.6,
  x: 3,
  y: 1,
  name: '233'
},
{
  value: 0.18,
  x: 3,
  y: 2,
  name: '232'
},
{
  value: 1.0,
  x: 3,
  y: 3,
  name: '233'
}],
  name: 'Correlation',
  dataLabels: [{
  enabled: true,
  format: '{point.value:,.2f} <br> ({point.options.name})'
}],
  type: 'heatmap'
}],
  title: {
  text: 'Correlation matrix'
},
  tooltip: {
  formatter: function() {
return this.series.xAxis.categories[this.point.x] + " - " + this.series.yAxis.categories[this.point.y] + "<br> Correlation : " + Highcharts.numberFormat(this.point.value,2) + "<br> Count : " + this.point.options.name}
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