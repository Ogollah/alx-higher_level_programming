#!/usr/bin/node

function postLanguage() {
  const lang = $("#language_code").val();
  $.ajax({
    type: "GET",
    url: "https://www.fourtonfish.com/hellosalut/hello/?lang=" + lang,
    success: (translation) => {
      $("#hello").text(translation.hello);
    },
  });
}

window.onload = () => {
  $("#btn_translate").focus(() => {
    $("#btn_translate").keypress((key) => {
      if (key.which === 13) {
        postLang();
      }
    });
    $("#btn_translate").click(() => {
      postLanguage();
    });
  });
};
