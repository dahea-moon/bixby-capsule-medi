var http = require('http');
var config = require('config');
var dates = require('dates');
var tool = require('lib/tool.js');


module.exports.function = function searchBasedDestination (destination, dateTimeExpression, where) {
  var curtime = new dates.ZonedDateTime.now();
  var userday = curtime.getDayOfWeek();
  var usertime = dateTimeExpression.dateTime.time.hour;
  var usermin = dateTimeExpression.dateTime.time.minute;
  if (usermin < 10) {
    var usermin = '0' + usermin

  var longt = destination.point.longitude
  var lat = destination.point.latitude

  var target = tool.changeKoreantoUrl(where);

  const response = http.getUrl('http://bixby-medi.herokuapp.com/api/' + target + '/search_nearest/', {
      format: 'json',
      query: {
        longtitude: longt,
        latitude: lat,
        curday: userday,
        curtime: usertime + ':' + usermin,        
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
        }
      }
      nearests.push(info)
  })
  } else if (target == 'moonlight') {
      var openduty = 'duty' + userday + '_open'; 
      var closeduty = 'duty' + userday + '_close';
      response.forEach(function(moon) {
      if (moon.duty8 == 'true') {
        let info = {
          'name': moon.name,
          'address': moon.address,
          'call': moon.call,
          'open': moon.openduty,
          'close': moon.closeduty,
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
      'open': moon.openduty,
      'close': moon.closeduty,
      'location' : {
        'longitude': moon.longt,
        'latitude': moon.langt
      }
        }
      nearests.push(info)
      }
      })
    } else {
      var openduty = 'duty' + userday + '_open'; 
      var closeduty = 'duty' + userday + '_close';
      response.forEach(function(hospital) {
        if (hospital.duty8 == 'true') {
          let info = {
            'name': hospital.name,
            'address': hospital.address,
            'call': hospital.call,
            'open': hospital.openduty,
            'close': hospital.closeduty,
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
          'call': hospital.call,
          'open': hospital.openduty,
          'close': hospital.closeduty,
          'location' : {
            'longitude': hospital.longt,
            'latitude': hospital.langt
          }
        }
        nearests.push(info)
      }
      })
    }
  return nearests;
}
}