var vm = new Vue({
  el: '#ttt',

  data: {
    slides: false,
    events: []
  },
  created: function(){
  	var self = this
	  	axios.get('/api/afisha/').then(function(response){
	 			self.events = response.data
        self.update()

	 		});

  },
  methods:{
    update: function(){
      var self = this
      self.slides = false
      setTimeout(self.slides = true, 200)
    }
  },

  components: {
    'carousel-3d': Carousel3d.Carousel3d,
    'slide': Carousel3d.Slide
  },
  delimiters: ["[[","]]"]
});
