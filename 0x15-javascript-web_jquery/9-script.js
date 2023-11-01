#!/usr/bin/node

$.ajax({
  type: "GET",
  url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
  success: (translation) => {
    $("#hello").text(translation.hello);
  },
});
