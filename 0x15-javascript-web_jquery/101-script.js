#!/usr/bin/node

window.onload = function () {
  $("#add_item").click(() => {
    $("UL.my_list").append("<li>Item</li>");
  });

  $("#remove_item").click(() => {
    $("UL.my_list LI").last().remove();
  });

  $("#clear_list").click(() => {
    $("UL.my_list").empty();
  });
};
