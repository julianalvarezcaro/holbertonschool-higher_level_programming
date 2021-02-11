#!/usr/bin/node

const $ = window.$;
const element = $('header');

$('#toggle_header').click(function () {
  if (element.hasClass('green')) {
    element.addClass('red');
    element.removeClass('green');
  } else {
    element.addClass('green');
    element.removeClass('red');
  }
});
