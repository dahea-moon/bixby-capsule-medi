var http = require('http');
var config = require('config');
var dates = require('dates');
var datetime = new dates.ZonedDateTime.now().getDateTime();
var tool = require('tool.js');

module.exports.function = function search_nearest (curlocation, datetime, where) {
  var response = http.getUrl(config.get('local.url') + where + '/', {
      format: 'json',
      query: {
        userlongt: curlocation.longtitude,
        userlangt: curlocation.langtitude,
        usertime: datetime,
      }
    })
  
  var hospitals = [];
  for (var hospital of response) {
    hospitals.push({
      "이름": hospital.name,
      "주소": hospital.address,
    })
  }
  return hospitals;
