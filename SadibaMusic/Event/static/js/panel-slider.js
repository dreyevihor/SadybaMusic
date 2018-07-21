var vm = new Vue({
  el: '#ttt',
  data: {
    show: false,
    min_date: null,
    max_date: null,
    place: null,
    events: [],
    indents: [],
    zoom_img: '',
    places: [],
    buy_form_show: false
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
      for(var i = 0; i < this.events.length; i++){
        this.places.push(this.events[i].place)
      }
      function onlyUnique(value, index, self) { 
          return self.indexOf(value) === index && value !== null;
      }
      this.places = this.places.filter(onlyUnique)

	  	
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
  		return {'left': 'calc(' + Math.random()*300 +'px)' };
  	},

    openBuyForm: function(index){
        this.buy_form_show = this.events[index].phones_of_managers
    }


  },
  delimiters: ["[[","]]"]
});