var barcode = document.getElementById('barcode');

barcode.onmousedown = function(e) {

var coords = getCoords(barcode);
  var shiftX = e.pageX - coords.left;
  var shiftY = e.pageY - coords.top;

  barcode.style.position = 'absolute';
  document.body.appendChild(barcode);
  moveAt(e);

  barcode.style.zIndex = 1000;

  function moveAt(e) {
    barcode.style.left = e.pageX - shiftX + 'px';
    barcode.style.top = e.pageY - shiftY + 'px';
  }

  // 3, перемещать по экрану
  document.onmousemove = function(e) {
    moveAt(e);
  }
  document.onmouseup = function(){
    document.onmousemove = null;
    barcode.onmouseup = null;
  }

  function getCoords(elem) {   // кроме IE8-
  var box = elem.getBoundingClientRect();
  return {
    top: box.top + pageYOffset,
    left: box.left + pageXOffset
  };
}

  // 4. отследить окончание переноса
  barcode.onmouseup = function() {
    document.onmousemove = null;
    barcode.onmouseup = null;
  }
  barcode.ondragstart = function() {
  return false;
};
}

var place = document.getElementById('place');

place.onmousedown = function(e) {

var coords = getCoords(place);
  var shiftX = e.pageX - coords.left;
  var shiftY = e.pageY - coords.top;

  place.style.position = 'absolute';
  document.body.appendChild(place);
  moveAt(e);

  place.style.zIndex = 1000;

  function moveAt(e) {
    place.style.left = e.pageX - shiftX + 'px';
    place.style.top = e.pageY - shiftY + 'px';
  }

  // 3, перемещать по экрану
  document.onmousemove = function(e) {
    moveAt(e);
  }
  document.onmouseup = function(){
    document.onmousemove = null;
    place.onmouseup = null;
  }

  function getCoords(elem) {   // кроме IE8-
  var box = elem.getBoundingClientRect();
  return {
    top: box.top + pageYOffset,
    left: box.left + pageXOffset
  };
}

  // 4. отследить окончание переноса
  place.onmouseup = function() {
    document.onmousemove = null;
    place.onmouseup = null;
  }
  place.ondragstart = function() {
  return false;
};
}

var row = document.getElementById('row');

row.onmousedown = function(e) {

var coords = getCoords(row);
  var shiftX = e.pageX - coords.left;
  var shiftY = e.pageY - coords.top;

  row.style.position = 'absolute';
  document.body.appendChild(row);
  moveAt(e);

  row.style.zIndex = 1000;

  function moveAt(e) {
    row.style.left = e.pageX - shiftX + 'px';
    row.style.top = e.pageY - shiftY + 'px';
  }

  // 3, перемещать по экрану
  document.onmousemove = function(e) {
    moveAt(e);
  }
  document.onmouseup = function(){
    document.onmousemove = null;
    row.onmouseup = null;
  }

  function getCoords(elem) {   // кроме IE8-
  var box = elem.getBoundingClientRect();
  return {
    top: box.top + pageYOffset,
    left: box.left + pageXOffset
  };
}

  // 4. отследить окончание переноса
  row.onmouseup = function() {
    document.onmousemove = null;
    row.onmouseup = null;
  }
  row.ondragstart = function() {
  return false;
};
}


var price = document.getElementById('price');

price.onmousedown = function(e) {

var coords = getCoords(price);
  var shiftX = e.pageX - coords.left;
  var shiftY = e.pageY - coords.top;

  price.style.position = 'absolute';
  document.body.appendChild(price);
  moveAt(e);

  price.style.zIndex = 1000;

  function moveAt(e) {
    price.style.left = e.pageX - shiftX + 'px';
    price.style.top = e.pageY - shiftY + 'px';
  }

  // 3, перемещать по экрану
  document.onmousemove = function(e) {
    moveAt(e);
  }
  document.onmouseup = function(){
    document.onmousemove = null;
    price.onmouseup = null;
  }

  function getCoords(elem) {   // кроме IE8-
  var box = elem.getBoundingClientRect();
  return {
    top: box.top + pageYOffset,
    left: box.left + pageXOffset
  };
}

  // 4. отследить окончание переноса
  price.onmouseup = function() {
    document.onmousemove = null;
    price.onmouseup = null;
  }
  price.ondragstart = function() {
  return false;
};
}

