var http = require('http');
var config = require('config');
var console = require('console');
var tool = require('lib/tool.js');


module.exports.function = function search_weekday ( destination, where ) {
  
  var findDay = tool.weekdayToKorean(weekday);
  var longt = destination.point.longitude
  var lat = destination.point.latitude

  var target = tool.changeKoreantoUrl(where);

  const response = http.getUrl('http://bixby-medi.herokuapp.com/api/' + target + '/search_nearest/', {
      format: 'json',
      query: {
        longtitude: longt,
        latitude: lat,
        curday: findDay,

        curtime: '10:00',
      }
    });

  let nearests = [];
  if (target == 'AED') {
    response.forEach(function(aed){
      let info = {
        'address': aed.address,
        'place': aed.place,
        'manager': aed.manager,
        'call': aed.call,
        'location': {
            'longitude': aed.longt,
            'latitude': aed.langt
          },
        'curlocation': curlocation
      }
      nearests.push(info);
    })
  } else if (target == 'sooyusil') {
    response.forEach(function(sooyu) {
      let info = {
        'name': sooyu.name,
        'address': sooyu.address,
        'call': sooyu.call,
        'location': {
          'longitude': sooyu.longt,
          'latitude': sooyu.langt
        },
        'curlocation': curlocation
      }
      nearests.push(info)
  })
  } else if (target == 'moonlight') {
      if (userday == 1) {
      response.forEach(function(moon) {
      if (moon.duty8 == 'true') {
      let info = {
      'name': moon.name,
      'address': moon.address,
      'call': moon.call,
      'open': moon.duty1_open,
      'close': moon.duty1_close,
      'holiday_open': moon.duty8_open,
      'holiday_close': moon.duty8_close,
      'location' : {
      'longitude': moon.longt,
      'latitude': moon.langt
      }
      }
      nearests.push(info)
      } else {
      let info = {
      'name': moon.name,
      'address': moon.address,
      'call': moon.call,
      'open': moon.duty1_open,
      'close': moon.duty1_close,
      'location' : {
      'longitude': moon.longt,
      'latitude': moon.langt
      }
      }
      nearests.push(info)
      } } )
      } else if (userday == 2) {
      response.forEach(function(moon) {
      if (moon.duty8 == 'true') {
      let info = {
      'name': moon.name,
      'address': moon.address,
      'call': moon.call,
      'open': moon.duty1_open,
      'close': moon.duty1_close,
      'holiday_open': moon.duty8_open,
      'holiday_close': moon.duty8_close,
      'location' : {
      'longitude': moon.longt,
      'latitude': moon.langt
      }
      }
      nearests.push(info)
      } else {
      let info = {
      'name': moon.name,
      'address': moon.address,
      'call': moon.call,
      'open': moon.duty1_open,
      'close': moon.duty1_close,
      'location' : {
      'longitude': moon.longt,
      'latitude': moon.langt
      }
      }
      nearests.push(info)
      } } )
      } else if (userday == 3) {
      response.forEach(function(moon) {
      if (moon.duty8 == 'true') {
      let info = {
      'name': moon.name,
      'address': moon.address,
      'call': moon.call,
      'open': moon.duty1_open,
      'close': moon.duty1_close,
      'holiday_open': moon.duty8_open,
      'holiday_close': moon.duty8_close,
      'location' : {
      'longitude': moon.longt,
      'latitude': moon.langt
      }
      }
      nearests.push(info)
      } else {
      let info = {
      'name': moon.name,
      'address': moon.address,
      'call': moon.call,
      'open': moon.duty1_open,
      'close': moon.duty1_close,
      'location' : {
      'longitude': moon.longt,
      'latitude': moon.langt
      }
      }
      nearests.push(info)
      } } )
      } else if (userday == 4) {
      response.forEach(function(moon) {
      if (moon.duty8 == 'true') {
      let info = {
      'name': moon.name,
      'address': moon.address,
      'call': moon.call,
      'open': moon.duty1_open,
      'close': moon.duty1_close,
      'holiday_open': moon.duty8_open,
      'holiday_close': moon.duty8_close,
      'location' : {
      'longitude': moon.longt,
      'latitude': moon.langt
      }
      }
      nearests.push(info)
      } else {
      let info = {
      'name': moon.name,
      'address': moon.address,
      'call': moon.call,
      'open': moon.duty1_open,
      'close': moon.duty1_close,
      'location' : {
      'longitude': moon.longt,
      'latitude': moon.langt
      }
      }
      nearests.push(info)
      } } )
      } else if (userday == 5) {
      response.forEach(function(moon) {
      if (moon.duty8 == 'true') {
      let info = {
      'name': moon.name,
      'address': moon.address,
      'call': moon.call,
      'open': moon.duty1_open,
      'close': moon.duty1_close,
      'holiday_open': moon.duty8_open,
      'holiday_close': moon.duty8_close,
      'location' : {
      'longitude': moon.longt,
      'latitude': moon.langt
      }
      }
      nearests.push(info)
      } else {
      let info = {
      'name': moon.name,
      'address': moon.address,
      'call': moon.call,
      'open': moon.duty1_open,
      'close': moon.duty1_close,
      'location' : {
      'longitude': moon.longt,
      'latitude': moon.langt
      }
      }
      nearests.push(info)
      } } )
      } else if (userday == 6) {
      response.forEach(function(moon) {
      if (moon.duty8 == 'true') {
      let info = {
      'name': moon.name,
      'address': moon.address,
      'call': moon.call,
      'open': moon.duty1_open,
      'close': moon.duty1_close,
      'holiday_open': moon.duty8_open,
      'holiday_close': moon.duty8_close,
      'location' : {
      'longitude': moon.longt,
      'latitude': moon.langt
      }
      }
      nearests.push(info)
      } else {
      let info = {
      'name': moon.name,
      'address': moon.address,
      'call': moon.call,
      'open': moon.duty1_open,
      'close': moon.duty1_close,
      'location' : {
      'longitude': moon.longt,
      'latitude': moon.langt
      }
      }
      nearests.push(info)
      } } )
      } else if (userday == 7) {
      response.forEach(function(moon) {
      if (moon.duty8 == 'true') {
      let info = {
      'name': moon.name,
      'address': moon.address,
      'call': moon.call,
      'open': moon.duty1_open,
      'close': moon.duty1_close,
      'holiday_open': moon.duty8_open,
      'holiday_close': moon.duty8_close,
      'location' : {
      'longitude': moon.longt,
      'latitude': moon.langt
      }
      }
      nearests.push(info)
      } else {
      let info = {
      'name': moon.name,
      'address': moon.address,
      'call': moon.call,
      'open': moon.duty1_open,
      'close': moon.duty1_close,
      'location' : {
      'longitude': moon.longt,
      'latitude': moon.langt
      }
      }
      nearests.push(info)
      } } ) }
      } else {
      if (userday == 1) {
      response.forEach(function(hospital) {
      if (hospital.duty8 == 'true') {
      let info = {
      'name': hospital.name,
      'address': hospital.address,
      'place': hospital.place,
      'call': hospital.call,
      'open': hospital.duty1_open,
      'close': hospital.duty1_close,
      'holiday_open': hospital.duty8_open,
      'holiday_close': hospital.duty8_close,
      'location' : {
      'longitude': hospital.longt,
      'latitude': hospital.langt
      }
      }
      nearests.push(info)
      } else {
      let info = {
      'name': hospital.name,
      'address': hospital.address,
      'place': hospital.place,
      'call': hospital.call,
      'open': hospital.duty1_open,
      'close': hospital.duty1_close,
      'location' : {
      'longitude': hospital.longt,
      'latitude': hospital.langt
      }
      }
      nearests.push(info)
      } } )
      } else if (userday == 2) {
      response.forEach(function(hospital) {
      if (hospital.duty8 == 'true') {
      let info = {
      'name': hospital.name,
      'address': hospital.address,
      'place': hospital.place,
      'call': hospital.call,
      'open': hospital.duty1_open,
      'close': hospital.duty1_close,
      'holiday_open': hospital.duty8_open,
      'holiday_close': hospital.duty8_close,
      'location' : {
      'longitude': hospital.longt,
      'latitude': hospital.langt
      }
      }
      nearests.push(info)
      } else {
      let info = {
      'name': hospital.name,
      'address': hospital.address,
      'place': hospital.place,
      'call': hospital.call,
      'open': hospital.duty1_open,
      'close': hospital.duty1_close,
      'location' : {
      'longitude': hospital.longt,
      'latitude': hospital.langt
      }
      }
      nearests.push(info)
      } } )
      } else if (userday == 3) {
      response.forEach(function(hospital) {
      if (hospital.duty8 == 'true') {
      let info = {
      'name': hospital.name,
      'address': hospital.address,
      'place': hospital.place,
      'call': hospital.call,
      'open': hospital.duty1_open,
      'close': hospital.duty1_close,
      'holiday_open': hospital.duty8_open,
      'holiday_close': hospital.duty8_close,
      'location' : {
      'longitude': hospital.longt,
      'latitude': hospital.langt
      }
      }
      nearests.push(info)
      } else {
      let info = {
      'name': hospital.name,
      'address': hospital.address,
      'place': hospital.place,
      'call': hospital.call,
      'open': hospital.duty1_open,
      'close': hospital.duty1_close,
      'location' : {
      'longitude': hospital.longt,
      'latitude': hospital.langt
      }
      }
      nearests.push(info)
      } } )
      } else if (userday == 4) {
      response.forEach(function(hospital) {
      if (hospital.duty8 == 'true') {
      let info = {
      'name': hospital.name,
      'address': hospital.address,
      'place': hospital.place,
      'call': hospital.call,
      'open': hospital.duty1_open,
      'close': hospital.duty1_close,
      'holiday_open': hospital.duty8_open,
      'holiday_close': hospital.duty8_close,
      'location' : {
      'longitude': hospital.longt,
      'latitude': hospital.langt
      }
      }
      nearests.push(info)
      } else {
      let info = {
      'name': hospital.name,
      'address': hospital.address,
      'place': hospital.place,
      'call': hospital.call,
      'open': hospital.duty1_open,
      'close': hospital.duty1_close,
      'location' : {
      'longitude': hospital.longt,
      'latitude': hospital.langt
      }
      }
      nearests.push(info)
      } } )
      } else if (userday == 5) {
      response.forEach(function(hospital) {
      if (hospital.duty8 == 'true') {
      let info = {
      'name': hospital.name,
      'address': hospital.address,
      'place': hospital.place,
      'call': hospital.call,
      'open': hospital.duty1_open,
      'close': hospital.duty1_close,
      'holiday_open': hospital.duty8_open,
      'holiday_close': hospital.duty8_close,
      'location' : {
      'longitude': hospital.longt,
      'latitude': hospital.langt
      }
      }
      nearests.push(info)
      } else {
      let info = {
      'name': hospital.name,
      'address': hospital.address,
      'place': hospital.place,
      'call': hospital.call,
      'open': hospital.duty1_open,
      'close': hospital.duty1_close,
      'location' : {
      'longitude': hospital.longt,
      'latitude': hospital.langt
      }
      }
      nearests.push(info)
      } } )
      } else if (userday == 6) {
      response.forEach(function(hospital) {
      if (hospital.duty8 == 'true') {
      let info = {
      'name': hospital.name,
      'address': hospital.address,
      'place': hospital.place,
      'call': hospital.call,
      'open': hospital.duty1_open,
      'close': hospital.duty1_close,
      'holiday_open': hospital.duty8_open,
      'holiday_close': hospital.duty8_close,
      'location' : {
      'longitude': hospital.longt,
      'latitude': hospital.langt
      }
      }
      nearests.push(info)
      } else {
      let info = {
      'name': hospital.name,
      'address': hospital.address,
      'place': hospital.place,
      'call': hospital.call,
      'open': hospital.duty1_open,
      'close': hospital.duty1_close,
      'location' : {
      'longitude': hospital.longt,
      'latitude': hospital.langt
      }
      }
      nearests.push(info)
      } } )
      } else if (userday == 7) {
      response.forEach(function(hospital) {
      if (hospital.duty8 == 'true') {
      let info = {
      'name': hospital.name,
      'address': hospital.address,
      'place': hospital.place,
      'call': hospital.call,
      'open': hospital.duty1_open,
      'close': hospital.duty1_close,
      'holiday_open': hospital.duty8_open,
      'holiday_close': hospital.duty8_close,
      'location' : {
      'longitude': hospital.longt,
      'latitude': hospital.langt
      }
      }
      nearests.push(info)
      } else {
      let info = {
      'name': hospital.name,
      'address': hospital.address,
      'place': hospital.place,
      'call': hospital.call,
      'open': hospital.duty1_open,
      'close': hospital.duty1_close,
      'location' : {
      'longitude': hospital.longt,
      'latitude': hospital.langt
      }
      }
      nearests.push(info)
      } } )
      }}
  return nearests;
}