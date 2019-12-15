var http = require('http');
var config = require('config');

module.exports.changeKoreantoUrl = function (userword) {
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