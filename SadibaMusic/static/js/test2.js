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
    		headers = {HTTP_X_CSRFTOKEN: this.csrftoken};
			axios.post('/test/', {'login': this.login, 'password': this.password}, headers)
			console.log(data)
			console.log(headers)
		}
	}
})