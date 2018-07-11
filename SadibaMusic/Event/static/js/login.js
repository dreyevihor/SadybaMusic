new Vue({
	el: 'form',
	data:{
		login: "",
		password: "",
		csrftoken: ""
	},
	created: function(){
		this.csrftoken = Cookies.get('csrftoken');
	},
	methods:{
		submit: function(){
			this.csrftoken = Cookies.get('csrftoken'); // Using JS Cookies library
    		headers = {"X-CSRFToken": this.csrftoken};
			axios.post('/login/', {'login': this.login, 'password': this.password},
			 {headers: headers})
			console.log(data)
			console.log(headers)
		}
	}
})