new Vue({
  el: "#app",
  data: {
    message: "Related pics demo",
    imageInput: ""
  }
});

function getImageRawData(url) {
  //Option with catch
  fetch(`https://related-pics.herokuapp.com/?url=${url}`)
    //.then(async r => jsonApiResponce = JSON.parse(r.text()))
    .then(async r => console.log(await r.text()))
    .catch(e => console.error("Boo..." + e));

  //No fear...
  (async () => console.log(await await fetch(url)))();
}

//getImageRawData("https://images.pexels.com/photos/3683191/pexels-photo-3683191.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260");

function formAction(data) {
  testImage(data.children[0].value).then(result => {
    if (result == "success") getImageRawData(data.children[0].value);
  });
}

function testImage(url, timeoutT) {
  return new Promise(function(resolve, reject) {
    var timeout = timeoutT || 5000;
    var timer,
      img = new Image();
    img.onerror = img.onabort = function() {
      clearTimeout(timer);
      reject("error");
    };
    img.onload = function() {
      clearTimeout(timer);
      resolve("success");
    };
    timer = setTimeout(function() {
      // reset .src to invalid URL so it stops previous
      // loading, but doens't trigger new load
      img.src = "//!!!!/noexist.jpg";
      reject("timeout");
    }, timeout);
    img.src = url;
  });
}
