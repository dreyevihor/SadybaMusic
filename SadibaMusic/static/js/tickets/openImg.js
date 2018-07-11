var vm1 = new Vue({
  el: '#img',
  data: {
    image: '',
  },
  methods: {
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length)
        return;
      this.createImage(files[0]);
      console.log(this.image)
    },
    createImage(file) {
      var image = new Image();
      var reader = new FileReader();
      var vm = this;

      reader.onload = (e) => {
        vm.image = e.target.result;
        console.log(vm.image)
      };
      reader.readAsDataURL(file);
    },
    removeImage: function (e) {
      this.image = '';
    }
  },
  watch:{
    image: function(){
      vm2.image = this.image
    }
  },
});

var vm2 = new Vue({
 el: '#app',
 data:{
  image:'',
  rotatePrice: false,
  rotateRow: false,
  rotatePlace: false,
  rotateBarcode: false,
 },
 methods: {
    click: function(){
        self = this
        var spineBarcode = document.getElementById('barcode').firstElementChild;
        spineBarcode.onmousedown = function(e){
          self.rotateBarcode = !self.rotateBarcode
        }

        var spineRow = document.getElementById('row').firstElementChild;
        spineRow.onmousedown = function(e){
          self.rotateRow = !self.rotateRow
        }

        var spinePlace = document.getElementById('place').firstElementChild;
        spinePlace.onmousedown = function(e){
          self.rotatePlace = !self.rotatePlace
        }

        var spinePrice = document.getElementById('price').firstElementChild;
        spinePrice.onmousedown = function(e){
          self.rotatePrice = !self.rotatePrice
        }



        var barcode = document.getElementById('barcode');

        barcode.onmousedown = function(e) {
          barcode.style.width = barcode.getBoundingClientRect().height + 'px';
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
            barcode.style.width = barcode.getBoundingClientRect().height + 'px';

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


        var template = document.getElementById('template');

        template.onmousedown = function(e) {

        var coords = getCoords(template);
          var shiftX = e.pageX - coords.left;
          var shiftY = e.pageY - coords.top;

          template.style.position = 'absolute';
          document.body.appendChild(template);
          moveAt(e);

          template.style.zIndex = 1000;

          function moveAt(e) {
            template.style.left = e.pageX - shiftX + 'px';
            template.style.top = e.pageY - shiftY + 'px';
          }

          // 3, перемещать по экрану
          document.onmousemove = function(e) {
            moveAt(e);
          }
          document.onmouseup = function(){
            document.onmousemove = null;
            template.onmouseup = null;
          }

          function getCoords(elem) {   // кроме IE8-
          var box = elem.getBoundingClientRect();
          return {
            top: box.top + pageYOffset,
            left: box.left + pageXOffset
          };
        }

          // 4. отследить окончание переноса
          template.onmouseup = function() {
            document.onmousemove = null;
            template.onmouseup = null;
          }
          template.ondragstart = function() {
          return false;
        };
        }


  },
 },
 created: function(){
    window.addEventListener('click', this.click);
 },
  destroyed: function () {
      window.removeEventListener('click', this.click);
  },
});

var vm3 = new Vue({
  el: '#submit',
  data: {
    rowData: '',
    priceData: '',
    placeData: '',
    barcodeData: '',
    ticketData:'',
    token: '',
  },
  methods: {
    submit: function(){
      var row = document.getElementById('row').getBoundingClientRect();
      var price = document.getElementById('price').getBoundingClientRect();
      var place = document.getElementById('place').getBoundingClientRect();
      var barcode = document.getElementById('barcode').getBoundingClientRect();
      var ticket = document.getElementById('template').getBoundingClientRect();
      this.rowData = {
        "isRotated": vm2.rotateRow,
        "left": (row.left - ticket.left)/ticket.width,
        top: (row.top - ticket.top)/ticket.height
      };
      this.priceData = {
        "isRotated": vm2.rotatePrice,
        "left": (price.left - ticket.left)/ticket.width,
        "top": (price.top - ticket.top)/ticket.height
      };
      this.placeData = {
        "isRotated": vm2.rotatePlace,
        "left": (place.left - ticket.left)/ticket.width,
        "top": (place.top - ticket.top)/ticket.height
      };
      this.barcodeData = {
        isRotated: vm2.rotateBarcode,
        left: (barcode.left - ticket.left)/ticket.width,
        top: (barcode.top - ticket.top)/ticket.height,
        width: barcode.width/ticket.width,
        height: barcode.height/ticket.height
      };
      if(this.barcodeData.left + this.barcodeData.width > 0 && this.barcodeData.left + this.barcodeData.width<1
         && this.rowData.left > 0 && this.rowData.left<1
         && this.placeData.left > 0 && this.placeData.left<1
         && this.priceData.left > 0 && this.priceData.left<1
         && this.barcodeData.top + this.barcodeData.height > 0 && this.barcodeData.top + this.barcodeData.height<1
         && this.rowData.top > 0 && this.rowData.top<1
         && this.placeData.top > 0 && this.placeData.top<1
         && this.priceData.top > 0 && this.priceData.top<1
         ){
          
        vm3.token = Cookies.get('csrftoken');
        var fb = new FormData();

        fb.append('image', vm1.image);
        fb.append('barcode', JSON.stringify(this.barcodeData));
        fb.append('row', JSON.stringify(this.rowData));
        fb.append('place', JSON.stringify(this.placeData));
        fb.append('price', JSON.stringify(this.priceData));
        headers = {"X-CSRFToken": vm3.token,
                   "content-type": "multipart/form-data"};
        axios({method: 'post',
                url: '/tickets/ticketSchema/',
                data: fb,
                headers: headers
        });
    
    }
          
    }

  },

})
