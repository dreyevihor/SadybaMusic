new Vue({
  el: '#ttt',
  data: {
    show: false,
    min_date: null,
    max_date: null,
    place: null,
    events: [],
    indents: [],
    zoom_img: '',
    places: []

  },

  created: function(){
  	vm = this
	  	axios.get('/api/afisha/').then(function(response){
	 			vm.events =response.data
	 		});

  },

  watch:{
  	events: function(val){
  		steps = this.events.length - this.indents.length
  		if (steps > 0) {
	  		for (var i = this.indents.length; i < this.events.length; i++) {
	  			this.indents[i] = this.getStyle()
	  		}

	  	} else if(steps < 0){
	  		this.indents = this.indents.slice(Math.abs(steps))
	  	}
	  	
  	}

  },
  computed:{
  	crutch: function(){
  		vm = this
	  	axios.get('/api/afisha/', {
	  		params: {
	  			place: vm.place,
	  			min_date: vm.min_date,
	  			max_date: vm.max_date
	  			}
	 		}).then(function(response){
	 			vm.events =response.data
	 		});	 		
  		}
  },

  
  methods:{
  	getStyle: function(){
  		return {'left': 'calc(' + Math.random()*400 +'px)' };
  	}



  },
  delimiters: ["[[","]]"]
});