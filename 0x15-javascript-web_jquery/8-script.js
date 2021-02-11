#!/usr/bin/node

const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.get(url, function (data, textStatus) {
  for (const film of data.results) {
    $('#list_movies').append(`<li>${film.title}</li>`);
  }
});
