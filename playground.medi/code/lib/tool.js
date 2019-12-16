var http = require('http');
var config = require('config');

module.exports.changeKoreantoUrl = function (userword) {
  var result = '';

  if (userword.indexOf('약') != -1) {
    result = 'pharmacy'
  }
  else if (userword.indexOf('응급') != -1) {
    result = 'emergency'
  }
  else if (userword.indexOf('어린이') != -1) {
    result = 'moonlight'
  }
  else if (userword.indexOf('소아') != -1) {
    result = 'child'
  }
  else if (userword.indexOf('심장') != -1) {
    result = 'AED'
  }
  else if (userword.indexOf('수유') != -1) {
    result = 'sooyusil'
  }
  else if (userword.indexOf('외과') != -1 && userword.indexOf('성형') == -1 && userword.indexOf('정형') == -1) {
    result = 'external'
  }
  else if (userword.indexOf('내과') != -1) {
    result = 'internal'
  }
  else if (userword.indexOf('치과') != -1) {
    result = 'dental'
  }
  else if (userword.indexOf('정형') != -1) {
    result = 'bone'
  }
  else if (userword.indexOf('이비') != -1) {
    result = 'nose'
  }
  else if (userword.indexOf('가정') != -1) {
    result = 'family'
  }
  else if (userword.indexOf('부인') != -1 || userword.indexOf('여성') != -1) {
    result = 'women'
  }
  else if (userword.indexOf('종합') != -1) {
    result = 'total'
  }
  else if (userword.indexOf('신경') != -1) {
    result = 'nerve'
  }
  else if (userword.indexOf('보건') != -1) {
    result = 'public_health'
  }
  else if (userword.indexOf('한의원') != -1) {
    result = 'oriental'
  }
  else if (userword.indexOf('신경') != -1) {
    result = 'nerve'
  }
  else if (userword.indexOf('항') != -1) {
    result = 'anal'
  }
  else if (userword.indexOf('피부') != -1) {
    result = 'skin'
  }
  else if (userword.indexOf('비뇨') != -1) {
    result = 'men'
  }
  else if (userword.indexOf('요양') != -1) {
    result = 'nursing'
  }
  else if (userword.indexOf('성형') != -1) {
    result = 'plastic'
  }
  else if (userword.indexOf('안과') != -1) {
    result = 'eye'
  }
  else if (userword.indexOf('정신') != -1) {
    result = 'nursing'
  }

  return result;
}


module.exports.weekdayToKorean = function (userword) {
  var result = '';

  if (userword.indexOf('월') != -1) {
    result = 1
  } else if (userword.indexOf('화') != -1) {
    result = 2
  } else if (userword.indexOf('수') != -1) {
    result = 3
  } else if (userword.indexOf('목') != -1) {
    result = 4
  } else if (userword.indexOf('금') != -1) {
    result = 5
  } else if (userword.indexOf('토') != -1) {
    result = 6
  } else {
    result = 7
  }

  return result
}