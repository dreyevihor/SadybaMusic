new Vue({
	el: "#portfolio-list",
	data: {
			limit: 3,
			offset: 0,
			url: "/api/portfolio/?limit=3&offset=0",
			loading: false,
			events: [],
			show: false

	},
	methods: {
		onScroll: function(event){
			var list = document.getElementById("portfolio-list")
			var	listHeight = list.offsetHeight
			var diffHeight = listHeight - window.pageYOffset
			console.log(diffHeight)
			if(diffHeight <=0 && !(this.loading)){
				this.load()
			}
		},
		load: function() {
			var vm = this
			vm.loading = true
			axios.get(vm.url).then(function(response){
				var resp = response.data,
					result = resp.results
				vm.events = vm.events.concat(result)
				vm.url = resp.next
			}).catch(function(errors){
				console.log(errors)

			})
			vm.loading = false
		},
		
	},
	created: function(){
		this.load()
		window.addEventListener('scroll', this.onScroll);
		},
	destroyed: function () {
        window.removeEventListener('scroll', this.onScroll);
    },
    components: {
    'carousel-3d': Carousel3d.Carousel3d,
    'slide': Carousel3d.Slide
  },
	delimiters: ["[[","]]"]
})