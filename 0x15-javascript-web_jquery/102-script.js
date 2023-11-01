#!/usr/bin/node

window.onload = () => {
  $("#btn_translate").click(() => {
    const lang = $("#language_code").val();
    $.ajax({
      type: "GET",
      url: "https://www.fourtonfish.com/hellosalut/hello/?lang=" + lang,
      success: (translation) => {
        $("#hello").text(translation.hello);
      },
    });
  });
};
