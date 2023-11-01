#!/usr/bin/node
const header = $("header");
$("#toggle_header").click(() => {
  header.toggleClass("red");
  header.toggleClass("green");
});
